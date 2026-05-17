# Lab 11 - Differences Between AI Concepts
# Programming for Artificial Intelligence

"""
Task 1: Describe the Difference Between the Following Concepts
"""

concepts = {

    "1. LangChain": """
    LangChain is a Python framework used to build applications powered by Large Language Models (LLMs).
    It helps connect LLMs with tools, databases, APIs, and memory.
    Example: Building a chatbot that can search the web and remember previous messages.
    """,

    "2. LLMs (Large Language Models)": """
    LLMs are AI models trained on huge amounts of text data to understand and generate human language.
    They can answer questions, write code, summarize text, and more.
    Examples: GPT-4, Claude, Gemini, LLaMA.
    """,

    "3. RAG (Retrieval-Augmented Generation)": """
    RAG is a technique where an LLM first RETRIEVES relevant documents from a database,
    then uses that information to GENERATE a better and more accurate answer.
    It helps LLMs answer questions about specific/custom data they were not trained on.
    """,

    "4. FAISS (Facebook AI Similarity Search)": """
    FAISS is a library by Facebook/Meta used to search through large collections of vectors quickly.
    It finds the most similar vectors to a given query vector.
    Used in RAG systems to find relevant documents based on meaning (semantic search).
    """,

    "5. Vector": """
    A vector is a list of numbers that represents the meaning of text in a mathematical way.
    Example: The word 'cat' might be represented as [0.2, 0.8, 0.1, ...].
    Similar words have similar vectors. This is also called an 'embedding'.
    """,

    "6. VectorDB (Vector Database)": """
    A VectorDB is a special database designed to store and search vectors (embeddings).
    Unlike regular databases that match exact values, VectorDB matches by SIMILARITY.
    Examples: Pinecone, Chroma, Weaviate, FAISS.
    Used in AI apps to find relevant content by meaning, not just keywords.
    """,

    "7. Generative AI (GenAI)": """
    Generative AI refers to AI systems that can CREATE new content - text, images, audio, video, code.
    It learns patterns from training data and generates new similar content.
    Examples: ChatGPT (text), DALL-E (images), Sora (video), GitHub Copilot (code).
    """,

    "8. GANs (Generative Adversarial Networks)": """
    GANs are a type of deep learning model consisting of two neural networks:
    - Generator: tries to create fake/realistic data (e.g., fake images)
    - Discriminator: tries to detect if data is real or fake
    They compete against each other, making the generator better over time.
    Used for: generating realistic images, deepfakes, data augmentation.
    """
}

for concept, explanation in concepts.items():
    print(f"\n{'='*60}")
    print(f"  {concept}")
    print(f"{'='*60}")
    print(explanation)
