"""
Test script to verify Hugging Face integration works correctly.
"""

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from embeddings_utils import embed_texts

def test_hf_embeddings():
    """Test that Hugging Face embeddings work correctly."""
    load_dotenv()
    
    if not os.getenv("HF_TOKEN"):
        print("❌ Please set HF_TOKEN in your .env file")
        return False
    
    try:
        # Initialize client
        client = InferenceClient(
            provider="hf-inference",
            api_key=os.getenv("HF_TOKEN"),
        )
        
        # Test with a simple text
        test_texts = ["This is a test sentence for embeddings."]
        
        print("🔄 Testing Hugging Face embeddings...")
        embeddings = embed_texts(client, test_texts)
        
        print(f"✅ Success! Generated embeddings with shape: {embeddings.shape}")
        print(f"📊 Embedding dimension: {embeddings.shape[1]}")
        print(f"🔢 Number of texts: {embeddings.shape[0]}")
        
        # Test with different model
        print("\n🔄 Testing with sentence-transformers model...")
        embeddings_st = embed_texts(client, test_texts, model="sentence-transformers/all-MiniLM-L6-v2")
        print(f"✅ sentence-transformers model works! Shape: {embeddings_st.shape}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = test_hf_embeddings()
    if success:
        print("\n🎉 All tests passed! Hugging Face integration is working.")
    else:
        print("\n💥 Tests failed. Please check your setup.")
