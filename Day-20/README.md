# 🕒 Day 20: Conversational AI & Chatbots

🏁 Goal: Build simple chatbots using OpenRouter with CLI and a Streamlit chat UI, including basic memory.

---

## 📚 Overview

You will:
- Create a CLI chatbot using OpenRouter
- Add short-term memory to maintain context
- Build a Streamlit chat interface with chat history

---

## ✅ Learning Objectives

1) Use OpenRouter via OpenAI client for conversational turns
2) Maintain conversation history for context-aware replies
3) Build a minimal web chat UI with Streamlit

---

## ⚙️ Quick Setup (Day-20 only)

- Install dependencies:
```bash
pip install -r Day-20/requirements.txt
```

- Create `.env` (repo root or `Day-20/`) with:
```bash
OPENROUTER_API_KEY=your_openrouter_api_key
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_MODEL_NAME=openai/gpt-3.5-turbo
```

---

## ▶️ How to Run

1) CLI Chat:
```bash
python Day-20/01_cli_chat.py
```

2) CLI Chat with Memory:
```bash
python Day-20/02_chat_memory.py
```

3) Streamlit Chat UI:
```bash
streamlit run Day-20/03_streamlit_chat.py
```

---

## 📁 Files

- `01_cli_chat.py`: Minimal single-turn CLI chatbot using OpenRouter
- `02_chat_memory.py`: Multi-turn CLI chatbot with short-term memory using OpenRouter
- `03_streamlit_chat.py`: Streamlit web chat with session-based memory using OpenRouter
- `openrouter_provider.py`: OpenRouter integration provider

---

## 🧪 Tips

- Keep system instructions concise and stable across turns
- Limit history length to stay within token budget
- Handle empty inputs and provide an `exit` command in CLI
- Use OpenRouter models for cost-effective LLM access
- Configure OpenRouter API key and model in `.env` file

---

Build helpful, context-aware chat experiences with OpenRouter!
