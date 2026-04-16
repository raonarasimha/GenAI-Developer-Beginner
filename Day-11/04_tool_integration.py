"""
Day 11 - Tool Integration (OpenAI Agents SDK with OpenRouter)
Register function tools with an Agent and invoke them via the agent loop using OpenRouter API.
"""

import os
from dotenv import load_dotenv
from agents import Agent, Runner, RunConfig
from agents.tool import function_tool
from openrouter_provider import create_openrouter_provider

load_dotenv()


@function_tool
def echo(text: str) -> str:
    """Return the given text as-is."""
    return text


@function_tool
def uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()


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
        name="ToolsAgent",
        instructions="Use tools when asked. Keep answers brief.",
        tools=[echo, uppercase],
        model=provider.model_name
    )
    
    # Run with custom provider
    r1 = Runner.run_sync(
        agent, 
        "Use echo to repeat: connected",
        run_config=RunConfig(model_provider=provider)
    )
    r2 = Runner.run_sync(
        agent, 
        "Use uppercase on: agent sdk",
        run_config=RunConfig(model_provider=provider)
    )
    
    print("--------------------------------")
    print("Response from Open Agentic SDK:")
    print(f"Echo result: {r1.final_output}")
    print(f"Uppercase result: {r2.final_output}")


if __name__ == "__main__":
    main()


