#!/usr/bin/env python3
"""Cross-platform verifier for frozen Zombie Memory prompt hashes.

By default hashes repository bytes from an exact Git ref, avoiding working-tree
EOL conversion (for example Windows core.autocrlf). This is a handoff utility;
it does not execute a model or inspect gold answers.
"""

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

PROMPT_DIR = "experiments/holdout/zombie-memory-holdout-v0.1/generated"
MANIFEST_PATH = f"{PROMPT_DIR}/prompt-hashes.json"
CONDITIONS = ("plain", "timestamp", "status", "ttea")


def git_bytes(ref: str, path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        check=True,
        capture_output=True,
    )
    return result.stdout


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", default="HEAD", help="exact commit/tag/ref whose repository bytes should be verified")
    args = parser.parse_args()

    manifest = json.loads(git_bytes(args.ref, MANIFEST_PATH).decode("utf-8"))
    expected = manifest["sha256"]
    failures = []
    checked = {}

    for condition in CONDITIONS:
        path = f"{PROMPT_DIR}/{condition}.json"
        actual = sha256(git_bytes(args.ref, path))
        checked[condition] = actual
        if actual != expected[condition]:
            failures.append({"condition": condition, "expected": expected[condition], "actual": actual})

    result = {
        "status": "pass" if not failures else "fail",
        "ref": args.ref,
        "hash_basis": "git repository bytes via git show (not working-tree bytes)",
        "checked": checked,
        "failures": failures,
    }
    print(json.dumps(result, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
