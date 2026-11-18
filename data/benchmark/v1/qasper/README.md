# QASPER scientific-reading slice

This frozen slice contains 6 development and 20 held-out test questions with
existing practitioner answers. It samples only `qasper-dev-v0.3.json` from the
upstream release. The local `dev`/`test` split is independent of QASPER's official
split: it is **not** a new official QASPER test score.

`manifest.jsonl` binds each input and reference to SHA-256 hashes. Inputs contain
the complete supplied paper text and captions; reference answers, annotation IDs,
and gold evidence remain in separate files. Block IDs identify dataset paragraphs
or captions, not PDF pages. Images, PDF layout, and resolved bibliography entries
are unavailable; original `BIBREF`/`TABREF` extraction markers remain visible.

## Selection

The freezer fixes answer-type quotas before model outputs: test has 8 extractive,
4 yes/no, 4 free-form, and 4 unanswerable questions; development has 2 extractive,
2 yes/no, 1 free-form, and 1 unanswerable question. A paper contributes at most
two cases. Selection favors distinct source papers and uses a stable question-ID
hash to break ties. Paper-title hashes determine splits, keeping a source paper
in one split even across benchmark tracks.

Exclude questions if any annotation uses figure/table evidence (`FLOAT SELECTED`),
an evidence paragraph cannot map uniquely to the supplied text, an answerable
reference has no evidence, answer types disagree, yes/no labels conflict, or an
extractive answer is a bare unresolved bibliography/table/figure marker. Papers
above 150,000 supplied text characters are excluded. Remaining multiple human
answers are preserved; their semantic agreement is not assumed. `source.json`
records actual counts, exclusions, quotas, source hashes, and licence provenance.

## Preparation and interpretation

Run the freezer from the repository root with a fresh output directory:

```shell
python scripts/prepare_qasper.py --out runs/scratch/reproduced-qasper
```

This downloads pinned public data and performs deterministic preparation only.
It makes no model calls and does not run an evaluation. Reproduction reuses the
ignored source cache and verifies its hashes. The committed data need no download.

Report answer F1 and evidence F1 separately, preserving multi-reference answers
and answer-type slices. Each score is independently maximized across reference
annotations, following the [pinned official evaluator](https://github.com/allenai/qasper-led-baseline/blob/afd0fb96bf78ce8cd8157639c6f6a6995e4f9089/scripts/evaluator.py).
Answer F1 uses its token normalization; extractive spans are joined with comma-space.
Lexical answer F1 can undercount valid paraphrases. Evidence F1 compares sets of
unique source-block IDs, so several quotes from one block count once. This adapts
the official paragraph-list score to the benchmark's quoted-evidence format.
All means, including answer-type slices, include every planned attempt; failed
or invalid predictions receive zero. Missing attempt records reject the score
file. The official evaluator's type slices omit missing predictions, so those
slice denominators differ when an attempt fails.
Unanswerable questions require explicit abstention; empty evidence is legitimate
there. Questions from one source paper form one statistical cluster. This slice
tests scientific evidence reading, not overall paper merit or reading-club value.

See [licence and attribution](LICENSE.md) and [source metadata](source.json).
