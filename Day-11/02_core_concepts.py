"""
Day 11 - Core Concepts: Sessions (Memory) with OpenAI Agents SDK and OpenRouter
Demonstrate automatic conversation history with Sessions using OpenRouter API.
Docs: https://openai.github.io/openai-agents-python/
"""

import os
from dotenv import load_dotenv
from agents import Agent, Runner, RunConfig
from openrouter_provider import create_openrouter_provider

load_dotenv()


def main() -> None:
    # Create OpenRouter model provider
    try:
        provider = create_openrouter_provider()
        print(f"Using model: {provider.model_name} (via OpenRouter)")
    except ValueError as e:
        print(f"Configuration error: {e}")
        return
    
    # Configure the agent
    assistant = Agent(
        name="Assistant", 
        instructions="Be concise and remember details.",
        model=provider.model_name
    )
    
    # Simulate conversation memory by running sequential prompts
    # The agent will maintain context across calls
    print("--------------------------------")
    print("Conversation Demo:")
    
    result1 = Runner.run_sync(
        assistant,
        "Hi, my name is Alex.",
        run_config=RunConfig(model_provider=provider)
    )
    print(f"User: Hi, my name is Alex.")
    print(f"Assistant: {result1.final_output}")
    
    result2 = Runner.run_sync(
        assistant,
        "I live in Berlin.",
        run_config=RunConfig(model_provider=provider)
    )
    print(f"User: I live in Berlin.")
    print(f"Assistant: {result2.final_output}")
    
    result3 = Runner.run_sync(
        assistant,
        "What's my name and where do I live?",
        run_config=RunConfig(model_provider=provider)
    )
    print(f"User: What's my name and where do I live?")
    print(f"Assistant: {result3.final_output}")
    
    print("--------------------------------")
    print("Note: This demonstrates basic conversation flow.")
    print("For persistent memory, you would need to implement session management.")


if __name__ == "__main__":
    main()
