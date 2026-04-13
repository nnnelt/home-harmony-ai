from typing import Dict, Any

def load_text_search_model():
    """
    Placeholder for loading a text search model (e.g., TF-IDF, embeddings).
    Run once at startup.
    """
    print("✅ Text search model loaded")

def search_products(query: str) -> Dict[str, Any]:
    """
    Placeholder text-based search logic.
    Returns the query and dummy product matches.
    """
    return {
        "query": query,
        "results": [
            f"Product matching '{query}' #1",
            f"Product matching '{query}' #2"
        ]
    }
