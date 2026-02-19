"""
02 – Zero-shot Prompt
=====================
The model performs a task with no prior examples.
*Different example*: sentiment analysis instead of true/false classification.
"""

from __future__ import annotations
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from .config import llm_model


def run() -> None:
    params = {
        GenParams.MAX_NEW_TOKENS: 64,
        GenParams.TEMPERATURE: 0.3,
    }

    prompt = """Classify the sentiment of the following review as Positive, Negative, or Neutral:

Review: "The new café downtown has excellent espresso but the seating area is way too small."

Sentiment:
"""

    response = llm_model(prompt, params)
    print(f"Prompt:\n{prompt}")
    print(f"Response: {response}\n")
