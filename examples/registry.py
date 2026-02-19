"""Central registry – maps CLI names to example runner functions."""

from __future__ import annotations

from .ex01_basic_prompt import run as run_basic_prompt
from .ex02_zero_shot import run as run_zero_shot
from .ex03_one_shot import run as run_one_shot
from .ex04_few_shot import run as run_few_shot
from .ex05_chain_of_thought import run as run_cot
from .ex06_self_consistency import run as run_self_consistency
from .ex07_gen_params import run as run_gen_params
from .ex08_prompt_template import run as run_prompt_template
from .ex09_runnable_lambda import run as run_runnable_lambda
from .ex10_str_output_parser import run as run_str_output_parser
from .ex11_lcel_pattern import run as run_lcel

EXAMPLES: dict[str, callable] = {
    "basic_prompt": run_basic_prompt,
    "zero_shot": run_zero_shot,
    "one_shot": run_one_shot,
    "few_shot": run_few_shot,
    "chain_of_thought": run_cot,
    "self_consistency": run_self_consistency,
    "gen_params": run_gen_params,
    "prompt_template": run_prompt_template,
    "runnable_lambda": run_runnable_lambda,
    "str_output_parser": run_str_output_parser,
    "lcel_pattern": run_lcel,
}
