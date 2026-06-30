from app.services.search_service import SearchService

search = SearchService()

results = search.search(
    "What is optical fiber?"
)

print("=" * 60)

print("Results:", len(results))

print("=" * 60)

for result in results:
    print(result.payload["text"])
    print("-" * 60)