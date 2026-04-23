import json
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

def create_vectorstore():
    with open("data/knowledge.json") as f:
        data = json.load(f)

    docs = [Document(page_content=str(v)) for v in data.values()]

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    return FAISS.from_documents(docs, embeddings)