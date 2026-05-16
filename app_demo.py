import gradio as gr
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

print("Loading RAG...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_db = FAISS.load_local("vector_db", embeddings, allow_dangerous_deserialization=True)
print("✅ RAG ready!")

def answer_question(question):
    # Get relevant documents from PDF
    docs = vector_db.similarity_search(question, k=3)
    
    # Return relevant passages
    answer = "Based on the document:\n\n"
    for i, doc in enumerate(docs, 1):
        answer += f"{i}. {doc.page_content}\n\n"
    
    return answer

demo = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(label="Ask a question"),
    outputs=gr.Textbox(label="Answer"),
    title="🏛️ Tamil Nadu Q&A",
    description="Ask about TN policies"
)

if __name__ == "__main__":
    demo.launch(share=True)