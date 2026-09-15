# Task-to-path coverage gate


Before deriving file hashes, preserve the user's task text or a source reference
and create a requirement ledger. Do not derive the ledger only from the files
that the implementation happened to change.

| Requirement ID | User requirement / source | Required destination paths | Verification method | Unresolved items |
| --- | --- | --- | --- | --- |
| R1 | Exact requested deliverable | Canonical repository-relative path(s) | Regular-file byte check | None, or explicit gap |

Every task requirement needs a row. Every file-backed row needs at least one
explicit path. List deletions, source removal during rename, content quality and
other side effects separately with their own evidence method; the current checker
does not prove these. Out-of-scope does not mean completed.

Let R be the union of all regular-file paths in the reviewed ledger and C the
contract's file keys. Before running the checker, require R = C:
- R minus C: required files omitted from verification; block a whole-task claim.
- C minus R: untraced contract files; explain and reconcile the ledger.
- Empty mappings or unresolved requirements: coverage remains unverified.

A valid byte-check PASS cannot override a failed coverage gate. Conversely,
coverage agreement does not establish correct content. Preserve ledger revisions;
do not remove a missing requirement simply to make equality hold.
This comparison is currently procedural, not implemented inside check.py.
Requirement extraction itself still requires review against the original request.

### Fixed omission example (illustration, not an agent result)

Request: publish a guide and update its index.
Ledger: R1 -> docs/guide.md; R2 -> docs/README.md.
Contract containing only docs/guide.md has a missing docs/README.md requirement,
even if the guide returns PASS. The permitted report is partial completion.
A contract containing both paths passes coverage only; remote verification is
still required. Two requirements may legitimately map to the same file.

