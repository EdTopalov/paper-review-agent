# Deliberative review design

Variant `deliberative_review` enforces planning, investigation, drafting, criticism,
and resolution. Its hypothesis is fewer missed counterexamples and unsupported
judgments, improving expert review-label agreement and controlled claim assessment
compared with native ReAct.

## Five phases

| Phase | Model and controller behavior |
|---|---|
| Plan | Define up to three concrete evidence checks. |
| Investigate | Choose literal searches or bounded reads; record observed passages and coverage. |
| Draft | Produce the ordinary task output and a source-linked evidence ledger. |
| Critic | In a fresh context, approve the draft or identify consequential issues and request a precise evidence check. |
| Resolve | Optionally perform one targeted read, then revise or preserve uncertainty; enforce the shared output and citation checks. |

## Memory and context

The source archive preserves exact observed excerpts, stable IDs, locations, and
truncation status. An editable ledger holds obligations, fallible findings, support,
counterevidence, and unknowns. References must name observed source IDs; unread
material remains unknown.

The same-model critic receives the task, draft, archive, ledger, and coverage,
excluding the investigator's conversation and gold labels. State is local to one
task. It can approve a sound draft; the reviewer may reject unsupported criticism.

## Common budgets

The model, rubric, tools, output schema, and input limits are shared. Every role
consumes the common `2 * (max_reads + 3)` ordinary-decision cap. Searches and
reads consume reading actions; API requests and retries enter cost accounting.

- Default `max_reads=5`: 16 ordinary decisions, at most three exploratory actions
  and one targeted read within the shared five-action reading cap.
- Selection `max_reads=20`: 46 ordinary decisions, at most 18 exploratory actions
  and one targeted read within the shared 20-action reading cap.

Ordinary submissions require matching, observed quotations. At the decision cap,
one final API call receives only the task and observed source fragments, with no
tools or retries. It returns a public-schema answer or null, independently of
the ledger. A non-null answer is accepted with citation diagnostics retained;
null is a failure. Including this call, the decision maxima are 17 and 47.

A valid critic-approved draft can finish early; invalid outputs and repair use
remaining capacity. Reserved roles reduce exploration and can introduce ledger
failures; a same-model critic can repeat errors or prompt unnecessary changes.
Citation and provenance checks establish neither scientific correctness nor a
quality advantage. The [earlier-schedule audit](M3-results/deliberative-audit.md)
shows both a useful targeted verification and a ledger failure.

Architectural sources are [Plan-and-Solve Prompting](https://arxiv.org/abs/2305.04091)
and [Self-Refine](https://arxiv.org/abs/2303.17651). This original controller does
not copy their code or reproduce their experiments. See the
[implementation](../src/paper_review/deliberative_runner.py) and
[comparison protocol](benchmark-protocol.md) for behavior and metrics.
