from app.services.ingestion_service import IngestionService

service = IngestionService()

count = service.ingest_pdf(
    "data/uploads/Unit 4 Fiber Optics.pdf"
)

print("=" * 60)
print("Stored chunks:", count)
print("=" * 60)