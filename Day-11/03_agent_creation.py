"""
Day 11 - Agent Creation & Configuration (OpenAI Agents SDK with OpenRouter)
Create a basic Agent with instructions and run a prompt using OpenRouter API.
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
        name="Planner",
        instructions="You plan tasks in clear, numbered steps. Keep it short.",
        model=provider.model_name
    )
    
    # Run with custom provider
    result = Runner.run_sync(
        agent, 
        "Plan how to summarize a 2-page document.",
        run_config=RunConfig(model_provider=provider)
    )
    
    print("--------------------------------")
    print("Response from Open Agentic SDK:")
    print(result.final_output)


if __name__ == "__main__":
    main()


