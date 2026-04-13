from typing import Dict, Any
import random

# Example set of designers
designers = [
    {"name": "Alice", "styles": ["Modern", "Minimalist"], "budget": "High"},
    {"name": "Bob", "styles": ["Classic", "Bohemian"], "budget": "Medium"},
    {"name": "Carol", "styles": ["Industrial"], "budget": "Low"},
    {"name": "Dave", "styles": ["Modern"], "budget": "Medium"},
]

def match_designers(style: str, budget: str) -> Dict[str, Any]:
    """
    Rule-based matchmaking: filter designers by style and budget.
    Returns matched designers or random fallback.
    """
    matches = [d for d in designers if style in d["styles"] and d["budget"] == budget]
    if not matches:
        # Fallback to random picks if no exact matches
        matches = random.sample(designers, k=min(2, len(designers)))
    return {"matched_designers": matches}
