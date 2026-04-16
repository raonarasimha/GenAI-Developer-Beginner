"""
Day 8 - Prompt Optimization Strategies
=====================================

Systematic approaches to improve prompt performance.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def test_prompt_variations():
    """Test different versions of the same prompt."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # Version 1: Basic prompt
    prompt_v1 = "Write a summary of machine learning."
    
    # Version 2: More specific
    prompt_v2 = "Write a 3-sentence summary of machine learning for beginners."
    
    # Version 3: With context
    prompt_v3 = "You are a teacher. Write a 3-sentence summary of machine learning for high school students."
    
    prompts = [prompt_v1, prompt_v2, prompt_v3]
    results = []
    
    for i, prompt in enumerate(prompts, 1):
        response = client.chat.completions.create(
            model="qwen/qwen3-coder:free",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        results.append({
            "version": f"v{i}",
            "prompt": prompt,
            "response": response.choices[0].message.content,
            "tokens": response.usage.total_tokens
        })
    
    return results

def iterative_refinement():
    """Show iterative prompt improvement."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # Initial prompt
    initial_prompt = "Explain Python."
    
    # First iteration - add specificity
    refined_prompt = "Explain Python programming language in simple terms."
    
    # Second iteration - add structure
    final_prompt = "Explain Python programming language in 3 points: 1) What it is, 2) Why use it, 3) Basic syntax."
    
    prompts = [initial_prompt, refined_prompt, final_prompt]
    results = []
    
    for i, prompt in enumerate(prompts, 1):
        response = client.chat.completions.create(
            model="qwen/qwen3-coder:free",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        results.append({
            "iteration": i,
            "prompt": prompt,
            "response": response.choices[0].message.content,
            "tokens": response.usage.total_tokens
        })
    
    return results

def error_analysis():
    """Analyze common prompt errors."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # Problematic prompt (ambiguous)
    bad_prompt = "Help me with this."
    
    # Improved prompt (specific)
    good_prompt = "Help me write a Python function to calculate the average of a list of numbers."
    
    try:
        bad_response = client.chat.completions.create(
            model="qwen/qwen3-coder:free",
            messages=[{"role": "user", "content": bad_prompt}],
            temperature=0.1
        )
        
        good_response = client.chat.completions.create(
            model="qwen/qwen3-coder:free",
            messages=[{"role": "user", "content": good_prompt}],
            temperature=0.1
        )
        
        return {
            "bad_prompt": {
                "prompt": bad_prompt,
                "response": bad_response.choices[0].message.content,
                "issue": "Too vague and ambiguous"
            },
            "good_prompt": {
                "prompt": good_prompt,
                "response": good_response.choices[0].message.content,
                "improvement": "Specific and actionable"
            }
        }
    except Exception as e:
        return {"error": str(e)}

def performance_metrics():
    """Calculate basic performance metrics."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = "Write a haiku about programming."
    
    # Test multiple times for consistency
    responses = []
    total_tokens = 0
    
    for i in range(3):
        response = client.chat.completions.create(
            model="qwen/qwen3-coder:free",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        responses.append(response.choices[0].message.content)
        total_tokens += response.usage.total_tokens
    
    # Calculate metrics
    avg_tokens = total_tokens / 3
    response_lengths = [len(r) for r in responses]
    avg_length = sum(response_lengths) / len(response_lengths)
    
    return {
        "responses": responses,
        "avg_tokens": avg_tokens,
        "avg_length": avg_length,
        "consistency": len(set(responses)) == 1  # True if all responses are identical
    }

def main():
    """Demonstrate prompt optimization strategies."""
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set OPENAI_API_KEY in your .env file")
        return
    
    test_prompt_variations()
    iterative_refinement()
    error_analysis()
    performance_metrics()
    
    print("Prompt optimization completed.")

if __name__ == "__main__":
    main()
