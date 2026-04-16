"""
Day 11 - OpenAI Agents SDK: Hello World with OpenRouter
Minimal example using the OpenAI Agents SDK Agent + Runner with OpenRouter API.
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
    agent = Agent(
        name="Assistant", 
        instructions="You are a helpful assistant.",
        model=provider.model_name
    )
    
    # Run with custom provider
    result = Runner.run_sync(
        agent, 
        "Write a haiku about recursion in programming.",
        run_config=RunConfig(model_provider=provider)
    )
    
    print("--------------------------------")
    print("Response from Open Agentic SDK:")
    print(result.final_output)


if __name__ == "__main__":
    main()
