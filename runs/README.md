# Saved runs

- [M3 development smoke](m3-smoke-20261118/README.md): four methods on T17 and a separate synthetic selection pilot; execution checks, not a benchmark.
- [Historical M2 comparison](m2-integrated-20261026/README.md): one run of the native agent and baseline.
- [PyAgent v1](m3-comparison-pyagent-20/README.md), [parser v2](m3-comparison-pyagent-parser-v2-20/README.md): single-run, 20-paper comparisons with two reads and 1,500 output tokens.
- [Earlier evidence](archive/README.md): selected failures and the original raw archive.

Each task has `README.md` for reading and `trace.jsonl` for replay. Model inputs
and request settings are stored as changes; `paper_review.trace.read_events(path)`
restores every complete request. Results and optional audits are terminal events in that same
trace. Each experiment has one settings file and one evaluated-source archive.

Python generates the Markdown pages from saved traces. Scores, review text,
action explanations, and audit judgments come from the model; Python formats
the pages and calculates aggregate metrics. `paper-review summarize <directory>`
rebuilds the pages offline, without model calls or API charges.

Task pages show the review once and a short entry for each decision: purpose,
key arguments, and outcome. Full arguments and observations remain in the
structured trace; unused API response metadata is omitted.

Historical reports describe their archived implementation. The M3 smoke records
the new source revision and preserves its failures. The full repeated comparison
and human assessment in the [M3 protocol](../milestones/M3-protocol.md) remain pending.
