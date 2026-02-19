"""
09 – RunnableLambda
===================
Wrap a plain Python function into a LangChain runnable step.
*Different example*: uppercase preprocessing (cheat-sheet used format_prompt).
"""

from __future__ import annotations
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from .config import get_llm


def run() -> None:
    template = """Translate the following word to Spanish: {word}"""
    prompt = PromptTemplate.from_template(template)

    # A lambda that formats variables into the prompt string
    def format_and_upper(variables: dict) -> str:
        text = prompt.format(**variables)
        return text.upper()  # just to show transformation

    chain = (
        RunnableLambda(format_and_upper)
        | get_llm()
        | StrOutputParser()
    )

    result = chain.invoke({"word": "butterfly"})
    print(f"Chain result: {result}\n")
