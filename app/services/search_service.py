from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService


class SearchService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_service = VectorService()

    def search(self, question: str):

        query_vector = self.embedding_service.embed([question])[0]

        results = self.vector_service.search(query_vector)

        return results