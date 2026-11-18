# Evidence-assessment benchmark experiment

Model: `gpt-6-luna`. Split: `test`. 12 tasks per variant and 1 repetitions.

[Frozen plan](plan.json) · [Evaluated source](source.zip) · [Per-track quality scores](scores.json) · [Attempt records](records.jsonl)

Completion is a returned prediction, not a correctness score. Quality is reported separately for each track; evidence matching does not establish that the explanation is sound. Costs include failed attempts and retries.

| Variant | Completed / attempts | Calls / attempt | Input/output tokens / attempt | USD / attempt | Seconds / attempt |
|---|---:|---:|---:|---:|---:|
| deliberative_review | 12/12 | 22.92 | 90830.2/3634.3 | 0.012859 | 51.73 |

## Content by track

Repeat values show run variation before pooling. Failures remain in every denominator. The JSON report includes evidence F1, category slices, group intervals, and per-attempt costs.

| Track | Variant | Primary measure | Each repeat | Pooled |
|---|---|---|---|---:|
| selection | deliberative_review | Choice accuracy | r1: 0.417 | 0.417 |

## Attempts

- [deliberative_review-r1/SB-18f34443b4ea](deliberative_review-r1/SB-18f34443b4ea/README.md): ok
- [deliberative_review-r1/SB-3f2caf640d8b](deliberative_review-r1/SB-3f2caf640d8b/README.md): ok
- [deliberative_review-r1/SB-4dd14ec2ecf0](deliberative_review-r1/SB-4dd14ec2ecf0/README.md): ok
- [deliberative_review-r1/SB-66e931b708c9](deliberative_review-r1/SB-66e931b708c9/README.md): ok
- [deliberative_review-r1/SB-7402e4ad7d74](deliberative_review-r1/SB-7402e4ad7d74/README.md): ok
- [deliberative_review-r1/SB-80e0d3dc1ce0](deliberative_review-r1/SB-80e0d3dc1ce0/README.md): ok
- [deliberative_review-r1/SB-86910a1a2a2b](deliberative_review-r1/SB-86910a1a2a2b/README.md): ok
- [deliberative_review-r1/SB-a60c27fb6809](deliberative_review-r1/SB-a60c27fb6809/README.md): ok
- [deliberative_review-r1/SB-e9e07484ab89](deliberative_review-r1/SB-e9e07484ab89/README.md): ok
- [deliberative_review-r1/SB-f094fd9a487e](deliberative_review-r1/SB-f094fd9a487e/README.md): ok
- [deliberative_review-r1/SB-f8e22c0984b8](deliberative_review-r1/SB-f8e22c0984b8/README.md): ok
- [deliberative_review-r1/SB-fbf196ced965](deliberative_review-r1/SB-fbf196ced965/README.md): ok
