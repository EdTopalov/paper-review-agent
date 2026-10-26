# Saved runs

- [Final comparison](m2-integrated-20261026/README.md): start here for results and task links.
- [Earlier evidence](archive/README.md): selected failures and the original raw archive.

Each task has `README.md` for reading and `trace.jsonl` for replay. Model inputs
are stored incrementally; `paper_review.trace.read_events(path)` restores every
complete request. Results and optional audits are terminal events in that same
trace. Each experiment has one settings file and one evaluated-source archive.

Python generates the Markdown pages from saved traces. Scores, review text,
action explanations, and audit judgments come from the model; Python formats
the pages and calculates aggregate metrics. `paper-review summarize <directory>`
rebuilds the pages offline, without model calls or API charges.

Reports were reformatted offline. No new experiment has been run with the current
source; saved results still describe the archived implementation. Run a new
comparison into a fresh directory to measure the current code.
