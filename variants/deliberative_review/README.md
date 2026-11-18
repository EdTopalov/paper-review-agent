# Deliberative review

Select this agent with `--variant deliberative_review`.
Prompt version: `m3-deliberative-review-v2`.
Controller policy: `plan-investigate-draft-critic-resolve-doubled-cap-final-v2`.

The controller enforces planning, evidence gathering, drafting, fresh criticism,
and bounded resolution. Its hypothesis is fewer missed counterexamples and scope
errors, measured through expert review-label agreement and controlled claim
assessment.

The ordinary decision caps are 16 for five reading actions and 46 for 20.
At exhaustion, one call without tools or retries returns an answer or null,
giving at most 17 or 47 decisions. Ordinary submissions retain the observed-quote
gate; forced non-null answers retain citation diagnostics without that gate.
Null counts as failure. The reading caps stay unchanged.

After the [standard installation and API setup](../../README.md), run a review:

```powershell
paper-review review data/dev/toy.json --variant deliberative_review --out runs/scratch/deliberative-example
```

Outputs include the review, phase trace, and usage accounting.

Sources: [controller](../../src/paper_review/deliberative_runner.py),
[finalizer](../../src/paper_review/finalization.py),
[dispatch](../../src/paper_review/runner.py), [tests](../../tests/test_deliberative.py).

The [design](../../milestones/deliberative-review-design.md) defines memory,
context boundaries, budgets, sources, and the mechanism audit. The
[comparison protocol](../../milestones/benchmark-protocol.md) defines evaluation.
