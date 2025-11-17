#!/usr/bin/env python3
"""
loader.py — Loading and validating YAML questions
"""

import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
QUESTIONS_DIR = BASE_DIR / "questions"


def list_question_files():
    """Return all YAML files inside /questions."""
    if not QUESTIONS_DIR.exists():
        raise FileNotFoundError(f"Questions directory not found: {QUESTIONS_DIR}")

    return sorted(f for f in QUESTIONS_DIR.glob("*.yml"))


def select_questions_file():
    """Show an interactive menu to select a YAML file."""
    files = list_question_files()

    if not files:
        raise FileNotFoundError("No .yml files found in /questions")

    print("=== Select a question set ===\n")

    for i, f in enumerate(files, 1):
        print(f"  {i}. {f.name}")

    print("\nType 'exit' to quit.\n")

    while True:
        choice = input("Choose a file number: ").strip()

        if choice.lower() == "exit":
            print("Exiting quiz.")
            exit(0)

        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(files):
                return files[idx - 1]

        print("Invalid choice, try again.\n")


def load_questions(path=None):
    """
    Load and return questions from a YAML file.
    If path is None, the user selects it via menu.
    """
    if path is None:
        path = select_questions_file()

    if not path.exists():
        raise FileNotFoundError(f"YAML file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        raise ValueError(f"Invalid YAML format in {path}")

    if "quiz" not in data:
        raise ValueError(f"Invalid YAML: missing 'quiz' key in {path}")

    quiz = data["quiz"]

    if "metadata" not in quiz:
        raise ValueError(f"Invalid YAML: missing 'metadata' in quiz section ({path})")

    if "questions" not in quiz:
        raise ValueError(f"Invalid YAML: missing 'questions' list in quiz section ({path})")

    if not isinstance(quiz["questions"], list):
        raise ValueError(f"'questions' must be a list in {path}")

    return quiz