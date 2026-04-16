# 🕒 Day 9: LangChain Fundamentals & Agents

🏁 **Goal**: Build applications using LangChain framework and create intelligent agents.

---

## 📚 Overview

LangChain is a powerful framework for building applications with Large Language Models (LLMs). This day covers core concepts, memory management, and agent creation using modern LangChain patterns.

### **OpenRouter Integration**
All examples use OpenRouter API for access to multiple AI models through a single interface.

---

## ✅ Learning Objectives

### **1. LangChain Introduction** 
* **File**: `01_langchain_introduction.py`
* **Topics**: Basic prompt templates, modern LCEL syntax, OpenRouter setup
* **Duration**: 15 mins

### **2. Advanced Components**
* **File**: `02_langchain_components.py`
* **Topics**: Chat prompts, structured output, multi-step chains
* **Duration**: 20 mins

### **3. Memory Management**
* **File**: `03_memory_management.py`
* **Topics**: Conversation memory, context preservation
* **Duration**: 15 mins

### **4. Basic Agents**
* **File**: `04_basic_agents.py`
* **Topics**: Agent creation, tool integration, modern approach
* **Duration**: 15 mins

### **5. Agent Tools**
* **File**: `05_agent_tools.py`
* **Topics**: Custom tools, multiple tool integration
* **Duration**: 15 mins

---

## ⚙️ Quick Setup

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Create `.env` file**:
```bash
OPEN_ROUTER_API_KEY=your_openrouter_api_key
BASE_URL=https://openrouter.ai/api/v1
OPEN_ROUTER_MODEL=openai/gpt-oss-20b:free
```

3. **Get OpenRouter API key**:
   - Visit [https://openrouter.ai/keys](https://openrouter.ai/keys)
   - Sign up and get your API key

4. **Run examples**:
```bash
python 01_langchain_introduction.py
python 02_langchain_components.py
python 03_memory_management.py
python 04_basic_agents.py
python 05_agent_tools.py
```

---

## 🔧 Key Features

- **Modern LangChain**: Uses latest LCEL syntax and patterns
- **OpenRouter Integration**: Access to multiple AI models
- **Memory Systems**: Conversation context preservation
- **Agent Tools**: Custom tool creation and integration
- **Error-Free**: No deprecation warnings or parsing errors

---

## 📖 Key Concepts

### **LangChain Architecture**
- **LLMs/Chat Models**: The AI models that generate responses
- **Prompts**: Instructions and context for the models
- **Chains**: Sequences of operations and model calls
- **Agents**: Autonomous systems that can use tools
- **Memory**: Systems for maintaining state and context
- **Tools**: External functions and APIs agents can use

### **Agent Types**
- **Zero-shot ReAct**: Uses reasoning and action
- **Conversational**: Maintains conversation context
- **Structured**: Uses structured output formats
- **Custom**: Built for specific use cases

### **Memory Types**
- **Buffer**: Stores all messages
- **Summary**: Maintains conversation summaries
- **Entity**: Tracks specific entities
- **Vector**: Uses embeddings for similarity

---

## 📖 What You'll Learn

- LangChain fundamentals and modern patterns
- Memory management for conversations
- Agent creation with tool integration
- Custom tool development
- OpenRouter API usage

---

*Build intelligent AI applications with LangChain! 🚀*
