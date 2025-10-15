from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pinecone import Pinecone
from openai import OpenAI
import os
from dotenv import load_dotenv
import logging
from tools import SAMPLE_TOOLS

load_dotenv()

# Set logging level to reduce spam
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


# Initialize clients
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("coffee-tools")

app = FastAPI(title="COFFEE Router")

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class Tool(BaseModel):
    id: str
    name: str
    description: str
    mcp_server: str  # e.g., "brave-search", "github"
    full_definition: str  # The actual MCP tool JSON/schema

class RouterQuery(BaseModel):
    query: str
    top_k: int = 3

class RouterResponse(BaseModel):
    tools: list[dict]
    query_embedding: list[float]

# # Initialize with sample tools (you'd pull from DB in production)
# SAMPLE_TOOLS = [
#     {
#         "id": "brave_search",
#         "name": "Brave Search",
#         "description": "Search the web using Brave Search API. Returns top results for any query.",
#         "mcp_server": "brave-search",
#         "full_definition": '{"type": "function", "name": "search", "description": "Search the web"}'
#     },
#     {
#         "id": "github_repos",
#         "name": "GitHub Repository Finder",
#         "description": "Search and retrieve GitHub repositories by language, stars, or keywords.",
#         "mcp_server": "github",
#         "full_definition": '{"type": "function", "name": "search_repos", "description": "Find GitHub repos"}'
#     },
#     {
#         "id": "slack_msg",
#         "name": "Slack Message Retriever",
#         "description": "Query Slack messages from connected workspaces. Can search by keyword or user.",
#         "mcp_server": "slack",
#         "full_definition": '{"type": "function", "name": "search_messages", "description": "Find Slack messages"}'
#     },
#     {
#         "id": "sql_query",
#         "name": "SQL Database Query",
#         "description": "Execute SQL queries against connected PostgreSQL databases. Returns structured data.",
#         "mcp_server": "postgres",
#         "full_definition": '{"type": "function", "name": "query_db", "description": "Execute SQL"}'
#     },
# ]

@app.on_event("startup")
async def startup():
    """Seed the vector DB with tools on startup"""
    try:
        index.describe_index_stats()
        print("Index exists, skipping seeding")
    except:
        print("Seeding vector DB with tools...")
        for tool in SAMPLE_TOOLS:
            # Generate embedding for tool description
            response = openai_client.embeddings.create(
                input=tool["description"],
                model="text-embedding-3-small"
            )
            embedding = response.data[0].embedding
            
            # Upsert to Pinecone (id, vector, metadata)
            index.upsert([(
                tool["id"],
                embedding,
                {"name": tool["name"], "description": tool["description"], "full_definition": tool["full_definition"], "mcp_server": tool["mcp_server"]}
            )])
        print("Seeding complete")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/seed-tools")
async def seed_tools():
    """Manually seed the vector DB (for debugging)"""
    try:
        for tool in SAMPLE_TOOLS:
            response = openai_client.embeddings.create(
                input=tool["description"],
                model="text-embedding-3-small"
            )
            embedding = response.data[0].embedding
            
            index.upsert([(
                tool["id"],
                embedding,
                {"name": tool["name"], "description": tool["description"], "full_definition": tool["full_definition"], "mcp_server": tool["mcp_server"]}
            )])
        
        return {"status": "seeded", "tools_count": len(SAMPLE_TOOLS)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# @app.get("/index-stats")
# async def get_index_stats():
#     """Check Pinecone index stats"""
#     try:
#         stats = index.describe_index_stats()
#         return {"stats": stats}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

@app.get("/index-stats")
async def get_index_stats():
    """Check Pinecone index stats"""
    try:
        stats = index.describe_index_stats()
        print("Stats:", stats)
        # Extract the total vector count
        total_vectors = stats.get("total_vector_count", 0)
        return {
            "total_tools": total_vectors,
            "status": "success"
        }
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/route", response_model=RouterResponse)
async def route_query(req: RouterQuery):
    """Main router endpoint: find relevant tools for a query"""
    try:
        # Embed the incoming query
        query_response = openai_client.embeddings.create(
            input=req.query,
            model="text-embedding-3-small"
        )
        query_embedding = query_response.data[0].embedding
        
        # Search Pinecone for similar tool descriptions
        search_results = index.query(
            vector=query_embedding,
            top_k=req.top_k,
            include_metadata=True
        )
        
        # Format results
        tools = []
        for match in search_results["matches"]:
            tools.append({
                "id": match["id"],
                "name": match["metadata"]["name"],
                "description": match["metadata"]["description"],
                "mcp_server": match["metadata"]["mcp_server"],
                "full_definition": match["metadata"]["full_definition"],
                "score": match["score"]  # Similarity score (0-1)
            })
        
        return RouterResponse(tools=tools, query_embedding=query_embedding)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/add-tool")
async def add_tool(tool: Tool):
    """Admin endpoint: add new tool to router"""
    try:
        response = openai_client.embeddings.create(
            input=tool.description,
            model="text-embedding-3-small"
        )
        embedding = response.data[0].embedding
        
        index.upsert([(
            tool.id,
            embedding,
            {
                "name": tool.name,
                "description": tool.description,
                "full_definition": tool.full_definition,
                "mcp_server": tool.mcp_server
            }
        )])
        
        return {"status": "tool added", "id": tool.id}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tools")
async def list_tools():
    """Get all registered tools"""
    return {"tools": SAMPLE_TOOLS}

@app.get("/all-tools")
async def get_all_tools():
    """Get all tools metadata for token calculation"""
    try:
        # Fetch all tools from index
        stats = index.describe_index_stats()
        total_count = stats.get("total_vector_count", 0)
        
        # Query all vectors (paginate if needed)
        all_tools = []
        results = index.query(
            vector=[0] * 1536,  # Dummy vector
            top_k=total_count,
            include_metadata=True
        )
        
        for match in results["matches"]:
            all_tools.append({
                "id": match["id"],
                "description": match["metadata"]["description"]
            })
        
        return {"tools": all_tools}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)