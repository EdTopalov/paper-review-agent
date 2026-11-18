# Development smoke test, 18 November 2026

Purpose: verify the four-method runner, evidence-memory context, error retention,
usage accounting, and separate paper-selection workflow. This is not a comparative
benchmark. There is one T17 attempt per method and two synthetic candidate reviews.
All calls use `gpt-6-luna`; no secondary-model or repeated benchmark was run.
Implementation and hypotheses were committed first at `09bf303`.

## T17 execution

[Generated report and per-task traces](t17/README.md) ·
[Configuration](t17/experiment.json) · [Evaluated source](t17/source.zip)

| Method | Outcome | Reads | Decisions/API calls | Rejected submissions | Estimated USD |
|---|---|---:|---:|---:|---:|
| `agent` | Decision budget exhausted | 3 | 8 | 5 | 0.002833130 |
| `pyagent_react` | Accepted review | 3 | 6 | 2 | 0.003003910 |
| `evidence_memory` | Decision budget exhausted | 5 | 8 | 3 | 0.009458300 |
| `baseline` | Returned review | 0 | 1 | 0 | 0.002568425 |

All four traces pass sequence, argument, budget, identity, and call-accounting
checks. A correctly recorded task failure is still a failed review; the trace
checks do not turn it into benchmark success.

The native and evidence-memory attempts exhibit citation-repair budget exhaustion.
For evidence memory, the first rejected quotation flattens a source line break
in `er-\nrors`. Later submissions introduce further quotation changes, including
an absent table label. The final request still contains the exact observed
page fragments and the latest repair diagnostics. This supports a repair-instability
diagnosis for this trajectory; it does not establish a failure rate or that memory
caused it. The original [F05](../../data/failures/F05.json) and planned T17 repetitions
remain relevant. No mechanism was tuned after this result.

## Separate selection pilot

[Choice, rationale, and candidate traces](selection/README.md) ·
[Structured decision and totals](selection/selection.json)

Both synthetic candidate reviews completed. One comparative call selected `toy`,
explained a trade-off against `selection-negative-result`, and recorded uncertainty.
The five API calls, including candidate reviews, cost an estimated $0.001372525.
Both candidate traces pass the ordinary review checks; the selector returned valid
candidate IDs and the required comparison.

There is no human preference reference. The rationale favors the toy's reported
outcomes while discounting the alternative's hypothetical status, although both
fixtures are hypothetical and both report outcomes. This deserves a consistency
check in later human evaluation; valid output structure alone does not establish
that the choice or rationale is sound.

Total live work: six review attempts plus one comparative decision, **28 API calls**,
estimated **$0.019236290**. Failed attempts are included; no evidence judge was run.
The [full protocol](../../milestones/M3-protocol.md) remains planned.

## Reproduce

After the shared installation, choose fresh output directories:

```shell
paper-review eval --variants agent pyagent_react evidence_memory baseline --task-ids T17 --model gpt-6-luna --repeats 1 --workers 3 --out runs/scratch/reproduced-t17-smoke
paper-review select data/dev/toy.json data/dev/selection-negative-result.json --variant evidence_memory --model gpt-6-luna --brief "Discuss experimental design, uncertainty, and useful follow-up studies" --out runs/scratch/reproduced-selection-smoke
```

Offline verification of the committed evidence:

```shell
paper-review check runs/m3-smoke-20261118/t17
paper-review check runs/m3-smoke-20261118/selection/reviews/toy
paper-review check runs/m3-smoke-20261118/selection/reviews/selection-negative-result
```
