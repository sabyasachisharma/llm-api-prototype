from datetime import datetime
from pydantic import BaseModel

class MockDataSchema(BaseModel):
    id: int
    title: str
    subject: str
    description: str
    link: str
    date: datetime

class SearchResult(BaseModel):
    item: MockDataSchema
    similarity_score: float

class SearchResponse(BaseModel):
    results: list[SearchResult] 