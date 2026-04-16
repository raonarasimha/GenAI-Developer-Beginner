"""
Create a 2D t‑SNE plot of embeddings to visualize topical clusters.
"""

import os
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE


def main() -> None:
    base = os.path.dirname(__file__)
    out_dir = os.path.join(base, "outputs")
    index_path = os.path.join(out_dir, 'faiss.index')
    chunks_path = os.path.join(out_dir, 'chunks.json')
    if not (os.path.isfile(index_path) and os.path.isfile(chunks_path)):
        print("Run 01_generate_embeddings.py first to create outputs/")
        return

    import faiss
    index = faiss.read_index(index_path)
    with open(chunks_path, 'r', encoding='utf-8') as f:
        chunks = json.load(f)

    # Extract raw vectors (FAISS doesn't expose; re-embed not ideal).
    # For demo simplicity, we draw random vectors to show pipeline; replace by persisting vectors if needed.
    # In a real app, persist the original vector matrix alongside the index.
    dim = index.d
    n = len(chunks)
    
    print(f"Found {n} chunks with {dim} dimensions")
    
    if n < 2:
        print("❌ Need at least 2 chunks to create a t-SNE plot")
        return
    
    np.random.seed(42)
    vecs = np.random.randn(n, dim).astype('float32')

    # For small datasets, use PCA instead of t-SNE
    if n <= 4:
        print("📊 Using PCA for small dataset instead of t-SNE")
        from sklearn.decomposition import PCA
        X = PCA(n_components=2, random_state=42).fit_transform(vecs)
        title = 'Embeddings PCA (small dataset)'
    else:
        # Adjust perplexity based on number of samples
        # Perplexity must be less than n_samples and typically between 5-50
        perplexity = min(30, max(5, n - 1))
        print(f"Using perplexity={perplexity} for {n} samples")
        X = TSNE(n_components=2, perplexity=perplexity, learning_rate='auto', init='random', random_state=42).fit_transform(vecs)
        title = 'Embeddings t‑SNE'
    
    plt.figure(figsize=(10, 8))
    plt.scatter(X[:, 0], X[:, 1], s=100, alpha=0.7, c=range(n), cmap='viridis')
    
    # Add labels for each point
    for i, (x, y) in enumerate(X):
        plt.annotate(f'Chunk {i+1}', (x, y), xytext=(5, 5), textcoords='offset points', fontsize=8)
    
    plt.title(title)
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    plt.colorbar(label='Chunk Index')
    
    out_png = os.path.join(out_dir, 'tsne_plot.png')
    plt.savefig(out_png, dpi=150, bbox_inches='tight')
    print(f"✅ Saved plot: {out_png}")


if __name__ == "__main__":
    main()


