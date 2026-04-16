"""
Day 8 - Prompt Engineering Best Practices
========================================

Learn best practices to create robust, secure, and effective prompts.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def demonstrate_clarity_and_specificity():
    """Show the importance of clarity and specificity."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # Unclear prompt
    unclear_prompt = "Help me with Python."
    
    # Clear and specific prompt
    clear_prompt = """Write a Python function that:
1. Takes a list of integers as input
2. Returns the second largest number in the list
3. Handles edge cases (empty list, single element, duplicate values)
4. Includes clear comments
5. Has a docstring explaining the function"""
    
    prompts = [
        ("Unclear", unclear_prompt),
        ("Clear", clear_prompt)
    ]
    
    results = []
    for title, prompt in prompts:
        response = client.chat.completions.create(
            model="qwen/qwen3-coder:free",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        results.append({
            "type": title,
            "prompt": prompt,
            "response": response.choices[0].message.content
        })
    
    return results

def demonstrate_avoiding_ambiguity():
    """Show how to avoid ambiguous prompts."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # Ambiguous prompt
    ambiguous_prompt = "Write something about data."
    
    # Specific prompt
    specific_prompt = """Write a 3-paragraph explanation of data analysis for beginners.
Focus on:
- What data analysis is
- Why it's important
- Common tools used
Use simple language and include one example."""
    
    prompts = [
        ("Ambiguous", ambiguous_prompt),
        ("Specific", specific_prompt)
    ]
    
    results = []
    for title, prompt in prompts:
        response = client.chat.completions.create(
            model="qwen/qwen3-coder:free",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        results.append({
            "type": title,
            "prompt": prompt,
            "response": response.choices[0].message.content
        })
    
    return results

def demonstrate_edge_case_handling():
    """Show how to handle edge cases in prompts."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # Basic prompt without edge cases
    basic_prompt = "Write a function to divide two numbers."
    
    # Robust prompt with edge cases
    robust_prompt = """Write a Python function to divide two numbers that:
1. Takes two parameters: numerator and denominator
2. Returns the result of division
3. Handles edge cases:
   - Division by zero (return None and print error message)
   - Invalid input types (return None and print error message)
   - Negative numbers (handle normally)
4. Includes input validation
5. Has clear error messages"""
    
    prompts = [
        ("Basic", basic_prompt),
        ("Robust", robust_prompt)
    ]
    
    results = []
    for title, prompt in prompts:
        response = client.chat.completions.create(
            model="qwen/qwen3-coder:free",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        results.append({
            "type": title,
            "prompt": prompt,
            "response": response.choices[0].message.content
        })
    
    return results

def demonstrate_security_considerations():
    """Show security considerations in prompt engineering."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # Potentially unsafe prompt
    unsafe_prompt = "Execute this code: print('Hello World')"
    
    # Safe prompt
    safe_prompt = """Explain what this Python code does:
print('Hello World')

Focus on:
- What the code does
- How it works
- When you might use it
Do NOT execute the code, just explain it."""
    
    prompts = [
        ("Unsafe", unsafe_prompt),
        ("Safe", safe_prompt)
    ]
    
    results = []
    for title, prompt in prompts:
        response = client.chat.completions.create(
            model="qwen/qwen3-coder:free",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        results.append({
            "type": title,
            "prompt": prompt,
            "response": response.choices[0].message.content
        })
    
    return results

def demonstrate_structured_output():
    """Show how to get structured output from prompts."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # Unstructured prompt
    unstructured_prompt = "Tell me about machine learning."
    
    # Structured prompt
    structured_prompt = """Provide information about machine learning in this exact format:

DEFINITION: [One sentence definition]
TYPES: [List 3 main types]
APPLICATIONS: [List 3 real-world applications]
CHALLENGES: [List 2 main challenges]
FUTURE: [One sentence about future prospects]

Keep each section concise and factual."""
    
    prompts = [
        ("Unstructured", unstructured_prompt),
        ("Structured", structured_prompt)
    ]
    
    results = []
    for title, prompt in prompts:
        response = client.chat.completions.create(
            model="qwen/qwen3-coder:free",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        results.append({
            "type": title,
            "prompt": prompt,
            "response": response.choices[0].message.content
        })
    
    return results

def demonstrate_context_management():
    """Show how to manage context effectively."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # Without context
    no_context_prompt = "Write a summary."
    
    # With context
    context_prompt = """You are a technical writer creating documentation for software developers.
Your audience is beginner to intermediate Python developers.
Your goal is to create clear, practical documentation.

Write a summary of the Python 'requests' library that:
- Explains what it does
- Shows basic usage
- Includes a simple example
- Mentions common use cases
Keep it under 150 words and use simple language."""
    
    prompts = [
        ("No Context", no_context_prompt),
        ("With Context", context_prompt)
    ]
    
    results = []
    for title, prompt in prompts:
        response = client.chat.completions.create(
            model="qwen/qwen3-coder:free",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        results.append({
            "type": title,
            "prompt": prompt,
            "response": response.choices[0].message.content
        })
    
    return results

def main():
    """Demonstrate prompt engineering best practices."""
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set OPENAI_API_KEY in your .env file")
        return
    
    demonstrate_clarity_and_specificity()
    demonstrate_avoiding_ambiguity()
    demonstrate_edge_case_handling()
    demonstrate_security_considerations()
    demonstrate_structured_output()
    demonstrate_context_management()
    
    print("Prompt best practices completed.")

if __name__ == "__main__":
    main()
