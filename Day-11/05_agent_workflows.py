"""
Day 11 - Agent Workflows & Execution (OpenAI Agents SDK with OpenRouter)
Demonstrate a simple session workflow: plan -> execute -> summarize using OpenRouter API.
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
        name="Workflow", 
        instructions="Plan, then execute, then summarize.",
        model=provider.model_name
    )
    
    # Execute workflow steps sequentially
    print("--------------------------------")
    print("Workflow Demo:")
    
    # Step 1: Plan
    plan_result = Runner.run_sync(
        agent,
        "Plan how to write a short blog post about AI agents.",
        run_config=RunConfig(model_provider=provider)
    )
    print(f"Step 1 - Plan: {plan_result.final_output}")
    
    # Step 2: Execute
    execute_result = Runner.run_sync(
        agent,
        "Execute the plan in 2 sentences.",
        run_config=RunConfig(model_provider=provider)
    )
    print(f"Step 2 - Execute: {execute_result.final_output}")
    
    # Step 3: Summarize
    summary_result = Runner.run_sync(
        agent,
        "Summarize the result in one sentence.",
        run_config=RunConfig(model_provider=provider)
    )
    print(f"Step 3 - Summarize: {summary_result.final_output}")
    
    print("--------------------------------")
    print("Workflow completed successfully!")


if __name__ == "__main__":
    main()


