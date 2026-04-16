"""
Day 8 - Basic Prompt Patterns
============================

This file demonstrates fundamental prompt patterns that work across different LLMs.
These patterns are the building blocks of effective prompt engineering.

Key Patterns:
- Zero-shot prompting
- Few-shot prompting
- Chain-of-thought prompting
- Role-based prompting
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))

def demonstrate_zero_shot_prompting():
    """
    Zero-shot prompting: Asking the model to perform a task without examples.
    
    Best for:
    - Simple, straightforward tasks
    - When the model already understands the task
    - General knowledge questions
    """
    
    zero_shot_examples = [
        "What is the capital of France?",
        "Translate 'Hello, how are you?' to Spanish",
        "Write a short poem about nature",
        "Explain what photosynthesis is",
        "Calculate 15 * 23"
    ]
    print("Zero-Shot: 5 examples prepared")
    
    return zero_shot_examples

def demonstrate_few_shot_prompting():
    """
    Few-shot prompting: Providing examples to guide the model's output.
    
    Best for:
    - Tasks requiring specific formatting
    - Complex reasoning tasks
    - When you need consistent output structure
    - Teaching the model a specific pattern
    """
    
    # Example 1: Text classification
    classification_example = """
    Classify the sentiment of the following text as positive, negative, or neutral:
    
    Text: "I love this new restaurant!"
    Sentiment: positive
    
    Text: "The service was terrible and the food was cold."
    Sentiment: negative
    
    Text: "The weather is cloudy today."
    Sentiment: neutral
    
    Text: "This movie exceeded all my expectations!"
    Sentiment: positive
    
    Text: "The product arrived on time."
    Sentiment: neutral
    """
    # Example 2: Code generation with specific format
    code_example = """
    Write a Python function that follows this pattern:
    
    Input: "hello world"
    Output: def reverse_string(text):
                return text[::-1]
    
    Input: "calculate factorial of 5"
    Output: def factorial(n):
                if n <= 1:
                    return 1
                return n * factorial(n-1)
    
    Input: "check if number is prime"
    Output: def is_prime(n):
                if n < 2:
                    return False
                for i in range(2, int(n**0.5) + 1):
                    if n % i == 0:
                        return False
                return True
    """
    
    print("Few-Shot: 2 examples prepared")
    
    return classification_example, code_example

def demonstrate_chain_of_thought():
    """
    Chain-of-thought prompting: Asking the model to show its reasoning process.
    
    Best for:
    - Complex problem solving
    - Mathematical reasoning
    - Logical deduction
    - Multi-step tasks
    """
    
    # Example 1: Mathematical reasoning
    math_example = """
    Let's solve this step by step:
    
    Question: If a train travels 120 miles in 2 hours, and then 180 miles in 3 hours, 
    what is the average speed for the entire journey?
    
    Let's think through this:
    1. First, let's find the total distance traveled
    2. Then, let's find the total time taken
    3. Finally, we'll calculate the average speed
    
    Step 1: Total distance = 120 miles + 180 miles = 300 miles
    Step 2: Total time = 2 hours + 3 hours = 5 hours
    Step 3: Average speed = Total distance / Total time = 300 miles / 5 hours = 60 mph
    
    Therefore, the average speed for the entire journey is 60 mph.
    """
    # Example 2: Logical reasoning
    logic_example = """
    Let's solve this step by step:
    
    Question: If all roses are flowers, and some flowers are red, can we conclude that some roses are red?
    
    Let's think through this:
    1. We know that all roses are flowers (Roses ⊂ Flowers)
    2. We know that some flowers are red (Some Flowers ∩ Red ≠ ∅)
    3. But we don't know if the red flowers include any roses
    4. The red flowers could be tulips, daisies, or other flowers
    5. Therefore, we cannot conclude that some roses are red
    
    Answer: No, we cannot conclude that some roses are red.
    """
    
    print("Chain-of-Thought: 2 examples prepared")
    
    return math_example, logic_example

def demonstrate_role_based_prompting():
    """
    Role-based prompting: Assigning a specific persona or role to the model.
    
    Best for:
    - Getting expert-level responses
    - Creative writing with specific voice
    - Technical explanations at different levels
    - Simulating different perspectives
    """
    
    role_examples = {
        "Expert": "You are a senior software engineer with 15 years of experience in Python development. Explain the concept of decorators in Python.",
        
        "Teacher": "You are a patient high school teacher explaining complex concepts to students. Explain how photosynthesis works.",
        
        "Creative Writer": "You are a bestselling author known for vivid descriptions and engaging storytelling. Write a short story about a magical library.",
        
        "Business Analyst": "You are a data analyst presenting findings to executives. Explain the impact of AI on business operations in simple terms.",
        
        "Scientist": "You are a research scientist writing for a peer-reviewed journal. Describe the methodology for a machine learning experiment."
    }
    print("Role-Based: 5 roles prepared")
    
    return role_examples

def test_patterns_with_api():
    """Test different prompt patterns with the API."""
    
    print("\nTesting Patterns with API")
    
    if not os.getenv("OPENAI_API_KEY"):
        print("OpenAI API key not found. Skipping API tests.")
        return
    
    try:
        # Test zero-shot
        zero_shot_prompt = "What is the square root of 144?"
        
        response = client.chat.completions.create(
           model="openai/gpt-oss-20b:free",
            messages=[{"role": "user", "content": zero_shot_prompt}]
           
        )
        print(f"Zero-shot: {response.choices[0].message.content[:80]}...")
        
        # Test few-shot
        few_shot_prompt = """
        Convert the following temperatures from Celsius to Fahrenheit:
        
        Celsius: 0
        Fahrenheit: 32
        
        Celsius: 100
        Fahrenheit: 212
        
        Celsius: 25
        Fahrenheit: 77
        
        Celsius: 37
        Fahrenheit: 98.6
        
        Celsius: 50
        Fahrenheit: 122
        """
        
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=[{"role": "user", "content": few_shot_prompt}]
        )
        print(f"Few-shot: {response.choices[0].message.content}...")
        
    except Exception as e:
        print(f"API Error: {e}")

def main():
    """Main function to demonstrate all basic prompt patterns."""
    
    print("Day 8: Basic Prompt Patterns")
    
    # # Demonstrate different prompt patterns
    # demonstrate_zero_shot_prompting()
    # demonstrate_few_shot_prompting()
    # demonstrate_chain_of_thought()
    # demonstrate_role_based_prompting()
    
    # Test with API
    test_patterns_with_api()
    
    print("\nBasic Prompt Patterns Complete!")

if __name__ == "__main__":
    main()
