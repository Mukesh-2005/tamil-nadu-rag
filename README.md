# 🏛️ Tamil Nadu Government Documents Q&A RAG System

An AI-powered question-answering system that retrieves information from Tamil Nadu government documents using Retrieval Augmented Generation (RAG).

## 🎯 Overview

This system allows users to ask questions about Tamil Nadu policies and get answers directly from government documents. It uses vector embeddings to find relevant passages and presents them to the user.

## ✨ Features

- ✅ **PDF Document Loading** - Automatically load and process PDF documents
- ✅ **Vector Embeddings** - Convert documents into searchable embeddings
- ✅ **Semantic Search** - Find relevant passages based on meaning, not just keywords
- ✅ **Web Interface** - User-friendly Gradio interface
- ✅ **REST API** - FastAPI endpoint for integration
- ✅ **Real Answers** - Retrieves actual content from documents

## 🔧 Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | FastAPI, Python |
| ML Framework | LangChain, PyTorch |
| Embeddings | Sentence Transformers |
| Vector DB | FAISS |
| UI | Gradio |
| PDF Processing | PyPDF, ReportLab |

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/Mukesh-2005/tamil-nadu-rag.git
cd tamil-nadu-rag

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 How to Run

### Step 1: Create Sample PDF
```bash
python create_pdf.py
```
Creates `sample.pdf` with Tamil Nadu government document content.

### Step 2: Build Vector Database
```bash
python build_rag.py
```
Converts PDF into embeddings and creates `vector_db/` folder.

### Step 3: Run Gradio Demo (Recommended)
```bash
python app_demo.py
```
Opens web interface at `http://localhost:7860`

### Step 4 (Optional): Run FastAPI
```bash
uvicorn rag_api:app
```
API available at `http://localhost:8000/docs`

## 📊 How It Works

1. **User Question**  
   ↓  
2. **Vector Embedding** (Sentence Transformers)  
   ↓  
3. **FAISS Similarity Search**  
   ↓  
4. **Retrieve Top 3 Passages**  
   ↓  
5. **Display Results to User**


## 💻 Usage Example

**Question:** "What benefits do farmers get?"

**Answer:** System retrieves from document:
- Farmers get free electricity for 8 hours daily
- Solar pump subsidies available for all registered farmers
- Training programs for sustainable agriculture provided

## 📁 Project Structure

```plaintext
tamil-nadu-rag/
├── create_pdf.py          # Create sample PDF document
├── build_rag.py           # Build vector database
├── rag_api.py             # FastAPI endpoints
├── app_demo.py            # Gradio web interface
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── sample.pdf             # Generated PDF (after run)
└── vector_db/             # Generated vector database (after run)
```


## 📋 Requirements

- Python 3.10+
- 2GB RAM minimum
- 500MB disk space (for models)

## 🎯 Results

| Metric | Value |
|--------|-------|
| PDF Loading | ✅ Success |
| Vector DB Creation | ✅ 2 chunks created |
| Search Accuracy | ✅ High (semantic) |
| Response Time | ✅ < 2 seconds |
| Q&A System | ✅ Fully Functional |

## 🌐 Live Demo

[Deployed on Hugging Face Spaces](https://huggingface.co/spaces/YOUR_USERNAME/tamil-nadu-rag)

## 🎓 What I Learned

- Building RAG systems with LangChain
- Vector embeddings and similarity search
- FastAPI REST API development
- Gradio web interface creation
- End-to-end ML system deployment

## 📈 Future Enhancements

- [ ] Support multiple PDF files
- [ ] Add LLM for generating answers (not just retrieval)
- [ ] Real Tamil Nadu government documents
- [ ] Multi-language support (Tamil + English)
- [ ] Database for conversation history
- [ ] User authentication

## 👤 Author

**Mukesh K**
- GitHub: [@Mukesh-2005](https://github.com/Mukesh-2005)
- LinkedIn: [Mukesh K](https://linkedin.com/in/mukesh-k)
- Email: starmukesh2005@gmail.com

## 📜 License

MIT License - feel free to use this project

## 🙏 Acknowledgments

- LangChain documentation
- Hugging Face community
- FAISS by Meta
- FastAPI framework

## 📞 Support

For issues or questions, create an issue on GitHub.

---

**Built during Month 4 learning phase - RAG & LLM Systems (May 2026)**
