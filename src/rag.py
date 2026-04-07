from langchain.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

# dummy data for demo
documents = [
    "Server downtime issue resolved by restart",
    "Database connection timeout fixed",
    "User access issue resolved by permission reset"
]

vector_db = FAISS.from_texts(documents, embeddings)

def retrieve_similar(query):
    results = vector_db.similarity_search(query, k=3)
    return [r.page_content for r in results]
