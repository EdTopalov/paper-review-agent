# Evidence-assessment benchmark experiment

Model: `gpt-6-luna`. Split: `dev`. 5 tasks per variant and 1 repetitions.

[Frozen plan](plan.json) · [Evaluated source](source.zip) · [Per-track quality scores](scores.json) · [Attempt records](records.jsonl)

Completion is a returned prediction, not a correctness score. Quality is reported separately for each track; evidence matching does not establish that the explanation is sound. Costs include failed attempts and retries.

| Variant | Completed / attempts | Calls / attempt | Input/output tokens / attempt | USD / attempt | Seconds / attempt |
|---|---:|---:|---:|---:|---:|
| deliberative_review | 5/5 | 7.20 | 17058.0/1629.8 | 0.002927 | 24.80 |

## Content by track

Repeat values show run variation before pooling. Failures remain in every denominator. The JSON report includes evidence F1, category slices, group intervals, and per-attempt costs.

| Track | Variant | Primary measure | Each repeat | Pooled |
|---|---|---|---|---:|
| controlled | deliberative_review | Verdict accuracy | r1: 1.000 | 1.000 |
| qasper | deliberative_review | Answer F1 | r1: 1.000 | 1.000 |
| reviewcritique | deliberative_review | Binary macro-F1 | r1: 1.000 | 1.000 |

## Attempts

- [deliberative_review-r1/CB-1459e1c65b75](deliberative_review-r1/CB-1459e1c65b75/README.md): ok
- [deliberative_review-r1/CB-d052e074ba2d](deliberative_review-r1/CB-d052e074ba2d/README.md): ok
- [deliberative_review-r1/QASPER-312e9cc11b90](deliberative_review-r1/QASPER-312e9cc11b90/README.md): ok
- [deliberative_review-r1/RC-31d344c750b5](deliberative_review-r1/RC-31d344c750b5/README.md): ok
- [deliberative_review-r1/RC-be6017406ed2](deliberative_review-r1/RC-be6017406ed2/README.md): ok
