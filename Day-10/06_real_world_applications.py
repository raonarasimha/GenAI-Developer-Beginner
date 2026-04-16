"""
Day 10 - Real-World Applications with OpenRouter
Example: a simple content workflow crew.
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


def build_content_crew(model_name: str = None) -> Crew:
    """
    Build a CrewAI content workflow crew using OpenRouter API.
    
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

    researcher = Agent(
        role="Researcher",
        goal="Provide 3 latest trends in AI education",
        backstory="You find up-to-date, concise info.",
        llm=llm,
        verbose=False,
    )

    writer = Agent(
        role="Writer",
        goal="Draft a short social post based on the trends",
        backstory="You write engaging, clear posts.",
        llm=llm,
        verbose=False,
    )

    t1 = Task(
        description="List 3 trends in AI education (bullets).",
        expected_output="3 bullet points.",
        agent=researcher,
    )

    t2 = Task(
        description="Create a 2-3 sentence LinkedIn post summarizing those trends.",
        expected_output="A short social post.",
        agent=writer,
    )

    return Crew(agents=[researcher, writer], tasks=[t1, t2], verbose=False)


def main() -> None:
    try:
        crew = build_content_crew()
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


