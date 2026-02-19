"""
07 – GenParams exploration
==========================
Shows how to use GenTextParamsMetaNames to discover and set generation parameters.
"""

from __future__ import annotations
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from .config import llm_model


def run() -> None:
    # Print available parameter names
    print("Available GenParams fields:")
    print(f"  MAX_NEW_TOKENS = {GenParams.MAX_NEW_TOKENS}")
    print(f"  MIN_NEW_TOKENS = {GenParams.MIN_NEW_TOKENS}")
    print(f"  TEMPERATURE    = {GenParams.TEMPERATURE}")
    print(f"  TOP_P          = {GenParams.TOP_P}")
    print(f"  TOP_K          = {GenParams.TOP_K}")
    print()

    # Low temperature → deterministic
    params_low = {
        GenParams.MAX_NEW_TOKENS: 60,
        GenParams.TEMPERATURE: 0.0,
    }
    response_low = llm_model("Name three famous Italian painters:", params_low)
    print(f"[temperature=0.0]  {response_low.strip()}")

    # High temperature → creative
    params_high = {
        GenParams.MAX_NEW_TOKENS: 60,
        GenParams.TEMPERATURE: 1.0,
    }
    response_high = llm_model("Name three famous Italian painters:", params_high)
    print(f"[temperature=1.0]  {response_high.strip()}\n")
