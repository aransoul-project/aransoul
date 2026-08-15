# Invalid execution run

Run ID: `live-20260814T203307.026357Z`

Classification: **Invalid execution run**

All 40 request attempts returned HTTP 400 before model inference because the
provider rejected `uniqueItems` in the Structured Outputs response schema.
The original `manifest.json` and `responses.jsonl` are retained unchanged as
the complete execution record. This run must not be scored, deleted,
overwritten, or interpreted as an empirical condition result.
