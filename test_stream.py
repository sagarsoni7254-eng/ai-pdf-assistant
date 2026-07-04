from app.services.llm_service import LLMService

llm = LLMService()

context = "Python is a programming language."

question = "What is Python?"

for chunk in llm.stream_ask(
    context=context,
    question=question,
    history=[],
):
    print(chunk, end="", flush=True)