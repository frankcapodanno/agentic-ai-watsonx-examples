# LangChain + IBM Watsonx

A hands-on project that demonstrates **every technique** from the
*"Foundations of Generative AI and LangChain"*, each with
**different examples** so you can compare and learn.

---

## Topics covered

| # | Example | Cheat-sheet concept |
|---|---------|---------------------|
| 1 | `basic_prompt` | Basic Prompt |
| 2 | `zero_shot` | Zero-shot Prompt |
| 3 | `one_shot` | One-shot Prompt |
| 4 | `few_shot` | Few-shot Prompt |
| 5 | `chain_of_thought` | Chain-of-Thought (CoT) |
| 6 | `self_consistency` | Self-consistency |
| 7 | `gen_params` | GenParams exploration |
| 8 | `prompt_template` | PromptTemplate |
| 9 | `runnable_lambda` | RunnableLambda |
| 10 | `str_output_parser` | StrOutputParser |
| 11 | `lcel_pattern` | LCEL Pattern |

---

## Prerequisites

- **Python 3.10+ <= 3.12 **
- An **IBM Cloud** account with Watsonx.ai access

## Setup

```powershell
# 1. Create and activate a virtual environment (recommended)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set environment variables
$env:WATSONX_URL = "https://us-south.ml.cloud.ibm.com"
$env:WATSONX_PROJECT_ID = "skills-network"     # or your project id
$env:WATSONX_API_KEY = "<your-ibm-api-key>"    # optional inside Skills Network
```

## Run

```powershell
# List all examples
python main.py list

# Run a single example
python main.py run basic_prompt
python main.py run lcel_pattern

# Run ALL examples in order
python main.py run all
```

## Project structure

```
python-cheatsheet-examples/
├── main.py                        # CLI entry point
├── requirements.txt               # pinned dependencies
├── README.md                      # this file
├── LICENSE                        # Unlicense (public domain)
└── examples/
    ├── __init__.py
    ├── config.py                  # WatsonxLLM + llm_model helper
    ├── registry.py                # maps names → run() functions
    ├── ex01_basic_prompt.py
    ├── ex02_zero_shot.py
    ├── ex03_one_shot.py
    ├── ex04_few_shot.py
    ├── ex05_chain_of_thought.py
    ├── ex06_self_consistency.py
    ├── ex07_gen_params.py
    ├── ex08_prompt_template.py
    ├── ex09_runnable_lambda.py
    ├── ex10_str_output_parser.py
    └── ex11_lcel_pattern.py
```

## Notes

- Every example uses **different prompts/tasks** compared to the original
  cheat-sheet so you get extra practice.
- All IBM Watsonx config is centralised in `examples/config.py`.
- You can override `WATSONX_URL`, `WATSONX_PROJECT_ID`, and
  `WATSONX_APIKEY` via environment variables.

## License

This project is released into the **public domain** under the
[Unlicense](LICENSE) — free to use, modify, and redistribute for any
purpose (including commercial), with no conditions whatsoever.
The software is provided **AS IS**, without warranty of any kind.

---
