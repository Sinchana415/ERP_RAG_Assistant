# ERP RAG Assistant (Lightweight Retrieval-Augmented Generation System)

## Project Overview

The **ERP RAG Assistant** is a lightweight Retrieval-Augmented Generation (RAG) application designed to solve a common enterprise problem: **inefficient knowledge retrieval from large ERP manuals and policy documents**.

Instead of manually searching through hundreds of pages of PDFs, users can ask natural-language questions and receive **accurate answers with source-backed context**.

This project demonstrates how modern NLP techniques can be integrated into ERP systems to improve productivity, reduce training time, and enable intelligent self-service support.

---

## Objectives

* Ingest ERP manuals and policy documents (PDFs)
* Convert documents into searchable semantic embeddings
* Retrieve relevant document passages using vector similarity search
* Generate natural-language answers based on retrieved context
* Provide a simple, web-based demo UI

---

## Key Features

* **Semantic Search** using vector embeddings (not keyword-based)
* **PDF ingestion & chunking** for large ERP manuals
* **Fast local retrieval** using FAISS vector database
* **LLM-powered answers** with contextual grounding
* **Interactive Streamlit UI** for live demo
* Modular architecture (easy to extend or integrate)

---

## Architecture (High-Level)

1. **Document Ingestion**

   * ERP PDFs are loaded and split into chunks
   * Each chunk is converted into an embedding vector

2. **Vector Storage (FAISS)**

   * Embeddings are stored locally in a FAISS index

3. **Query Processing**

   * User question → embedding
   * FAISS retrieves most relevant document chunks

4. **Answer Generation**

   * Retrieved context is passed to the LLM
   * LLM generates a concise, grounded answer

5. **Frontend (Streamlit)**

   * Users interact via a web-based UI

---

## Tech Stack

| Component              | Technology                             |
| ---------------------- | -------------------------------------- |
| Language               | Python 3.10+                           |
| RAG Framework          | LangChain                              |
| Embeddings             | Sentence Transformers (MiniLM)         |
| Vector Database        | FAISS (Local)                          |
| LLM                    | OpenAI GPT (or pluggable local models) |
| Document Loader        | PyPDF                                  |
| Frontend               | Streamlit                              |
| Environment Management | python-dotenv                          |

---

## Project Structure

```
ERP_RAG_Assistant/
│
├── data/
│   └── erp_manuals/          # ERP PDF documents
│
├── src/
│   ├── ingest.py             # Builds FAISS vector index
│   ├── rag.py                # Retrieval + generation logic
│   └── app.py                # Streamlit web app
│
├── tests/
│   └── test_retrieval.py     # Basic retrieval tests
│
├── vectorstore/              # Generated FAISS index (ignored in Git)
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Setup Instructions

### 1 Clone the Repository

```bash
git clone https://github.com/your-username/ERP_RAG_Assistant.git
cd ERP_RAG_Assistant
```

### 2 Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3 Install Dependencies

```bash
pip install -r requirements.txt
```

### 4 Set Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Running the Project

### Step 1: Ingest Documents

```bash
python src/ingest.py
```

This will:

* Read ERP PDFs
* Generate embeddings
* Build a FAISS vector index

### Step 2: Launch the Web App

```bash
streamlit run src/app.py
```

Open browser:

```
http://localhost:8501
```

---

## Sample Questions to Ask

* "How do I create a purchase order in the ERP system?"
* "What are the steps for invoice processing?"
* "Explain the approval workflow in ERP"
* "What is the role of finance module in ERP?"

---

## Why `vectorstore/` Is Not on GitHub

The FAISS index is:

* Auto-generated
* Machine-specific
* Rebuildable from source documents

Therefore, it is excluded via `.gitignore` and recreated using `ingest.py`.

This follows **industry best practices**.

---

## Future Enhancements

* Source citations with page numbers
* Role-based access control
* Support for multiple ERP domains
* Local LLM integration (offline mode)
* Deployment on cloud / internal servers

---

## Academic / Industry Relevance

This project demonstrates:

* Practical use of NLP in enterprise systems
* Retrieval-Augmented Generation (RAG)
* Vector databases in real-world applications
* Clean software engineering practices

Suitable for:

* Academic demos
* Internship evaluations
* ERP innovation prototypes

---

## Author

**Sinchana HS**
ERP RAG Assistant – Python Project

---
 *This project was built to demonstrate how AI can make ERP systems more intelligent, accessible, and user-friendly.*


