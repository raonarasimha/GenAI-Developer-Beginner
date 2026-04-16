"""
Day 9 - LangChain Introduction with OpenRouter
Concise intro: minimal demo using PromptTemplate + LLMChain with OpenRouter API.
OpenRouter provides access to multiple AI models through a single API.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()


def build_intro_chain(model_name: str = None):
	"""
	Build a LangChain using OpenRouter API.
	
	Args:
		model_name: The model to use. If None, uses OPEN_ROUTER_MODEL from .env
	"""
	# Get configuration from environment variables
	api_key = os.getenv("OPEN_ROUTER_API_KEY")
	base_url = os.getenv("BASE_URL")
	default_model = os.getenv("OPEN_ROUTER_MODEL")
	
	# Validate required environment variables
	if not api_key:
		raise ValueError("OPEN_ROUTER_API_KEY not set in .env file")
	if not base_url:
		raise ValueError("BASE_URL not set in .env file")
	if not default_model:
		raise ValueError("OPEN_ROUTER_MODEL not set in .env file")
	
	# Use provided model or default from .env
	model_to_use = model_name if model_name else default_model
	
	llm = ChatOpenAI(
		model=model_to_use,
		temperature=0,
		openai_api_base=base_url,
		openai_api_key=api_key,
		default_headers={
			"HTTP-Referer": "https://github.com/your-repo/langchain-demo",
			"X-Title": "LangChain OpenRouter Demo"
		}
	)
	
	prompt = PromptTemplate(
		input_variables=["topic", "words"],
		template=(
			"You are a clear technical writer. "
			"Explain {topic} to a beginner in under {words} words."
		),
	)
	print(prompt)
	# Use modern LangChain syntax: prompt | llm
	return prompt | llm





def main() -> str:
	"""
	Execute the LangChain demo and return the result.
	
	Returns:
		str: The AI-generated explanation of LangChain
		
	Raises:
		ValueError: If required environment variables are missing
		Exception: For other errors during execution
	"""
	try:
		chain = build_intro_chain()
		out = chain.invoke({"topic": "LangChain", "words": "60"})
		# Modern LangChain returns content directly
		text = out.content if hasattr(out, 'content') else str(out)
		return text.strip()
	except ValueError as e:
		raise ValueError(f"Configuration error: {e}. Please check your .env file contains OPEN_ROUTER_API_KEY, BASE_URL, and OPEN_ROUTER_MODEL")
	except Exception as e:
		raise Exception(f"Execution error: {e}")


if __name__ == "__main__":
	try:
		result = main()
		print("--------------------------------")
		print("Response from langchain:")
		print(result)
	except (ValueError, Exception) as e:
		print(f"Error: {e}")
		exit(1)
