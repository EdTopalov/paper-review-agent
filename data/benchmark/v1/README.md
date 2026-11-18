# Frozen evidence-assessment benchmark

This benchmark tests scientific reading, review criticism, bounded claim
assessment, and paper selection under an explicit club brief. It contains **102
cases: 26 development and 76 test**. The data are prepared and validated; this
directory contains no agent predictions or model evaluation results.

| Track | Development | Test | Reference target |
|---|---:|---:|---|
| [QASPER](qasper/README.md) | 6 | 20 | Existing practitioner answers and evidence paragraphs for scientific questions. |
| [ReviewCritique](reviewcritique/README.md) | 6 | 20 | Existing expert reliability labels for paper-review segments. |
| [Controlled appraisal](controlled/README.md) | 8 | 24 | Deterministic verdicts for hypothetical reports with one decisive change per pair. |
| [Selection pilot](selection/README.md) | 6 | 12 | Deterministic choices among hypothetical papers under eligibility and preference rules. |

The tracks have separate purposes and scores. There is no combined benchmark
score or reference overall paper rating. Development cases support debugging;
test cases support a later frozen comparison. Paper-title groups, controlled
scientific families, and selection base sets do not cross these splits.

## Inputs and references

Each track has `inputs/`, `references/`, a `manifest.jsonl`, and a `source.json`.
The top-level [manifest](manifest.jsonl) lists task IDs, tracks, splits, statistical
groups, paths, and SHA-256 hashes. [benchmark.json](benchmark.json) binds the
catalog and source notices. Loaders validate the complete corpus before selecting
a slice. Exact source revisions, download hashes, filtering, and transformations
are recorded in each track's source metadata.

A public input contains `id`, `kind`, `instructions`, and `documents`. Each
document has an ID, title, and ordered `blocks` with an ID and source text. The
task adds `question` for QA, `comment` and unannotated `comment_context` for
critique, `statement` for appraisal, or `brief` for selection. Block IDs identify
dataset text locations, not PDF pages. Existing reading tools use 1-based block
indices and expose the document/block mapping.

References contain human answers, expert labels, evidence locations, or synthetic
oracle facts. They remain outside model requests and model traces. Export public
inputs when using an external harness; do not send reference files or the full
manifest to the model. The supplied runner passes only the public input to each
architecture.

Every prediction contains a nonblank `explanation` and an `evidence` array.
Each evidence item is `{document_id, block_id, quote}` with a verbatim quotation;
at most eight items are allowed. The additional output fields are:

| Kind | Required fields |
|---|---|
| `qa` | `answer`; use `Yes`/`No` for yes/no questions and `Unanswerable` for abstention. |
| `critique` | `verdict`: `reliable` or `deficient`; `error_types`: an array of category names. |
| `claim` | `verdict`: `supported`, `contradicted`, or `insufficient`. |
| `selection` | `selected_id`: a candidate ID or `null`; `tied_ids`: all equally preferred IDs, including the selected ID when tied. |

For a unique selection, `tied_ids` may be empty or contain the selected ID.
Abstention requires an empty tie list. Duplicate exact evidence items, unknown
selection IDs, inconsistent ties, and schema-invalid predictions are rejected.
The shared contracts are in
[benchmark_tasks.py](../../../src/paper_review/benchmark_tasks.py).

## Scoring and denominators

[benchmark_scoring.py](../../../src/paper_review/benchmark_scoring.py) scores
existing records offline. Each selected task, variant, and repetition must have
one record, including failed attempts. A plan fixes the expected grid; score with
that plan to detect an entirely missing variant or final repetition. Different
models require separate comparisons. Failed runs and invalid predictions receive
zero content and evidence scores and remain in attempt denominators.

- **Completion** is a schema-valid returned prediction. It does not establish
  citation validity or assessment quality.
- **QASPER answer F1** is token overlap after lowercasing and removing punctuation
  and English articles. Answer and evidence scores each independently maximize
  over retained human references. Evidence F1 compares sets of unique
  `(document_id, block_id)` locations. This is a block-based adaptation of the
  official evidence metric, not an official QASPER leaderboard score. Both empty
  evidence sets score one; an empty and nonempty set score zero. Answer-type
  slices include every attempted case of that type, including failed attempts.
- **ReviewCritique** reports binary macro-F1, which averages the F1 of the two
  fixed classes, plus per-class precision/recall and expert error-category slices.
  These measure agreement with expert segment labels, not overall paper quality.
  This slice has no annotated evidence spans, so no reference evidence F1 is
  invented for it.
- **Controlled appraisal** reports verdict accuracy and pair accuracy. Pair
  accuracy requires both changed-source conditions to be correct. Evidence F1
  compares cited locations with the oracle's decisive locations.
- **Selection** reports acceptable-choice accuracy, including correct abstention,
  eligibility violations, exact best-set recovery, and results by input order and
  candidate count. Choosing an acceptable tied candidate earns choice credit;
  identifying the complete tie is a separate measure.
- **Citation validity** checks location existence and quotation matching. Quote
  verification rate uses submitted quotations as its denominator. An attempt has
  all citations verified only when it supplies at least one quotation and every
  quotation matches. Empty evidence can be appropriate for abstention but earns
  no verified-citation success. Matching text does not establish semantic support.

Content score is answer F1 for QA and a zero-or-one reference match for other
tracks. Content success requires a score of one. Reports include each repetition,
tokens, cost, latency, and failed attempts. Unknown accounting remains unknown.
`pass_power_k` estimates success on every one of `k` attempts using
`C(successes, k) / C(repetitions, k)`, averaged over tasks. It assumes independent
attempts. Paired 95% bootstrap intervals resample source-paper or synthetic-family
means, preserving repetitions and correlated cases within a group.

## Offline use

Run these commands from the repository root after the
[project installation](../../../README.md). They make no model calls:

```shell
paper-review benchmark-verify
paper-review benchmark-export --split dev --out runs/scratch/benchmark-dev-inputs
paper-review benchmark-plan --split test --model gpt-6-luna --repeats 3 --out runs/scratch/benchmark-plan.json
paper-review benchmark-run --plan runs/scratch/benchmark-plan.json --out runs/benchmark-pending
```

The plan records all four architectures (`agent`, `pyagent_react`,
`deliberative_review`, and `baseline`), model configuration, scheduling, and dataset
and source hashes. Planning preserves existing output files. `benchmark-run`
validates the plan by default and creates no experiment directory; only an
explicit `--execute` enables billed model requests. No execution is needed to
prepare or inspect the benchmark.

After experiment records exist, scoring is also offline:

```shell
paper-review benchmark-score --records runs/experiment/records.jsonl --plan runs/experiment/plan.json
```

Use the plan's split and tracks when scoring a restricted slice. Preparation
scripts and fresh-output reproduction commands are documented in each track.

## Scope and source terms

QASPER uses a text-only subset of the upstream development release, with a new
local split and existing annotations. It excludes questions dependent on figure
or table evidence and retains extraction artifacts. Lexical F1 can miss valid
paraphrases. See its [attribution and licence](qasper/LICENSE.md).

ReviewCritique uses 26 segments from 13 source papers. Expert labels can involve
reasonable scope disagreements. Same-review context restores references and
pronouns; it may include the original reviewer's prose recommendation, but no
expert reliability label or numerical score metadata. The
[upstream licence](reviewcritique/LICENSE) permits research benchmarking and
restricts model training and redistribution; preserve its attribution and terms.

Controlled and selection data are original CC0 hypothetical reports. Their oracle
labels test explicit facts and policies. They do not measure unrestricted review
quality or human reading-club preference. Selection ties occur only in development
cases. Test cases therefore cannot establish tie-resolution performance.

Selection inputs contain up to nine candidates and 54 blocks. With the default
five reading actions, five `read_pages` calls retrieve at most 15 additional full
blocks; the initial context provides the first block. A literal search returns at
most eight matches. A tight budget can leave candidates
uninspected and interact with input order. The baseline receives full text, so
report reading limits and order effects alongside quality and cost. A separate
larger reading budget can distinguish evidence coverage from comparison ability.

The 24 controlled test cases form four scientific families, and the 12 selection
test cases form four base sets with three orders each. These small numbers of
independent groups limit statistical claims. None of these tracks replaces a
semantic audit of complete generated reviews.
