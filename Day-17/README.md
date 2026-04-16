# 🕒 Day 17: Embeddings & Similarity Search Fundamentals

🏁 Goal: Learn how to chunk text, create embeddings, build a FAISS index, and run similarity search to power basic retrieval.

---

## 🧠 Core Concepts Explained

### 📝 **What are Embeddings?**
Embeddings are numerical representations of text that capture semantic meaning. Think of them as coordinates in a high-dimensional space where similar texts are positioned close together.

**Key Properties:**
- **Semantic Similarity**: "cat" and "kitten" will have similar embeddings
- **Fixed Dimensions**: Each text becomes a vector of the same length (e.g., 1024 numbers)
- **Mathematical Operations**: You can measure distance between texts using vector math

**Example:**
```python
# Text: "The weather is sunny today"
# Embedding: [0.1, -0.3, 0.8, 0.2, ...] (1024 numbers)
```

### 🔍 **What is Similarity Search?**
Similarity search finds the most relevant documents for a query by comparing their embeddings. It's like asking "which documents are most similar to my question?"

**How it works:**
1. Convert your query to an embedding
2. Compare it with all document embeddings using cosine similarity
3. Return the top-k most similar documents

**Real-world analogy:** Like finding similar songs on Spotify or similar products on Amazon.

### ✂️ **What is Chunking?**
Chunking splits long documents into smaller, manageable pieces. This is crucial because:
- **Context Limits**: AI models have token limits (e.g., 8K tokens)
- **Precision**: Smaller chunks provide more focused, relevant results
- **Efficiency**: Faster processing and better retrieval

**Chunking Strategies:**
- **Size**: How many characters per chunk (e.g., 800 chars)
- **Overlap**: How much text overlaps between chunks (e.g., 200 chars)
- **Method**: Fixed size, sentence boundaries, or semantic splitting

**Example:**
```
Original: "Machine learning is a subset of artificial intelligence..."
Chunk 1: "Machine learning is a subset of artificial intelligence that focuses on algorithms..."
Chunk 2: "...algorithms that can learn and make decisions from data without being explicitly programmed..."
```

---

## 🎯 **How These Concepts Work Together**

Let's see how embeddings, chunking, and similarity search work together using the sample files:

### 📄 **Sample Content** (`assets/sample_content.txt`)
The sample file contains engaging content about American politics and recent news, including:
- 2024 Presidential Election and campaign dynamics
- Congressional gridlock and bipartisan efforts
- Supreme Court decisions and their impact
- State and local politics
- Media and political communication
- International relations and foreign policy

### 🔄 **The Complete Pipeline**

1. **Chunking**: The sample text gets split into manageable pieces
2. **Embedding**: Each chunk becomes a numerical vector
3. **Indexing**: Vectors are stored in FAISS for fast search
4. **Querying**: Your question becomes a vector and finds similar chunks

### 🧪 **Try These Fun Example Queries**
When you run the similarity search, try asking:

- *"What about the 2024 election?"* → Will find content about the presidential race
- *"Tell me about Congress"* → Will retrieve information about congressional gridlock
- *"What are the Supreme Court decisions?"* → Will find content about recent court cases
- *"How does social media affect politics?"* → Will return the media and communication section
- *"What about foreign policy?"* → Will find information about international relations

The system will:
- Convert your question to an embedding
- Find the most relevant chunks from the political content
- Return them ranked by similarity score

---

## 📚 Overview

You will:
- Load local `.txt` files and chunk them into manageable pieces
- Create embeddings with Hugging Face (`intfloat/multilingual-e5-large`)
- Build a FAISS index for fast similarity search
- Compare chunking strategies and visualize embeddings in 2D

---

## ✅ Learning Objectives

After completing this lesson, you will be able to:

1) **Understand Chunking**: Learn how to split documents into optimal-sized pieces with proper overlap
2) **Create Embeddings**: Convert text into numerical vectors that capture semantic meaning
3) **Build Vector Index**: Store embeddings in FAISS for fast similarity search
4) **Retrieve Relevant Content**: Find the most similar chunks for any query
5) **Visualize Embeddings**: See how similar texts cluster together in 2D space
6) **Optimize Strategies**: Compare different chunking approaches for better results

---

## ⚙️ Quick Setup (Day-17 only)

- Install dependencies:
```bash
pip install -r requirements.txt
```

- Create `.env` (repo root or ``) with:
```bash
HF_TOKEN=your_huggingface_token
```
  - Get your token from: https://huggingface.co/settings/tokens
  - Make sure it has "Inference Providers" permission

- Sample content is already included in `assets/sample_content.txt`
- You can add your own `.txt` files to the `assets/` directory for testing

---

## ▶️ How to Run

### 🚀 **Step-by-Step Learning Path**

**1) Test Your Setup First**
```bash
python test_hf_integration.py
```
*This verifies your Hugging Face API connection and shows you how embeddings work.*

**2) Generate Your First Embeddings**
```bash
python 01_generate_embeddings.py
```
*This loads your text files, chunks them, creates embeddings, and builds a searchable index.*

**3) Try Similarity Search**
```bash
python 02_similarity_search.py
```
*Enter your own questions and see how the system finds relevant chunks!*

**4) Experiment with Chunking**
```bash
python 03_chunking_experiments.py
```
*Compare different chunk sizes and overlaps to see which works best.*

**5) Visualize Your Embeddings**
```bash
python 04_tsne_visualize.py
```
*See how similar texts cluster together in 2D space.*

### 📁 **Output Files**
All results are saved to `outputs/`:
- `faiss.index`: Your searchable vector index
- `chunks.json`: All text chunks with their metadata
- `tsne_plot.png`: 2D visualization of your embeddings

---

## 📁 Files Explained

### 🔧 **Core Utilities**
- `embeddings_utils.py`: All the helper functions for loading, chunking, embedding, and searching

### 🎯 **Learning Scripts**
- `01_generate_embeddings.py`: **Start here!** Creates embeddings from your text files
- `02_similarity_search.py`: **Try this next!** Search for relevant content with your own queries
- `03_chunking_experiments.py`: **Experiment!** Compare different chunking strategies
- `04_tsne_visualize.py`: **Visualize!** See your embeddings in 2D space

### 🧪 **Testing & Setup**
- `test_hf_integration.py`: Verify your Hugging Face API setup works correctly

### 📂 **Data & Output**
- `assets/`: Contains `sample_content.txt` with comprehensive examples (add your own `.txt` files here)
- `outputs/`: Generated files (index, chunks, visualizations)

---

## 🧪 Tips for Success

### 📏 **Chunking Best Practices**
- **Start with**: chunk_size ≈ 800 characters, overlap ≈ 200 characters
- **Adjust based on content**: Technical docs might need larger chunks, conversational text smaller ones
- **Overlap is crucial**: Prevents losing context at chunk boundaries

### 🔍 **Search Optimization**
- **Keep top-k small**: 3-6 results usually sufficient
- **Clean your text**: Remove extra whitespace and boilerplate before embedding
- **Test different queries**: Try various phrasings to see how the system responds

### 🤖 **Model Selection**
- **Default**: `intfloat/multilingual-e5-large` (good for most languages)
- **Alternative**: `sentence-transformers/all-MiniLM-L6-v2` (faster, smaller)
- **Change model**: Edit the `model` parameter in `embed_texts()` calls

### 💡 **Learning Tips**
- **Start simple**: Use the sample files first, then try your own documents
- **Experiment**: Try different chunk sizes and see how it affects search quality
- **Visualize**: The t-SNE plot helps you understand how your embeddings cluster
- **Iterate**: Run experiments multiple times with different parameters

---

Happy searching!
