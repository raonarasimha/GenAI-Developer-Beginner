"""
Streamlit chat UI with session-based memory using OpenRouter via OpenAI client.
"""

import os
import streamlit as st
from dotenv import load_dotenv


def generate_reply(client, model_name: str, system: str, history: list[tuple[str, str]], user: str) -> str:
    # Build messages with conversation history
    messages = [{"role": "system", "content": system}]
    
    # Add conversation history
    for u, a in history:
        messages.append({"role": "user", "content": u})
        messages.append({"role": "assistant", "content": a})
    
    # Add current user message
    messages.append({"role": "user", "content": user})
    
    try:
        resp = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.6,
            max_tokens=1000
        )
        
        if resp.choices and len(resp.choices) > 0:
            return resp.choices[0].message.content.strip()
        else:
            return "No response generated"
            
    except Exception as e:
        return f"Error: {e}"


def main() -> None:
    load_dotenv()
    st.set_page_config(page_title="Day-20 Chat", layout="wide")
    st.title("Day-20: Conversational AI & Chatbots")

    # Check for OpenRouter configuration
    try:
        from openrouter_provider import create_openrouter_provider
        provider = create_openrouter_provider()
        client = provider.get_client()
        model_name = provider.get_model_name()
        st.success(f"✅ Using OpenRouter model: {model_name}")
    except ValueError as e:
        st.error(f"Configuration error: {e}")
        st.stop()
    except ImportError:
        st.error("Please install openai: pip install openai")
        st.stop()

    if "history" not in st.session_state:
        st.session_state.history = []  # list[(user, assistant)]

    system = st.text_input("System Prompt", "You are a helpful assistant. Keep replies under 3 sentences.")
    user_input = st.text_input("Message", "Hello! How can you help me today?")
    if st.button("Send", type="primary") and user_input:
        reply = generate_reply(client, model_name, system, st.session_state.history, user_input)
        st.session_state.history.append((user_input, reply))

    st.subheader("Conversation")
    for u, a in st.session_state.history:
        st.markdown(f"**You:** {u}")
        st.markdown(f"**Bot:** {a}")

    if st.button("Clear History"):
        st.session_state.history = []
        st.success("History cleared.")


if __name__ == "__main__":
    main()


