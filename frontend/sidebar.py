import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

from app.services.database_service import DatabaseService
from app.services.document_service import DocumentService


def sidebar():

    db = DatabaseService()
    docs = DocumentService()

    with st.sidebar:

        st.title("📄 AI PDF Assistant")

        st.divider()

        # ----------------------------
        # Documents
        # ----------------------------

        st.subheader(
            f"📂 Documents ({docs.get_document_count()})"
        )

        documents = docs.get_documents()

        if not documents:

            st.info("No PDF uploaded")

        else:

            for document in documents:

                col1, col2 = st.columns([5, 1])

                with col1:

                    st.markdown(
                        f"**📄 {document['filename']}**"
                    )

                    st.caption(
                        f"🧩 {document['chunks']} Chunks"
                    )

                with col2:

                    if st.button(
                        "🗑",
                        key=f"delete_{document['filename']}"
                    ):

                        success = docs.delete_document(
                            document["filename"]
                        )

                        if success:

                            # Delete PDF file
                            pdf = Path(document["source"])

                            if pdf.exists():
                                pdf.unlink()

                            st.success(
                                f"{document['filename']} deleted."
                            )

                            st.rerun()

                        else:

                            st.error(
                                "Unable to delete document."
                            )

        st.divider()

        # ----------------------------
        # Actions
        # ----------------------------

        st.subheader("⚙️ Actions")

        if st.button("🗑 Clear Chat"):

            st.session_state.messages = []

            st.success("Chat cleared!")

            st.rerun()

        if st.button("🗑 Clear Database"):

            db.clear_database()

            st.session_state.messages = []

            if "processed_files" in st.session_state:
                st.session_state.processed_files = []

            st.success(
                "Knowledge base cleared successfully!"
            )

            st.rerun()

        st.divider()

        # ----------------------------
        # Statistics
        # ----------------------------

        st.subheader("📊 Statistics")

        st.write(
            f"📄 Documents : {docs.get_document_count()}"
        )

        st.write(
            f"🧩 Chunks : {docs.get_chunk_count()}"
        )

        st.write("🤖 Model : llama3.2")