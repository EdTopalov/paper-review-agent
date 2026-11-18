# Reading-club paper-selection pilot

Given two or more local paper inputs and a short club brief, select the candidate
with the most defensible research and discussion value for that brief. A rigorous
negative result can be preferable to a positive result with weak evidence. Return
one choice, specific comparisons against every other completed candidate, tied
alternatives when justified, and remaining uncertainties.

## Implemented mechanism

`paper-review select` reviews each candidate independently using the requested
reviewer variant. It then makes one structured-output model call over the brief,
final review objects, citation diagnostics, and failures. The selector receives
no additional paper text and must not imply that it read unseen pages. Its
cross-paper memory consists of final reviews; all candidates remain in context.
`evidence_memory` changes context within each paper, not the selector's memory
policy. There is no cross-run memory or learned user profile.

The controller requires distinct inputs and candidate IDs, at least two completed
reviews, a valid selected ID, and a trade-off against every other completed
candidate. Failed reviews remain visible and their costs are included. A
selection does not establish that excluded failed candidates were less valuable.
Selection ID checks validate the workflow; they do not validate the rationale.

After [installation](../README.md#installation), run:

```shell
paper-review select data/dev/toy.json data/dev/selection-negative-result.json --variant evidence_memory --model gpt-6-luna --brief "Discuss experimental design, uncertainty, and useful follow-up studies" --out runs/scratch/selection-dev
```

These inputs are explicitly synthetic development fixtures, not a selection
benchmark. A run writes `README.md`, `selection.json`, `selection-trace.jsonl`,
and one normal review/trace under `reviews/<candidate-id>/`. Total API calls,
tokens, USD, and latency include candidate reviews and the final decision.
Each trace event records the reviewer variant. The selector prompt and schema
are versioned independently from the unchanged M2 assessment rubric.

## Hypothesis and later experiment

The pilot tests whether the existing reviewer interface supplies enough explicit
evidence and uncertainty for an auditable comparative decision. Before a live
smoke test, the prediction is that the workflow reviews both fixtures, identifies
a supplied candidate, and explains a concrete trade-off without inventing
additional paper inspection. One successful smoke test verifies execution, not
selection quality or the value of memory.

A later selection benchmark should freeze candidate sets and club briefs,
including rigorous negative results, weak positive results, topic mismatches,
and sets where no candidate is compelling. Have at least two club members record
acceptable choices/ties, evidence-backed preferences, and disagreements before
model runs. Separate development sets from held-out sets.

Compare all-review memory to a bounded shortlist that retains the current leader,
its evidence, and unresolved comparisons while evicting other detailed reviews.
That would test cross-paper memory directly. Reuse identical precomputed reviews
when isolating selector memory; rerun the entire pipeline separately to measure
end-to-end cost and error propagation. Repeat candidate orders and decisions to
measure order effects and within-method variation. Report agreement with human
acceptable sets, critical factual errors, omitted contenders, ties, API cost,
latency, and retained-context size. Do not combine these outcomes with the
20-paper independent-assessment evaluation.
