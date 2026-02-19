"""
04 – Few-shot Prompt
====================
Multiple examples to establish a clear pattern.
*Different example*: product-category classification (cheat-sheet used emotion classification).
"""

from __future__ import annotations
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from .config import llm_model


def run() -> None:
    params = {
        GenParams.MAX_NEW_TOKENS: 10,
        GenParams.TEMPERATURE: 0.2,
    }

    prompt = """Classify each product into a category.

Product: "Nike Air Max 90"
Category: Footwear

Product: "Samsung Galaxy S24"
Category: Electronics

Product: "Barilla Spaghetti No.5"
Category: Food

Now classify:
Product: "Kindle Paperwhite"
Category:
"""

    response = llm_model(prompt, params)
    print(f"Prompt:\n{prompt}")
    print(f"Response: {response}\n")
