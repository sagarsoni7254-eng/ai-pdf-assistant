import sys
from pathlib import Path

# Add project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

from app.services.search_service import SearchService
from app.services.llm_service import LLMService


search = SearchService()
llm = LLMService()


def chat_page():

    st.header("💬 Chat with your PDF")

    # ----------------------------
    # Chat History
    # ----------------------------

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.write(message["content"])

            if (
                message["role"] == "assistant"
                and "sources" in message
            ):

                st.divider()

                st.subheader("📚 Sources")

                for source in message["sources"]:

                    title = (
                        f"📄 {source['filename']}  |  "
                        f"🧩 Chunk {source['chunk_index']}"
                    )

                    with st.expander(title):

                        st.markdown(
                            f"**Source File:** `{source['filename']}`"
                        )

                        st.markdown(
                            f"**Chunk Index:** `{source['chunk_index']}`"
                        )

                        st.divider()

                        st.write(source["text"])

    # ----------------------------
    # Chat Input
    # ----------------------------

    question = st.chat_input(
        "Ask anything about your PDFs..."
    )

    if not question:
        return

    # ----------------------------
    # Store User Message
    # ----------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):

        st.write(question)

    # ----------------------------
    # Search
    # ----------------------------

    with st.spinner("Searching knowledge base..."):

        results = search.search(question)

    context = ""

    sources = []

    for result in results:

        payload = result.payload

        context += payload["text"] + "\n\n"

        sources.append(
            {
                "filename": payload.get(
                    "filename",
                    "Unknown PDF"
                ),
                "chunk_index": payload.get(
                    "chunk_index",
                    0
                ),
                "text": payload.get(
                    "text",
                    ""
                ),
            }
        )

    # ----------------------------
    # Ask LLM
    # ----------------------------

    with st.spinner("Generating answer..."):

        answer = llm.ask(
            context=context,
            question=question,
            history=st.session_state.messages,
        )

    # ----------------------------
    # Display Assistant
    # ----------------------------

    with st.chat_message("assistant"):

        st.write(answer)

        st.divider()

        st.subheader("📚 Sources")

        for source in sources:

            title = (
                f"📄 {source['filename']}  |  "
                f"🧩 Chunk {source['chunk_index']}"
            )

            with st.expander(title):

                st.markdown(
                    f"**Source File:** `{source['filename']}`"
                )

                st.markdown(
                    f"**Chunk Index:** `{source['chunk_index']}`"
                )

                st.divider()

                st.write(source["text"])

    # ----------------------------
    # Save Assistant Message
    # ----------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources,
        }
    )