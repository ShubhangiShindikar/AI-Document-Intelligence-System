# 📄 AI Document Intelligence System

An AI-powered document analysis application that enables users to upload PDF documents, generate concise summaries, and ask natural language questions based on the document content using Retrieval-Augmented Generation (RAG).



## 🚀 Features

- 📂 Upload PDF documents
- 📑 Automatic document text extraction
- ✂️ Intelligent text chunking
- 🔍 Semantic search using FAISS
- 🤖 AI-powered question answering
- 📝 Automatic document summarization
- 💻 Interactive Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- LangChain
- FAISS
- Sentence Transformers
- PyPDF2 / PDF Processing


---

## 📁 Project Structure

```
AI-Document-Intelligence-System/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── utils/
│   ├── chatbot.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── pdf_loader.py
│   ├── pdf_generator.py
│   ├── summary.py
│   └── vector_store.py
│
└── images/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ShubhangiShindikar/AI-Document-Intelligence-System.git
```

### 2. Navigate to the Project

```bash
cd AI-Document-Intelligence-System
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

### 5. Run the Application

```bash
streamlit run app.py
```

---

## 📷 Screenshots

### Home Page

(Add screenshot here)

### Summary Generation

(Add screenshot here)

### Question Answering

(Add screenshot here)

---

## 💡 How It Works

1. Upload a PDF document.
2. Extract text from the document.
3. Split text into manageable chunks.
4. Generate vector embeddings.
5. Store embeddings in a FAISS vector database.
6. Retrieve the most relevant chunks based on the user's question.
7. Generate accurate answers using the Gemini API.
8. Generate concise summaries of the uploaded document.

---

## 🎯 Applications

- Research Paper Analysis
- Resume Screening
- Legal Document Review
- Academic Learning
- Business Report Analysis
- Document Search and Retrieval

---

## 🔮 Future Enhancements

- Multi-document support
- OCR for scanned PDFs
- Chat history
- User authentication
- Cloud deployment
- Support for Word and PowerPoint documents

---

## 👩‍💻 Author

**Shubhangi Shindikar**

GitHub: https://github.com/ShubhangiShindikar

LinkedIn: *(Add your LinkedIn profile URL here)*

---

## ⭐ If you found this project useful, consider giving it a star!
