#!/usr/bin/env python3
"""
engine.py — Quiz engine
"""

import random
import time
from datetime import datetime, timezone

from quiz.loader import load_questions
from quiz.utils import normalize, parse_multi_answer, format_colored
from quiz.logger import log_error


def run_quiz(num_questions=None):
    """
    Run the quiz.
    
    :param num_questions: maximum number of questions to ask (default: all)
    """
    # Load and randomize questions
    questions = load_questions()
    random.shuffle(questions)

    # Limit number of questions if requested
    if num_questions is not None:
        questions = questions[:min(num_questions, len(questions))]

    print("=== LPIC Quiz ===")
    print("Type 'exit' to quit.\n")

    session_start = time.time()
    start_dt = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

    total = 0
    correct = 0
    error_session = []

    for q in questions:
        total += 1
        question = q["question"]
        choices = q["choices"]
        correct_answers = q["correct"]

        print(f"\nQuestion {total}: {question}\n")
        for i, c in enumerate(choices, 1):
            print(f"  {i}. {c}")

        try:
            raw_input = input("\nAnswer (e.g., 1 3): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nQuiz interrupted.")
            break

        if raw_input.lower() == "exit":
            print("Exiting quiz.")
            break

        nums = parse_multi_answer(raw_input, len(choices))
        if not nums:
            print(format_colored(f"❌ Invalid answer: choose numbers between 1 and {len(choices)}.", "red"))
            user_answers_text = []
        else:
            user_answers_text = [choices[n - 1] for n in nums]

        normalized_correct = [normalize(a) for a in correct_answers]
        normalized_user = [normalize(a) for a in user_answers_text]

        is_correct = sorted(normalized_user) == sorted(normalized_correct)

        if is_correct:
            print(format_colored("✅ Correct!", "green"))
            correct += 1
        else:
            print(format_colored("❌ Wrong!", "red"))
            print(f"Correct answer(s): {', '.join(correct_answers)}")

            error_session.append({
                "question": question,
                "user_answer": user_answers_text,
                "correct": correct_answers,
            })

            log_error(question, user_answers_text, correct_answers)

    # Session summary
    duration_s = int(time.time() - session_start)
    print("\n=== Session Summary ===\n")
    print(f"Start:   {start_dt}")
    print(f"Duration: {duration_s} seconds")
    print(f"Total questions: {total}")
    print(f"Correct answers: {correct}")
    print(f"Errors: {len(error_session)}")

    if error_session:
        print("\nDetails of errors:")
        for e in error_session:
            print(f"  - Q='{e['question']}' | Answer='{e['user_answer']}' | Correct='{e['correct']}'")

    print("\nAll errors have been logged to 'errors.log'.\n")
