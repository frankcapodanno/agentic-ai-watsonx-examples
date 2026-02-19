"""
01 – Basic Prompt
=================
The simplest form: give the model a short phrase and let it continue.
*Different example from the cheat-sheet* (which used "The wind is").
"""

from __future__ import annotations
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from .config import llm_model


def run() -> None:
    params = {
        GenParams.MAX_NEW_TOKENS: 150,
        GenParams.MIN_NEW_TOKENS: 10,
        GenParams.TEMPERATURE: 0.5,
        GenParams.TOP_P: 0.2,
        GenParams.TOP_K: 1,
    }

    prompt = "Why we judge people by their appearance?"

    response = llm_model(prompt, params)
    print(f"Prompt : {prompt}")
    print(f"Response: {response}\n")
