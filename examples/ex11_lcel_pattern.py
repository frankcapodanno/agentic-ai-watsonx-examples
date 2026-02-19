"""
11 – LCEL Pattern (LangChain Expression Language)
==================================================
Pipe operator (|) for composable chains.
*Different example*: summarise-then-translate pipeline (cheat-sheet used Q&A).
"""

from __future__ import annotations
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from .config import get_llm


def run() -> None:
    # ----- Chain 1: Summarise a paragraph -----
    summary_template = """Summarise the following text in one sentence:

{text}

Summary:
"""
    summary_prompt = PromptTemplate.from_template(summary_template)

    def format_summary(variables: dict) -> str:
        return summary_prompt.format(**variables)

    llm = get_llm()

    summary_chain = (
        RunnableLambda(format_summary)
        | llm
        | StrOutputParser()
    )

    paragraph = (
        "The Amazon rainforest produces roughly 20 percent of the world's oxygen "
        "and is home to an estimated 10 percent of all species on Earth. "
        "Deforestation threatens biodiversity and accelerates climate change."
    )

    summary = summary_chain.invoke({"text": paragraph})
    print(f"Summary : {summary.strip()}\n")

    # ----- Chain 2: Translate that summary to Italian -----
    translate_template = """Translate the following sentence into Italian:

{sentence}

Translation:
"""
    translate_prompt = PromptTemplate.from_template(translate_template)

    def format_translate(variables: dict) -> str:
        return translate_prompt.format(**variables)

    translate_chain = (
        RunnableLambda(format_translate)
        | llm
        | StrOutputParser()
    )

    translation = translate_chain.invoke({"sentence": summary.strip()})
    print(f"Italian : {translation.strip()}\n")
