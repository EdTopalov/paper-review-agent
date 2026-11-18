# Repeated evidence-assessment benchmark

Completed rounds: 3/5. Terminal attempts: 924/1440. Benchmark: 684/1140; original M2: 240/300.

[Progress](progress.json) · [Aggregate attempts](records.jsonl) · [Offline scores](scores.json)

Methods: native ReAct (`agent`), PyAgent (`pyagent_react`), and the full-text `baseline`. Failed attempts remain in all-attempt content, cost, and latency denominators. Citation matching does not establish semantic support.

Each round starts with the original M2 sample when enabled, followed by a benchmark core stage (five reading actions) and a selection stage (20 reading actions). Each stage has its own immutable configuration, source archive, records, and traces under `r<round>/<stage>/`. Stages use one local repeat. Aggregate copies set `repeat` to the global round, retain `source_repeat: 1` and `source_round`, and point `trace_path` to the original trace. Original trace identities are unchanged.

Benchmark scores are refreshed only after both benchmark stages complete a full round. An unfinished next round can have additional aggregate records without entering the last complete-round scores.

| Method | Track | Attempts | Completed | Mean content score | Exact content success |
|---|---|---:|---:|---:|---:|
| agent | controlled | 72 | 72 | 1.0000 | 1.0000 |
| agent | qasper | 60 | 57 | 0.4040 | 0.2167 |
| agent | reviewcritique | 60 | 51 | 0.5333 | 0.5333 |
| agent | selection | 36 | 35 | 0.8333 | 0.8333 |
| pyagent_react | controlled | 72 | 69 | 0.9167 | 0.9167 |
| pyagent_react | qasper | 60 | 53 | 0.2904 | 0.1167 |
| pyagent_react | reviewcritique | 60 | 58 | 0.6333 | 0.6333 |
| pyagent_react | selection | 36 | 36 | 0.8889 | 0.8889 |
| baseline | controlled | 72 | 72 | 0.9722 | 0.9722 |
| baseline | qasper | 60 | 60 | 0.4321 | 0.2000 |
| baseline | reviewcritique | 60 | 60 | 0.6000 | 0.6000 |
| baseline | selection | 36 | 35 | 0.9722 | 0.9722 |

QA content score is answer F1; other content scores are reference-match indicators. Exact QA success requires answer F1 of one. Per-class metrics, evidence F1, pair accuracy, order diagnostics, repeated-run statistics, costs, and grouped paired intervals are in `scores.json`.

## Original M2 sample

These 20-paper results use the unchanged review rubric and remain separate from benchmark content scores. Citation verification is a mechanical measure, not assessment quality. Each local stage uses one repeat; round numbers below identify separate attempts. [Round summaries](m2-rounds.json).

| Round | Method | Completed / attempts | All citations verified | Mean USD / attempt |
|---|---|---:|---:|---:|
| [1](r1/m2/README.md) | agent | 19/20 | 19 | 0.002176 |
| [1](r1/m2/README.md) | pyagent_react | 18/20 | 18 | 0.002218 |
| [1](r1/m2/README.md) | baseline | 20/20 | 12 | 0.003386 |
| [2](r2/m2/README.md) | agent | 20/20 | 20 | 0.002120 |
| [2](r2/m2/README.md) | pyagent_react | 20/20 | 20 | 0.002278 |
| [2](r2/m2/README.md) | baseline | 20/20 | 10 | 0.000554 |
| [3](r3/m2/README.md) | agent | 19/20 | 19 | 0.001862 |
| [3](r3/m2/README.md) | pyagent_react | 20/20 | 20 | 0.002182 |
| [3](r3/m2/README.md) | baseline | 20/20 | 13 | 0.000545 |
| [4](r4/m2/README.md) | agent | 18/20 | 18 | 0.002174 |
| [4](r4/m2/README.md) | pyagent_react | 19/20 | 19 | 0.002279 |
| [4](r4/m2/README.md) | baseline | 20/20 | 9 | 0.000564 |
