"""
Day 8 - Advanced Prompt Techniques
=================================

Advanced techniques for fine-tuning model behavior.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def demonstrate_system_vs_user_prompts():
    """Show difference between system and user prompts."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # System prompt sets the context
    system_prompt = "You are a helpful coding assistant. Always provide clear, well-commented code."
    user_prompt = "Write a Python function to calculate factorial."
    
    response = client.chat.completions.create(
        model="qwen/qwen3-coder:free",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.1
    )
    
    return response.choices[0].message.content

def demonstrate_temperature_control():
    """Show how temperature affects creativity."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = "Write a short story about a robot learning to paint."
    
    # Low temperature - more focused
    low_temp_response = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528:free",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    
    # High temperature - more creative
    high_temp_response = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528:free",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )
    
    return {
        "low_temperature": low_temp_response.choices[0].message.content,
        "high_temperature": high_temp_response.choices[0].message.content
    }

def demonstrate_max_tokens_control():
    """Show how max_tokens controls response length."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = "Explain machine learning in simple terms."
    
    # Short response
    short_response = client.chat.completions.create(
        model="qwen/qwen3-coder:free",
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Longer response
    long_response = client.chat.completions.create(
        model="qwen/qwen3-coder:free",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return {
        "short": short_response.choices[0].message.content,
        "long": long_response.choices[0].message.content
    }

def demonstrate_context_window():
    """Show context window management."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # Long context
    long_context = "This is a very long context that demonstrates how the model handles large amounts of information. " * 50
    
    response = client.chat.completions.create(
        model="qwen/qwen3-coder:free",
        messages=[
            {"role": "user", "content": f"{long_context} Summarize the above text in one sentence."}
        ]
    )
    
    return response.choices[0].message.content

def main():
    """Demonstrate advanced prompt techniques."""
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set OPENAI_API_KEY in your .env file")
        return
    
    #demonstrate_system_vs_user_prompts()
    demonstrate_temperature_control()
    #demonstrate_max_tokens_control()
    #demonstrate_context_window()
    
    print("Advanced prompt techniques completed.")

if __name__ == "__main__":
    main()
