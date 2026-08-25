#!/usr/bin/env python3
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_FILENAMES = [
    re.compile(r"answer[-_ ]?key", re.I),
    re.compile(r"blind[-_ ]?(id[-_ ]?)?map", re.I),
    re.compile(r"reviewer[-_ ]?(only|packet|response|submission)", re.I),
    re.compile(r"adjudicator[-_ ]?(submission|packet|response)", re.I),
    re.compile(r"sealed", re.I),
]
FORBIDDEN_JSON_KEYS = {
    "expected_label","gold_label","answer_key","private_map","blind_id",
    "required_behavior_atoms","forbidden_behavior_atoms","best_action_mode",
    "best_observable_behavior","observable_pass","observable_fail",
    "candidate_expected_outcome","first_adjudicator_label","second_adjudicator_label",
    "selected_label","review_metadata","adjudication"
}
SUSPICIOUS_BLIND_ID = re.compile(r'"blind_id"\s*:\s*"[A-Z]+[0-9]{2,}"', re.I)

def walk_json(x, path="$"):
    if isinstance(x, dict):
        for k,v in x.items():
            if k in FORBIDDEN_JSON_KEYS:
                raise AssertionError(f"forbidden JSON key {k!r} at {path}")
            walk_json(v, f"{path}.{k}")
    elif isinstance(x, list):
        for i,v in enumerate(x):
            walk_json(v, f"{path}[{i}]")

files = [p for p in ROOT.rglob("*") if p.is_file()]
for p in files:
    rel = p.relative_to(ROOT).as_posix()
    for rx in FORBIDDEN_FILENAMES:
        if rx.search(rel):
            raise AssertionError(f"forbidden filename: {rel}")
    text = p.read_text(encoding="utf-8")
    if p.name != "validate_snapshot.py" and SUSPICIOUS_BLIND_ID.search(text):
        raise AssertionError(f"suspicious blind-id payload in {rel}")
    if p.suffix == ".json":
        walk_json(json.loads(text))

inv = json.loads((ROOT/"candidate-inventory.v0.2.model-facing.json").read_text(encoding="utf-8"))
assert len(inv["cases"]) == 16
assert sum(c["track"]=="strict_primary" for c in inv["cases"]) == 14
assert sum(c["track"]=="controlled_scope_diagnostic" for c in inv["cases"]) == 2
assert len({c["public_id"] for c in inv["cases"]}) == 16
assert inv["gold_included"] is False
assert inv["blind_mapping_included"] is False
assert inv["reviewer_material_included"] is False

agg = json.loads((ROOT/"aggregation-policy.v0.1.json").read_text(encoding="utf-8"))
assert agg["case_counts"] == {"strict_primary":14,"controlled_scope_diagnostics":2}
assert agg["primary_macro_groups"] == 6
assert agg["strict_contrast_pairs"] == 7

print(f"PASS: scanned {len(files)} files")
print("PASS: leakage filename/content/key scan")
print("PASS: inventory 16 = 14 primary + 2 diagnostic")
print("PASS: unique public IDs")
print("PASS: aggregation counts 6 macro groups / 7 contrast pairs")
