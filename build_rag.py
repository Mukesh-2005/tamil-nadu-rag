from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

print("Loading PDF...")
loader = PyPDFLoader("sample.pdf")
documents = loader.load()
print(f"✅ Loaded {len(documents)} pages")

print("\nSplitting into chunks...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)
print(f"✅ Split into {len(chunks)} chunks")

print("\nCreating embeddings...")
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Building vector database...")
vector_db = FAISS.from_documents(chunks, embeddings)
vector_db.save_local("vector_db")
print("✅ Vector DB created and saved!")