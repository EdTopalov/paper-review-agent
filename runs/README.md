# Saved runs

- [M3 comparison and plot](../milestones/M3-results/README.md): complete comparable repetitions on the frozen assessment benchmark; [M2 appendix](../milestones/M3-results/M2.md) retains the original 20-paper comparison.
- [T17 diagnostic](m3-t17-final-r10/README.md): ten repeated attempts with the final decision policy.
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

Historical reports describe their archived implementation. Earlier-policy runs
remain saved evidence; only the final-policy roots listed in the generated report
supply current comparison metrics. Unfinished repetitions remain available in
their run directories and do not enter those metrics.
