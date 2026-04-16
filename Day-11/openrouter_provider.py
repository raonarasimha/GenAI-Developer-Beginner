"""
Day 11 - Custom OpenRouter Model Provider for Open Agentic SDK
Custom model provider to enable OpenRouter API integration with Open Agentic SDK.
Based on: https://github.com/openai/openai-agents-python/blob/main/examples/model_providers/custom_example_provider.py
"""

import os
from openai import AsyncOpenAI
from agents import Model, ModelProvider, OpenAIChatCompletionsModel, set_tracing_disabled


class OpenRouterModelProvider(ModelProvider):
    """Custom model provider for OpenRouter API integration."""
    
    def __init__(self, api_key: str, base_url: str, model_name: str):
        """
        Initialize the OpenRouter model provider.
        
        Args:
            api_key: OpenRouter API key
            base_url: OpenRouter API base URL
            model_name: Model name to use
        """
        self.api_key = api_key
        self.base_url = base_url
        self.model_name = model_name
        
        # Create custom OpenAI client for OpenRouter
        self.client = AsyncOpenAI(
            base_url=base_url,
            api_key=api_key,
            default_headers={
                "HTTP-Referer": "https://github.com/your-repo/open-agentic-demo",
                "X-Title": "Open Agentic SDK OpenRouter Demo"
            }
        )
        
        # Disable tracing to avoid conflicts
        set_tracing_disabled(disabled=True)
    
    def get_model(self, model_name: str | None) -> Model:
        """
        Get the model instance.
        
        Args:
            model_name: Model name (if None, uses the default model)
            
        Returns:
            Model: The model instance
        """
        model_to_use = model_name or self.model_name
        return OpenAIChatCompletionsModel(
            model=model_to_use,
            openai_client=self.client
        )


def create_openrouter_provider() -> OpenRouterModelProvider:
    """
    Create an OpenRouter model provider using environment variables.
    
    Returns:
        OpenRouterModelProvider: Configured provider
        
    Raises:
        ValueError: If required environment variables are missing
    """
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")
    model_name = os.getenv("OPENAI_MODEL_NAME")
    
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set in .env file")
    if not base_url:
        raise ValueError("OPENAI_BASE_URL not set in .env file")
    if not model_name:
        raise ValueError("OPENAI_MODEL_NAME not set in .env file")
    
    return OpenRouterModelProvider(api_key, base_url, model_name)
