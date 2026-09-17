#!/usr/bin/env python3
"""Candidate remote document-state verifier. Python standard library + Git."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import PurePosixPath
import re
import subprocess
import tempfile


def git(directory, *args):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    return subprocess.run(["git", "-C", str(directory), *args],
                          check=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, timeout=60, env=env).stdout


def validate(contract):
    if not isinstance(contract, dict) or set(contract) != {"repository", "branch", "commit", "files"}:
        raise ValueError("Required fields: repository, branch, commit, files")
    if not isinstance(contract["repository"], str) or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", contract["repository"]):
        raise ValueError("Invalid GitHub owner/repository")
    if not isinstance(contract["commit"], str) or not re.fullmatch(r"[0-9a-f]{40}", contract["commit"]):
        raise ValueError("Expected full lowercase 40-character commit SHA")
    branch = contract["branch"]
    if not isinstance(branch, str) or not branch or branch.startswith("-"):
        raise ValueError("Invalid branch")
    git(".", "check-ref-format", "refs/heads/" + branch)
    files = contract["files"]
    if not isinstance(files, dict) or not files:
        raise ValueError("At least one expected file is required")
    for path, digest in files.items():
        if (not isinstance(path, str) or not path or
                str(PurePosixPath(path)) != path or path.startswith("/") or
                ".." in PurePosixPath(path).parts or "\\" in path or
                any(ord(c) < 32 for c in path)):
            raise ValueError("Expected canonical relative file path")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ValueError("Expected lowercase SHA-256 digest")


def inspect(directory, contract):
    """Inspect freshly fetched objects; never trust working-tree files."""
    observed = git(directory, "rev-parse", "FETCH_HEAD^{commit}").decode().strip()
    result = {"expected_commit": contract["commit"], "observed_commit": observed,
              "files": [], "status": "FAIL"}
    if observed != contract["commit"]:
        result["reason"] = "VERSION_MISMATCH"
        return result
    entries = git(directory, "ls-tree", "-r", "-z", observed).split(b"\0")
    tree = {}
    for entry in entries:
        if entry:
            metadata, path = entry.split(b"\t", 1)
            tree[path] = metadata.split()
    for path, expected in contract["files"].items():
        item = {"path": path, "expected_sha256": expected}
        metadata = tree.get(path.encode("utf-8"))
        if metadata is None:
            item["status"] = "MISSING"
        elif metadata[0] not in (b"100644", b"100755"):
            item["status"] = "NOT_REGULAR_FILE"
        else:
            content = git(directory, "cat-file", "blob", metadata[2].decode())
            digest = hashlib.sha256(content).hexdigest()
            item.update(observed_sha256=digest,
                        status="PASS" if digest == expected else "CONTENT_MISMATCH")
        result["files"].append(item)
    result["status"] = "PASS" if all(f["status"] == "PASS" for f in result["files"]) else "FAIL"
    return result


def verify(contract):
    validate(contract)
    with tempfile.TemporaryDirectory(prefix="document-check-") as directory:
        git(directory, "init", "--bare", "--quiet")
        git(directory, "fetch", "--quiet", "--depth=1", "--no-tags",
            "https://github.com/" + contract["repository"] + ".git",
            "refs/heads/" + contract["branch"])
        return inspect(directory, contract)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", help="JSON expectations fixed before verification")
    parser.add_argument("--completion", action="store_true",
                        help="Include a scoped completion receipt only after fresh verification")
    args = parser.parse_args()
    try:
        with open(args.contract, encoding="utf-8") as source:
            contract = json.load(source)
        result = verify(contract)
        result.update(repository=contract["repository"], branch=contract["branch"])
    except (ValueError, OSError, subprocess.SubprocessError) as error:
        # Do not expose credential-bearing Git stderr or environment values.
        result = {"status": "UNVERIFIED", "reason": type(error).__name__}
    result["checked_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result["scope"] = "remote branch snapshot and expected file bytes only"
    if args.completion:
        result["completion"] = None
        if result["status"] == "PASS":
            result["completion"] = {
                "claim": "Specified remote file bytes verified at the recorded branch snapshot",
                "repository": result["repository"],
                "branch": result["branch"],
                "commit": result["observed_commit"],
                "paths": [item["path"] for item in result["files"]],
                "checked_at": result["checked_at"],
            }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return {"PASS": 0, "FAIL": 1, "UNVERIFIED": 2}[result["status"]]


if __name__ == "__main__":
    raise SystemExit(main())
