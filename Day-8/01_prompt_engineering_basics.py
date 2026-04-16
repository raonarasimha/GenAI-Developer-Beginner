"""
Day 8 - Prompt Engineering Basics
================================

This file demonstrates the fundamental concepts of prompt engineering.
Prompt engineering is the practice of designing inputs to AI models to achieve desired outputs.

Key Concepts:
- Prompt structure and components
- Why prompt engineering matters
- Basic prompt patterns
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables (API key)
load_dotenv()

# Initialize OpenAI client
client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))

def demonstrate_basic_prompt():
    """Demonstrates a basic prompt structure and why it matters."""
    
    # Example 1: Poor prompt (vague and unclear)
    poor_prompt = "Write about AI"
    
    # Example 2: Good prompt (clear, specific, with context)
    good_prompt = """
    Write a 200-word blog post about artificial intelligence for a general audience.
    Focus on recent developments in 2024 and their potential impact on daily life.
    Use simple language and include one practical example.
    """
    
    print("Basic Prompt Engineering Demo")
    print(f"Poor: '{poor_prompt}' - Too vague, no requirements")
    print(f"Good: '{good_prompt.strip()}' - Clear length, specific audience")
    
    return good_prompt

def demonstrate_prompt_components():
    """Shows the key components of a well-structured prompt."""
    
    print("\nPrompt Components Analysis")
    
    # Example prompt broken down into components
    example_prompt = """
    You are an expert Python developer with 10 years of experience.
    
    Task: Create a function that calculates the factorial of a number.
    
    Requirements:
    - Handle edge cases (negative numbers, zero)
    - Include proper error handling
    - Add comprehensive comments
    - Use iterative approach (not recursive)
    
    Output format: Return only the Python code with comments.
    """
    
    print("Components: Role/Context, Task/Instruction, Constraints, Output Format")
    
    return example_prompt

def demonstrate_prompt_importance():
    """Shows why prompt engineering is crucial for AI applications."""
    
    print("\nWhy Prompt Engineering Matters")
    
    # Example: Same task, different prompts, different results
    task = "Explain machine learning"
    
    prompts = {
        "vague": "Explain machine learning",
        "specific": "Explain machine learning to a 10-year-old child in 3 sentences",
        "technical": "Provide a technical explanation of machine learning algorithms for a data scientist",
        "business": "Explain how machine learning can benefit a small business owner"
    }
    
    print(f"Task: {task} - Different prompts produce different results")
    print("Key Takeaway: Same task, different results based on prompt phrasing.")

def test_prompt_with_api():
    """Demonstrates how different prompts produce different results."""
    
    print("\nTesting Prompts with API")
    
    # Check if API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("OpenAI API key not found. Set OPENAI_API_KEY in .env file to test.")
        return
    
    try:
        # Test with a simple prompt
        test_prompt = "Hello, can you tell me a joke about AI?"
        print(f"Testing: '{test_prompt}'")
        
        response = client.chat.completions.create(
            extra_body={},
            model="deepseek/deepseek-r1-0528:free",
            messages=[
                {"role": "user", "content": test_prompt}
            ]
        )
        
        result = response.choices[0].message.content
        print(f"Result: {result}")
        
    except Exception as e:
        print(f"API Error: {e}")

def main():
    """Main function to run all prompt engineering demonstrations."""
    
    print("Day 8: Prompt Engineering Basics")
    
    # Demonstrate basic prompt concepts
    demonstrate_basic_prompt()
    
    # Show prompt components
    demonstrate_prompt_components()
    
    # Explain why prompt engineering matters
    demonstrate_prompt_importance()
    
    # Test with API (if available)
    test_prompt_with_api()
    
    print("\nPrompt Engineering Basics Complete!")

if __name__ == "__main__":
    main()
