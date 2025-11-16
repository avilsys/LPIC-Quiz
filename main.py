#!/usr/bin/env python3
"""
main.py — Launch the LPIC quiz
"""

import argparse
from quiz.engine import run_quiz

def parse_args():
    parser = argparse.ArgumentParser(description="Launch the LPIC quiz")
    parser.add_argument(
        "-q", "--questions",
        type=int,
        default=20,
        help="Number of questions to ask (default: 20)"
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    run_quiz(num_questions=args.questions)
