#!/usr/bin/env python3
"""
loader.py — Loading and validating YAML questions
"""

import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Path to the questions file
QUESTIONS_FILE = BASE_DIR / "questions" / "LPIC-201.yml"


def load_questions():
    """Load and return questions from the YAML file."""
    if not QUESTIONS_FILE.exists():
        raise FileNotFoundError(f"YAML file not found: {QUESTIONS_FILE}")

    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if "quiz" not in data or "questions" not in data["quiz"]:
        raise ValueError("Invalid YAML: missing 'quiz' or 'questions' key")

    return data["quiz"]["questions"]
