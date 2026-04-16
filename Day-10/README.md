# 🕒 Day 10: CrewAI: Multi-Agent Systems with OpenRouter

🏁 **Goal**: Create collaborative multi-agent systems with role-based agents using OpenRouter API.

---

## 📚 Overview

CrewAI is a framework for orchestrating role-playing autonomous AI agents. It enables you to create teams of specialized agents that work together to accomplish complex tasks through collaboration and task delegation. This implementation uses OpenRouter API to access multiple AI models through a single interface.

---

## ✅ Learning Objectives

### **1. Introduction to CrewAI (15 mins)**
* **Topics:**
    * What is CrewAI?
    * Multi-agent systems concept
    * Role-based agent architecture
    * CrewAI vs other frameworks
    * OpenRouter integration
* **Summary**: Understand the fundamentals of CrewAI and multi-agent collaboration with OpenRouter.
* **Prompt**: "CrewAI is like having a team of specialized AI assistants working together."
* **Example**: [See `01_crewai_introduction.py`](./01_crewai_introduction.py)

---

### **2. Agent Creation & Roles (20 mins)**
* **Topics:**
    * Creating agents with specific roles
    * Agent capabilities and tools
    * Role definition and specialization
    * Agent personality and behavior
    * OpenRouter model configuration
* **Summary**: Learn how to create specialized agents with defined roles and capabilities using OpenRouter.
* **Prompt**: "Each agent has a specific role and expertise - like team members in a company."
* **Example**: [See `02_agent_creation.py`](./02_agent_creation.py)

---

### **3. Task Definition & Delegation (20 mins)**
* **Topics:**
    * Task creation and description
    * Task dependencies and sequencing
    * Task delegation strategies
    * Task validation and completion
    * Multi-model task execution
* **Summary**: Master task management and delegation in multi-agent systems with OpenRouter.
* **Prompt**: "Tasks are like projects that get broken down and assigned to the right agents."
* **Example**: [See `03_task_management.py`](./03_task_management.py)

---

### **4. Crew Formation & Orchestration (15 mins)**
* **Topics:**
    * Crew creation and configuration
    * Agent coordination and communication
    * Process management (sequential vs parallel)
    * Crew execution and monitoring
    * OpenRouter API optimization
* **Summary**: Build and orchestrate teams of agents working together using OpenRouter.
* **Prompt**: "Crews are like project teams - they coordinate and collaborate to achieve goals."
* **Example**: [See `04_crew_orchestration.py`](./04_crew_orchestration.py)

---

### **5. Advanced CrewAI Features (20 mins)**
* **Topics:**
    * Custom tools and integrations
    * Memory and context sharing
    * Error handling and recovery
    * Performance optimization
    * OpenRouter model switching
* **Summary**: Explore advanced features for building robust multi-agent systems with OpenRouter.
* **Prompt**: "Advanced features make your agent teams more powerful and reliable."
* **Example**: [See `05_advanced_features.py`](./05_advanced_features.py)

---

### **6. Real-World Applications (10 mins)**
* **Topics:**
    * Content creation workflows
    * Research and analysis teams
    * Customer service automation
    * Project management automation
    * Multi-model deployment strategies
* **Summary**: Apply CrewAI to practical business scenarios using OpenRouter.
* **Prompt**: "Real-world applications show how multi-agent systems solve actual problems."
* **Example**: [See `06_real_world_applications.py`](./06_real_world_applications.py)

---

## ⚙️ Quick Setup (Day-10 only)

### **1. Install Dependencies**
```bash
pip install -r Day-10/requirements.txt
```

### **2. Set Up Environment Variables**
Create `.env` (repo root or `Day-10/`) with:
```bash
OPENROUTER_API_KEY=your_openrouter_api_key
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_MODEL_NAME=openai/gpt-3.5-turbo
```

### **3. Run Examples**
Run any example:
```bash
python Day-10/01_crewai_introduction.py
```

---

## 🔧 Troubleshooting

### **Common Issues**

#### **1. "LLM Provider NOT provided" Error**
- **Cause**: Incorrect model name format or unsupported model
- **Solution**: Use a supported model format like `openai/gpt-3.5-turbo`

#### **2. "Configuration error"**
- **Cause**: Missing environment variables
- **Solution**: Ensure all three variables are set in your `.env` file

#### **3. "API key invalid"**
- **Cause**: Invalid or expired OpenRouter API key
- **Solution**: Get a new API key from [OpenRouter](https://openrouter.ai/)

#### **4. "Connection timeout"**
- **Cause**: Network issues or incorrect API base URL
- **Solution**: Verify internet connection and use `https://openrouter.ai/api/v1`

### **Recommended Model Names**
```bash
# Free models (with credits)
OPENAI_MODEL_NAME=openai/gpt-3.5-turbo
OPENAI_MODEL_NAME=anthropic/claude-3-haiku
OPENAI_MODEL_NAME=google/gemini-pro

# Paid models (better performance)
OPENAI_MODEL_NAME=openai/gpt-4
OPENAI_MODEL_NAME=anthropic/claude-3-sonnet
OPENAI_MODEL_NAME=google/gemini-pro-1.5
```

---

## 📖 Key Concepts

### **CrewAI Architecture**
- **Agents**: Specialized AI assistants with specific roles
- **Tasks**: Work items that agents need to complete
- **Crews**: Teams of agents working together
- **Processes**: How agents coordinate and execute tasks
- **Tools**: Capabilities that agents can use
- **OpenRouter Integration**: Access to multiple AI models through single API

### **Agent Types**
- **Researcher**: Gathers and analyzes information
- **Writer**: Creates content and documents
- **Reviewer**: Evaluates and improves work
- **Coordinator**: Manages workflow and communication
- **Specialist**: Domain-specific expertise

### **Process Types**
- **Sequential**: Tasks executed one after another
- **Parallel**: Multiple tasks executed simultaneously
- **Hierarchical**: Tasks with dependencies and priorities
- **Collaborative**: Agents working together on shared tasks

### **OpenRouter Benefits**
- **Model Flexibility**: Switch between different AI models
- **Cost Optimization**: Choose models based on task requirements
- **Performance**: Access to latest model versions
- **Unified API**: Single interface for multiple providers

---

## 🛠️ Tools & Resources

- **CrewAI Documentation**: Official guides and tutorials
- **CrewAI GitHub**: Source code and examples
- **CrewAI Discord**: Community support and discussions
- **CrewAI Templates**: Pre-built crew configurations
- **OpenRouter Documentation**: API reference and model list

---

## 🚀 Next Steps

- Explore advanced CrewAI features
- Build custom tools and integrations
- Optimize crew performance with different models
- Deploy CrewAI applications with OpenRouter
- Experiment with model switching strategies

---

*CrewAI enables you to build intelligent teams of AI agents powered by OpenRouter! 🤖👥*
