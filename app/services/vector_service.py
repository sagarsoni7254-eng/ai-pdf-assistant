
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct


class VectorService:
    def __init__(self):
        self.client = QdrantClient(
            host="localhost",
            port=6333,
        )

        self.collection_name = "documents"

    def create_collection(self):
        collections = self.client.get_collections().collections

        names = [c.name for c in collections]

        if self.collection_name not in names:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE,
                ),
            )

            print("✅ Collection created")
        else:
            print("✅ Collection already exists")

    def insert_points(self, points):
        qdrant_points = []

        for point in points:
            qdrant_points.append(
                PointStruct(
                    id=point["id"],
                    vector=point["vector"],
                    payload=point["payload"],
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=qdrant_points,
        )

        print(f"✅ Stored {len(points)} chunks in Qdrant")

    def search(self, query_vector, limit=5):
        response = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=limit,
        )

        return response.points