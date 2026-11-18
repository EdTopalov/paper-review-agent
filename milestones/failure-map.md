# Failure map after M2

This map revisits every risk in the [original proposal](M1.md#failure-map).
An observed failure is evidence that a mechanism can fail; one occurrence does
not establish its frequency. Source-checked analyses and provisional model audits
are not human quality labels.

| M1 risk | Evidence and current status | Response and next measurement |
|---|---|---|
| Abstract hype hides weak support. | Not directly measured. [F06](../data/failures/F06.json) demonstrates the related problem of turning partial evidence into a paper-wide conclusion. | Check central claims against methods/results and counterevidence; human coverage labels must inspect the full snapshot. |
| Parsing corrupts tables, formulas, or results. | Known text-only limitation. [F05](../data/failures/F05.json) records quotation repair around PDF hyphenation; this does not demonstrate incorrect scientific conclusions. | Keep snapshots frozen; mark missing visual evidence as uncertainty and separate extraction failures from reasoning errors. |
| Rubric favors a topic or paper type. | Unmeasured. Twenty well-known ML papers, mostly empirical systems work, cannot establish fairness across fields or types. | Human labels by paper type and a separately reported, more diverse supplemental sample; preserve M2 comparability. |
| Scores fluctuate or inflate in weak batches. | M2 scores cluster, but one run per condition cannot separate sampling variation, model drift, or paper similarity. | Repeat baseline and every agent on identical inputs; report within-paper score spread and paired differences before comparing methods. Do not infer rating accuracy without human references. |
| Close-score review forces changes or wastes reads. | The planned batch-level close-score review was not implemented in M2; this risk is untested. Citation repair can consume decisions ([F05](../data/failures/F05.json)), which is a different mechanism. | Keep these mechanisms distinct. A future selection pilot should permit ties and record whether additional reading changes a decision. |
| Plausible assessment cites unsupported evidence. | Observed beyond citation mechanics. [F01](../data/failures/F01.json) expands a genuine interface requirement into a transfer restriction; [F06](../data/failures/F06.json) omits a relevant quantitative follow-up while making a general claim. Exact quotes do not prevent either error. | Label claim scope, central evidence coverage, and defect-versus-uncertainty calibration. Test whether a structured evidence memory or review step helps. |
| Reference scores reproduce model biases. | M2 contains no human gold scores. [F07](../data/failures/F07.json) shows a model judge contradicting both a numerical table and its own explanation. | Preserve the M2 judge for historical comparability, but calibrate compatible claim labels against independent humans. Report disagreement and abstention; do not call model verdicts ground truth. |

## Substantive review failures

**Unsupported extrapolation (F01, archived prototype).** The Reflexion review
turns a requirement for a termination heuristic and binary reward into a claim
that transfer is restricted. The cited statement establishes the requirement;
it does not establish how difficult transfer is. This is an interpretation error,
independent of whether the quote can be located. A qualified open question would
be defensible. Its frequency in later versions is unknown.

**Coverage-driven overgeneralization (F06, integrated M2).** The AutoGen review
describes the math comparison as qualitative after reading pages 8–10. Page 11
contains an additional 12-problem quantitative comparison. The agent next reads
pages 15–17 and later submits the broader criticism. The valid quote from page 10
does not support dismissing the whole comparison as qualitative. The follow-up
is still small, so this example does not prove that the paper merits a higher
score. It demonstrates a materially incomplete rationale.

**Judge arithmetic contradiction (F07, integrated M2).** The evidence audit says
ReAct does not improve WebShop success over Act while citing 40.0% versus 30.1%.
The frozen table agrees with those numbers and the paper explicitly describes
an improvement. Other qualifications in the audited observation can still be
debated; this contradiction alone invalidates treating the judge's reasoning as
reliable human ground truth.

## Operational failures and frequency

[F02](../data/failures/F02.json) and [F03](../data/failures/F03.json) document wrong
pages and edited quotations in archived runs. Page-specific observations and
citation rejection address these mechanics, but later verified completion does
not establish review quality. [F04](../data/failures/F04.json) documents a literal
search query contract mismatch and a wasted read, followed by recovery.

For [F05](../data/failures/F05.json), the integrated M2 T17 run exhausts its decision
budget after four rejected submissions. The observed sequence is established;
the relative contributions of model behavior and conservative normalization
remain hypotheses. Repeat T17 with every condition, retaining successful and
failed attempts. Report rejected submissions, remaining reading budget, and the
number of budget-exhaustion failures divided by all T17 attempts. Replays of a
fixed decision prefix test recovery conditional on that prefix; they do not
estimate the end-to-end failure rate. A successful rerun does not erase the
original failure, and one failure does not establish a stable failure rate.

The [human quality protocol](../data/quality/README.md) defines independent labels
for the substantive failures. It does not supply or imply completed annotation.
