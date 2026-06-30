import uuid
from pathlib import Path

from app.services.pdf_loader import PDFLoader
from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService


class IngestionService:

    def __init__(self):
        self.pdf_loader = PDFLoader()
        self.embedding_service = EmbeddingService()
        self.vector_service = VectorService()

    def ingest_pdf(self, pdf_path: str):

        pdf_path = Path(pdf_path)

        document_id = str(uuid.uuid4())

        filename = pdf_path.name

        source = str(pdf_path)

        # Read PDF and create chunks
        chunks = self.pdf_loader.load_and_chunk(source)

        if not chunks:
            print("⚠️ No text found in PDF.")
            return 0

        # Generate embeddings
        embeddings = self.embedding_service.embed(chunks)

        # Ensure collection exists
        self.vector_service.create_collection()

        points = []

        for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

            points.append(
                {
                    "id": str(uuid.uuid4()),
                    "vector": embedding,
                    "payload": {
                        "document_id": document_id,
                        "filename": filename,
                        "source": source,
                        "chunk_index": index,
                        "text": chunk,
                    },
                }
            )

        # Store vectors
        self.vector_service.insert_points(points)

        print(f"✅ {filename}")
        print(f"   Document ID : {document_id}")
        print(f"   Chunks      : {len(points)}")

        return len(points)