"""
Day 11 - Advanced Features & Best Practices (OpenAI Agents SDK with OpenRouter)
Demonstrate guardrails-style validation, a brief router handoff, and agent-as-tool using OpenRouter API.
"""

import os
from dotenv import load_dotenv
from agents import Agent, Runner, RunConfig
from agents.tool import function_tool
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
    
    # Configure agents
    router = Agent(
        name="Router", 
        instructions="If math, say 'send to math'. Else 'send to text'.",
        model=provider.model_name
    )
    
    math_agent = Agent(
        name="Math", 
        instructions="Answer math succinctly.",
        model=provider.model_name
    )
    
    text_agent = Agent(
        name="Text", 
        instructions="Answer text succinctly.",
        model=provider.model_name
    )

    # Run with custom provider
    q = "Rewrite: openai agents sdk is lightweight"
    route = Runner.run_sync(
        router, 
        q,
        run_config=RunConfig(model_provider=provider)
    ).final_output.lower()
    
    final = Runner.run_sync(
        math_agent if "math" in route else text_agent, 
        q,
        run_config=RunConfig(model_provider=provider)
    )
    
    print("--------------------------------")
    print("Router Demo:")
    print(f"Query: {q}")
    print(f"Route: {route}")
    print(f"Response: {final.final_output}")

    # Agent as a tool: a sub-agent used as a callable tool
    @function_tool
    def summarize(text: str) -> str:
        s = Agent(
            name="Summarizer", 
            instructions="Summarize in 1 sentence.",
            model=provider.model_name
        )
        return Runner.run_sync(
            s, 
            f"Summarize: {text}",
            run_config=RunConfig(model_provider=provider)
        ).final_output

    caller = Agent(
        name="Caller",
        instructions="When asked to summarize, call the 'summarize' tool.",
        tools=[summarize],
        model=provider.model_name
    )
    
    out = Runner.run_sync(
        caller, 
        "Use summarize on: OpenAI Agents SDK enables tools and sessions.",
        run_config=RunConfig(model_provider=provider)
    )
    
    print("--------------------------------")
    print("Agent as Tool Demo:")
    print(f"Result: {out.final_output}")


if __name__ == "__main__":
    main()


