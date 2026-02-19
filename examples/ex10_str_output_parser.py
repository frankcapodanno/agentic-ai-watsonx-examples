"""
10 – StrOutputParser
====================
Extracts a clean string from LLM output — typically the last step in a chain.
*Different example*: capital-city lookup.
"""

from __future__ import annotations
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from .config import get_llm


def run() -> None:
    template = """What is the capital of {country}? Answer in one word."""
    prompt = PromptTemplate.from_template(template)

    def format_prompt(variables: dict) -> str:
        return prompt.format(**variables)

    chain = (
        RunnableLambda(format_prompt)
        | get_llm()
        | StrOutputParser()
    )

    for country in ["Japan", "Brazil", "Egypt"]:
        result = chain.invoke({"country": country})
        print(f"Capital of {country}: {result.strip()}")
    print()
