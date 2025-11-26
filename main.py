#!/usr/bin/env python3
"""
main.py — Launch the LPIC quiz
"""

import argparse
from quiz.engine import run_quiz

def parse_args():
    parser = argparse.ArgumentParser(description="Launch the LPIC quiz")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-q", "--questions", type=int, default=20, help="Number of questions to ask (default: 20)")
    group.add_argument("--id", type=str, help="Ask only the question with the given ID")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    run_quiz(num_questions=args.questions, question_id=args.id)
