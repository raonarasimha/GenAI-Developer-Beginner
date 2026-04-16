"""
Day 10 - Task Definition & Delegation with OpenRouter
Shows simple sequential tasks with dependencies.
OpenRouter provides access to multiple AI models through a single API.
"""

import os
from dotenv import load_dotenv

load_dotenv()

try:
    from crewai import Agent, Task, Crew
    from langchain_openai import ChatOpenAI
except ImportError as e:
    print(f"Missing dependency: {e}. Install with: pip install crewai langchain-openai")
    raise


def build_task_crew(model_name: str = None) -> Crew:
    """
    Build a CrewAI crew with task dependencies using OpenRouter API.
    
    Args:
        model_name: The model to use. If None, uses OPENAI_MODEL_NAME from .env
    """
    # Get configuration from environment variables
    api_key = os.getenv("OPENROUTER_API_KEY")
    base_url = os.getenv("OPENAI_API_BASE")
    default_model = os.getenv("OPENAI_MODEL_NAME")
    
    # Validate required environment variables
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not set in .env file")
    if not base_url:
        raise ValueError("OPENAI_API_BASE not set in .env file")
    if not default_model:
        raise ValueError("OPENAI_MODEL_NAME not set in .env file")
    
    # Use provided model or default from .env
    model_to_use = model_name if model_name else default_model
    
    print(f"Using model: {model_to_use}")
    
    llm = ChatOpenAI(
        model=model_to_use,
        temperature=0,
        openai_api_base=base_url,
        openai_api_key=api_key,
        default_headers={
            "HTTP-Referer": "https://github.com/your-repo/crewai-demo",
            "X-Title": "CrewAI OpenRouter Demo"
        }
    )

    planner = Agent(
        role="Planner",
        goal="Create a short plan for a blog post",
        backstory="You quickly outline content structure.",
        llm=llm,
        verbose=False,
    )

    writer = Agent(
        role="Writer",
        goal="Draft the blog post based on the plan",
        backstory="Turn outlines into concise drafts.",
        llm=llm,
        verbose=False,
    )

    t1 = Task(
        description="Outline a 3-section blog post about 'Getting started with CrewAI'",
        expected_output="An outline with 3 sections.",
        agent=planner,
    )

    t2 = Task(
        description="Write a short draft using the outline from the previous task.",
        expected_output="A 1-paragraph draft.",
        agent=writer,
    )

    return Crew(agents=[planner, writer], tasks=[t1, t2], verbose=False)


def main() -> None:
    try:
        crew = build_task_crew()
        result = crew.kickoff()
        print("--------------------------------")
        print("Response from CrewAI:")
        print(str(result)[:500])
    except ValueError as e:
        print(f"Configuration error: {e}")
        exit(1)
    except Exception as e:
        print(f"Execution error: {e}")
        exit(1)


if __name__ == "__main__":
    main()


