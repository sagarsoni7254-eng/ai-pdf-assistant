<div align="center">

# 🤖 AI PDF Assistant

### Chat with Your PDFs Using Local AI

A modern **Retrieval-Augmented Generation (RAG)** application that allows users to upload one or more PDF documents and ask questions using a **local Large Language Model (LLM)** powered by **Ollama** and **Qdrant Vector Database**.

---

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000?style=for-the-badge)
![Qdrant](https://img.shields.io/badge/Qdrant-Vector_Database-FF6F00?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Retrieval_Augmented_Generation-2E8B57?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

---

### 🚀 Built with Python • Streamlit • Ollama • Qdrant

⭐ If you find this project useful, consider giving it a star!

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
- Future Roadmap
- Contributing
- License
- Author

---

# 🚀 Overview

AI PDF Assistant is a local Retrieval-Augmented Generation (RAG) application that enables users to interact with PDF documents using natural language.

Instead of manually searching through long PDF files, users can upload one or more documents and ask questions in plain English. The application retrieves the most relevant information using semantic search and generates answers with a local Large Language Model.

Unlike cloud-based AI applications, this project runs entirely on your machine using Ollama and Qdrant, helping keep your documents private while providing fast responses.

The project is designed as a modular, scalable codebase suitable for learning, portfolio projects, and further development.

---
# ✨ Features

## 📄 Document Management

- 📤 Upload one or multiple PDF documents
- 📚 Automatic PDF text extraction
- ✂️ Intelligent text chunking
- 🧠 Metadata-aware document processing
- 🗂️ Document Manager
- 🗑️ Delete individual documents
- 🧹 Clear the complete knowledge base

---

## 🤖 AI Chat

- 💬 Interactive chat interface
- 🧠 Conversation memory
- 📖 Context-aware responses
- 📚 Rich source references
- 🔍 Semantic document search
- ⚡ Fast local inference using Ollama
- 📝 Chat history

---

## 🔍 Retrieval-Augmented Generation (RAG)

- Automatic text chunking
- Sentence embeddings
- Vector similarity search
- Context retrieval
- Metadata filtering
- Grounded AI responses
- Multi-document search

---

## 📊 User Interface

- 🎨 Modern Streamlit interface
- 📂 Sidebar document manager
- 📈 Knowledge base statistics
- 📤 Multiple PDF upload
- 🧹 Clear Chat
- 🗑️ Clear Database
- 📱 Simple and responsive layout

---

# 🌟 Project Highlights

✅ 100% Local AI

✅ No OpenAI API Required

✅ Privacy Friendly

✅ Multiple PDF Support

✅ Conversation Memory

✅ Rich Source References

✅ Qdrant Vector Database

✅ Semantic Search

✅ Modular Architecture

✅ Production-Oriented Code Structure

---

# 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.11+ |
| User Interface | Streamlit |
| Local LLM | Ollama (Llama 3.2) |
| Vector Database | Qdrant |
| Embedding Model | all-MiniLM-L6-v2 |
| PDF Processing | PyMuPDF |
| Vector Search | Semantic Similarity Search |
| Version Control | Git & GitHub |
| Dependency Management | uv |

---

# 📌 Why This Project?

This project demonstrates the implementation of a complete Retrieval-Augmented Generation (RAG) pipeline using modern AI tools and frameworks.

It combines document processing, semantic search, vector databases, and local large language models into a single application capable of answering questions based on uploaded PDF documents.

The project is designed with a modular architecture, making it easy to extend with additional features such as streaming responses, PDF previews, dashboards, hybrid search, and cloud deployment.

---

# 🎯 Use Cases

This application can be used for:

- 📚 Study Notes
- 📖 Research Papers
- 📑 Company Documentation
- 📄 User Manuals
- 📘 E-books
- 🧾 Technical Documentation
- 🎓 Educational Material
- 📋 Project Reports

---

# 📈 Current Version

**Version:** `v1.0`

### Included Features

- ✅ Multiple PDF Upload
- ✅ Local LLM (Ollama)
- ✅ Semantic Search
- ✅ Qdrant Vector Database
- ✅ Conversation Memory
- ✅ Rich Source References
- ✅ Document Manager
- ✅ Sidebar Statistics
- ✅ Clear Database
- ✅ Modular Service Architecture

---

# 🏆 Project Goals

The primary goals of this project are:

- Build a complete local RAG application
- Learn vector databases and semantic search
- Explore local LLM deployment with Ollama
- Develop a modular and scalable architecture
- Create a portfolio-ready AI application
- Demonstrate modern AI engineering practices

---
# 🏗️ System Architecture

The AI PDF Assistant follows a modular Retrieval-Augmented Generation (RAG) architecture.

```text
                    +----------------------+
                    |    Upload PDF(s)     |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    |   PDF Text Loader    |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    |    Text Chunking     |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    | Sentence Embeddings  |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    |  Qdrant Vector DB    |
                    +----------+-----------+
                               ▲
                               |
                    User Question
                               |
                               ▼
                    +----------------------+
                    | Semantic Retrieval   |
                    +----------+-----------+
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

# 🔄 RAG Pipeline

The application follows the Retrieval-Augmented Generation workflow.

### Step 1 — Upload PDF

The user uploads one or more PDF documents using the Streamlit interface.

↓

### Step 2 — Extract Text

The application extracts readable text from every page of the uploaded PDF.

↓

### Step 3 — Chunking

Large documents are divided into smaller chunks so they can be embedded efficiently.

↓

### Step 4 — Generate Embeddings

Each text chunk is converted into a high-dimensional vector using the embedding model.

↓

### Step 5 — Store in Qdrant

The generated vectors are stored inside Qdrant together with useful metadata.

Example metadata:

```json
{
  "document_id": "...",
  "filename": "AI.pdf",
  "chunk_index": 12,
  "text": "Artificial Intelligence..."
}
```

↓

### Step 6 — User Question

The user asks a question in natural language.

↓

### Step 7 — Semantic Search

The question is embedded and compared against all stored vectors.

The most relevant chunks are retrieved.

↓

### Step 8 — Context Building

Retrieved chunks are combined into a prompt.

Conversation history is also included.

↓

### Step 9 — Ollama

The prompt is sent to the local Llama model.

↓

### Step 10 — Response

The assistant generates an answer together with supporting source references.

---

# 📂 Project Structure

```text
AI PDF Assistant
│
├── app
│   ├── api
│   │   └── upload.py
│   │
│   ├── core
│   │   ├── config.py
│   │   ├── constants.py
│   │   └── logger.py
│   │
│   ├── services
│   │   ├── chunker.py
│   │   ├── database_service.py
│   │   ├── document_service.py
│   │   ├── embedding_service.py
│   │   ├── ingestion_service.py
│   │   ├── llm_service.py
│   │   ├── pdf_loader.py
│   │   ├── search_service.py
│   │   └── vector_service.py
│   │
│   └── main.py
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
├── README.md
└── LICENSE
```

---

# 🧩 Service Layer

The application is divided into reusable service modules.

| Service | Responsibility |
|----------|----------------|
| PDF Loader | Extract text from PDF files |
| Chunker | Split documents into chunks |
| Embedding Service | Generate vector embeddings |
| Vector Service | Store and search vectors in Qdrant |
| Search Service | Retrieve relevant chunks |
| LLM Service | Communicate with Ollama |
| Database Service | Clear and manage the knowledge base |
| Document Service | Manage uploaded documents |

---

# 🔐 Metadata Stored with Every Chunk

Each document chunk is stored with metadata to support advanced features.

Current metadata includes:

- Document ID
- Filename
- Source Path
- Chunk Index
- Chunk Text

This metadata enables:

- Individual document deletion
- Rich source references
- Document statistics
- Future page-aware citations

---

# 📊 Data Flow

```text
PDF
 │
 ▼
Text Extraction
 │
 ▼
Chunking
 │
 ▼
Embeddings
 │
 ▼
Qdrant
 │
 ▼
Semantic Search
 │
 ▼
Context
 │
 ▼
Ollama
 │
 ▼
Answer + Sources
```

---

# 💡 Design Principles

The project follows several software engineering principles:

- Modular architecture
- Separation of concerns
- Service-oriented design
- Reusable components
- Scalable project structure
- Easy future extensibility
- Clean and maintainable code

---