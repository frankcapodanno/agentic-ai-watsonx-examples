#!/usr/bin/env python
"""
CLI runner for the LangChain + IBM Watsonx cheat-sheet examples.

Usage:
    python main.py list               # show all available examples
    python main.py run basic_prompt   # run a specific example
    python main.py run all            # run every example in order
"""

from __future__ import annotations

import argparse
import sys

from examples.registry import EXAMPLES


def list_examples() -> None:
    print("Available examples:\n")
    for i, key in enumerate(EXAMPLES, 1):
        print(f"  {i:>2}. {key}")
    print()


def run_example(name: str) -> None:
    if name == "all":
        for key, fn in EXAMPLES.items():
            print(f"\n{'='*60}")
            print(f"  {key}")
            print(f"{'='*60}\n")
            fn()
        return

    fn = EXAMPLES.get(name)
    if fn is None:
        print(f"Unknown example: '{name}'")
        print("Use 'python main.py list' to see available names.")
        sys.exit(1)

    print(f"\n== {name} ==\n")
    fn()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="LangChain + IBM Watsonx cheat-sheet examples"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="List available examples")
    run_p = sub.add_parser("run", help="Run a specific example (or 'all')")
    run_p.add_argument("name", help="Example name or 'all'")

    return parser


def main() -> None:
    args = build_parser().parse_args()

    if args.command == "list":
        list_examples()
    elif args.command == "run":
        run_example(args.name)


if __name__ == "__main__":
    main()
