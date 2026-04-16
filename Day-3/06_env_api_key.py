import os
from dotenv import load_dotenv

try:
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed, skip loading .env

if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("Loaded API key from environment.")
        print(f"API Key: {api_key}")  # Print only the first 4 characters for security
    else:
        print("API key not found. Please set OPENAI_API_KEY in your environment or .env file.")