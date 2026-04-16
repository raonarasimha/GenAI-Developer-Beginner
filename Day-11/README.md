# 🕒 Day 11: Open Agentic SDK Fundamentals with OpenRouter

🏁 **Goal**: Understand and use Open Agentic SDK for advanced agent development with OpenRouter API.

---

## 📚 Overview

OpenAI Agents SDK is a lightweight, production-ready SDK for building agentic apps with a small set of primitives: Agents, Handoffs, Guardrails, and Sessions. It supports tools, tracing, and multi-agent orchestration out of the box. This implementation uses OpenRouter API to access multiple AI models through a single interface.

**Docs**: [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)

---

## ✅ Learning Objectives

### **1. Introduction to Open Agentic SDK (15 mins)**
* **Topics:**
    * What is Open Agentic SDK?
    * Agentic AI concepts
    * SDK architecture and components
    * Comparison with other agent frameworks
    * OpenRouter integration with custom model providers
* **Summary**: Understand the fundamentals of Open Agentic SDK and its role in building autonomous AI agents with OpenRouter.
* **Prompt**: "OpenAI Agents SDK enables you to create AI agents that can think, plan, and act autonomously."
* **Example**: [See `01_open_agentic_introduction.py`](./01_open_agentic_introduction.py)

---

### **2. Core Concepts & SDK Primitives (20 mins)**
* **Topics:**
    * Tools (function tools)
    * Sessions (automatic memory)
    * Orchestrating multiple agents
    * Custom model providers for OpenRouter
* **Summary**: Learn the core SDK primitives for building agents with OpenRouter.
* **Prompt**: "Understanding the architecture helps you build more effective and reliable agents."
* **Example**: [See `02_core_concepts.py`](./02_core_concepts.py)

---

### **3. Agent Creation & Configuration (20 mins)**
* **Topics:**
    * Creating basic agents
    * Agent personality and behavior
    * Configuration parameters
    * Agent initialization and setup
    * OpenRouter API setup with custom providers
* **Summary**: Master the process of creating and configuring autonomous agents with OpenRouter.
* **Prompt**: "Well-configured agents are the foundation of effective autonomous systems."
* **Example**: [See `03_agent_creation.py`](./03_agent_creation.py)

---

### **4. Tool Integration & Development (15 mins)**
* **Topics:**
    * Built-in tools and capabilities
    * Custom tool creation
    * Tool registration and management
    * Tool execution and error handling
    * Multi-model tool usage with OpenRouter
* **Summary**: Extend agent capabilities through custom tools and integrations with OpenRouter.
* **Prompt**: "Tools give agents the ability to interact with the real world and perform actions."
* **Example**: [See `04_tool_integration.py`](./04_tool_integration.py)

---

### **5. Agent Workflows & Execution (20 mins)**
* **Topics:**
    * Workflow definition and design
    * Task planning and execution
    * Multi-step reasoning
    * Workflow monitoring and debugging
    * OpenRouter performance optimization
* **Summary**: Build complex agent workflows that can handle sophisticated tasks with OpenRouter.
* **Prompt**: "Workflows orchestrate how agents think, plan, and execute tasks."
* **Example**: [See `05_agent_workflows.py`](./05_agent_workflows.py)

---

### **6. Advanced Features & Best Practices (10 mins)**
* **Topics:**
    * Memory management and persistence
    * Error handling and recovery
    * Performance optimization
    * Security considerations
    * Multi-agent orchestration with custom providers
* **Summary**: Apply advanced features and best practices for production-ready agents with OpenRouter.
* **Prompt**: "Advanced features make your agents more robust and production-ready."
* **Example**: [See `06_advanced_features.py`](./06_advanced_features.py)

---

## ⚙️ Quick Setup (Day-11 only)

### **1. Install Dependencies**
```bash
pip install -r Day-11/requirements.txt
```

### **2. Set Up Environment Variables**
Create `.env` (repo root or `Day-11/`) with:
```bash
OPENAI_API_KEY=your_openrouter_api_key
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL_NAME=moonshotai/kimi-k2:free
```

### **3. Run Examples**
Run any example:
```bash
python Day-11/01_open_agentic_introduction.py
```

---

## 🔧 How It Works

### **Custom Model Provider**
The Open Agentic SDK requires custom model providers for non-standard APIs like OpenRouter. We've implemented:

- **`openrouter_provider.py`**: Custom model provider that wraps OpenRouter API
- **`OpenRouterModelProvider`**: Class that handles OpenRouter-specific configuration
- **`RunConfig`**: Used to specify the custom provider for each agent run

### **Key Components**
```python
# Create custom provider
provider = create_openrouter_provider()

# Use with agents
agent = Agent(name="Assistant", model=provider.model_name)

# Run with custom provider
result = Runner.run_sync(
    agent, 
    "Your prompt",
    run_config=RunConfig(model_provider=provider)
)
```

### **Tool Integration**
```python
from agents.tool import function_tool

@function_tool
def my_tool(text: str) -> str:
    """Tool description."""
    return text.upper()
```

---

## 🔧 Troubleshooting

### **Common Issues**

#### **1. "Configuration error"**
- **Cause**: Missing environment variables
- **Solution**: Ensure all three variables are set in your `.env` file

#### **2. "API key invalid"**
- **Cause**: Invalid or expired OpenRouter API key
- **Solution**: Get a new API key from [OpenRouter](https://openrouter.ai/)

#### **3. "Connection timeout"**
- **Cause**: Network issues or incorrect API base URL
- **Solution**: Verify internet connection and use `https://openrouter.ai/api/v1`

#### **4. "Unknown prefix" error**
- **Cause**: Open Agentic SDK doesn't recognize model prefixes
- **Solution**: Use the custom model provider (already implemented)

#### **5. "TypeError: 'module' object is not callable"**
- **Cause**: Incorrect tool decorator import
- **Solution**: Use `from agents.tool import function_tool` instead of `from agents import tool`

### **Recommended Model Names**
```bash
# Free models (with credits)
OPENAI_MODEL_NAME=moonshotai/kimi-k2:free
OPENAI_MODEL_NAME=openai/gpt-3.5-turbo
OPENAI_MODEL_NAME=anthropic/claude-3-haiku

# Paid models (better performance)
OPENAI_MODEL_NAME=openai/gpt-4
OPENAI_MODEL_NAME=anthropic/claude-3-sonnet
OPENAI_MODEL_NAME=google/gemini-pro-1.5
```

---

## 📖 Key Concepts

### **Open Agentic SDK Architecture**
- **Agents**: Autonomous AI entities with reasoning capabilities
- **Tools**: Functions and APIs that agents can use
- **Workflows**: Orchestrated sequences of agent actions
- **Memory**: Persistent storage for agent state and context
- **Reasoning**: AI-powered decision making and planning
- **Custom Model Providers**: Enable integration with non-standard APIs like OpenRouter

### **Agent Types**
- **Task-Oriented**: Focused on specific objectives
- **Conversational**: Interactive and responsive
- **Analytical**: Data processing and analysis
- **Creative**: Content generation and ideation
- **Automation**: Process automation and workflow management

### **Tool Categories**
- **Information Retrieval**: Search, lookup, and data access
- **Computation**: Calculations, processing, and analysis
- **Communication**: APIs, messaging, and notifications
- **File Operations**: Reading, writing, and file management
- **System Integration**: External service connections

### **OpenRouter Benefits**
- **Model Flexibility**: Switch between different AI models
- **Cost Optimization**: Choose models based on task requirements
- **Performance**: Access to latest model versions
- **Unified API**: Single interface for multiple providers

---

## 🛠️ Tools & Resources

- **Open Agentic SDK Documentation**: Official guides and tutorials
- **Open Agentic SDK GitHub**: Source code and examples
- **Custom Model Provider Example**: [Reference Implementation](https://github.com/openai/openai-agents-python/blob/main/examples/model_providers/custom_example_provider.py)
- **Community Forums**: Support and discussions
- **Tutorial Videos**: Step-by-step learning resources
- **OpenRouter Documentation**: API reference and model list

---

## 🚀 Next Steps

- Explore advanced agent patterns
- Build multi-agent systems
- Integrate with external services
- Deploy production agent applications
- Optimize with different OpenRouter models

---

## ✅ **Status: All Examples Working!**

All Day 11 examples are now successfully running with OpenRouter integration:

- ✅ **01_open_agentic_introduction.py**: Basic agent with haiku generation
- ✅ **02_core_concepts.py**: Conversation flow demonstration
- ✅ **03_agent_creation.py**: Agent planning and task execution
- ✅ **04_tool_integration.py**: Custom tools with echo and uppercase functions
- ✅ **05_agent_workflows.py**: Multi-step workflow execution
- ✅ **06_advanced_features.py**: Router pattern and agent-as-tool demonstration

---

*Open Agentic SDK empowers you to create truly autonomous AI agents powered by OpenRouter! 🤖🧠*
