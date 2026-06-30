from app.services.search_service import SearchService
from app.services.llm_service import LLMService

search_service = SearchService()
llm = LLMService()

question = "What is optical fiber?"

results = search_service.search(question)

context = ""

for result in results:
    context += result.payload["text"] + "\n\n"

answer = llm.ask(context, question)

print("=" * 60)
print("Question:")
print(question)
print("=" * 60)
print("Answer:")
print(answer)
print("=" * 60)