# Evidence-assessment benchmark design

The benchmark tests whether an agent interprets paper evidence correctly and
changes its judgment when decisive evidence changes. It supplements the frozen
20-paper M2 comparison, whose completion and citation checks do not independently
measure assessment quality. The [protocol](benchmark-protocol.md) specifies the
frozen cases, common interfaces, budgets, and scoring.

## Why four tracks

| Track | Ability tested | Independent reference |
|---|---|---|
| [QASPER](https://huggingface.co/datasets/allenai/qasper) | Answer a scientific question and locate supporting evidence. | Existing practitioner answers and evidence paragraphs. |
| [ReviewCritique](https://github.com/jiangshdd/ReviewCritique) | Distinguish reliable criticism from a deficient review segment. | Existing expert segment labels. |
| [Controlled appraisal](../data/benchmark/v1/controlled/README.md) | Revise a bounded scientific verdict when one decisive fact changes. | Conclusions calculated from hypothetical study records before rendering the text. |
| [Explicit-brief selection](../data/benchmark/v1/selection/README.md) | Compare candidates against eligibility requirements and preferences. | A deterministic policy, including abstention when no candidate qualifies. |

Scientific questions test evidence acquisition and interpretation. ReviewCritique
adds substantive assessment targets beyond quotation matching. Controlled pairs
isolate sensitivity to decisive evidence; both members must be correct to earn
pair credit. Selection adds comparative reasoning, larger candidate lists, and
order diagnostics under an explicit club brief.

## Labels and attribution

No new manual annotation is required. QASPER preserves multiple human references
and follows the [pinned evaluator's answer normalization](https://github.com/allenai/qasper-led-baseline/blob/afd0fb96bf78ce8cd8157639c6f6a6995e4f9089/scripts/evaluator.py).
ReviewCritique preserves expert labels and supplies unannotated original-review
context. Controlled and selection targets come from code rather than an LLM
judging its own generated answers. All tracks separate public inputs from
reference answers, expert explanations, and oracle facts.

QASPER's [attribution and CC BY 4.0 notice](../data/benchmark/v1/qasper/LICENSE.md)
and ReviewCritique's [preserved upstream licence](../data/benchmark/v1/reviewcritique/LICENSE)
apply to their respective subsets. ReviewCritique permits research benchmarking
and restricts training and redistribution. Original hypothetical reports are
CC0; [source metadata](../data/benchmark/v1/README.md#inputs-and-references)
records pinned revisions, hashes, filtering, and transformations.

## Grouped development and test sets

The [frozen corpus](../data/benchmark/v1/README.md) has 26 development and 76 test
cases. Source-paper title groups, controlled scientific families, and selection
candidate sets remain within one split. Counterfactual pairs and candidate-order
variants stay together. Development supports debugging and adjustments; its
outcomes are excluded from test statistics. Repetitions and reordered copies
measure variation without creating additional independent papers or studies.

## Scope

These tracks measure scientific reading, expert-label agreement, controlled
evidence sensitivity, and policy-based selection. Public material may occur in
model pretraining; lexical answer F1 can miss valid paraphrases; expert segment
labels can involve judgment. Synthetic cases and the small numbers of independent
families constrain generalization. The selection task is one bounded reading
episode, rather than rolling memory across separately reviewed papers. None of
the targets establishes overall paper merit or human reading-club preference.
