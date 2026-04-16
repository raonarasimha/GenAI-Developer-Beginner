"""
Query the saved FAISS index and print top‑k similar chunks.
"""

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from embeddings_utils import (
    load_artifacts,
    embed_texts,
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
    outputs = os.path.join(base, "outputs")
    index, chunks = load_artifacts(outputs)

    q = input("Enter your query: ").strip()
    if not q:
        print("(empty query)")
        return

    q_vec = embed_texts(client, [q])[0]
    import faiss, numpy as np
    faiss.normalize_L2(q_vec.reshape(1, -1))
    scores, idxs = index.search(q_vec.reshape(1, -1).astype('float32'), 5)

    print("Top matches:")
    for rank, (i, s) in enumerate(zip(idxs[0], scores[0]), 1):
        if i < 0:
            continue
        print(f"#{rank} (score {s:.3f}):\n{chunks[i][:300]}\n---")


if __name__ == "__main__":
    main()


