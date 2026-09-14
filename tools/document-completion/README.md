# GitHub document completion check

Status: **Candidate executable prototype**. Requires Python 3.9+ and Git.

Checks one narrow claim: at retrieval time, the named GitHub branch resolved to
an expected commit, and all specified regular files contained the expected bytes.
It fetches into a new temporary bare repository and reads Git blobs, not local drafts.

## Contract and command

Prepare expectations before running the check. Use the intended document bytes to
calculate SHA-256; do not derive expectations from the remote result being tested.
The commit must be the full remote branch commit (after squash merge this differs
from the PR head). Each file path is relative to the repository root.

```json
{
  "repository": "owner/repository",
  "branch": "main",
  "commit": "FULL_40_CHARACTER_LOWERCASE_COMMIT_SHA",
  "files": {"docs/example.md": "EXPECTED_64_CHARACTER_SHA256"}
}
```

```sh
python3 tools/document-completion/check.py contract.json > result.json
python3 -m unittest discover -s tools/document-completion -p 'test_*.py' -v
```

Exit 0 / PASS: branch commit and every requested file match.
Exit 1 / FAIL: observed version, file presence/type, or contents disagree.
Exit 2 / UNVERIFIED: invalid input, unavailable access, timeout, or other read error.
A missing remote branch is UNVERIFIED because fetch failure alone cannot reliably
distinguish access failure from absence. A moved branch fails the strict version
contract even if document contents still match; review and explicitly amend the
contract rather than automatically accepting a newer commit.

The report records expected/observed commit, file SHA-256 comparisons, and UTC check
time. Comparison is byte-exact, including line endings. Symlinks and submodules do
not qualify as regular documents. Other repository files are outside the contract.
Private repositories require existing Git credentials; the tool does not request
or record tokens. Git configuration and the local execution environment are trusted.

## Evidence boundary

This implements a narrow operational application of [EREQ](../../docs/experiments/ereq/README.md)
and external-action verification. It is not the EREQ semantic scorer and does not
change EREQ Candidate or AGBench paused status.

PASS does not establish authorship, authorization, content quality, correctness of
the user's requirements, who previously read a file, or continued branch state
after retrieval. The checker performs a new readback; it cannot prove the assistant
performed an earlier one. It does not parse or prevent natural-language completion
claims. To use it as a gate, the calling workflow must require exit 0 before making
the specific verified claim. Reports are unsigned and can be edited; they are not
independent attestations. Self-generated expectations can encode the same mistake
as the implementation, so review the contract against the user's intended task.

Development tests cover success, draft-only files, wrong commit, wrong bytes,
missing required files, symlinks, local modifications, invalid contracts, and
unavailable verification. These are software checks, not model-performance results.

## Initial verification (2026-09-14)

Nine development tests passed. A live GitHub read at
2026-09-14T08:39:56.125124+00:00 returned PASS for `aransoul-project/aransoul`,
branch `main`, expected and observed commit
`b2db7194e52345658f909e7f53193cf4a52a5b17`.

| File | Expected and observed SHA-256 |
| --- | --- |
| `research/README.md` | `f9c0498cb77d00ca06bf1955e382e59a600c5a5049a9acc415e985cd5089406e` |
| `research/context-governance/README.md` | `49e918871098ecb91c472e02408bfedc4c9b7ac4ee27afa58bfac7e830b55c68` |

Expectations were computed from the previously fetched, reviewed merge commit
before the checker made its fresh fetch. This exercises the live transport and
byte comparison; it is not an independent content-quality review.

## Completion receipt entry point (pending execution verification)

```sh
python3 tools/document-completion/check.py contract.json --completion > result.json
```

This entry point always runs a fresh verification. It adds a structured
`completion` receipt only on PASS; FAIL and UNVERIFIED produce `completion: null`
and retain nonzero exit codes. The receipt binds the limited claim to repository,
branch, observed commit, specified paths, and check time. It accepts no prior
report as evidence. Callers must check the current exit code and current output;
never reuse a report left over from an earlier invocation.

This gates the CLI's receipt generation only. It is not installed as a mandatory
ChatGPT response gate and cannot stop an assistant from making an unrelated claim.
No automatic repository workflow or branch protection has been enabled.

Three added tests cover receipt status/exit behavior, timeout suppression, and
success followed by unavailable verification without reusing a receipt. They mock
the verifier to isolate output control; the existing tests exercise Git objects.
The execution environment was unavailable for this amendment, so these tests and
the modified CLI have **not been run**. The nine-test result above applies only to
the earlier implementation at commit `4d9654e8a19ad2707b8d4b8c4be26a01f622cf65`.
Keep this PR in draft until the updated suite and a live invocation are verified.
