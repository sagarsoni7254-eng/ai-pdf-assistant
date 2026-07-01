<div align="center">

# 🤖 AI PDF Assistant

### Chat with Your PDFs Using Local AI

A production-ready **Retrieval-Augmented Generation (RAG)** application that allows users to upload one or more PDF documents and ask questions using a **local Large Language Model (LLM)** powered by **Ollama** and **Qdrant Vector Database**.

---

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black?style=for-the-badge)
![Qdrant](https://img.shields.io/badge/Qdrant-Vector%20Database-orange?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Retrieval--Augmented--Generation-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

### 🚀 Built with Python • Streamlit • Ollama • Qdrant

</div>

---

# 📖 Table of Contents

- Overview
- Features
- System Architecture
- Project Structure
- Technology Stack
- Installation
- Configuration
- Usage
- Screenshots
- RAG Workflow
- Future Improvements
- Author
- License

---

# 🚀 Overview

AI PDF Assistant is a modern Retrieval-Augmented Generation (RAG) application that enables users to interact with PDF documents using natural language.

Instead of manually searching through hundreds of pages, users can simply ask questions and receive AI-generated answers backed by relevant information retrieved directly from uploaded documents.

Unlike many cloud-based AI assistants, this project runs **entirely locally**, ensuring better privacy, faster experimentation, and no dependency on external APIs.

The application combines semantic search, vector embeddings, and a local Large Language Model to provide accurate answers with supporting document references.

---

# ✨ Features

## 📄 Document Management

- Upload one or multiple PDF documents
- Automatic PDF text extraction
- Intelligent document chunking
- Store document embeddings in Qdrant
- View uploaded documents
- Delete individual documents
- Clear complete knowledge base

---

## 🤖 AI Chat

- Local LLM using Ollama
- Semantic document search
- Multi-document question answering
- Context-aware conversation
- Conversation memory
- Rich source references
- Chat history

---

## 🔍 Retrieval-Augmented Generation (RAG)

- Automatic text chunking
- Embedding generation
- Vector similarity search
- Context retrieval
- Grounded AI responses
- Metadata-aware search

---

## 📊 User Interface

- Modern Streamlit interface
- Document Manager
- Sidebar statistics
- Progress indicators
- Multiple PDF support
- Clear chat
- Clear database

---

# 🏗️ System Architecture

```text
                    +----------------------+
                    |    Upload PDF(s)     |
                    +----------+-----------+
                               |
                               |
                               ▼
                    +----------------------+
                    |   PDF Text Loader    |
                    +----------+-----------+
                               |
                               |
                               ▼
                    +----------------------+
                    |    Text Chunking     |
                    +----------+-----------+
                               |
                               |
                               ▼
                    +----------------------+
                    | Sentence Embeddings  |
                    +----------+-----------+
                               |
                               |
                               ▼
                    +----------------------+
                    |  Qdrant Vector DB    |
                    +----------+-----------+
                               |
                               |
                 User Question |
                               ▼
                    +----------------------+
                    | Semantic Retrieval   |
                    +----------+-----------+
                               |
                               |
                               ▼
                    +----------------------+
                    |     Ollama LLM       |
                    +----------+-----------+
                               |
                               ▼
                    AI Answer + Sources
```

---

# 📂 Project Structure

```text
AI PDF Assistant
│
├── app
│   ├── api
│   ├── core
│   └── services
│       ├── chunker.py
│       ├── database_service.py
│       ├── document_service.py
│       ├── embedding_service.py
│       ├── ingestion_service.py
│       ├── llm_service.py
│       ├── pdf_loader.py
│       ├── search_service.py
│       └── vector_service.py
│
├── frontend
│   ├── chat_page.py
│   ├── sidebar.py
│   ├── streamlit_app.py
│   └── upload_page.py
│
├── tests
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| User Interface | Streamlit |
| Local LLM | Ollama |
| Vector Database | Qdrant |
| Embedding Model | all-MiniLM-L6-v2 |
| PDF Processing | PyMuPDF |
| Vector Search | Semantic Similarity |
| Version Control | Git & GitHub |

---

# 🌟 Key Highlights

✅ 100% Local AI

✅ No OpenAI API Required

✅ Privacy Friendly

✅ Multiple PDF Support

✅ Conversation Memory

✅ Rich Source References

✅ Semantic Search

✅ Modern Architecture

✅ Modular Codebase

✅ Easy to Extend

---

> **End of Part 1**