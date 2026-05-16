from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Tamil Nadu RAG")

class Question(BaseModel):
    text: str

@app.post("/ask")
def ask_question(q: Question):
    return {
        "question": q.text, 
        "answer": "RAG system ready. Test in progress."
    }

@app.get("/health")
def health():
    return {"status": "ok"}