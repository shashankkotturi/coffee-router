import requests
import time

# Seed tools first
# print("Seeding tools...")
# seed_response = requests.post("https://coffee-router-production.up.railway.app/seed-tools")
# print(seed_response.json())

# Wait a moment for seeding to complete
time.sleep(2)


url = "https://coffee-router-production.up.railway.app/route"
payload = {
    "query": "I need to search for code repositories",
    "top_k": 5
}

response = requests.post(url, json=payload)
print(response.json())