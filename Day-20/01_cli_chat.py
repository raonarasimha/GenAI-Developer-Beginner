"""
Single-turn CLI chatbot using OpenRouter via OpenAI client.
Demonstrates basic chatbot functionality without conversation memory.
"""

import os
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

    system = "You are a concise, friendly assistant."
    
    print("Single-turn chatbot - each response is independent.")
    print("Type 'exit' to quit.")
    
    while True:
        user = input("You: ").strip()
        if not user:
            continue
        if user.lower() == "exit":
            break

        # Simple single-turn conversation - no memory
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ]

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
            else:
                print("Bot: No response generated")
                
        except Exception as e:
            print(f"Bot: Error - {e}")


if __name__ == "__main__":
    main()


