"""
03 – One-shot Prompt
====================
Provide a single example so the model learns the pattern.
*Different example*: English → Italian translation (cheat-sheet used English → French).
"""

from __future__ import annotations
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from .config import llm_model


def run() -> None:
    params = {
        GenParams.MAX_NEW_TOKENS: 30,
        GenParams.TEMPERATURE: 0.1,
    }

    prompt = """Here is an example of translating a sentence from English to Italian:

English: "Good morning, how are you?"
Italian: "Buongiorno, come stai?"

Now, translate the following sentence from English to Italian:
English: "Can you recommend a good restaurant nearby?"
"""

    response = llm_model(prompt, params)
    print(f"Prompt:\n{prompt}")
    print(f"Response: {response}\n")
