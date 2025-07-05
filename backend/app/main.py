from asyncio import sleep
import asyncio
import time
from fastapi import FastAPI
import openai
from dotenv import load_dotenv
import os
import requests
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel

load_dotenv()
# Initialize OpenAI client with the API key from environment variables
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = FastAPI()
BRAVE_API_KEY = "BSA4-s"   # or paste your key here for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can restrict this to specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CompetitorRequest(BaseModel):
    keywords: list
    competitors: list  # List of competitor domains or URLs (e.g., ["peec.ai", "replika.ai", "woebothealth.com"])

def build_prompt(keywords, competitors):
    keywords_string = ", ".join([f'"{k}"' for k in keywords])
    brands_string = ", ".join([f'"{b}"' for b in competitors])
    n_keywords = len(keywords)
    n_brands = len(competitors)
    return (
        f"You are a JSON-generating tool for brand familiarity ranking only.\n"
        f"There are {n_keywords} keywords: [{keywords_string}] and {n_brands} brands: [{brands_string}].\n"
        "For EACH keyword, output exactly one object in a JSON array, matching this schema:\n"
        '[{"keyword": "...", "positions": {"Brand1": null or 1, "Brand2": null or 2, ...}},{"keyword": "...", "positions": {"Brand1": null or 1, "Brand2": null or 2, ...}} ...]\n\n'
        "Output array *MUST* have exactly as many items as there are keywords provided (no fewer or more), and each 'positions' always has ALL brand keys given, in the same order, even if value is null. "
        "No non-JSON content, no summary, no markdown. no uncompleted json. schema array list length must match keywords length.\n"
        'example output: "results:[{keyword:\"ElectricalCar\",positions:{Xiaomi:null,Tesla:null,BMW:null,Honda:null,Peugeot:null,\"Mercedes-Benz\":null,},},{keyword:\"DCChargerEVCars\",positions:{Xiaomi:null,Tesla:null,BMW:null,Honda:null,Peugeot:null,\"Mercedes-Benz\":null,},},{keyword:\"SmallElectricCars\",positions:{Xiaomi:null,Tesla:null,BMW:null,Honda:null,Peugeot:null,\"Mercedes-Benz\":null,},},{keyword:\"LuxuryElectricCars\",positions:{Xiaomi:null,Tesla:11,BMW:1,Honda:null,Peugeot:null,\"Mercedes-Benz\":2,},},{keyword:\"LongRangeElectricVehicles\",positions:{Xiaomi:null,Tesla:2,BMW:13,Honda:null,Peugeot:null,\"Mercedes-Benz\":6,},},{keyword:\"Under40kElectricCars\",positions:{Xiaomi:null,Tesla:4,BMW:null,Honda:null,Peugeot:null,\"Mercedes-Benz\":null,},},{keyword:\"SUVElectricCars\",positions:{Xiaomi:null,Tesla:null,BMW:null,Honda:3,Peugeot:null,\"Mercedes-Benz\":null,},},{keyword:\"FastElectricCars\",positions:{Xiaomi:null,Tesla:13,BMW:null,Honda:null,Peugeot:null,\"Mercedes-Benz\":null,},},],"'
    )
def brave_search(query):
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {"Accept": "application/json", "X-Subscription-Token": BRAVE_API_KEY}
    params = {"q": query}
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json().get("web", []).get("results", [])

async def compare_sites_on_keywords(keywords, competitors):
    comparisons = []

    for kw in keywords:
        serp = brave_search(kw)
        time.sleep(4.5)
        await asyncio.sleep(3)  # To avoid hitting rate limits, you can adjust this as needed

        positions = {}
        for comp in competitors:
            # Look for first occurrence where the name appears in the title or description
            target = comp.lower()
            found = None
            for idx, res in enumerate(serp):
                # Can also check 'description' or 'body' if you want
                title = res.get('title', '').lower()
                desc = res.get('description', '').lower()  # or 'body'
                if target in title or target in desc:
                    found = idx+1  # 1-based position
                    break
            positions[comp] = found  # None if not found
        comparisons.append({"keyword": kw, "positions": positions})
        
    return comparisons
@app.post("/compare")
async def compare(request: CompetitorRequest):
    raw = await compare_sites_on_keywords(request.keywords, request.competitors)
    # Just a quick basic summary (not using OpenAI here, but you could add it)
    summary = {
        "total_keywords": len(request.keywords),
        "results": raw
    }
    return summary

@app.post("/compare-chatgpt")
def compare_chatgpt(request: CompetitorRequest):
    prompt = build_prompt(request.keywords, request.competitors)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        response_format={
            "type": "json_object",
        }
    )
    content = response.choices[0].message.content.strip()
    try:

        result = json.loads(content)
        
        return {"success": True,  "results": result.results if hasattr(result, 'results') else result}
    except Exception:
        return {"success": False, "error": "Could not parse model output as JSON.", "raw_result": content}

@app.get("/search")
async def search( requests=dict):
    try:
        # Check if OpenAI API is reachable
        response = client.responses.create(
            model="gpt-4.1",
            tools=[{"type": "web_search_preview"}],
            input=requests.get("query")
        )

        print(response.output_text)
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}
@app.get("/")
async def root():
    response = "Hello, World!"
    
    """     client = openaai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, who are you?"}
        ]
    )
    response = client.choices[0].message.content """



    return {"message": response}