from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from pathlib import Path

# Embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load FAISS index
VECTORSTORE_PATH = Path("vectorstore")

db = FAISS.load_local(
    VECTORSTORE_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k": 3})



def answer_question(query: str):
    docs = retriever.invoke(query)  # ✅ FIXED LINE

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
    You are an ERP assistant. Use the context below to answer the question.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    answer = (
    "Based on the ERP manual:\n\n"
    + "\n\n".join(doc.page_content[:500] for doc in docs)
)

    sources = [doc.metadata.get("source", "") for doc in docs]

    return answer, sources





