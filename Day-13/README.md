# 🕒 Day 13: Basic RAG Implementation

🏁 Goal: Build a simple Retrieval-Augmented Generation (RAG) pipeline that indexes local documents and answers questions using retrieved context + an LLM.

---

## 📚 Overview

You will:
- Load local text files
- Chunk and embed them with OpenAI embeddings
- Store embeddings in an in-memory FAISS index
- Retrieve top-k chunks for a query
- Ask an LLM to answer using only the retrieved context

---

## ✅ Learning Objectives

1) Document ingestion and chunking
2) Embedding and vector indexing (FAISS)
3) Retrieval and context construction
4) Answer generation with OpenRouter LLMs via OpenAI Chat Completions API

---

## ⚙️ Quick Setup (Day-13 only)

- **Activate the project virtual environment:**
```bash
# From project root
.\venv\Scripts\Activate.ps1
```

- **Install dependencies:**
```bash
pip install -r Day-13/requirements.txt
```

- Create `.env` (repo root or `Day-13/`) with:
```bash
# Required for OpenRouter LLM
OPENROUTER_API_KEY=your_openrouter_api_key
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_MODEL_NAME=meta-llama/llama-4-maverick:free
```

- Sample docs: `Day-13/assets/` are included. Feel free to add more `.txt` files.

---

## ▶️ How to Run

**First, test your OpenRouter integration:**
```bash
python Day-13/test_openrouter_integration.py
```

**Then run the RAG system:**

1) Build index and answer one question (CLI):
```bash
python Day-13/01_build_index.py
```

2) Simple RAG Q&A (CLI):
```bash
python Day-13/02_simple_rag.py
```

3) Streamlit RAG App:
```bash
streamlit run Day-13/03_streamlit_rag_app.py
```

---

## 📁 Files

- `rag_utils.py`: Shared helpers (load, chunk, embed, build index, retrieve, answer)
- `01_build_index.py`: Minimal demo building index and answering
- `02_simple_rag.py`: Simple RAG CLI
- `03_streamlit_rag_app.py`: Small web app for RAG Q&A
- `test_openrouter_integration.py`: Test script to verify OpenRouter setup
- `assets/`: Sample `.txt` documents

---

## 🧪 Tips

- Keep chunks ~500–1000 characters with ~20–30% overlap
- **Note**: OpenRouter does NOT support embeddings - the system uses mock embeddings
- **Mock embeddings work fine** for RAG demonstration and learning purposes
- Use OpenRouter models (like `meta-llama/llama-4-maverick:free`) for cost-effective answers
- Limit context size to avoid token overflow
- Configure OpenRouter API key and model in `.env` file
- **Note**: OpenRouter API keys have usage limits - check your account settings if you hit limits
- **Always use the project's virtual environment** for consistent package management

---

Happy building!


