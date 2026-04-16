"""
Day 20 - OpenRouter Provider for Chatbot Implementation
Custom provider to enable OpenRouter API integration with OpenAI client for chatbots.
"""

import os
from openai import OpenAI


class OpenRouterProvider:
    """OpenRouter provider for OpenAI client integration."""
    
    def __init__(self, api_key: str, base_url: str, model_name: str):
        """
        Initialize the OpenRouter provider.
        
        Args:
            api_key: OpenRouter API key
            base_url: OpenRouter API base URL
            model_name: Model name to use
        """
        self.api_key = api_key
        self.base_url = base_url
        self.model_name = model_name
        
        # Create OpenAI client for OpenRouter
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            default_headers={"HTTP-Referer": "http://localhost:3000", "X-Title": "Day 20 - Chatbot Implementation"},
        )

    def get_client(self) -> OpenAI:
        """Returns the configured OpenAI client."""
        return self.client

    def get_model_name(self) -> str:
        """Returns the configured model name."""
        return self.model_name


def create_openrouter_provider() -> OpenRouterProvider:
    """
    Creates and returns an OpenRouterProvider instance using environment variables.
    
    Raises:
        ValueError: If required environment variables are not set.
    """
    from dotenv import load_dotenv
    load_dotenv()  # Ensure .env is loaded
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    base_url = os.getenv("OPENAI_API_BASE")
    model_name = os.getenv("OPENAI_MODEL_NAME")
    
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY environment variable not set.")
    if not base_url:
        raise ValueError("OPENAI_API_BASE environment variable not set.")
    if not model_name:
        raise ValueError("OPENAI_MODEL_NAME environment variable not set.")
        
    return OpenRouterProvider(api_key, base_url, model_name)
