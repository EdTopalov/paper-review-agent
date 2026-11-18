# Planner–reader–critic review agent

Variant flag: `deliberative_review`. The controller and scripted checks are
implemented. This is the third agent in the main comparison; model runs follow
development verification. Its internal critic is never an evaluation label.

## Mechanism and motivation

The reviewer uses an enforced planning, investigation, criticism, and revision
cycle. This changes which decisions occur and what information each role sees.
It targets substantive assessment failures: inferring a paper-wide omission from
an unread section, overlooking contrary results in an appendix, or expressing a
stronger conclusion than the reported evidence supports. See the
[failure map](failure-map.md), especially F01 and F06.

| Phase | Model decision | Controller responsibility |
|---|---|---|
| Plan | Identify up to three concrete evidence checks and prioritize them. | Reserve capacity for criticism and final repair. |
| Investigate | Choose searches or reads that address the checks. | Execute the existing tools, record observed passages and coverage, enforce limits. |
| Draft | Produce the existing task output and concise source-linked check records. | Validate structure and quotations; preserve errors for repair. |
| Critique | Approve or identify a consequential unsupported conclusion, contradiction, or unresolved check; propose a targeted read when useful. | Supply a fresh context containing the task, draft, observed passages, and coverage, excluding the reader's conversation. |
| Resolve | Inspect requested evidence, revise the conclusion, or preserve uncertainty. | Apply the unchanged final schema and observed-source quotation checks. |

The critic can approve a sound draft. It is not required to invent a flaw, and
the final reviewer may reject an unsupported criticism. Critic approval never
overrides quotation checks or counts as an evaluation label. Different contexts
using the same model can still produce correlated mistakes.

## Memory and evidence

Maintain an immutable archive of observed source excerpts with page/block IDs.
Keep a separate working ledger of evidence obligations, tentative conclusions,
supporting and conflicting source references, and unresolved questions. Record
which locations were read and whether observations were truncated. Uninspected
material stays unknown rather than becoming an asserted absence.

Ledger interpretations are model judgments; only their source provenance and
quotation fidelity can be checked mechanically. Planner/draft outputs supply
notes alongside their ordinary decisions, without extra bookkeeping calls.
The critic receives source material directly rather than trusting a summary of
it. Memory is local to the current task; references and expert benchmark labels
never enter any role's context.

## Shared resource limits

Use the same model, task rubric, source tools, input limits, and output contract
as the other variants. Every role uses the shared API accounting and decision
budget; transport retries count toward calls and cost. No role receives the full
paper outside the reading budget.

An explicit default schedule fits the existing eight-decision cap:

1. One planning decision.
2. Up to three exploratory reading decisions.
3. One draft decision.
4. One critic decision.
5. At most one targeted reading decision.
6. One final revision/submission decision.

This permits at most four reading actions within the shared five-read cap. The
reserved reasoning stages therefore reduce exploration capacity, which is an
intentional trade-off to measure. A critic-approved, source-valid draft can end
the run after at most six decisions. Remaining capacity handles criticism or
citation repair; exhausted capacity must not trigger hidden extra model calls.
For other configured limits, reserve these stages explicitly. The controller
requires at least one configured reading action, giving four decision slots;
at that minimum it can assess the initial excerpt without exploratory reads.
Preserve failures and incurred costs.

## Hypothesis and evaluation

Prediction: directed criticism and evidence gathering will reduce unsupported
scientific judgments compared with native ReAct. Expected signals are higher
ReviewCritique macro-F1 and controlled pair accuracy, especially for overlooked
counterevidence and scope errors. Improvement in citation completion is not the
primary hypothesis. Report QASPER answer/evidence F1, selection correctness,
completion, decisions, tokens, cost, and latency separately.

The unchanged M2 comparison remains necessary. The new benchmark supplies
independent narrow content targets; critic opinions supply none. Retain all
repetitions and group-based uncertainty estimates. Record concise phase choices,
challenged claims, source locations requested, repair outcomes, and final changes
in traces, without requesting private reasoning.

The main comparison is `agent`, `pyagent_react`, `deliberative_review`, and
`baseline`.
A later ablation can remove the mandatory critic while retaining the planner and
ledger, freeing the saved decisions for investigation. This separates structured
verification from the rest of the redesign.

Before model evaluation, use scripted clients to verify phase order, early
acceptance, shared budget exhaustion, targeted evidence repair, invalid critic
output handling, exact quotation preservation, and absence of reference leakage.
Freeze implementation and hypotheses before refreshing plans and collecting
development results; reserve test cases for the final comparison.

## Sources and limits

Planning and revision are architectural ideas from
[Plan-and-Solve Prompting](https://arxiv.org/abs/2305.04091) and
[Self-Refine](https://arxiv.org/abs/2303.17651). The controller adds
source-limited criticism and explicit budget reservation; it does not claim to
reproduce those systems or reuse their code.

Extra roles can increase cost, reduce evidence coverage, repeat the same model's
errors, or induce unnecessary criticism. The nine-candidate selection condition
is particularly sensitive to reduced reading capacity. These are measurable
risks, and a more elaborate controller is not assumed to be a better reviewer.
