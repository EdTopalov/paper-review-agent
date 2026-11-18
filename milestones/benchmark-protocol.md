# Evidence-assessment benchmark protocol

This compares `agent`, `pyagent_react`, `deliberative_review`, and `baseline` on frozen tasks.
The unchanged 20-paper [M2 comparison](M3-protocol.md) remains separate.
[Design and source terms](benchmark-design.md) explain reference targets and attribution.

## Dataset and reference separation

The [corpus](../data/benchmark/v1/README.md) contains 26 development and 76 test cases:

| Track | Dev / test | Test groups | Primary measures |
|---|---:|---|---|
| QASPER | 6 / 20 | 20 papers | Answer F1: normalized token overlap; evidence F1: unique source-block overlap. Both independently maximize over human references. |
| ReviewCritique | 6 / 20 | 10 papers | Binary macro-F1: mean F1 of reliable and deficient classes; per-class precision/recall. |
| Controlled appraisal | 8 / 24 | 4 families, 12 pairs | Verdict accuracy; pair accuracy requires both conditions correct. |
| Explicit-brief selection | 6 / 12 | 4 candidate sets, 3 orders each | Acceptable-choice accuracy, including abstention; all-orders-correct and same-choice consistency. |

QASPER and ReviewCritique retain existing human labels; hypothetical targets are programmatic.
Paper-title groups, scientific families, and candidate sets do not cross splits.
Development is excluded from test statistics. Test selection has 3, 6, or 9 candidates;
ties occur only in development. Source/licence metadata accompany each track.

Public `inputs/` contain tasks and text blocks, whose IDs are not PDF page numbers.
Separate `references/` hold answers, labels, explanations, and oracle facts, excluded from model requests/traces.

## Common task adapters and budgets

Methods share task instructions, structured predictions, and fresh context per attempt.
Reading agents receive the task, block catalog, and first block, then use search/read tools.
Baseline receives all blocks in one call. Ordinary agent submissions require quotes
matching observed text. At the cap, one final call requests a nullable public answer
without tools or retries. A valid non-null answer completes with citation diagnostics;
null, missing/invalid output and transport errors remain failures. Ledgers do not gate
forced public answers. Content correctness is independent of completion and quotes.

All blocks use `gpt-6-luna`, low reasoning, at most 4,000 output tokens per request,
a 90-second timeout and one transport retry, except the final call's zero retries.
Traces record resolved model IDs/timestamps.
Seeded job shuffling controls scheduling, not API sampling.

| Stage | Tasks per method / round | Reading cap | Ordinary decisions | Maximum with final call |
|---|---:|---:|---:|---:|
| M2 / benchmark core | 20 / 64 | 5 | 16 | 17 |
| Benchmark selection | 12 | 20 | 46 | 47 |

Baseline has one decision. Deliberative roles share the cap; initial exploration
remains three core or 18 selection reads, with at most one critic-requested read.
The critic sees observed sources only. Selection has up to 54 blocks.
The [real-paper selection pilot](selection-pilot.md) is separate.

The [saved plans](benchmark-plans/) contain one-repeat smoke and three-repeat test examples.
Final collection uses three repetitions and separate eight-worker blocks per agent;
baseline uses four workers. Each round runs M2, core, then selection. Three rounds
across four methods plan 912 benchmark attempts plus 240 M2 attempts. Traces retain
local repeat 1; aggregates identify global rounds and original source provenance.
Separate worker pools and start times prevent a controlled latency comparison.

## Preparation, collection, and artifacts

From the repository root with the [environment installed](../README.md):

```shell
paper-review benchmark-verify
python scripts/prepare_benchmark_plans.py --out runs/scratch/fresh-benchmark-plans
paper-review benchmark-run --plan runs/scratch/fresh-benchmark-plans/dev-core-smoke-luna6.json --out runs/benchmark-dev-core
python scripts/run_existing_benchmark.py --model gpt-6-luna --variants agent --repeats 3 --workers 8 --out runs/m3-final-agent-20261118-luna6
python scripts/run_existing_benchmark.py --model gpt-6-luna --variants pyagent_react --repeats 3 --workers 8 --out runs/m3-final-pyagent_react-20261118-luna6
python scripts/run_existing_benchmark.py --model gpt-6-luna --variants deliberative_review --repeats 3 --workers 8 --out runs/m3-final-deliberative_review-20261118-luna6
python scripts/run_existing_benchmark.py --model gpt-6-luna --variants baseline --repeats 3 --workers 4 --out runs/m3-final-baseline-20261118-luna6
```

These commands make no model calls; append `--execute` to a runner to collect predictions.
Use fresh outputs. Plans bind tasks, configuration, shuffled jobs, data hashes, and implementation
bytes, including local edits; regenerate after source changes. The scheduler saves `experiment.json`,
`progress.json` with timing/ETA, aggregate `records.jsonl`, `scores.json`, and `README.md`.
Each `r<round>/<stage>/` preserves its plan/source archive, records, readable predictions,
and per-attempt `trace.jsonl`. [Source reconstruction](../data/benchmark/v1/README.md#offline-use)
uses pinned downloads and hash verification without model calls.

## Scoring and reporting

Completion means a valid returned prediction, including non-null forced answers. Incorrect
or failed predictions score zero on exact-content measures and remain in attempt denominators;
missing cells reject scoring. Quote-matching rates
use submitted quotes. Report tracks, repeats, and groups separately, with decisions,
reading/tool/API calls, tokens, USD, and latency per attempt. Costs include retries;
unknown usage stays unknown. Compare run variation before interpreting method differences.
`pass^k` averages `C(s,k)/C(n,k)` over tasks with s exact successes in n repeats:
success on all k attempts. Exact QA success requires answer F1 = 1.

Scorer comparisons use paired 95% bootstrap intervals over paper/family/candidate-set means,
keeping repeats and correlated cases together. Plot bars instead show 95% Student-t intervals
across complete repetition means; one repetition has no bar. Its 76 equally weighted exact
outcomes are descriptive; track metrics remain separate. Rebuild offline:

```shell
paper-review benchmark-score --tracks qasper reviewcritique controlled --records runs/m3-final-agent-20261118-luna6/r1/core/records.jsonl --plan runs/m3-final-agent-20261118-luna6/r1/core/plan.json
python -m pip install -r requirements-report.txt
python scripts/report_m3_results.py runs/m3-final-agent-20261118-luna6 runs/m3-final-pyagent_react-20261118-luna6 runs/m3-final-deliberative_review-20261118-luna6 runs/m3-final-baseline-20261118-luna6 --out milestones/M3-results
python scripts/report_m3_m2_results.py
```

The report includes only complete comparable rounds and writes `README.md`,
`results.json`, `accuracy-cost.svg`, and `accuracy-cost.png`. The collected blocks'
[current report](M3-results/README.md) preserves per-track metrics and provenance.
