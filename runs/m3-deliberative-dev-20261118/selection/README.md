# Evidence-assessment benchmark experiment

Model: `gpt-6-luna`. Split: `dev`. 1 tasks per variant and 1 repetitions.

[Frozen plan](plan.json) · [Evaluated source](source.zip) · [Per-track quality scores](scores.json) · [Attempt records](records.jsonl)

Completion is a returned prediction, not a correctness score. Quality is reported separately for each track; evidence matching does not establish that the explanation is sound. Costs include failed attempts and retries.

| Variant | Completed / attempts | Calls / attempt | Input/output tokens / attempt | USD / attempt | Seconds / attempt |
|---|---:|---:|---:|---:|---:|
| deliberative_review | 0/1 | 23.00 | 65312.0/3341.0 | 0.009774 | 54.49 |

## Content by track

Repeat values show run variation before pooling. Failures remain in every denominator. The JSON report includes evidence F1, category slices, group intervals, and per-attempt costs.

| Track | Variant | Primary measure | Each repeat | Pooled |
|---|---|---|---|---:|
| selection | deliberative_review | Choice accuracy | r1: 0.000 | 0.000 |

## Attempts

- [deliberative_review-r1/SB-6c9ae061e531](deliberative_review-r1/SB-6c9ae061e531/README.md): error
