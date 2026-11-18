# ReviewCritique: paper-grounded review-segment assessment

This frozen subset contains **26 cases from 13 source papers**: six development
cases from three papers and 20 test cases from ten papers. Each paper contributes
one expert-labelled reliable segment and one deficient segment. The test labels
are balanced, ten per class. These are existing annotations, not new human labels.

The source is Du et al. (2024), *LLMs Assist NLP Researchers: Critique Paper
(Meta-)Reviewing*, EMNLP, [paper](https://arxiv.org/abs/2406.16253) and
[dataset](https://github.com/jiangshdd/ReviewCritique). The exact upstream revision,
file hashes, selection counts, and transformations are in [source.json](source.json).
The source contains initial submissions rather than camera-ready papers.

## Task and labels

The agent receives the supplied paper text and one original review segment. It
judges the segment `reliable` or `deficient` at its stated scope, explains its
judgment, and can cite benchmark text-block IDs. `comment_context` supplies the
other text of the same original review so pronouns and references such as "this
strategy" have their original context. This is public unannotated review text;
the input excludes expert labels/explanations, numerical score metadata, and the
source decision field. Original reviewers may express their own recommendation
in prose; it is not an expert reliability label. Expert reference labels and
explanations are separate under `references/`.

The deficient slice selects `misunderstanding`, `neglect`, `inaccurate_summary`,
and `unstated_statement` annotations. Labels about other review segments, missing
external context, headings, boilerplate, and malformed records are filtered by
fixed rules. Reliable segments are drawn from criticism or questions, reducing
the shortcut where praise always means reliable. Word lengths and question form
are matched where possible. One pair is selected per paper; two cases from a
paper are not independent paper samples.

These labels measure agreement with expert assessment of the existing segment.
They are not infallible factual truth or an exhaustive checklist of paper flaws.
Some judgments involve interpretation or reasonable scope disagreements. Report
binary macro-F1 and per-class precision/recall, plus categories separately. Do not
map every deficient segment to a false scientific claim or use labels to assign
gold overall paper scores. No annotated evidence spans are supplied by this slice;
text-match citation checks do not substitute for semantic evidence labels.

Document text is split at source blank lines, with paragraphs longer than 8,000
characters divided into consecutive blocks. IDs such as `b0012` are benchmark
blocks, **not PDF page numbers**. Full supplied text is retained apart from outer
paragraph whitespace. Figures and original page layout are unavailable.

## Reproducible preparation

From the repository root with dependencies installed:

```shell
python scripts/prepare_reviewcritique.py --out runs/scratch/reproduced-benchmark/reviewcritique
python -m pytest -q tests/test_reviewcritique_prepare.py
```

The preparation command downloads pinned public source files into the ignored
`runs/scratch/benchmark-sources/reviewcritique/` cache, verifies their SHA-256
hashes, and freezes a fresh output directory. It makes no model calls. The original
100-paper human-review file supplies this subset; the separate LLM-review file
is not used. Selection is deterministic and precedes any agent outputs.

Paper identity uses the SHA-256 of a normalized title. Its first eight hex digits
modulo five assign development when zero and test otherwise. The first three
eligible development and ten eligible test papers in digest order are selected.
This shared rule prevents a paper with the same normalized title from crossing
the QASPER/ReviewCritique development/test boundary. Evidence/version alignment
beyond normalized title still requires the source identifiers in provenance.

## Attribution and usage

This directory is a modified subset: original segments and expert labels are
preserved, text is divided into blocks, error names are normalized, and reference
metadata is separated from agent inputs. Original upstream documentation is
retained in [UPSTREAM_README.md](UPSTREAM_README.md), and the complete upstream
[LICENSE](LICENSE) is included without alteration.

The source permits research evaluation, analysis, and benchmarking. It prohibits
model training and imposes attribution and redistribution requirements. This
subset is not training data and is not relicensed as unrestricted project code.
