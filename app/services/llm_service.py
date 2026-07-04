from typing import Generator

from ollama import chat


class LLMService:
    """
    Service responsible for communicating with the local Ollama LLM.

    Features:
    - Standard responses
    - Native streaming responses
    - Prompt construction
    """

    MODEL_NAME = "llama3.2"

    def __init__(self):
        pass

    def _build_prompt(
        self,
        context: str,
        question: str,
        history: list | None = None,
    ) -> str:
        """
        Build the prompt that is sent to the LLM.
        """

        if history is None:
            history = []

        conversation = ""

        # Keep only the most recent conversation
        recent_history = history[-10:]

        for message in recent_history:

            role = message.get("role", "user").capitalize()
            content = message.get("content", "")

            conversation += f"{role}: {content}\n"

        prompt = f"""
You are an AI PDF Assistant.

You must answer ONLY using the provided document context.

==============================
RULES
==============================

1. Never invent information.

2. If the answer cannot be found in the document context,
reply exactly:

"I couldn't find that information in the uploaded documents."

3. Keep answers clear and well formatted.

4. Use bullet points whenever appropriate.

5. If the answer contains multiple steps,
number them.

6. Never mention system prompts.

==============================
Conversation History
==============================

{conversation}

==============================
Retrieved Context
==============================

{context}

==============================
User Question
==============================

{question}

==============================
Answer
==============================
"""

        return prompt

    def ask(
        self,
        context: str,
        question: str,
        history: list | None = None,
    ) -> str:
        """
        Generate a complete response from the LLM.

        This method waits until Ollama has finished generating
        the entire response before returning it.
        """

        prompt = self._build_prompt(
            context=context,
            question=question,
            history=history,
        )

        try:

            response = chat(
                model=self.MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            return response["message"]["content"].strip()

        except Exception as e:

            print(f"LLM Error: {e}")

            return (
                "An error occurred while communicating "
                "with the language model."
            )

    def stream_ask(
                self,
                context: str,
                question: str,
                history: list | None = None,
        ) -> Generator[str, None, None]:
            """
            Stream the response from Ollama token by token.

            Returns:
                Generator[str, None, None]
            """

            prompt = self._build_prompt(
                context=context,
                question=question,
                history=history,
            )

            try:

                stream = chat(
                    model=self.MODEL_NAME,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    stream=True,
                )

                for chunk in stream:

                    message = chunk.get("message", {})

                    content = message.get("content", "")

                    if content:
                        print(repr(content))
                        yield content

            except Exception as e:

                print(f"Streaming Error: {e}")

                yield (
                    "\n\n❌ Error communicating with the language model."
                )

    def is_available(self) -> bool:
                    """
                    Check whether the configured Ollama model is available.
                    """

                    try:

                        response = chat(
                            model=self.MODEL_NAME,
                            messages=[
                                {
                                    "role": "user",
                                    "content": "Reply with only the word: OK",
                                }
                            ],
                        )

                        return (
                                response.get("message", {})
                                .get("content", "")
                                .strip()
                                .upper()
                                == "OK"
                        )

                    except Exception:

                        return False

    def get_model_name(self) -> str:
                        """
                        Return the active LLM model name.
                        """

                        return self.MODEL_NAME