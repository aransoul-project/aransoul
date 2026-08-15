# Technical Invalid Execution Run

Run ID: `live-20260815T184124.014730Z`

Replication: `replication-1`

Classification: **Technical Invalid — transient provider HTTP 500 on request 2 / Plain / ZM-P02**

Raw-data integrity review established:

- all 40 planned request attempts are permanently preserved;
- request 2 is condition `plain`, case `ZM-P02`, with `attempt: 1`;
- the provider returned HTTP 500 with error type/code `server_error`;
- request 2 has no model completion, returned model identifier, raw output text,
  or parsed response;
- the failure is therefore a technical provider execution failure, not a model
  substantive answer or parse/validation failure;
- the other 39 responses must not be used for partial scoring;
- `ZM-P02` must not be rerun individually.

The original `manifest.json` and `responses.jsonl` are retained unchanged as
the complete raw execution record. This run must not be scored or passed to the
Authority secondary diagnostic. No replacement replication was started as part
of this audit.
