# Human assessment quality protocol

Citation matching tests whether a quotation occurs on its cited page. It does not
test the interpretation, coverage of central evidence, or usefulness of a review.
This protocol adds independent human assessment while preserving the frozen
[20-paper sample](../eval/README.md). No human labels are supplied with the code.

## Sampling and blinding

Select task IDs and repetitions before inspecting the new results. Include every
variant, including the one-shot baseline, for each selected task and repetition.
The exporter uses the variants, tasks, and repetition count declared in
`experiment.json` and rejects an incomplete grid, including a repetition missing
for every variant. Explicit task/repetition subsets are permitted and recorded.
For standalone experiments without a manifest, it uses the observed grid and
the supplied sample. Use the complete grid if annotation time
permits; otherwise freeze a task subset and report that subset's size. Do not select
only failures, close scores, or successful outputs for comparative quality claims.

`export_quality_packets(experiment_dir, out_dir, sample_path, task_ids=None,
repeats=None, seed=20261118)` in [quality.py](../../src/paper_review/quality.py)
creates a fresh packet directory without model calls. It contains:

- `packets.jsonl`: shuffled reviews under stable blind IDs, including failed attempts.
- `papers/`: the exact frozen full-text snapshots, with PDF page boundaries.
- `labels-template.jsonl`: empty annotation fields; these are not labels.
- `protocol.json`: selected tasks, repetitions, dimensions, and shuffle seed.
- `private/key.jsonl`: condition mapping and source trace/review SHA-256 hashes.

The command-line equivalents, from an installed checkout, are:

```shell
paper-review quality-export --experiment runs/my-comparison --out runs/scratch/human-packets
paper-review quality-score --packets runs/scratch/human-packets --labels rater-a.jsonl rater-b.jsonl
```

Optional `quality-export --task-ids T01 T03 --repeats 1 2` exports that complete
subset across every condition. `quality-score --adjudication adjudicated.jsonl`
adds adjudicated decisions after the independent labels have been collected.

Give annotators the packets, snapshots, template, and this rubric. Withhold
`private/` and condition-level results until independent annotation ends. Blind IDs
hide explicit condition names; writing style can still reveal a condition. Keep
the private key separate when distributing packets. The hash records identify the
exact source traces; do not amend exported reviews or snapshots after annotation.
Each public packet is hashed into the private key, including paper identity,
snapshot hash, completion status, and review. Scoring rejects swapped sources,
duplicate IDs, or a packet set that differs from the declared protocol grid.

Use at least two people who can assess the paper's methods and evidence. Each
person copies the template to a separate file and supplies a stable `rater_id`.
Annotators inspect the entire supplied snapshot when judging a claim that evidence
is missing. Page images and figures are unavailable: mark genuinely undecidable
claims `unclear` and describe the extraction limitation. Do not use the generated
numeric paper score, reputation, or acceptance decision as a quality reference.

## Review labels

Rate every dimension from 0 to 2. Cite PDF pages and explain the judgment. The
dimensions evaluate the **review**, not the quality of the paper being reviewed.

| Field | 0 | 1 | 2 |
|---|---|---|---|
| `support` | A material claim contradicts or exceeds the supplied evidence. | Mostly grounded, with a minor unsupported inference or an unresolved ambiguity. | Material claims are supported at their stated scope; uncertainty is explicit. |
| `central_evidence_coverage` | Misses or misrepresents evidence central to its conclusion. | Identifies the contribution but omits important evidence or counterevidence. | Covers the main contribution and decisive evidence, including relevant caveats. |
| `calibration` | Presents an open question, an unread passage, or a scope boundary as a demonstrated defect. | Usually distinguishes defects and uncertainty, with some overstatement. | Distinguishes findings, limitations, and unresolved questions consistently. |
| `reading_club_usefulness` | Generic or misleading; gives little basis for deciding what to discuss. | Contains useful specifics but leaves the discussion value poorly explained. | Explains a concrete insight, evidence issue, or unresolved question worth discussing. |

Set `critical_factual_error` to true only for an incorrect claim that could
materially change the assessment or discussion decision. Explain the error and
give source pages. This flag is reported separately from the four dimensions.
Do not treat an exact quotation as proof that its attached interpretation is sound.

For every observation, supply one claim label:

- `supported`: the paper justifies the claim at its stated scope.
- `unsupported`: the claim is contradicted, ungrounded, or materially overstated.
- `unclear`: ambiguity or missing visual information prevents a fair judgment.

Every review and claim label needs a nonempty reason and valid `source_pages`.
Failed attempts remain in the packet and need no invented review labels.

## Aggregation, disagreement, and judge checks

`score_quality_labels(packet_dir, label_paths, adjudication_path=None)` validates
labels without API calls. Two distinct rater IDs are required for every completed
item before its final quality is available. The tool cannot establish that an ID
belongs to an independent human; the annotation procedure must establish this.

For one completed review, normalized quality is the sum of its four dimension
scores divided by 8. This transparent, equally weighted summary is an operational
measure, not a validated estimate of scientific merit. Report dimensions as well
as the summary. Without adjudication, aggregate the independent raters' scores by
their mean. Report items with any dimension, claim-verdict, or critical-error
disagreement. Discuss disagreements and optionally supply a separate adjudication
file in the same format; retain the original independent labels.

The primary **adequate-review rate** uses a prespecified threshold: all four
dimensions are at least 1 and `critical_factual_error` is false. Compute this
binary decision separately for each independent human rating. An item's
`adequate_probability` is the fraction of independent ratings that pass, or the
adjudicated binary decision when one is supplied. This fraction describes rater
agreement on adequacy; it is not a calibrated model probability. The variant's
`adequate_review_rate` is the mean of these item values over **all selected
attempts**. Failed attempts contribute zero. For example, one completion that
passes one of two human ratings and one failed attempt produce `(0.5 + 0)/2 =
0.25`. A critical factual error can disqualify an otherwise high-scoring review.

Variant quality is the mean over **all selected attempts**, with failed reviews
contributing zero quality and zero evidence coverage. An unlabelled completed
review is missing data, not a zero: variant quality remains null until its completed
reviews have two labels each; the adequate-review rate follows the same rule.
Always report selected attempts, completed reviews,
independently labelled completions, adjudications, and critical-error votes with
their judgment denominator. Report quality separately from completion, citation
verification, cost, and latency. Repeated attempts on a paper are not independent
papers; uncertainty should be calculated by resampling papers as clusters.

The optional existing M2 evidence audit is a separate, provisional model judgment.
Its judge model and rubric must remain fixed for comparisons. For claim-level
agreement only, collapse its `overstated` and `unsupported` labels into
`unsupported`, and its `uncertain` into `unclear`. Report matching labels divided
by compared claim labels. Before adjudication, each independent human claim label
is one comparison; after adjudication, an adjudicated item contributes its final
claim labels once. Do not compare this claim-label agreement with review-level
coverage or usefulness scores. No audit means no agreement estimate.

## Supplemental expert-labelled benchmark

[ReviewCritique](https://github.com/jiangshdd/ReviewCritique) contains expert
deficiency annotations and explanations for review segments: 100 papers with
human reviews and 20 papers with model-generated reviews. It is a useful candidate
for calibrating a judge's detection of contradictions, vague critiques, and
out-of-scope requests. It does not provide gold reading-club rankings or directly
score newly generated reviews of the frozen M2 papers.

A separate accession should pin an upstream commit and file hashes, preserve
paper-level splits, sample both deficient and non-deficient substantive segments,
hide expert labels from the judge, and report class counts and per-class recall.
Keep this result separate from the M2 comparison. The upstream
[README](https://github.com/jiangshdd/ReviewCritique/blob/main/README.md) permits
research evaluation and benchmarking. Its custom
[Apache NON-AI license](https://github.com/jiangshdd/ReviewCritique/blob/main/LICENSE)
prohibits model training without permission and requires attribution and license
preservation for redistribution. No ReviewCritique records are imported here;
inspect the pinned license before a future accession.
