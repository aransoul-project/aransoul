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

