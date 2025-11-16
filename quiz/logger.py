#!/usr/bin/env python3
"""
logger.py — Error logging management
"""

from pathlib import Path
from datetime import datetime, timezone

ERREURS_LOG = Path("errors.log")


def log_error(question, user_answers, correct_answers):
    with open(ERREURS_LOG, "a", encoding="utf-8") as f:
        f.write(
            f"{datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')} | "
            f"Q='{question}' | Rép='{user_answers}' | Correct='{correct_answers}'\n"
        )
