"""
Compare chunking strategies (size/overlap) by simple retrieval hit heuristics on a few queries.
"""

import os
from typing import List, Tuple
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from embeddings_utils import (
    load_texts_from_dir,
    chunk_text,
    embed_texts,
    build_index,
)


def evaluate_strategy(client: InferenceClient, docs: List[str], size: int, overlap: int, queries: List[str]) -> Tuple[int, int]:
    chunks: List[str] = []
    for d in docs:
        chunks.extend(chunk_text(d, chunk_size=size, overlap=overlap))
    vecs = embed_texts(client, chunks)
    index = build_index(vecs)
    import numpy as np, faiss
    hits = 0
    for q in queries:
        q_vec = embed_texts(client, [q])[0]
        faiss.normalize_L2(q_vec.reshape(1, -1))
        scores, idxs = index.search(q_vec.reshape(1, -1).astype('float32'), 3)
        # Heuristic: count a hit if score[0] > 0.3
        if len(scores[0]) and scores[0][0] > 0.3:
            hits += 1
    return hits, len(queries)


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
    docs = load_texts_from_dir(assets)
    if not docs:
        print("No .txt files in assets/")
        return

    queries = [
        "What is retrieval augmented generation?",
        "How does chunk overlap help?",
        "What is an embedding used for?",
    ]

    strategies = [(600, 150), (800, 200), (1000, 200)]
    for size, ov in strategies:
        hits, total = evaluate_strategy(client, docs, size, ov, queries)
        print(f"size={size}, overlap={ov} -> hits {hits}/{total}")


if __name__ == "__main__":
    main()


