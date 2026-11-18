# Deliberative review

Variant flag: `deliberative_review`. This agent enforces planning, evidence
gathering, drafting, criticism, and bounded revision. The controller and scripted
validation are implemented. Model evaluation follows development verification.

The target is substantive assessment error: declaring evidence absent after
partial reading, missing an appendix result, or overstating what a quotation
supports. A more elaborate controller is not assumed to produce a better review.

## Mechanism

1. The planner records at most three concrete evidence obligations and priorities.
2. The investigator uses the shared literal-search and page/block-reading tools.
3. The drafter returns the ordinary task output plus source-linked check records.
4. A critic receives a fresh context with the task, draft, observed passages, and
   coverage. It can approve or identify a consequential unsupported conclusion,
   contradiction, or unresolved obligation and request a targeted read.
5. The final reviewer resolves useful criticism through reading, revision, or an
   explicit uncertainty. Critic approval can end the run when the draft is valid.

The critic does not receive the investigator's conversation or unseen paper text.
An immutable evidence archive preserves exact observed excerpts and provenance;
a separate ledger holds tentative interpretations and unresolved obligations.
These notes are model judgments, not reference labels. All state is local to one
task. Source quotations must pass the shared location, matching, and observation
checks; critic approval cannot override them.

## Budget and hypothesis

All roles use the same configured model, rubric, source tools, output schema,
reading cap, and `max_reads + 3` decision cap as the other reading agents. Every
model request and transport retry enters normal usage and cost accounting.

With five configured reading actions, the eight-decision schedule allows one
plan, up to three exploratory reads, one draft, one critic, at most one targeted
read, and one final revision. An approved valid draft can finish earlier. The
reserved roles leave at most four actual reading actions, so stronger checking
can reduce coverage. A configured reading cap of at least one is required;
small budgets leave less or no exploratory reading beyond the initial excerpt.

The hypothesis is higher ReviewCritique macro-F1 and controlled pair accuracy
through fewer missed counterexamples and scope errors. Inspect phase choices,
challenged conclusions, requested evidence, final revisions, and failures to
connect scores with the mechanism. Report completion, answer/evidence F1,
selection accuracy, cost, and latency separately. Extra stages can repeat the
same model's errors, invent unnecessary criticism, or cost more without improving
quality. No quality advantage follows from citation validity alone.

The [implementation design](../../milestones/deliberative-review-design.md) gives
the schedule and checks. The [comparison protocol](../../milestones/benchmark-protocol.md)
defines frozen inputs, repeated model blocks, common limits, and scoring. Plans
must be refreshed after controller validation; a phase's opinion is never used
as an evaluation target.

## Sources

Planning and revision are architectural ideas from
[Plan-and-Solve Prompting](https://arxiv.org/abs/2305.04091) and
[Self-Refine](https://arxiv.org/abs/2303.17651). This controller adds source-limited
criticism and explicit budget reservation. It is an original implementation,
not a reproduction of either system. See [sources and licences](../../THIRD_PARTY.md).
