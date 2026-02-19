"""
Centralised IBM Watsonx LLM configuration.

Environment variables required:
  WATSONX_URL        – e.g. https://us-south.ml.cloud.ibm.com
  WATSONX_PROJECT_ID – your project id  (default: "skills-network")
  WATSONX_APIKEY     – your IAM API key (optional when running inside Skills Network)
"""

from __future__ import annotations

import os
import warnings

from langchain_ibm import WatsonxLLM
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

# ---------------------------------------------------------------------------
# Suppress noisy deprecation / connection warnings
# ---------------------------------------------------------------------------
warnings.filterwarnings("ignore")

# ---------------------------------------------------------------------------
# Default generation parameters (overridable per-example)
# ---------------------------------------------------------------------------
DEFAULT_PARAMS: dict = {
    GenParams.MAX_NEW_TOKENS: 256,
    GenParams.TEMPERATURE: 0.5,
    GenParams.TOP_P: 0.2,
}

# ---------------------------------------------------------------------------
# Model id
# ---------------------------------------------------------------------------
MODEL_ID = "ibm/granite-3-3-8b-instruct"


def get_llm(params: dict | None = None) -> WatsonxLLM:
    """Return a ready-to-use WatsonxLLM instance."""
    merged = {**DEFAULT_PARAMS, **(params or {})}
    return WatsonxLLM(
        model_id=MODEL_ID,
        url=os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com"),
        project_id=os.getenv("WATSONX_PROJECT_ID", "skills-network"),
        params=merged,
    )


def llm_model(prompt_txt: str, params: dict | None = None) -> str:
    """Convenience wrapper: build LLM, invoke, return text."""
    llm = get_llm(params)
    return llm.invoke(prompt_txt)
