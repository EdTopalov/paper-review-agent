# Deliberative mechanism audit

This offline audit covers only the completed first `gpt-6-luna` deliberative
repetition: [64 core attempts](../../runs/m3-deliberative-20261118-luna6/r1/core/records.jsonl)
and [12 selection attempts](../../runs/m3-deliberative-20261118-luna6/r1/selection/records.jsonl).
The implementation was frozen before these tests. Reference labels were used
after the outcomes for this audit, not supplied to the agent.

Across all 76 attempts, 66 returned accepted outputs and 34 met the
[mixed-task exact-content criterion](README.md). All ten failures exhausted
their decision budget and score zero. A valid critic result was recorded in
63/76 attempts: 17 approved, five requested revision, and 41 requested
investigation. Those 41 attempts entered a targeted-read phase; that count
includes unsuccessful tool actions and does not measure useful evidence gained.

## Successful targeted verification

CB-80bd654cbc97 asks whether the headline accuracy equals the arithmetic mean
across all reported seeds. The
[initial investigation](../../runs/m3-deliberative-20261118-luna6/r1/core/deliberative_review-r1/CB-80bd654cbc97/trace.jsonl#L6)
wastes an overwide read, reads blocks b0002–b0004, and gets no literal-search
matches. It has not observed the seed values.

| Phase | Recorded behavior |
|---|---|
| [Draft, decision 5](../../runs/m3-deliberative-20261118-luna6/r1/core/deliberative_review-r1/CB-80bd654cbc97/trace.jsonl#L27) | Returns `insufficient`, explicitly identifying the unread values. |
| [Critic, decision 6](../../runs/m3-deliberative-20261118-luna6/r1/core/deliberative_review-r1/CB-80bd654cbc97/trace.jsonl#L32) | Requests blocks b0005–b0007 to resolve the mean and aggregation rule. |
| [Targeted observation, decision 7](../../runs/m3-deliberative-20261118-luna6/r1/core/deliberative_review-r1/CB-80bd654cbc97/trace.jsonl#L38) | Exposes b0007: equally weighted seed accuracies 67, 69, 71, 73, 75. |
| [Revision, decision 8](../../runs/m3-deliberative-20261118-luna6/r1/core/deliberative_review-r1/CB-80bd654cbc97/trace.jsonl#L42) | Computes their mean as 71%, matching the headline, and changes to `supported`. |

The [frozen reference](../../data/benchmark/v1/controlled/references/CB-80bd654cbc97.json)
is `supported`; the [final submission](../../runs/m3-deliberative-20261118-luna6/r1/core/deliberative_review-r1/CB-80bd654cbc97/trace.jsonl#L46)
is accepted with both quotations verified. This is a concrete improvement from
an incomplete internal draft to a correct final answer through additional
evidence. The initial draft is an intermediate state, not a separately budgeted
comparison agent; this example cannot isolate the critic's causal contribution
from an additional reading opportunity.

## Correct interpretation lost to the ledger contract

On CB-449d322624b5, the claim denies additional numerical comparisons beyond
two illustrations. The
[observed appendix](../../runs/m3-deliberative-20261118-luna6/r1/core/deliberative_review-r1/CB-449d322624b5/trace.jsonl#L23)
reports 20 other held-out problems, with 12 solved by the method versus 11 by
the baseline. The [raw draft](../../runs/m3-deliberative-20261118-luna6/r1/core/deliberative_review-r1/CB-449d322624b5/trace.jsonl#L26)
correctly returns `contradicted`, matching the
[reference](../../data/benchmark/v1/controlled/references/CB-449d322624b5.json).

However, its ledger marks checks `contradicted` while placing E3 under
`support` and leaving `counterevidence` empty. The controller requires a
counterevidence reference for that status and
[rejects the draft](../../runs/m3-deliberative-20261118-luna6/r1/core/deliberative_review-r1/CB-449d322624b5/trace.jsonl#L27).
The critic then appends quotation prose to source IDs instead of returning bare
IDs, causing [another rejection](../../runs/m3-deliberative-20261118-luna6/r1/core/deliberative_review-r1/CB-449d322624b5/trace.jsonl#L31).
[Two revisions](../../runs/m3-deliberative-20261118-luna6/r1/core/deliberative_review-r1/CB-449d322624b5/trace.jsonl#L35)
repeat the ledger-status mismatch, ending in
[decision-budget exhaustion](../../runs/m3-deliberative-20261118-luna6/r1/core/deliberative_review-r1/CB-449d322624b5/trace.jsonl#L41).

The correct label inside rejected model output is not a completed prediction.
This attempt receives zero benchmark credit and retains its incurred cost. It
demonstrates that the memory/provenance interface can prevent delivery even
when the source interpretation is correct. Neither internal critic approval
nor a locally improved draft establishes final assessment accuracy.
