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
Baseline receives all blocks in one call. Agents require quotes to match observed text;
baseline accepts schema-valid answers with mismatches. Task adapters are shared interfaces.

All blocks use `gpt-6-luna`, low reasoning, at most 4,000 output tokens per request,
a 90-second timeout, and one retry. Traces record resolved model IDs/timestamps.
Seeded job shuffling controls scheduling, not API sampling.

| Stage | Tasks per method / round | Reading-action cap | Decision cap |
|---|---:|---:|---:|
| M2 and benchmark core | 20 and 64 | 5 | 8 |
| Benchmark selection | 12 | 20 | 23 |

Baseline has one decision. Deliberative roles share the decision budget, permitting at most
four core reads; the critic sees observed sources only. Selection has up to 54 blocks.
The [real-paper selection pilot](selection-pilot.md) is separate.

The four [saved JSON examples](benchmark-plans/) have two one-repeat smoke plans and two
**three-repeat** test plans. The scheduler targets **five repetitions**, each running M2, core, then selection.
The frozen [existing-method block](../runs/m3-existing-20261118-luna6/experiment.json) uses six workers;
the [deliberative block](../runs/m3-deliberative-20261118-luna6/experiment.json) uses four.
Separate schedules prevent controlled latency comparisons. Traces retain local repeat 1;
aggregate copies use global rounds with source provenance. Five rounds across four methods
plan 1,520 benchmark attempts plus 400 M2 attempts.

## Preparation, collection, and artifacts

From the repository root with the [environment installed](../README.md):

```shell
paper-review benchmark-verify
python scripts/prepare_benchmark_plans.py --out runs/scratch/fresh-benchmark-plans
paper-review benchmark-run --plan runs/scratch/fresh-benchmark-plans/dev-core-smoke-luna6.json --out runs/benchmark-dev-core
python scripts/run_existing_benchmark.py --model gpt-6-luna --variants agent pyagent_react baseline --repeats 5 --workers 6 --out runs/benchmark-existing
python scripts/run_existing_benchmark.py --model gpt-6-luna --variants deliberative_review --repeats 5 --workers 4 --out runs/benchmark-deliberative
```

These commands make no model calls; append `--execute` to a runner to collect predictions.
Use fresh outputs. Plans bind tasks, configuration, shuffled jobs, data hashes, and implementation
bytes, including local edits; regenerate after source changes. The scheduler saves `experiment.json`,
`progress.json` with timing/ETA, aggregate `records.jsonl`, `scores.json`, and `README.md`.
Each `r<round>/<stage>/` preserves its plan/source archive, records, readable predictions,
and per-attempt `trace.jsonl`. [Source reconstruction](../data/benchmark/v1/README.md#offline-use)
uses pinned downloads and hash verification without model calls.

## Scoring and reporting

Completion means a schema-valid returned prediction. Failures and invalid predictions score
zero and remain in attempt denominators; missing cells reject scoring. Quote-matching rates
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
paper-review benchmark-score --tracks qasper reviewcritique controlled --records runs/benchmark-existing/r1/core/records.jsonl --plan runs/benchmark-existing/r1/core/plan.json
python -m pip install -r requirements-report.txt
python scripts/report_m3_results.py runs/benchmark-existing runs/benchmark-deliberative --out runs/benchmark-report
```

The report includes only complete comparable rounds and writes `README.md`,
`results.json`, `accuracy-cost.svg`, and `accuracy-cost.png`. The collected blocks'
[current report](M3-results/README.md) preserves per-track metrics and provenance.
