"""
Build a FAISS index from local text files and run a single QA example.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

from rag_utils import (
    load_texts_from_dir,
    chunk_text,
    embed_chunks,
    build_faiss_index,
    embed_query,
    top_k,
    answer_with_context,
)


def main() -> None:
    load_dotenv()
    
    # Check for OpenRouter configuration
    try:
        from openrouter_provider import create_openrouter_provider
        provider = create_openrouter_provider()
        client = provider.get_client()
        model_name = provider.get_model_name()
        print(f"✅ Using OpenRouter model: {model_name}")
    except ValueError as e:
        print(f"Configuration error: {e}")
        return
    except ImportError:
        print("Please install openai: pip install openai")
        return

    docs = load_texts_from_dir(os.path.join(os.path.dirname(__file__), "assets"))
    if not docs:
        print("No .txt documents found in assets/")
        return

    chunks = []
    for doc in docs:
        chunks.extend(chunk_text(doc))

    embeddings = embed_chunks(client, chunks)
    index = build_faiss_index(embeddings)

    question = "What is RAG and how does it work?"
    q_vec = embed_query(client, question)
    idxs, _ = top_k(index, q_vec, k=4)
    context = [chunks[i] for i in idxs]
    answer = answer_with_context(client, question, context, model_name)
    print("Q:", question)
    print("A:", answer)


if __name__ == "__main__":
    main()


