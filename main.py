from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pinecone import Pinecone
from openai import OpenAI
import os
from dotenv import load_dotenv
import logging
from tools import SAMPLE_TOOLS
import google.generativeai as genai
import json

load_dotenv()

# Set logging level to reduce spam
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# Initialize clients
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("coffee-tools")

# Initialize Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
gemini_model = genai.GenerativeModel('gemini-2.0-flash-exp')

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
    mcp_server: str
    full_definition: str

class RouterQuery(BaseModel):
    query: str
    top_k: int = 3

class AgentQuery(BaseModel):
    query: str

class RouterResponse(BaseModel):
    tools: list[dict]
    query_embedding: list[float]

class AgentResponse(BaseModel):
    explanation: str
    tools: list[dict]
    intent_summary: str
    reasoning: str

@app.on_event("startup")
async def startup():
    """Seed the vector DB with tools on startup"""
    try:
        index.describe_index_stats()
        print("Index exists, skipping seeding")
    except:
        print("Seeding vector DB with tools...")
        for tool in SAMPLE_TOOLS:
            response = openai_client.embeddings.create(
                input=tool["description"],
                model="text-embedding-3-small"
            )
            embedding = response.data[0].embedding
            
            index.upsert([(
                tool["id"],
                embedding,
                {"name": tool["name"], "description": tool["description"], 
                 "full_definition": tool["full_definition"], "mcp_server": tool["mcp_server"]}
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
                {"name": tool["name"], "description": tool["description"], 
                 "full_definition": tool["full_definition"], "mcp_server": tool["mcp_server"]}
            )])
        
        return {"status": "seeded", "tools_count": len(SAMPLE_TOOLS)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/index-stats")
async def get_index_stats():
    """Check Pinecone index stats"""
    try:
        stats = index.describe_index_stats()
        total_vectors = stats.get("total_vector_count", 0)
        return {
            "total_tools": total_vectors,
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/route", response_model=RouterResponse)
async def route_query(req: RouterQuery):
    """Main router endpoint: find relevant tools for a query"""
    try:
        query_response = openai_client.embeddings.create(
            input=req.query,
            model="text-embedding-3-small"
        )
        query_embedding = query_response.data[0].embedding
        
        search_results = index.query(
            vector=query_embedding,
            top_k=req.top_k,
            include_metadata=True
        )
        
        tools = []
        for match in search_results["matches"]:
            tools.append({
                "id": match["id"],
                "name": match["metadata"]["name"],
                "description": match["metadata"]["description"],
                "mcp_server": match["metadata"]["mcp_server"],
                "full_definition": match["metadata"]["full_definition"],
                "score": match["score"]
            })
        
        return RouterResponse(tools=tools, query_embedding=query_embedding)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def clean_json_response(text: str) -> str:
    """Clean Gemini response to extract valid JSON"""
    text = text.strip()
    
    # Remove markdown code blocks
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    
    if text.endswith("```"):
        text = text[:-3]
    
    text = text.strip()
    
    # Find JSON object boundaries
    start = text.find("{")
    end = text.rfind("}") + 1
    
    if start != -1 and end > start:
        text = text[start:end]
    
    return text

@app.post("/agent-route", response_model=AgentResponse)
async def agent_route(req: AgentQuery):
    """Intelligent agent endpoint using Gemini to analyze and route queries"""
    try:
        # Step 1: Agent analyzes the query
        analysis_prompt = f"""You are an intelligent tool-routing agent. A user has asked: "{req.query}"

Your job is to:
1. Understand what the user wants to accomplish
2. Generate 1-3 focused search queries to find the most relevant tools from a tool database
3. Determine if this is a simple or complex request

The available tool categories include: web search, GitHub repos, Slack messages, SQL databases, file operations, API integrations, and more.

CRITICAL: Respond ONLY with valid JSON. Do not include ANY text before or after the JSON object. No explanations, no markdown, just pure JSON.

Format:
{{
  "intent_summary": "brief description of what user needs",
  "search_queries": ["query1", "query2"],
  "complexity": "simple"
}}"""

        analysis_response = gemini_model.generate_content(analysis_prompt)
        analysis_text = clean_json_response(analysis_response.text)
        
        try:
            analysis = json.loads(analysis_text)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parse error: {e}")
            logger.error(f"Response text: {analysis_text}")
            raise HTTPException(status_code=500, detail="Failed to parse agent analysis")

        # Step 2: Use the agent's queries to fetch tools
        all_tools = []
        for search_query in analysis.get("search_queries", [req.query]):
            # Call internal route function
            query_response = openai_client.embeddings.create(
                input=search_query,
                model="text-embedding-3-small"
            )
            query_embedding = query_response.data[0].embedding
            
            search_results = index.query(
                vector=query_embedding,
                top_k=3,
                include_metadata=True
            )
            
            for match in search_results["matches"]:
                tool = {
                    "id": match["id"],
                    "name": match["metadata"]["name"],
                    "description": match["metadata"]["description"],
                    "mcp_server": match["metadata"]["mcp_server"],
                    "full_definition": match["metadata"]["full_definition"],
                    "score": match["score"]
                }
                # Avoid duplicates
                if not any(t["id"] == tool["id"] for t in all_tools):
                    all_tools.append(tool)

        if not all_tools:
            raise HTTPException(status_code=404, detail="No tools found")

        # Step 3: Agent filters and ranks the tools
        ranking_prompt = f"""You found these tools for the user's query: "{req.query}"

Tools found:
{chr(10).join([f"{i+1}. {t['name']} (score: {t['score']:.2f}): {t['description']}" for i, t in enumerate(all_tools)])}

Now:
1. Select the 3-5 MOST relevant tools for this specific query
2. Explain to the user in a friendly way what you found and why these tools help (2-3 sentences max)
3. If some tools aren't relevant, don't include them

CRITICAL: Respond ONLY with valid JSON. No markdown, no extra text, just the JSON object.

Format:
{{
  "explanation": "Your natural language response to the user",
  "selected_tool_ids": ["tool_id1", "tool_id2"],
  "reasoning": "Brief technical reasoning"
}}"""

        ranking_response = gemini_model.generate_content(ranking_prompt)
        ranking_text = clean_json_response(ranking_response.text)
        
        try:
            ranking = json.loads(ranking_text)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parse error: {e}")
            logger.error(f"Response text: {ranking_text}")
            raise HTTPException(status_code=500, detail="Failed to parse agent ranking")

        # Filter to selected tools
        selected_tools = [t for t in all_tools if t["id"] in ranking.get("selected_tool_ids", [])]
        
        if not selected_tools:
            # Fallback: return top 3 tools by score
            selected_tools = sorted(all_tools, key=lambda x: x["score"], reverse=True)[:3]

        return AgentResponse(
            explanation=ranking.get("explanation", "I found some relevant tools for your query."),
            tools=selected_tools,
            intent_summary=analysis.get("intent_summary", "Tool search request"),
            reasoning=ranking.get("reasoning", "Selected based on relevance scores")
        )
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Agent route error: {str(e)}")
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
        stats = index.describe_index_stats()
        total_count = stats.get("total_vector_count", 0)
        
        all_tools = []
        results = index.query(
            vector=[0] * 1536,
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