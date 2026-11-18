# Repeated agent comparison

Collection is closed at its configured cutoff; see the [stop record](cutoff.jsonl).
Round 3 M2 retains 19 terminal attempts and one unfinished trace. Its last
progress snapshot says `running`; this process has stopped. Only complete
rounds enter comparison metrics.

Completed rounds: 2/3. Terminal attempts: 192/288. Benchmark: 152/228; original M2: 40/60.

[Progress](progress.json) · [Aggregate attempts](records.jsonl) · [Offline scores](scores.json)

Methods: `deliberative_review`. Failed attempts remain in all-attempt content, cost, and latency denominators. Citation matching does not establish semantic support.

Each round starts with the original M2 sample when enabled, followed by a benchmark core stage (five reading actions) and a selection stage (20 reading actions). Each stage has its own immutable configuration, source archive, records, and traces under `r<round>/<stage>/`. Stages use one local repeat. Aggregate copies set `repeat` to the global round, retain `source_repeat: 1` and `source_round`, and point `trace_path` to the original trace. Original trace identities are unchanged.

Benchmark scores are refreshed only after both benchmark stages complete a full round. An unfinished next round can have additional aggregate records without entering the last complete-round scores.

| Method | Track | Attempts | Completed | Mean content score | Exact content success |
|---|---|---:|---:|---:|---:|
| deliberative_review | controlled | 48 | 48 | 0.9375 | 0.9375 |
| deliberative_review | qasper | 40 | 40 | 0.3973 | 0.2000 |
| deliberative_review | reviewcritique | 40 | 40 | 0.5500 | 0.5500 |
| deliberative_review | selection | 24 | 24 | 0.3750 | 0.3750 |

QA content score is answer F1; other content scores are reference-match indicators. Exact QA success requires answer F1 of one. Per-class metrics, evidence F1, pair accuracy, order diagnostics, repeated-run statistics, costs, and grouped paired intervals are in `scores.json`.

## Original M2 sample

These 20-paper results use the unchanged review rubric and remain separate from benchmark content scores. Citation verification is a mechanical measure, not assessment quality. Each local stage uses one repeat; round numbers below identify separate attempts. [Round summaries](m2-rounds.json).

| Round | Method | Completed / attempts | All citations verified | Mean USD / attempt |
|---|---|---:|---:|---:|
| [1](r1/m2/README.md) | deliberative_review | 20/20 | 20 | 0.007604 |
| [2](r2/m2/README.md) | deliberative_review | 20/20 | 20 | 0.006799 |
