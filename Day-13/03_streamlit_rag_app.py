"""
Streamlit RAG app: index local .txt files, ask questions with retrieved context.
"""

import os
import streamlit as st
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


def build_index(client: OpenAI, assets_dir: str):
    docs = load_texts_from_dir(assets_dir)
    chunks = []
    for doc in docs:
        chunks.extend(chunk_text(doc))
    vecs = embed_chunks(client, chunks)
    index = build_faiss_index(vecs)
    return chunks, index


def main() -> None:
    load_dotenv()
    st.set_page_config(page_title="Basic RAG", layout="wide")
    st.title("Basic RAG (Retrieval-Augmented Generation)")

    # Check for OpenRouter configuration
    try:
        from openrouter_provider import create_openrouter_provider
        provider = create_openrouter_provider()
        client = provider.get_client()
        model_name = provider.get_model_name()
        st.success(f"✅ Using OpenRouter model: {model_name}")
    except ValueError as e:
        st.error(f"Configuration error: {e}")
        st.stop()
    except ImportError:
        st.error("Please install openai: pip install openai")
        st.stop()
    assets_dir = os.path.join(os.path.dirname(__file__), "assets")

    with st.spinner("Building index from assets/ ..."):
        chunks, index = build_index(client, assets_dir)

    question = st.text_input("Ask a question about your documents")
    k = st.slider("Top-k chunks", 1, 8, 4)

    if st.button("Get Answer", type="primary") and question:
        with st.spinner("Retrieving and answering..."):
            q_vec = embed_query(client, question)
            idxs, scores = top_k(index, q_vec, k=k)
            ctx = [chunks[i] for i in idxs]
            ans = answer_with_context(client, question, ctx, model_name)

        st.subheader("Answer")
        st.write(ans)

        with st.expander("Retrieved Chunks"):
            for i, (idx, sc) in enumerate(zip(idxs, scores), 1):
                st.markdown(f"**{i}. score: {sc:.3f}**\n\n{chunks[idx]}")


if __name__ == "__main__":
    main()


