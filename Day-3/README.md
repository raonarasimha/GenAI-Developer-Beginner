# 🕒 Hour 3: GenAI Integration, Data Handling, Tooling

🤖 **Goal:** Learn how to handle data, call GenAI APIs, and organize code for your AI app.

---

### ✅ 1. Lists & Dicts for Data (10 mins)
* **Topics:**
    * Create, access, loop over lists and dicts
    * Use for, if, and data functions (append, keys, etc.)
* **Summary:** Work with Python's most common data structures for storing and organizing information.
* **Prompt:** "Lists and dicts are your go-to tools for structured data in Python."
* **Example:** [Run `python 01_lists_dicts.py`](./01_lists_dicts.py)

---

### ✅ 2. JSON & File I/O (10 mins)
* **First:** The `json` module is built-in, but if you use other file formats (like Excel, CSV), you may need to install extra packages (e.g., `pip install pandas`).
* **Topics:**
    * Read/write JSON with `json.dumps()` and `json.loads()`
    * Save and read .json or .txt files with `open()`
* **Summary:** Read/write data files and understand how to work with API-compatible formats.
* **Prompt:** "APIs talk in JSON — learn how to read, write, and transform it."
* **Example:** [Run `python 02_json_fileio.py`](./02_json_fileio.py)

---

### ✅ 3. Using Libraries & APIs (10 mins)
* **First:**  
  - For HTTP requests: `pip install requests`  
  - For OpenAI: `pip install openai`
* **Topics:**
    * `import`, `pip install`
    * Use `requests` or `openai` to make API calls
    * Basic request/response handling
* **Summary:** Learn to interact with services like OpenAI and process responses.
* **Prompt:** "Use libraries to do powerful things — AI, HTTP requests, and more."
* **Example:** [Run `python 03_libraries_apis.py`](./03_libraries_apis.py)

---

### ✅ 4. Mini GenAI App (Class-Based) (15 mins)
* **Topics:**
    * Build a `GenAIChatBot` class
    * Method to send prompt → receive OpenAI reply
    * Handle API key securely
* **Summary:** Create a reusable class that powers your GenAI backend logic.
* **Prompt:** "This class is the heart of your chatbot or tool."
* **Example:** [Run `python 04_genai_chatbot.py`](./04_genai_chatbot.py)

---

### ✅ 5. CLI Chatbot Using input() (5 mins)
* **Topics:**
    * Loop for continuous prompts
    * Use `input()` to take user text
    * Send to `GenAIChatBot`
* **Summary:** Build an interactive terminal-based GenAI chatbot.
* **Prompt:** "Turn your code into a usable chatbot app from the terminal."
* **Example:** [Run `python 05_cli_chatbot.py`](./05_cli_chatbot.py)

---

### ✅ 6. Load API Key from .env (5 mins)
* **Topics:**
    * Create `.env` file
    * Install and import: pip install python-dotenv
    * Use `os.getenv()` to access API key
* **Summary:** Keep secrets out of your code using environment variables.
* **Prompt:** "Security first — never hardcode secrets in your app."
* **Example:** [Run `python 06_env_api_key.py`](./06_env_api_key.py)

---