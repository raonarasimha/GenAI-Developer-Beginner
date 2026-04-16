"""
Day 9 - Memory & State Management
Demonstrates conversation memory and state management in LangChain.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain.prompts import ChatPromptTemplate

load_dotenv()


class ConversationMemory:
    """Simple conversation memory implementation."""
    
    def __init__(self):
        self.messages = []
    
    def add_message(self, role: str, content: str):
        """Add a message to the conversation history."""
        if role == "human":
            self.messages.append(HumanMessage(content=content))
        elif role == "ai":
            self.messages.append(AIMessage(content=content))
    
    def get_history(self):
        """Get the conversation history."""
        return self.messages
    
    def clear(self):
        """Clear the conversation history."""
        self.messages = []


def build_memory_chain():
    """Build a chain with conversation memory."""
    llm = ChatOpenAI(
        model=os.getenv("OPEN_ROUTER_MODEL"),
        temperature=0.7,
        openai_api_base=os.getenv("BASE_URL"),
        openai_api_key=os.getenv("OPEN_ROUTER_API_KEY"),
        default_headers={
            "HTTP-Referer": "https://github.com/your-repo/langchain-demo",
            "X-Title": "LangChain Memory Demo"
        }
    )
    
    # Create memory instance
    memory = ConversationMemory()
    
    # Create prompt template that includes chat history
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Remember the conversation context."),
        ("placeholder", "{chat_history}"),
        ("human", "{input}")
    ])
    
    return llm, prompt, memory


def main() -> str:
    """
    Demonstrate conversation memory capabilities with a simple example.
    
    Returns:
        str: Conversation demonstration
    """
    if not os.getenv("OPEN_ROUTER_API_KEY"):
        raise ValueError("OPEN_ROUTER_API_KEY not set in .env file")
    
    llm, prompt, memory = build_memory_chain()
    results = []
    
    # Conversation 1: Introduce yourself
    results.append("=== Memory Demo: Simple Conversation ===")
    input1 = "Hi, my name is Alex."
    
    # Create chain with current memory
    chain = prompt | llm
    result1 = chain.invoke({
        "input": input1,
        "chat_history": memory.get_history()
    })
    response1 = result1.content if hasattr(result1, 'content') else str(result1)
    results.append(f"User: {input1}")
    results.append(f"Assistant: {response1}")
    # Save to memory
    memory.add_message("human", input1)
    memory.add_message("ai", response1)
    results.append("")
    
    # Conversation 2: Test memory recall
    results.append("=== Testing Memory ===")
    input2 = "What's my name?"
    
    # Use same chain with updated memory
    result2 = chain.invoke({
        "input": input2,
        "chat_history": memory.get_history()
    })
    response2 = result2.content if hasattr(result2, 'content') else str(result2)
    results.append(f"User: {input2}")
    results.append(f"Assistant: {response2}")
    
    # Show memory contents
    results.append("")
    results.append("=== Memory Contents ===")
    results.append(f"Messages stored: {len(memory.get_history())}")
    for i, msg in enumerate(memory.get_history()):
        role = "Human" if msg.__class__.__name__ == "HumanMessage" else "AI"
        results.append(f"{i+1}. {role}: {msg.content}")
    
    return "\n".join(results)


if __name__ == "__main__":
    try:
        result = main()
        print(result)
    except (ValueError, Exception) as e:
        print(f"Error: {e}")
        exit(1)


