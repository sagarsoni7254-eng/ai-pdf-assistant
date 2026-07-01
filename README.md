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
> 
> ---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/sagarsoni7254-eng/ai-pdf-assistant.git
```

Move into the project directory:

```bash
cd ai-pdf-assistant
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

### macOS / Linux

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

If using **uv**:

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install Ollama

Download and install Ollama:

https://ollama.com/download

Pull the required model:

```bash
ollama pull llama3.2
```

Start Ollama:

```bash
ollama serve
```

---

## 5️⃣ Start Qdrant

Run Qdrant locally using Docker:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

---

## 6️⃣ Run the Application

Start Streamlit:

```bash
streamlit run frontend/streamlit_app.py
```

Open your browser:

```
http://localhost:8501
```

---

# ⚙️ Configuration

Current configuration:

| Setting | Value |
|----------|--------|
| LLM | llama3.2 |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | Qdrant |
| UI | Streamlit |

---

# 🚀 How to Use

### Step 1

Upload one or more PDF documents.

---

### Step 2

The application automatically:

- Extracts text
- Splits text into chunks
- Creates embeddings
- Stores vectors in Qdrant

---

### Step 3

Ask questions in natural language.

Examples:

```
What is Optical Fiber?

Explain AI in simple words.

Summarize Chapter 3.

What are the advantages of Machine Learning?

List the important points.

Compare CNN and RNN.
```

---

### Step 4

The assistant:

- Searches relevant chunks
- Retrieves context
- Sends context to Ollama
- Generates an accurate answer
- Displays supporting sources

---

# 📸 Screenshots

> Screenshots will be added soon.

## 🏠 Home Page

```
screenshots/home.png
```

---

## 📄 Upload Documents

```
screenshots/upload.png
```

---

## 💬 Chat

```
screenshots/chat.png
```

---

## 📚 Rich Source References

```
screenshots/sources.png
```

---

## 📂 Sidebar

```
screenshots/sidebar.png
```

---

# 🧠 RAG Workflow

```text
User uploads PDF
        │
        ▼
Extract Text
        │
        ▼
Chunk Text
        │
        ▼
Generate Embeddings
        │
        ▼
Store in Qdrant
        │
        ▼
User asks question
        │
        ▼
Generate Question Embedding
        │
        ▼
Semantic Search
        │
        ▼
Retrieve Relevant Chunks
        │
        ▼
Build Prompt
        │
        ▼
Ollama LLM
        │
        ▼
Answer + Sources
```

---

# 💡 Example Questions

You can ask questions like:

- What is Artificial Intelligence?
- Explain this chapter in simple words.
- Summarize the uploaded document.
- What are the key points?
- Compare two concepts.
- Give me examples.
- Explain this topic for beginners.
- Create revision notes.
- List important interview questions.

---

# 📈 Current Features

- Multiple PDF Upload
- Semantic Search
- Local LLM
- Qdrant Vector Database
- Conversation Memory
- Rich Source References
- Document Manager
- Sidebar Statistics
- Clear Database
- Modern UI
- Modular Architecture

---