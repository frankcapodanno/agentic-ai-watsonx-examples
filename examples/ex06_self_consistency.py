"""
06 – Self-consistency
=====================
Generate multiple independent solutions and pick the most consistent answer.
*Different example*: coin-flip probability (cheat-sheet used age riddle).
"""

from __future__ import annotations
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from .config import llm_model


def run() -> None:
    params = {
        GenParams.MAX_NEW_TOKENS: 512,
        GenParams.TEMPERATURE: 0.7,
    }

    prompt = """A fair coin is flipped 3 times.
What is the probability of getting exactly 2 heads?

Provide three independent calculations using different reasoning methods,
then determine the most consistent result.
"""

    response = llm_model(prompt, params)
    print(f"Prompt:\n{prompt}")
    print(f"Response: {response}\n")
