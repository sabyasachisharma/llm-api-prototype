from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from .models import MockDataSchema, SearchResult
from .data_generator import mock_database

class SearchEngine:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.documents = mock_database
        self.document_vectors = None
        self._prepare_vectors()
    
    def _prepare_vectors(self):
        # Combine title, subject and description for better search
        texts = [
            f"{doc.title} {doc.subject} {doc.description}"
            for doc in self.documents
        ]
        self.document_vectors = self.vectorizer.fit_transform(texts)
    
    def search(self, query: str, top_k: int = 5) -> List[SearchResult]:
        # Transform query
        query_vector = self.vectorizer.transform([query])
        
        # Calculate similarities
        similarities = cosine_similarity(query_vector, self.document_vectors).flatten()
        
        # Get top k indices
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Create search results
        results = []
        for idx in top_indices:
            results.append(
                SearchResult(
                    item=self.documents[idx],
                    similarity_score=float(similarities[idx])
                )
            )
        
        return results

# Initialize search engine
search_engine = SearchEngine() 