from pathlib import Path

from app.services.vector_service import VectorService


class DatabaseService:

    def __init__(self):
        self.vector = VectorService()

    def clear_database(self):
        """
        Clears the complete knowledge base.

        1. Deletes Qdrant collection
        2. Creates a fresh collection
        3. Deletes all uploaded PDFs
        """

        # Delete existing collection
        self.vector.client.delete_collection(
            collection_name=self.vector.collection_name
        )

        # Create new empty collection
        self.vector.create_collection()

        # Delete uploaded PDF files
        upload_folder = Path("data/uploads")

        if upload_folder.exists():
            for file in upload_folder.glob("*"):
                if file.is_file():
                    file.unlink()

        print("✅ Knowledge base cleared successfully")