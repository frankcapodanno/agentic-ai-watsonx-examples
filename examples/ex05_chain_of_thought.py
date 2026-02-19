"""
05 – Chain-of-Thought (CoT) Prompting
======================================
Ask the model to reason step-by-step before answering.
*Different example*: travel-time word problem (cheat-sheet used apples).
"""

from __future__ import annotations
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from .config import llm_model


def run() -> None:
    params = {
        GenParams.MAX_NEW_TOKENS: 512,
        GenParams.TEMPERATURE: 0.5,
    }

    prompt = """Consider the problem:
'A train leaves Rome at 09:00 travelling at 120 km/h toward Milan, which is 600 km away.
Another train leaves Milan at 10:00 travelling at 150 km/h toward Rome.
At what time do the two trains meet?'

Break down each step of your calculation before giving the final answer.
"""

    response = llm_model(prompt, params)
    print(f"Prompt:\n{prompt}")
    print(f"Response: {response}\n")
