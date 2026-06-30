from ollama import chat


class LLMService:

    def ask(
        self,
        context: str,
        question: str,
        history: list | None = None,
    ):

        if history is None:
            history = []

        conversation = ""

        # Keep only the last 5 exchanges
        recent_history = history[-10:]

        for message in recent_history:

            role = message["role"].capitalize()

            conversation += (
                f"{role}: {message['content']}\n"
            )

        prompt = f"""
You are an AI PDF Assistant.

Your job is to answer ONLY using the provided document context.

If the answer cannot be found inside the context, say:

"I couldn't find that information in the uploaded documents."

----------------------------------------
Conversation History
----------------------------------------

{conversation}

----------------------------------------
Retrieved Context
----------------------------------------

{context}

----------------------------------------
Current Question
----------------------------------------

{question}

Answer:
"""

        response = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]