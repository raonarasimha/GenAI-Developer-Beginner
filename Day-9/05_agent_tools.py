"""
Day 9 - Agent Tools & Integration
Shows custom tools and advanced agent capabilities using modern approach.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


@tool
def calculator(expression: str) -> str:
    """Evaluate a basic math expression safely (digits and + - * /)."""
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        return "Invalid characters in expression."
    try:
        return str(eval(expression))
    except Exception:
        return "Error evaluating expression."


@tool
def text_uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()


@tool
def text_count_words(text: str) -> str:
    """Count the number of words in text."""
    return str(len(text.split()))


def build_advanced_agent():
    """Build an agent with multiple custom tools using modern approach."""
    llm = ChatOpenAI(
        model="moonshotai/kimi-k2:free",
        temperature=0,
        openai_api_base=os.getenv("BASE_URL"),
        openai_api_key=os.getenv("OPEN_ROUTER_API_KEY"),
        default_headers={
            "HTTP-Referer": "https://github.com/your-repo/langchain-demo",
            "X-Title": "LangChain Agent Tools Demo"
        }
    )
    
    # Create prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant with access to tools for calculations and text processing. Use the appropriate tools when needed."),
        ("human", "{input}")
    ])
    
    # Available tools
    tools = [calculator, text_uppercase, text_count_words]
    
    # Create chain with tools
    chain = prompt | llm.bind_tools(tools)
    
    return chain, tools


def main() -> str:
    """
    Demonstrate advanced agent tools and integration with modern approach.
    
    Returns:
        str: Agent tools demonstration results
    """
    if not os.getenv("OPEN_ROUTER_API_KEY"):
        raise ValueError("OPEN_ROUTER_API_KEY not set in .env file")
    
    chain, tools = build_advanced_agent()
    results = []
    
    # Simple demonstration
    results.append("=== Agent Tools Demo ===")
    query = "Calculate 15 + 7 and convert 'hello world' to uppercase"
    result = chain.invoke({"input": query})
    
    results.append(f"User Query: {query}")
    results.append(f"Agent Response: {result.content if hasattr(result, 'content') else str(result)}")
    results.append("")
    
    # Show available tools
    results.append("=== Available Tools ===")
    results.append(f"Tools: {len(tools)}")
    for i, tool in enumerate(tools):
        results.append(f"{i+1}. {tool.name}: {tool.description}")
    
    return "\n".join(results)


if __name__ == "__main__":
    try:
        result = main()
        print(result)
    except (ValueError, Exception) as e:
        print(f"Error: {e}")
        exit(1)


