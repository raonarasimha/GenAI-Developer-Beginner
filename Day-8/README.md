# 🕒 Day 8: Prompt Engineering & Optimization

🏁 **Goal**: Master the art of writing effective prompts for optimal AI model performance.

---

## 📚 Overview

Prompt engineering is the practice of designing and optimizing inputs to AI models to achieve desired outputs. This skill is fundamental to working with any LLM and directly impacts the quality of your AI applications.

---

## ⚙️ Quick Setup (install and configure)

Follow this before running any samples (similar to Day-3 style):

- Install dependencies (Day-8 only):
```bash
pip install -r requirements.txt
```

- Create a `.env` file (repo root or inside `Day-8/`) with:
```bash
OPENAI_API_KEY=your_openai_api_key
BASE_URL=https://openrouter.ai/api/v1
```

**Note**: The `BASE_URL` environment variable is required and should be set to `https://openrouter.ai/api/v1` to use the OpenRouter API service.

- Run a sample to verify:
```bash
python Day-8/01_prompt_engineering_basics.py
```

If you see a message asking to set `OPENAI_API_KEY`, ensure your `.env` file exists and the key is correct.

---

## ✅ Learning Objectives

### **1. Understanding Prompt Engineering Fundamentals (15 mins)**
* **Topics:**
    * What is prompt engineering?
    * Why prompt engineering matters
    * Basic prompt structure and components
* **Summary**: Learn the foundational concepts of prompt engineering and why it's crucial for AI applications.
* **Prompt**: "A well-crafted prompt is like giving clear instructions to a very smart assistant."
* **Example**: [See `01_prompt_engineering_basics.py`](./01_prompt_engineering_basics.py)

---

### **2. Basic Prompt Patterns (20 mins)**
* **Topics:**
    * Zero-shot prompting
    * Few-shot prompting with examples
    * Chain-of-thought prompting
    * Role-based prompting
* **Summary**: Master fundamental prompt patterns that work across different LLMs.
* **Prompt**: "Different patterns serve different purposes - choose the right tool for the job."
* **Example**: [See `02_basic_prompt_patterns.py`](./02_basic_prompt_patterns.py)

---

### **3. Advanced Prompt Techniques (20 mins)**
* **Topics:**
    * System prompts vs user prompts
    * Temperature and sampling parameters
    * Max tokens and response length control
    * Context window management
* **Summary**: Learn advanced techniques to fine-tune model behavior and responses.
* **Prompt**: "Advanced techniques give you precise control over AI model behavior."
* **Example**: [See `03_advanced_prompt_techniques.py`](./03_advanced_prompt_techniques.py)

---

### **4. Prompt Optimization Strategies (15 mins)**
* **Topics:**
    * Iterative prompt refinement
    * A/B testing prompts
    * Error analysis and debugging
    * Performance metrics for prompts
* **Summary**: Develop systematic approaches to improve prompt performance.
* **Prompt**: "Optimization is an iterative process - test, measure, improve, repeat."
* **Example**: [See `04_prompt_optimization.py`](./04_prompt_optimization.py)

---

### **5. Real-World Prompt Examples (20 mins)**
* **Topics:**
    * Content generation prompts
    * Code generation prompts
    * Analysis and summarization prompts
    * Creative writing prompts
* **Summary**: Apply prompt engineering to common real-world use cases.
* **Prompt**: "Real-world examples show how theory translates to practical applications."
* **Example**: [See `05_real_world_prompts.py`](./05_real_world_prompts.py)

---

### **6. Prompt Engineering Best Practices (10 mins)**
* **Topics:**
    * Clarity and specificity
    * Avoiding ambiguity
    * Handling edge cases
    * Security considerations
* **Summary**: Learn best practices to create robust, secure, and effective prompts.
* **Prompt**: "Best practices help you avoid common pitfalls and create better prompts."
* **Example**: [See `06_best_practices.py`](./06_best_practices.py)

---

## 🏠 Practice Exercises

### **Exercise 1: Prompt Comparison**
Compare different prompt approaches for the same task using the examples in the Python files.

### **Exercise 2: Prompt Optimization**
Optimize a given prompt for better results by testing variations.

### **Exercise 3: Creative Prompt Design**
Design prompts for creative tasks like storytelling and poetry.

---

## 📖 Key Concepts

### **Prompt Components**
- **System Message**: Sets the context and behavior
- **User Message**: The actual request or question
- **Examples**: Few-shot learning demonstrations
- **Constraints**: Limitations and requirements

### **Common Patterns**
- **Zero-shot**: Direct question without examples
- **Few-shot**: Question with 2-3 examples
- **Chain-of-thought**: Step-by-step reasoning
- **Role-based**: Assigning specific personas

### **Optimization Metrics**
- **Accuracy**: Correctness of responses
- **Consistency**: Reliability across runs
- **Efficiency**: Token usage and cost
- **User Satisfaction**: Quality of experience

---

## 🛠️ Tools & Resources

- **OpenAI Playground**: Interactive prompt testing
- **LangChain Prompt Templates**: Structured prompt management
- **Prompt Engineering Guide**: Best practices and examples
- **A/B Testing Tools**: Compare prompt performance

---

## 🚀 Next Steps

- Practice with different LLM models
- Experiment with various prompt patterns
- Build a prompt library for common tasks
- Learn about prompt injection and security

---

*Mastering prompt engineering is the foundation of effective AI application development! 🎯*
