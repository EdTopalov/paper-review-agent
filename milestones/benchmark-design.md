# Proposal: evidence-grounded assessment benchmark

Status: design proposal, not an implemented dataset or completed experiment.
The initial design assumes little or no new human annotation. It supplements the
frozen M2 sample; no existing task, snapshot, result, or rubric is replaced.

## What should improve

The existing 20-paper comparison measures execution, citation matching, cost, and
variation. It lacks independent targets for whether an assessment interprets the
paper correctly. Repeating that comparison cannot supply those targets.

The new benchmark should test three separable abilities:

1. Find and interpret the evidence needed to answer a scientific question.
2. Distinguish justified criticism from a substantive review error.
3. Use retained evidence to make a comparative decision under explicit requirements.

These are measurable parts of reviewing. None alone establishes overall research
merit or what a particular reading club would enjoy most. Numerical paper scores,
acceptance decisions, citations, and a model's preferred paper are not gold labels
for those broader constructs.

## Externally labelled core

| Source | Task | Primary automatic measures | Boundary |
|---|---|---|---|
| [QASPER](https://huggingface.co/datasets/allenai/qasper) | Full paper plus a scientific question; return an answer, answerability, and supporting evidence. | Official answer F1 and evidence F1, with yes/no and unanswerable outcomes reported separately. | Practitioner-labelled scientific reading, not holistic review quality. |
| [ReviewCritique](https://github.com/jiangshdd/ReviewCritique) | Paper plus an existing review segment; judge whether the segment is deficient and identify its deficiency. | Macro-F1 and per-class precision/recall against expert labels; separate factual contradiction/misunderstanding from vague or out-of-scope criticism. | Labels apply to supplied review segments, not arbitrary new reviews or an exhaustive list of a paper's flaws. |

QASPER separates question writers, who saw a title and abstract, from answerers,
who read the paper and selected evidence. Its annotators are NLP practitioners;
the dataset card explicitly distinguishes them from expert researchers. Use the
[official evaluation conventions](https://github.com/allenai/qasper-led-baseline)
and preserve multiple answers rather than inventing a single reference score.
An initial text-only slice can use extractive, yes/no, and unanswerable questions;
free-form answers remain a separately reported, harder slice. Answer F1 is lexical
overlap and can undercount valid paraphrases.

ReviewCritique includes paper text and expert annotations of human and generated
review segments. Remove headings and generic administrative material using a
rule fixed before running agents. An expert label of an unreliable segment can
mean vague or irrelevant criticism rather than factual falsity. Preserve that
distinction; raw accuracy over a majority-reliable set can be misleading.

Start with an approximately 40-case held-out core: 20 QASPER questions and 20
substantive ReviewCritique segments, with at most two cases per source paper.
Use a separate small development slice to validate adapters and scoring. These
are acquisition targets, subject to the available class balance and evidence;
report actual counts rather than filling missing classes with generated labels.
Expand the number of source papers before increasing repetitions extensively.
Twenty questions from ten papers provide ten paper clusters, not twenty
independent scientific documents.

This requires a common assessment-task interface for every architecture, such as
`question -> answer + evidence` and `review segment -> verdict + explanation`.
The same task contract, tools, evidence limits, and output schema must apply to
native ReAct, PyAgent, evidence memory, and the full-text baseline. A shared task
adapter is not a new agent variant. Existing free-form M2 reviews remain unchanged.

## Controlled evidence sensitivity

Add a small diagnostic set of paired research reports. Generate a structured
study record first, calculate the target facts and conclusions in code, and only
then render the report. An unconstrained model-written paper and its own model-
written answer key would not provide an independent reference.

| Pair changes | What the task can establish |
|---|---|
| A confidence interval includes zero versus lies wholly above zero, under the stated analysis. | Whether the reported interval supports the particular positive-effect claim. A nonsignificant result is not proof of no effect. |
| Evaluation examples are independent versus were used during prompt tuning. | Whether the claimed independent evaluation is actually independent. |
| Lower inference expense with or without a disclosed preparation expense that reverses total cost. | Whether the total-cost claim follows from the reported accounting. |
| Evidence is restricted to English versus includes the languages named in the conclusion. | Whether the conclusion exceeds the demonstrated scope. |
| All seeds are reported versus the headline describes the best seed as a typical outcome. | Whether the stated aggregation matches the evidence. |
| A quantitative appendix resolves an apparent omission versus the omission remains. | Whether criticism changes when relevant counterevidence exists. |

The last family directly addresses the M2 coverage failure. Include sound
controls, honest negative findings, and legitimate scope boundaries: criticizing
everything must score poorly. Ask for the bounded scientific conclusion or
critique verdict, not an invented gold score for overall paper quality.

An initial diagnostic can contain 12 held-out pairs plus a small development set.
Keep both versions of a pair in the same split, and hold out report templates or
study families where feasible. Otherwise models can memorize the expected label
from a development counterpart. Vary wording, numeric ranges, and evidence
locations; no title, filename, or synthetic-status cue should predict a label.
Disclose hypothetical provenance consistently at task level and in metadata.

Score ordinary verdict accuracy and **pair accuracy**: the proportion of pairs
where both versions are correct. A changed answer alone is insufficient because
both answers can be wrong. Add meaning-preserving variants, such as reordered
sections, where the answer should remain unchanged. Report these as synthetic
diagnostics, separately from externally labelled real-paper cases.

## Selection and memory

With no new preference labels, universal reading-club selection accuracy is
unknown. A controlled selection task can instead have explicit requirements and
known candidate facts. For example, a club looking for a method to reproduce
under a specified resource limit can require a matching task, sufficient disclosed
resources, and independently evaluated results. Another brief can explicitly seek
a methodological failure worth discussing. The same candidate need not win both.

Specify hard requirements separately from preferences. Use an acceptable-choice
set when candidates tie, and include cases with no eligible candidate. The
current pilot always selects one candidate; an abstention result would need to
be added for those cases. Ground-truth eligibility and controlled preferences
come from the task contract, not an automatic claim about scientific merit.

Test 3, 6, and 9 candidates, balanced candidate orders, and early versus late
decisive evidence. Include an early candidate that remains best and a later one
that changes the decision. Report requirement violations, correct acceptable-set
selection, retained decisive facts, order sensitivity, cost, and latency.
Synthetic candidate families and their order variants remain in one split.

The current `evidence_memory` variant curates history within one paper. The
selection pilot reviews papers independently and then submits all final reviews
in one call; it does not yet test rolling cross-paper memory. To isolate that
mechanism, compare all-review context with an explicit bounded evidence table or
shortlist using the same frozen candidate reviews. Evaluate the full review-plus-
selection pipeline separately to measure error propagation and total cost.
Longer candidate lists alone do not establish that a memory mechanism helps.

## Free-form reviews and judging

Continue collecting ordinary reviews of real papers. A judge can assess their
support, coverage, calibration, and usefulness, but those scores remain an
automated proxy when new human judgments are unavailable. Validate the judge on
held-out ReviewCritique labels and report its per-category mistakes. Success at
segment classification does not validate its entire review-level rubric.

Retain the M2 judge and rubric for the historical comparison. A different judge
or rubric on the new suite must be reported as a separate evaluation. Public
peer reviews can help locate candidate issues, but their absence is not evidence
that a novel criticism is wrong. Venue acceptance and reviewer ratings are noisy
external assessments, not reading-club ground truth.

## Acquisition and validity checks

- Pin upstream revisions, data hashes, licences, and filtering rules. The QASPER
  dataset card lists CC BY 4.0. ReviewCritique's
  [custom licence](https://github.com/jiangshdd/ReviewCritique/blob/main/LICENSE)
  permits research evaluation and benchmarking while prohibiting model training.
  Preserve required notices and check the pinned terms before redistribution.
- Split by source paper and study family before inspecting agent outputs. Keep
  questions, review segments, revisions, and counterfactuals of one paper together.
- Freeze exact supplied text and evidence identifiers. QASPER paragraphs are not
  PDF pages. Preserve paragraph IDs or provide a verified mapping; do not silently
  reinterpret paragraph numbers as PDF page numbers.
- Exclude or separately report figure/table-dependent cases for text-only agents.
  QASPER marks selected non-text evidence with `FLOAT SELECTED`. Preserve the
  exclusion counts and sampling limitations.
- Hide reference labels and expert explanations from agents. Keep input-derived
  context memory local to a task; reset cross-run learned state between conditions.
- Include cheap shortcut controls: question/comment without the paper, abstract
  only, majority label, and always-criticize. Strong shortcut performance signals
  that a task may not require the evidence-reading mechanism being compared.
- Diagnose evidence acquisition separately from interpretation. For a small slice,
  supply the labelled evidence to every method. Improvement there identifies a
  reading bottleneck; persistent errors point to interpretation or output policy.
- Keep failed attempts in success and cost denominators. A last rejected draft
  can be inspected diagnostically but is not a successful final review.
- Report each track separately. Cluster uncertainty by source paper or synthetic
  family, and do not pool repeated attempts or reordered copies as new papers.

## Recommended sequence

1. Audit data availability and labels without model calls. Build a few examples
   of each task, verify source mappings and scoring, and freeze development/test
   splits. No large evaluation matrix is justified at this stage.
2. Run a tiny correctness pilot on development cases. Check that majority-label,
   source-free, and sound-control cases reveal expected benchmark weaknesses.
3. Freeze adapters, hypotheses, and the held-out benchmark. Evaluate all four
   methods on the same core with one model and repeated attempts. Retain the
   frozen M2 repetitions as the separate milestone comparison.
4. Add the controlled pairs, then the second model. Add cross-paper memory and
   the selection stress suite once that mechanism is implemented. No full matrix
   is started automatically by this proposal.

This design supports claims about evidence reading, substantive critique
judgments, and controlled selection reliability. Broader claims about human
reading-club value remain open until suitable preference labels become available.
