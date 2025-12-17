# Project 4: Lightweight RAG Assistant for ERP Manuals

## 1. Project Overview & Problem Statement

Enterprise Resource Planning (ERP) systems contain extensive manuals, policies, and help documents.
Searching these documents manually is time-consuming and inefficient.

This project solves this problem by building a **Retrieval-Augmented Generation (RAG) system**
that allows users to ask natural-language questions and receive accurate answers
**with references to the source documents**.

---

## 2. Objective

- Ingest ERP help manuals and policy documents (PDF/TXT)
- Enable natural-language question answering
- Retrieve relevant document sections using vector search
- Generate answers using an LLM
- Display answers along with source document citations

---

## 3. Key Features

- Document ingestion and chunking
- Semantic search using FAISS vector database
- Sentence-transformer embeddings
- LLM-powered answer generation
- Source attribution for transparency
- Interactive web UI built using Streamlit
- Modular and extensible architecture

---

## 4. Technologies & Libraries Used

- **Python**
- **LangChain** – RAG orchestration
- **sentence-transformers** – Embedding model (`all-MiniLM-L6-v2`)
- **FAISS** – Vector database for similarity search
- **OpenAI API** (or compatible LLM)
- **PyPDF** – PDF document parsing
- **Streamlit** – Web-based demo UI
- **pytest** – Basic unit testing

---

## 5. Project Architecture

