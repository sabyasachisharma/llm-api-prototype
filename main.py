from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import json
from app.models import SearchResponse
from app.search import search_engine

app = FastAPI(
    title="Statista Search API",
    description="API for searching Statista statistics using natural language queries",
    version="1.0.0"
)

@app.get("/find", response_model=SearchResponse)
async def find(query: str):
    """
    Search for statistics using natural language query.
    Returns top 5 most relevant items with similarity scores.
    """
    results = search_engine.search(query, top_k=5)
    return SearchResponse(results=results)

@app.get("/stream/find")
async def stream_find(query: str):
    """
    Stream search results for statistics using natural language query.
    Returns top 10 most relevant items progressively.
    """
    async def generate_results():
        results = search_engine.search(query, top_k=10)
        
        # Stream results one by one with a small delay
        for result in results:
            # Convert to dict and then to JSON string
            result_dict = {
                "item": {
                    "id": result.item.id,
                    "title": result.item.title,
                    "subject": result.item.subject,
                    "description": result.item.description,
                    "link": result.item.link,
                    "date": result.item.date.isoformat()
                },
                "similarity_score": result.similarity_score
            }
            yield json.dumps(result_dict) + "\n"
            await asyncio.sleep(0.1)  # Small delay between results
    
    return StreamingResponse(
        generate_results(),
        media_type="application/x-ndjson"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 