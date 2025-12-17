import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "erp_manuals")
INDEX_PATH = os.path.join(BASE_DIR, "faiss_index")

documents = []

for filename in os.listdir(DATA_PATH):
    file_path = os.path.join(DATA_PATH, filename)

    if filename.lower().endswith(".pdf"):
        loader = PyPDFLoader(file_path)
        documents.extend(loader.load())

    elif filename.lower().endswith(".txt"):
        loader = TextLoader(file_path)
        documents.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local(INDEX_PATH)

print("✅ ERP documents indexed successfully")
