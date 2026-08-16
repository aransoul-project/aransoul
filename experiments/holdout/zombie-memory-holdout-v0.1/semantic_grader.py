#!/usr/bin/env python3
"""Deterministic semantic answer grader v0.1.

This module grades only a question, canonical answer, and candidate answer. It
does not read experiment responses, conditions, authority IDs, or score files.
"""

import argparse
import json
import re
from pathlib import Path


ALLOWED_LABELS = {"equivalent", "not_equivalent", "indeterminate"}
NUMBER_WORDS = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13",
    "fourteen": "14", "fifteen": "15", "sixteen": "16",
    "seventeen": "17", "eighteen": "18", "nineteen": "19",
    "twenty": "20",
}
STOP_WORDS = {
    "a", "an", "and", "approval", "approvals", "approve", "approved",
    "approves", "before", "first", "formerly", "is", "it", "later", "of",
    "second", "sign", "signs", "off", "the", "then", "to", "used", "was",
}
VAGUE_MARKERS = (
    "cannot determine", "can't determine", "not enough information",
    "insufficient information", "records conflict", "unclear", "unknown",
)


def normalize(text):
    value = text.casefold().replace("–", "-").replace("—", "-")
    value = re.sub(r"\b(\d+)\s*h\b", r"\1 hours", value)
    for word, number in NUMBER_WORDS.items():
        value = re.sub(rf"\b{word}\b", number, value)
    value = re.sub(r"\bhour\b", "hours", value)
    value = re.sub(r"\bday\b", "days", value)
    value = re.sub(r"\bstudent\b", "students", value)
    value = re.sub(r"\bincident\b", "incidents", value)
    value = re.sub(r"\bconnection\b", "connections", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def tokens(text):
    return normalize(text).split()


def numbers(text):
    return re.findall(r"\b\d+(?:\.\d+)?\b", normalize(text))


def content_tokens(text):
    return [token for token in tokens(text) if token not in STOP_WORDS]


def has_conflicting_alternatives(candidate):
    normalized = normalize(candidate)
    return bool(
        re.search(r"\beither\b.+\bor\b", normalized)
        or re.search(r"\b(?:or|versus|vs)\b", normalized)
        and len(set(numbers(candidate))) > 1
    )


def ordered_segments(gold):
    parts = re.split(r"\bthen\b|,", normalize(gold))
    segments = []
    for part in parts:
        meaningful = [token for token in part.split() if token not in STOP_WORDS]
        if meaningful:
            segments.append(meaningful)
    return segments if len(segments) > 1 else []


def segment_position(candidate_tokens, segment):
    positions = [candidate_tokens.index(token) for token in segment if token in candidate_tokens]
    return min(positions) if positions and len(positions) == len(segment) else None


def grade(question, gold, candidate):
    """Return exactly one semantic-equivalence label."""
    if not all(isinstance(value, str) for value in (question, gold, candidate)):
        return "indeterminate"
    if not candidate.strip():
        return "indeterminate"

    candidate_normalized = normalize(candidate)
    if has_conflicting_alternatives(candidate):
        return "indeterminate"
    if any(marker in candidate.casefold() for marker in VAGUE_MARKERS):
        return "indeterminate"

    gold_numbers = numbers(gold)
    candidate_numbers = numbers(candidate)
    if gold_numbers:
        if not all(number in candidate_numbers for number in gold_numbers):
            return "not_equivalent"
        gold_units = {token for token in content_tokens(gold) if not token.isdigit()}
        candidate_units = set(content_tokens(candidate))
        if gold_units and not gold_units.issubset(candidate_units):
            return "not_equivalent"
        return "equivalent"

    segments = ordered_segments(gold)
    if segments:
        candidate_token_list = tokens(candidate)
        positions = [segment_position(candidate_token_list, segment) for segment in segments]
        if any(position is None for position in positions):
            return "not_equivalent"
        return "equivalent" if positions == sorted(positions) else "not_equivalent"

    gold_content = set(content_tokens(gold))
    candidate_content = set(content_tokens(candidate))
    if gold_content.issubset(candidate_content):
        return "equivalent"

    # A generic location descriptor such as "entrance" may add specificity,
    # but every operative gold token must still remain present.
    return "not_equivalent"


def run_self_test(dataset_path):
    cases = json.loads(dataset_path.read_text(encoding="utf-8"))
    failures = []
    for case in cases:
        actual = grade(case["question"], case["gold"], case["candidate"])
        if actual not in ALLOWED_LABELS or actual != case["expected"]:
            failures.append({"id": case["id"], "expected": case["expected"], "actual": actual})
    return {
        "status": "synthetic_self_test_pass" if not failures else "synthetic_self_test_fail",
        "cases": len(cases),
        "passed": len(cases) - len(failures),
        "failed": len(failures),
        "failures": failures,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--question")
    parser.add_argument("--gold")
    parser.add_argument("--candidate")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument(
        "--dataset",
        type=Path,
        default=Path(__file__).with_name("semantic-scoring-synthetic-v0.1.json"),
    )
    args = parser.parse_args()

    if args.self_test:
        print(json.dumps(run_self_test(args.dataset), indent=2))
        return
    if None in (args.question, args.gold, args.candidate):
        parser.error("--question, --gold, and --candidate are required")
    print(grade(args.question, args.gold, args.candidate))


if __name__ == "__main__":
    main()
