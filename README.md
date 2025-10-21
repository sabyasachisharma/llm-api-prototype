# Statista Search API

A HTTP service providing natural language search for Statista statistics data using TF-IDF vectorization and cosine similarity ranking.

## Quick Start

### Using Docker (Recommended)
```bash
docker-compose up --build
# Access API: http://localhost:8000/docs
```

### Manual Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## API Endpoints

### GET /find
Search for statistics using natural language.

**Query Parameters:**
- `query` (string, required): Natural language search query

**Response:**
```json
{
    "results": [
        {
            "item": {
                "id": 1,
                "title": "string",
                "subject": "string",
                "description": "string",
                "link": "string",
                "date": "2024-03-20T12:00:00Z"
            },
            "similarity_score": 0.85
        }
    ]
}
```

### GET /stream/find
Stream search results progressively as newline-delimited JSON.

## Usage Example

```bash
curl "http://localhost:8000/find?query=e-commerce"
```

Visit http://localhost:8000/docs for interactive API documentation.

## Architecture

- **Data Layer**: Mock data generation with Faker, Pydantic models, in-memory vector storage
- **Search Engine**: TF-IDF vectorization with cosine similarity ranking
- **API Layer**: FastAPI with async endpoints and streaming support

## Key Components

- `main.py` - FastAPI application
- `app/search.py` - Search engine implementation
- `app/models.py` - Pydantic data models
- `app/data_generator.py` - Mock data generation
