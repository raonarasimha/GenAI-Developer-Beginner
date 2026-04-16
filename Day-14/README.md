# 🕒 Day 14: Model Context Protocol (MCP)

🏁 Goal: Run a minimal MCP server locally and call it from an agent to use external tools.

---

## 📚 Overview

MCP standardizes how models call tools and access context (files, APIs, DBs). In this day you will:
- Run a tiny MCP-like stdio server exposing simple tools (list files, read text)
- Connect an agent script to the server and use the tool output as context for an LLM

---

## ✅ Learning Objectives

1) Understand MCP fundamentals
2) Run a minimal MCP server (stdio)
3) Integrate with an LLM client and use tool outputs
4) Use OpenRouter LLMs via OpenAI Chat Completions API

---

## ⚙️ Quick Setup (Day-14 only)

- Install dependencies:
```bash
pip install -r Day-14/requirements.txt
```

- Create `.env` (repo root or `Day-14/`) with:
```bash
OPENROUTER_API_KEY=your_openrouter_api_key
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_MODEL_NAME=openai/gpt-3.5-turbo
```

---

## ▶️ How to Run

**First, test your OpenRouter integration:**
```bash
python Day-14/test_openrouter_integration.py
```

**Then run the MCP system:**

1) Start the MCP server (in one terminal):
```bash
python Day-14/01_mcp_server.py
```

2) In another terminal, run the agent integration demo:
```bash
python Day-14/02_agents_mcp_integration.py
```

If MCP integration is unavailable in your environment, the script prints clear guidance.

---

## 📁 Files

- `01_mcp_server.py`: Minimal stdio JSON server exposing tools:
  - `list_dir`: List files in `Day-14/assets`
  - `read_text`: Read a `.txt` file from `Day-14/assets`
- `02_agents_mcp_integration.py`: Calls the server and summarizes tool outputs via OpenRouter LLMs
- `openrouter_provider.py`: OpenRouter integration provider
- `test_openrouter_integration.py`: Test script to verify OpenRouter setup
- `assets/`: Test files for server tools

---

## 🧪 Tips

- Prefer stdio for local development
- Keep tool I/O small and text-only initially
- Validate file paths to avoid escaping the allowed directory
- Use OpenRouter models for cost-effective LLM access
- Configure OpenRouter API key and model in `.env` file

---

Happy exploring MCP!
