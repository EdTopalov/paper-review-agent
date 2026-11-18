# Repeated agent comparison

Completed rounds: 1/1. Terminal attempts: 304/304. Benchmark: 304/304; original M2: 0/0.

[Progress](progress.json) · [Aggregate attempts](records.jsonl) · [Offline scores](scores.json)

Methods: `agent`, `pyagent_react`, `deliberative_review`, `baseline`. Failed attempts remain in all-attempt content, cost, and latency denominators. Citation matching does not establish semantic support.

Each round starts with the original M2 sample when enabled, followed by a benchmark core stage (five reading actions) and a selection stage (20 reading actions). Each stage has its own immutable configuration, source archive, records, and traces under `r<round>/<stage>/`. Stages use one local repeat. Aggregate copies set `repeat` to the global round, retain `source_repeat: 1` and `source_round`, and point `trace_path` to the original trace. Original trace identities are unchanged.

Benchmark scores are refreshed only after both benchmark stages complete a full round. An unfinished next round can have additional aggregate records without entering the last complete-round scores.

| Method | Track | Attempts | Completed | Mean content score | Exact content success |
|---|---|---:|---:|---:|---:|
| agent | controlled | 24 | 23 | 0.9583 | 0.9583 |
| agent | qasper | 20 | 18 | 0.3987 | 0.2000 |
| agent | reviewcritique | 20 | 11 | 0.3500 | 0.3500 |
| agent | selection | 12 | 12 | 0.6667 | 0.6667 |
| pyagent_react | controlled | 24 | 24 | 0.9167 | 0.9167 |
| pyagent_react | qasper | 20 | 20 | 0.3462 | 0.1500 |
| pyagent_react | reviewcritique | 20 | 20 | 0.7500 | 0.7500 |
| pyagent_react | selection | 12 | 12 | 0.9167 | 0.9167 |
| deliberative_review | controlled | 24 | 24 | 0.7500 | 0.7500 |
| deliberative_review | qasper | 20 | 20 | 0.3897 | 0.2000 |
| deliberative_review | reviewcritique | 20 | 20 | 0.6000 | 0.6000 |
| deliberative_review | selection | 12 | 12 | 0.5000 | 0.5000 |
| baseline | controlled | 24 | 24 | 1.0000 | 1.0000 |
| baseline | qasper | 20 | 20 | 0.4215 | 0.2000 |
| baseline | reviewcritique | 20 | 20 | 0.7500 | 0.7500 |
| baseline | selection | 12 | 12 | 1.0000 | 1.0000 |

QA content score is answer F1; other content scores are reference-match indicators. Exact QA success requires answer F1 of one. Per-class metrics, evidence F1, pair accuracy, order diagnostics, repeated-run statistics, costs, and grouped paired intervals are in `scores.json`.
