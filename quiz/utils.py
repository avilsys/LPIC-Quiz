#!/usr/bin/env python3
"""
utils.py — Utility functions
"""

import re


def normalize(s: str) -> str:
    """Simple normalization for comparison."""
    return " ".join(s.lower().strip().split())


def parse_multi_answer(raw, max_choice):
    """
    Convert user input into a sorted list of unique numbers.
    Accepted formats: "1 3", "1,3", "1;3", "1-3"
    """
    cleaned = re.sub(r"[;,/-]", " ", raw)
    parts = cleaned.split()

    nums = []
    for p in parts:
        if p.isdigit():
            n = int(p)
            if 1 <= n <= max_choice:
                nums.append(n)
    return sorted(set(nums))


def format_colored(text, color=None):
    """Optional: add ANSI colors for terminal output"""
    colors = {
        "green": "\033[92m",
        "red": "\033[91m",
        "yellow": "\033[93m",
        "reset": "\033[0m",
    }
    if color in colors:
        return f"{colors[color]}{text}{colors['reset']}"
    return text
