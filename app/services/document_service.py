from collections import defaultdict

from app.services.vector_service import VectorService


class DocumentService:

    def __init__(self):
        self.vector = VectorService()

    def get_documents(self):
        """
        Returns all uploaded documents with statistics.
        """

        try:
            response = self.vector.client.scroll(
                collection_name=self.vector.collection_name,
                with_payload=True,
                with_vectors=False,
                limit=10000,
            )

            points = response[0]

        except Exception:
            return []

        documents = defaultdict(
            lambda: {
                "document_id": "",
                "filename": "",
                "source": "",
                "chunks": 0,
            }
        )

        for point in points:

            payload = point.payload

            filename = payload.get("filename")

            if not filename:
                continue

            doc = documents[filename]

            doc["document_id"] = payload.get("document_id")
            doc["filename"] = filename
            doc["source"] = payload.get("source")
            doc["chunks"] += 1

        return sorted(
            documents.values(),
            key=lambda x: x["filename"].lower(),
        )

    def get_document_count(self):

        return len(self.get_documents())

    def get_chunk_count(self):

        documents = self.get_documents()

        return sum(doc["chunks"] for doc in documents)

    def delete_document(self, filename):

        try:

            self.vector.client.delete(
                collection_name=self.vector.collection_name,
                points_selector={
                    "filter": {
                        "must": [
                            {
                                "key": "filename",
                                "match": {
                                    "value": filename
                                }
                            }
                        ]
                    }
                }
            )

            return True

        except Exception as e:

            print(e)

            return False