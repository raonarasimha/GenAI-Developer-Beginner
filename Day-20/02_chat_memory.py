"""
Multi-turn CLI chatbot with short-term memory using OpenRouter via OpenAI client.
Demonstrates conversation history tracking with deque for context-aware responses.
"""

import os
from collections import deque
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    
    # Check for OpenRouter configuration
    try:
        from openrouter_provider import create_openrouter_provider
        provider = create_openrouter_provider()
        client = provider.get_client()
        model_name = provider.get_model_name()
        print(f"✅ Using OpenRouter model: {model_name}")
    except ValueError as e:
        print(f"Configuration error: {e}")
        return
    except ImportError:
        print("Please install openai: pip install openai")
        return

    system = "You are a helpful assistant. Keep replies under 3 sentences."
    history = deque(maxlen=10)  # Store last 10 conversation turns for context

    print("Multi-turn chatbot with memory - responses are context-aware.")
    print("Type 'exit' to quit, 'history' to see conversation history.")
    while True:
        user = input("You: ").strip()
        if not user:
            continue
        if user.lower() == "exit":
            break
        if user.lower() == "history":
            print("\n--- Conversation History ---")
            for i, (u, a) in enumerate(history, 1):
                print(f"{i}. You: {u}")
                print(f"   Bot: {a}")
            print("--- End History ---\n")
            continue

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
                text = resp.choices[0].message.content.strip()
                print("Bot:", text)
                history.append((user, text))
            else:
                print("Bot: No response generated")
                
        except Exception as e:
            print(f"Bot: Error - {e}")


if __name__ == "__main__":
    main()


