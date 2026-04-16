"""
Day 8 - Real-World Prompt Examples
=================================

Apply prompt engineering to common real-world use cases.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def content_generation_prompts():
    """Demonstrate content generation prompts."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # Blog post outline
    blog_prompt = """Create a blog post outline about 'The Future of AI in Education' with:
1. Introduction
2. 3 main points
3. Conclusion
Keep each section brief."""
    
    # Social media post
    social_prompt = """Write a LinkedIn post about learning Python programming.
Make it engaging, include a call-to-action, and keep it under 200 characters."""
    
    # Email template
    email_prompt = """Write a professional email template for following up after a job interview.
Include: greeting, thank you, enthusiasm, next steps, closing."""
    
    prompts = [
        ("Blog Outline", blog_prompt),
        ("Social Media Post", social_prompt),
        ("Email Template", email_prompt)
    ]
    
    results = []
    for title, prompt in prompts:
        response = client.chat.completions.create(
            model="qwen/qwen3-coder:free",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        results.append({
            "type": title,
            "prompt": prompt,
            "response": response.choices[0].message.content
        })
    
    return results

def code_generation_prompts():
    """Demonstrate code generation prompts."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # Simple function
    function_prompt = """Write a Python function that:
- Takes a list of numbers as input
- Returns the sum of all even numbers
- Includes error handling for empty lists
- Has clear comments explaining each step"""
    
    # API integration
    api_prompt = """Write Python code to:
- Make a GET request to a weather API
- Parse the JSON response
- Extract temperature and weather description
- Handle potential errors gracefully
Use the requests library."""
    
    # Data processing
    data_prompt = """Write Python code to:
- Read a CSV file named 'sales_data.csv'
- Calculate total sales by month
- Create a simple bar chart
- Save the chart as 'sales_chart.png'
Use pandas and matplotlib."""
    
    prompts = [
        ("Function", function_prompt),
        ("API Integration", api_prompt),
        ("Data Processing", data_prompt)
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

def analysis_prompts():
    """Demonstrate analysis and summarization prompts."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # Text summarization
    text = """Machine learning is a subset of artificial intelligence that enables computers to learn and make decisions without being explicitly programmed. It uses algorithms to identify patterns in data and make predictions or decisions based on those patterns. Common applications include recommendation systems, image recognition, natural language processing, and autonomous vehicles. The field has seen rapid growth in recent years due to increased computational power, availability of large datasets, and improved algorithms."""
    
    summary_prompt = f"""Summarize the following text in 2-3 sentences:
{text}"""
    
    # Data analysis
    data_analysis_prompt = """Analyze this sales data and provide insights:
Month: Jan, Feb, Mar, Apr, May
Sales: 1000, 1200, 1100, 1400, 1600
Customers: 50, 60, 55, 70, 80

Provide:
1. Trend analysis
2. Key insights
3. Recommendations"""
    
    # Sentiment analysis
    sentiment_prompt = """Analyze the sentiment of this customer review:
'The product works well and the customer service was excellent. However, the delivery took longer than expected and the packaging could be better.'

Provide:
1. Overall sentiment (positive/negative/neutral)
2. Key positive points
3. Key negative points
4. Overall score (1-10)"""
    
    prompts = [
        ("Text Summarization", summary_prompt),
        ("Data Analysis", data_analysis_prompt),
        ("Sentiment Analysis", sentiment_prompt)
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

def creative_writing_prompts():
    """Demonstrate creative writing prompts."""
    client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))
    
    # Story writing
    story_prompt = """Write a short story (100 words) about:
- A programmer who discovers their code has become sentient
- Include dialogue and a surprising twist
- Make it engaging and creative"""
    
    # Poetry
    poetry_prompt = """Write a haiku about artificial intelligence.
Follow the 5-7-5 syllable pattern and make it thoughtful."""
    
    # Character creation
    character_prompt = """Create a character profile for a sci-fi story:
- Name and age
- Occupation and background
- Personality traits (3)
- Motivations and goals
- One unique ability or quirk"""
    
    prompts = [
        ("Short Story", story_prompt),
        ("Poetry", poetry_prompt),
        ("Character Creation", character_prompt)
    ]
    
    results = []
    for title, prompt in prompts:
        response = client.chat.completions.create(
            model="qwen/qwen3-coder:free",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )
        results.append({
            "type": title,
            "prompt": prompt,
            "response": response.choices[0].message.content
        })
    
    return results

def main():
    """Demonstrate real-world prompt examples."""
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set OPENAI_API_KEY in your .env file")
        return
    
    content_generation_prompts()
    code_generation_prompts()
    analysis_prompts()
    creative_writing_prompts()
    
    print("Real-world prompt examples completed.")

if __name__ == "__main__":
    main()
