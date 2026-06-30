import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

from app.services.ingestion_service import IngestionService


def upload_page():

    st.header("📤 Upload PDF(s)")

    ingestion = IngestionService()

    uploaded_files = st.file_uploader(
        "Choose one or more PDF files",
        type=["pdf"],
        accept_multiple_files=True,
        key="pdf_uploader"
    )

    # Initialize session state
    if "processed_files" not in st.session_state:
        st.session_state.processed_files = []

    if not uploaded_files:
        return

    upload_folder = Path("data/uploads")
    upload_folder.mkdir(parents=True, exist_ok=True)

    progress = st.progress(0)

    total_files = len(uploaded_files)

    processed_count = 0
    skipped_count = 0

    for index, uploaded_file in enumerate(uploaded_files):

        progress.progress((index + 1) / total_files)

        # Skip duplicates in current session
        if uploaded_file.name in st.session_state.processed_files:
            skipped_count += 1
            continue

        save_path = upload_folder / uploaded_file.name

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner(f"Processing {uploaded_file.name}..."):
            ingestion.ingest_pdf(str(save_path))

        st.session_state.processed_files.append(uploaded_file.name)

        processed_count += 1

    progress.empty()

    if processed_count:
        st.success(f"✅ Successfully processed {processed_count} PDF(s).")

    if skipped_count:
        st.info(f"ℹ️ Skipped {skipped_count} PDF(s) that were already processed.")

    st.subheader("📚 Uploaded Documents")

    for filename in st.session_state.processed_files:
        st.write(f"📄 {filename}")