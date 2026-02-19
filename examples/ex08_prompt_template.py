"""
08 – PromptTemplate
===================
Reusable prompt with dynamic placeholders.
*Different example*: recipe suggestion (cheat-sheet used a joke).
"""

from __future__ import annotations
from langchain_core.prompts import PromptTemplate
from .config import get_llm


def run() -> None:
    template = """Suggest a {difficulty} recipe for {dish} using only {max_ingredients} ingredients."""
    prompt = PromptTemplate.from_template(template)

    # Show the formatted string
    formatted = prompt.format(
        difficulty="easy",
        dish="pasta carbonara",
        max_ingredients="5",
    )
    print(f"Formatted prompt:\n  {formatted}\n")

    # Actually invoke the LLM
    llm = get_llm()
    response = llm.invoke(formatted)
    print(f"Response:\n{response}\n")
