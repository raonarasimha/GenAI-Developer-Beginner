# 🕓 Hour 4: GenAI Modules, CLI, API, UI, and Practice Challenges



### ✅ 1. 💻 FastAPI: Create a Simple API for Your Bot (10 mins)
* **Topics:**
    * Install and import FastAPI: `pip install fastapi uvicorn`
    * Run with: `uvicorn 01_fastapi_app:app --reload`
    * Install vs code extension : REST Client
    * Define POST route to receive prompt
    * Return GenAI response as JSON
    * Example:
      ```python
      from fastapi import FastAPI, Request
      app = FastAPI()

      @app.post("/chat")
      async def chat(req: Request):
          data = await req.json()
          response = GenAIChatBot().ask(data["prompt"])
          return {"response": response}
      ```
* **Summary:** Wrap your GenAI logic in a lightweight REST API with just a few lines.
* **Prompt:** "FastAPI lets you turn your bot into an API in minutes — ready for production."
* **Example:** [See `01_fastapi_app.py`](./01_fastapi_app.py)

---

### ✅ 2. 🖼️ Streamlit: Build a Simple UI for Your Bot (10 mins)
* **Topics:**
    * Install and import Streamlit:  
      ```bash
      pip install streamlit
      ```
    * Run the app:  
      ```bash
      streamlit run 02_streamlit_app.py
      ```
    * Create a basic textbox + button interface
    * Display OpenAI responses below
    * Example:
      ```python
      import streamlit as st
      st.title("GenAI Chatbot")
      prompt = st.text_input("Enter your prompt:")
      if st.button("Ask"):
          response = GenAIChatBot().ask(prompt)
          st.write(response)
      ```
* **Summary:** Build a minimal, beautiful UI for your GenAI app in minutes.
* **Prompt:** "Streamlit helps you share AI tools visually — no web dev required."
* **Example:** [See `02_streamlit_app.py`](./02_streamlit_app.py)

---

### ✅ 3. 📚 Python Modules: Import, Use, and Create Your Own (10 mins)
* **Topics:**
    * What is a Python module? (`import math`, `import os`, etc.)
    * How to use built-in modules (e.g., `random`, `datetime`)
    * How to create your own module (save code in `.py` file and import it)
    * Example:
      ```python
      # Using a built-in module
      import random
      print(random.randint(1, 10))

      # Creating your own module
      # mymodule.py
      def greet(name):
          return f"Hello, {name}!"

      # main.py
      from mymodule import greet
      print(greet("Alice"))
      ```
* **Summary:** Python modules help you organize code, reuse logic, and use powerful built-in features.
* **Prompt:** "Modules are Python’s way to organize and share code — both built-in and your own."
* **Example:** [See `03_modules/`](./03_modules/main.py)

---

## 🏠 Practice & Homework: Python Mini Challenges

Try these 5 sample problems to reinforce your learning. Each has a starter file:

1. **Reverse the Characters in a String**  
   [Try `python hw01_reverse_string.py`](./hw01_reverse_string.py)
2. **Count the Characters in the Last Word**  
   [Try `python hw02_count_last_word.py`](./hw02_count_last_word.py)
3. **Sum All Numbers in a List**  
   [Try `python hw03_sum_list.py`](./hw03_sum_list.py)
4. **Find the Largest Number in a List**  
   [Try `python hw04_largest_number.py`](./hw04_largest_number.py)
5. **Check if a Number is Prime**  
   [Try `python hw05_is_prime.py`](./hw05_is_prime.py)

---

### ✅ 6. Wrap-up & Next Steps (5 mins)
* **Topics:**
    * Recap: Data → Classes → APIs → CLI → API → UI
    * Share learning paths: FastAPI docs, Streamlit tutorials, OpenAI cookbooks, LangChain
* **Summary:** You’ve now built a full GenAI Python app — both API and UI powered.
* **Prompt:** "You’ve gone from zero to GenAI hero — now keep building, learning, and deploying!"
