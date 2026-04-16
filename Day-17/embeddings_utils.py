import os
import json
from typing import List, Tuple

import numpy as np
import faiss
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()


def load_texts_from_dir(path: str) -> List[str]:
    texts: List[str] = []
    for name in os.listdir(path):
        if name.lower().endswith('.txt'):
            with open(os.path.join(path, name), 'r', encoding='utf-8') as f:
                texts.append(f.read())
    return texts


def chunk_text(text: str, chunk_size: int = 800, overlap: int = 200) -> List[str]:
    chunks: List[str] = []
    i = 0
    while i < len(text):
        end = min(i + chunk_size, len(text))
        chunks.append(text[i:end])
        if end == len(text):
            break
        i = max(0, end - overlap)
    return chunks


def embed_texts(client: InferenceClient, texts: List[str], model: str = "intfloat/multilingual-e5-large") -> np.ndarray:
    """
    Create embeddings using Hugging Face InferenceClient.
    
    Args:
        client: Hugging Face InferenceClient instance
        texts: List of texts to embed
        model: Model name for embeddings (default: intfloat/multilingual-e5-large)
    
    Returns:
        Normalized embeddings as numpy array
    """
    # Process texts one by one to handle HF API limitations
    embeddings = []
    for i, text in enumerate(texts):
        try:
            result = client.feature_extraction(text, model=model)
            
            # Handle different response formats
            if isinstance(result, list):
                if len(result) > 0 and isinstance(result[0], list):
                    # Nested list format - take the first element
                    embedding = np.array(result[0], dtype='float32')
                else:
                    # Flat list format
                    embedding = np.array(result, dtype='float32')
            else:
                # Direct array format
                embedding = np.array(result, dtype='float32')
            
            # Ensure it's a 1D vector
            if embedding.ndim > 1:
                embedding = embedding.flatten()
                
            embeddings.append(embedding)
            
        except Exception as e:
            print(f"❌ Error embedding text {i+1}: {e}")
            print(f"   Text: {text[:100]}...")
            print(f"   Model: {model}")
            raise
    
    vecs = np.array(embeddings, dtype='float32')
    faiss.normalize_L2(vecs)
    return vecs


def build_index(vectors: np.ndarray) -> faiss.IndexFlatIP:
    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)
    return index


def search(index: faiss.IndexFlatIP, query_vec: np.ndarray, k: int = 5) -> Tuple[List[int], List[float]]:
    q = query_vec.reshape(1, -1).astype('float32')
    faiss.normalize_L2(q)
    scores, idxs = index.search(q, k)
    return idxs[0].tolist(), scores[0].tolist()


def save_artifacts(out_dir: str, index: faiss.IndexFlatIP, chunks: List[str]) -> None:
    os.makedirs(out_dir, exist_ok=True)
    faiss.write_index(index, os.path.join(out_dir, 'faiss.index'))
    with open(os.path.join(out_dir, 'chunks.json'), 'w', encoding='utf-8') as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)


def load_artifacts(out_dir: str) -> Tuple[faiss.IndexFlatIP, List[str]]:
    index = faiss.read_index(os.path.join(out_dir, 'faiss.index'))
    with open(os.path.join(out_dir, 'chunks.json'), 'r', encoding='utf-8') as f:
        chunks = json.load(f)
    return index, chunks


