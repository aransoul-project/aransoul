#!/usr/bin/env python3
import json, sys
from pathlib import Path

CONDITIONS = ("plain", "timestamp", "status", "ttea")


def load_cases(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def render_record(record, condition):
    lines = [f"[{record['id']}] {record['text']}"]
    if condition in ("timestamp", "status", "ttea"):
        lines.append(f"Time: {record['time']}")
    if condition == "status":
        lines.append(f"Status: {record['effect'].upper()}")
    if condition == "ttea":
        lines.extend([
            f"Truth: {record['truth']}",
            f"Effect: {record['effect']}",
            f"Authority: {record['authority']}",
        ])
    return "\n".join(lines)


def render_case(case, condition):
    records = "\n\n".join(render_record(r, condition) for r in case["records"])
    return {
        "id": case["id"],
        "condition": condition,
        "prompt": (
            "Read the records and answer both questions. Also identify the record IDs that currently control the answer.\n\n"
            + records
            + "\n\nCurrent question: " + case["current_question"]
            + "\nHistorical question: " + case["historical_question"]
            + "\nReturn JSON with id, current_answer, historical_answer, current_authority_record_ids."
        ),
    }


def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python renderer.py cases.json output_dir")
    cases = load_cases(sys.argv[1])
    out = Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    for condition in CONDITIONS:
        rendered = [render_case(c, condition) for c in cases]
        (out / f"{condition}.json").write_text(json.dumps(rendered, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
