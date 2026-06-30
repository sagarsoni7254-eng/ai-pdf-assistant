from app.services.embedding_service import EmbeddingService

embedder = EmbeddingService()

texts = [
    "Artificial Intelligence",
    "Machine Learning",
    "Optical Fiber",
]

vectors = embedder.embed(texts)

print("=" * 60)
print("Number of vectors:", len(vectors))
print("=" * 60)
print("Vector dimension:", len(vectors[0]))
print("=" * 60)
print(vectors[0][:10])