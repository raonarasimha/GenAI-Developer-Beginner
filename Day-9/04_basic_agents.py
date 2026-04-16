"""
Day 9 - Basic Agent Creation
Simple agent using LangChain Tools with modern approach.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

load_dotenv()


@tool
def search_tool(query: str) -> str:
    """Search for information on the web (simulated)."""
    # Simulate different search results based on query
    if "python" in query.lower():
        return "Search results for Python: Python is a high-level programming language known for its simplicity and readability. It's widely used in web development, data science, AI, and automation."
    elif "langchain" in query.lower():
        return "Search results for LangChain: LangChain is a framework for developing applications powered by language models. It provides tools for building chains, agents, and complex workflows."
    elif "programming" in query.lower():
        return "Search results for Programming: Programming is the process of creating instructions for computers to execute. Popular languages include Python, JavaScript, Java, and C++."
    else:
        return f"Search results for '{query}': Found various resources and information about this topic."


def build_agent():
    """Build a simple agent with tools using modern LangChain approach."""
    llm = ChatOpenAI(
        model="moonshotai/kimi-k2:free",
        temperature=0,
        openai_api_base=os.getenv("BASE_URL"),
        openai_api_key=os.getenv("OPEN_ROUTER_API_KEY"),
        default_headers={
            "HTTP-Referer": "https://github.com/your-repo/langchain-demo",
            "X-Title": "LangChain Basic Agent Demo"
        }
    )
    
    # Create a simple prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that can use tools to find information. When asked about topics, use the search tool to get information."),
        ("human", "{input}")
    ])
    
    # Create a simple chain that can use tools
    chain = prompt | llm.bind_tools([search_tool])
    
    return chain, [search_tool]


def main() -> str:
    """
    Demonstrate basic agent capabilities with modern approach.
    
    Returns:
        str: Agent demonstration results
    """
    if not os.getenv("OPEN_ROUTER_API_KEY"):
        raise ValueError("OPEN_ROUTER_API_KEY not set in .env file")
    
    chain, tools = build_agent()
    results = []
    
    # Simple agent demonstration
    results.append("=== Basic Agent Demo ===")
    query = "What is Python programming?"
    result = chain.invoke({"input": query})
    
    results.append(f"User Query: {query}")
    results.append(f"Agent Response: {result.content if hasattr(result, 'content') else str(result)}")
    results.append("")
    
    # Show what tools are available
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


