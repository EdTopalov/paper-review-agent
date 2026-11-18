# Repeated agent comparison

Completed rounds: 3/3. Terminal attempts: 288/288. Benchmark: 228/228; original M2: 60/60.

[Progress](progress.json) · [Aggregate attempts](records.jsonl) · [Offline scores](scores.json)

Methods: `agent`. Failed attempts remain in all-attempt content, cost, and latency denominators. Citation matching does not establish semantic support.

Each round starts with the original M2 sample when enabled, followed by a benchmark core stage (five reading actions) and a selection stage (20 reading actions). Each stage has its own immutable configuration, source archive, records, and traces under `r<round>/<stage>/`. Stages use one local repeat. Aggregate copies set `repeat` to the global round, retain `source_repeat: 1` and `source_round`, and point `trace_path` to the original trace. Original trace identities are unchanged.

Benchmark scores are refreshed only after both benchmark stages complete a full round. An unfinished next round can have additional aggregate records without entering the last complete-round scores.

| Method | Track | Attempts | Completed | Mean content score | Exact content success |
|---|---|---:|---:|---:|---:|
| agent | controlled | 72 | 70 | 0.9444 | 0.9444 |
| agent | qasper | 60 | 57 | 0.3869 | 0.2000 |
| agent | reviewcritique | 60 | 45 | 0.5333 | 0.5333 |
| agent | selection | 36 | 31 | 0.8333 | 0.8333 |

QA content score is answer F1; other content scores are reference-match indicators. Exact QA success requires answer F1 of one. Per-class metrics, evidence F1, pair accuracy, order diagnostics, repeated-run statistics, costs, and grouped paired intervals are in `scores.json`.

## Original M2 sample

These 20-paper results use the unchanged review rubric and remain separate from benchmark content scores. Citation verification is a mechanical measure, not assessment quality. Each local stage uses one repeat; round numbers below identify separate attempts. [Round summaries](m2-rounds.json).

| Round | Method | Completed / attempts | All citations verified | Mean USD / attempt |
|---|---|---:|---:|---:|
| [1](r1/m2/README.md) | agent | 18/20 | 18 | 0.002174 |
| [2](r2/m2/README.md) | agent | 20/20 | 20 | 0.002278 |
| [3](r3/m2/README.md) | agent | 19/20 | 19 | 0.002007 |
