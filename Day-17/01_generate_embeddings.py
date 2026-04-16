"""
Build embeddings and FAISS index from local .txt files and save artifacts.
"""

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from embeddings_utils import (
    load_texts_from_dir,
    chunk_text,
    embed_texts,
    build_index,
    save_artifacts,
)


def main() -> None:
    load_dotenv()
    if not os.getenv("HF_TOKEN"):
        print("Please set HF_TOKEN in your .env file")
        return

    client = InferenceClient(
        provider="hf-inference",
        api_key=os.getenv("HF_TOKEN"),
    )
    base = os.path.dirname(__file__)
    assets = os.path.join(base, "assets")
    outputs = os.path.join(base, "outputs")
    os.makedirs(outputs, exist_ok=True)

    docs = load_texts_from_dir(assets)
    if not docs:
        print("No .txt files found in assets/")
        return

    chunks = []
    for d in docs:
        chunks.extend(chunk_text(d, chunk_size=800, overlap=200))

    vecs = embed_texts(client, chunks)
    index = build_index(vecs)
    save_artifacts(outputs, index, chunks)
    print("Saved FAISS index and chunks.json to outputs/")


if __name__ == "__main__":
    main()


