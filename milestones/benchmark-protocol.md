# Evidence-assessment benchmark protocol

Status: data, common task adapters, offline scoring, and run plans are prepared.
Primary-model repetitions of the existing methods are
[running](../runs/m3-existing-20261118-luna6/README.md), alongside the
[deliberative block](../runs/m3-deliberative-20261118-luna6/README.md) and a
[secondary-model block](../runs/m3-all-20261118-luna56/README.md). The original
[M2 repeated comparison](M3-protocol.md) remains a separate experiment on its
unchanged 20 papers and rubric.

The round scheduler runs M2, core, and selection once before starting the next
round, targeting five completed repetitions of each method. Each stage keeps its
local repeat number and original trace; aggregate copies record the global round
with explicit source provenance. Separate model blocks and task tracks remain
separate statistics. `progress.json` links the active stage's live timing and ETA.
The primary blocks target five repetitions and the secondary block three.
Configured workers are six for existing primary methods, four for primary
deliberative review, and eight for the secondary block. These concurrent blocks
do not provide a controlled latency comparison.

## Reference targets and design

The [frozen dataset](../data/benchmark/v1/README.md) contains 26 development and
76 test cases. Its reference targets require no new manual annotation.
Development cases support debugging, scorer validation, and prompt or agent
adjustments. Test cases are reserved for the final comparison after the
implementation and hypotheses are frozen. Development outcomes are excluded
from test statistics; tuning against test outcomes requires a new evaluation
design rather than treating those cases as held out.

| Track | Test cases | Independent groups | Primary measure |
|---|---:|---:|---|
| QASPER scientific questions | 20 | 20 source papers | Mean answer F1 and evidence F1, separately. |
| ReviewCritique review segments | 20 | 10 source papers | Binary macro-F1 and per-class precision/recall. |
| Controlled claim appraisal | 24 | 4 scientific families, 12 pairs | Verdict accuracy and both-members-correct pair accuracy. |
| Explicit-brief selection | 12 | 4 candidate sets, 3 orders each | Acceptable-choice accuracy, including abstention, and order consistency. |

Development and test are separated by source-paper title, scientific family, or
candidate set. The test QASPER slice has eight extractive, four yes/no, four
free-form, and four unanswerable questions. ReviewCritique contributes one
reliable criticism and one deficient segment from each paper; the two classes
are balanced. Controlled pairs change one decisive block while keeping the
statement fixed. Selection uses 3, 6, or 9 candidates with explicit eligibility
requirements and preferences. Ties are present only in development; test results
cannot establish tie-resolution performance.

QASPER labels are existing practitioner answers and evidence. ReviewCritique
labels are expert judgments of supplied segments, with their original review
context. Controlled targets are calculated from hypothetical study records.
Selection targets follow a stated policy rather than an inferred human taste.
Do not pool these constructs into one quality score or interpret them as gold
overall paper ratings. The [design rationale](benchmark-design.md) explains the
choice of sources and remaining validity gaps.

## Common task and architecture comparison

`agent`, `pyagent_react`, `deliberative_review`, and `baseline` use the shared
controllers with the same benchmark task contract and structured prediction.
The adapter changes instructions, output fields, and source-location handling
equally for every method. It is not an additional architecture. Reference files,
expert explanations, and oracle facts are excluded from model requests and
model traces. Each attempt starts with fresh context and memory.

Source locations are identified blocks rather than PDF pages. Reading agents
receive the task, document/block catalog, and first block, then use the existing
literal-search and block-reading tools. Baseline receives every supplied block
in one call. Agents require submitted quotes to match observed text; baseline
can return a schema-valid answer with mismatching quotes. Content metrics are
therefore separate from that acceptance-rule advantage.

The architecture hypotheses remain those in the [M3 protocol](M3-protocol.md).
On this additional suite, the preregistered predictions are:

- PyAgent should preserve content accuracy and completion under the same reading
  budget; text-action errors may consume decisions and increase cost.
- Deliberative review should improve ReviewCritique macro-F1 and controlled pair
  accuracy by checking explicit evidence obligations and challenging unsupported
  conclusions. Its mandatory roles may instead reduce coverage or increase cost.
- The full-text baseline may outperform reading agents when evidence acquisition
  is the bottleneck. Citation matching alone cannot resolve that comparison.

Inspect reading choices, protocol errors, repeated rejected submissions, phase
transitions, critic challenges, and final revisions to connect outcomes to these
mechanisms. Deliberative controller integration and scripted checks precede plan
refresh and model runs. This selection
task places multiple candidate documents in one bounded reading episode. It does
not implement rolling memory between separately reviewed papers. The real-paper
[`select` pilot](selection-pilot.md) remains separate.

## Prepared model blocks and budgets

All saved plans compare four methods with the same configuration within a block.
The primary model is `gpt-6-luna`; the optional secondary model is `gpt-5.6-luna`.
Record resolved response model IDs and timestamps because aliases can change.
Each test block uses three repeats, six workers, low reasoning, at most 4,000 output
tokens per request, a 90-second timeout, and one retry. A seeded shuffle mixes
tasks, methods, and repeats; it does not seed API sampling.

| Plan type | Tasks | Repeats | Planned attempts | Reading actions per attempt |
|---|---:|---:|---:|---:|
| Development core smoke | 5 | 1 | 20 | 5 |
| Development selection smoke | 1 | 1 | 4 | 20 |
| Test core, per model | 64 | 3 | 768 | 5 |
| Test selection, per model | 12 | 3 | 144 | 20 |

The two smoke plans cover one QA task, a same-paper critique pair, a controlled
pair, and one selection case. They are future correctness checks and do not enter
test statistics. A full model block plans 912 attempts; the second model is a
separate optional block, not a pooled result. These are counts of planned attempts,
not completed runs or instructions to start them automatically.

Selection gets a larger budget because nine candidates contain 54 blocks.
Twenty reading actions allow all blocks to be inspected in groups of three.
The core limit of five actions would permit only 15 additional complete blocks;
search returns at most eight matches. Under that limit, candidate coverage and
position could dominate comparative reasoning. Even with the larger budget,
report which decisive blocks were actually observed and interpret order effects
with the baseline's complete-input advantage in view. Decision limits are reading
budget plus three; baseline has one decision. Deliberative planning, drafting,
and criticism consume the same decisions. With five reading actions configured,
the full deliberative schedule can use at most four reads; it reserves capacity
for a possible final revision. Its critic receives only observed source material.

## Offline preparation and inspection

From the repository root with the documented environment installed:

```shell
paper-review benchmark-verify
python scripts/prepare_benchmark_plans.py --out runs/scratch/fresh-benchmark-plans
paper-review benchmark-run --plan milestones/benchmark-plans/dev-core-smoke-luna6.json --out runs/benchmark-dev-core
paper-review benchmark-run --plan milestones/benchmark-plans/test-core-luna6-r3.json --out runs/benchmark-test-core
```

These commands make no model calls. The last two validate plans only and create
no experiment directory. Saved plans are in [benchmark-plans/](benchmark-plans/).
They bind task IDs, data/source hashes, model settings, and shuffled job grids.
The source hash covers current implementation bytes, including uncommitted edits;
the recorded Git revision alone is not proof of their contents. A source change
invalidates a saved plan. Regenerate plans into a fresh directory after a code
change. Use `--root data/benchmark/v1` if moving a plan to another checkout.

Only adding `--execute` to `benchmark-run` enables billed model requests. No
execution is part of preparation. When execution is deliberately started later,
use a fresh output directory for each plan. It will contain `plan.json`,
`source.zip`, `records.jsonl`, `scores.json`, a readable `README.md`, and one
`trace.jsonl` and readable prediction per method/repeat/task. Reference labels
are used only by the offline scorer after model prediction.

To rebuild the source-derived corpus without model calls:

```shell
python scripts/prepare_benchmark.py --rebuild-sources --out runs/scratch/reproduced-benchmark-v1
paper-review benchmark-verify --root runs/scratch/reproduced-benchmark-v1
```

This downloads pinned public sources when absent from the ignored cache and
verifies their hashes. Normal use needs only the supplied frozen files. Each
track retains original attribution, licence terms, and transformation metadata.

## Scoring and reporting

After predictions exist, score them without model calls, using the original plan
to enforce the complete task/method/repetition grid:

```shell
paper-review benchmark-score --tracks qasper reviewcritique controlled --records runs/benchmark-test-core/records.jsonl --plan runs/benchmark-test-core/plan.json
paper-review benchmark-score --tracks selection --records runs/benchmark-test-selection/records.jsonl --plan runs/benchmark-test-selection/plan.json
```

Failed attempts and invalid predictions receive zero content/evidence score and
remain in success, latency, and cost denominators. Do not retry failed cells
selectively, remove errors, or substitute a rejected draft for a final answer.
Keep incomplete experiments; the scorer rejects an incomplete grid. Unknown
usage remains unknown. Preserve failed-request costs and billing uncertainty.

Report each track and repeat before comparing methods. Include completion,
content targets, decisions, reading/tool/model calls, input/output/cached tokens,
estimated dollars, and latency per attempted task. Quotations are a separate matching measure; their
denominator is submitted quotes. Correct decision plus matching text does not
prove a sound explanation. QASPER answer F1 measures lexical token overlap, and
evidence F1 compares unique source-block sets, independently maximizing over
human references. Answer-type slices include failures. See the
[metric definitions](../data/benchmark/v1/README.md#scoring-and-denominators).

For binary or exact content success, report `pass^k`, the estimated probability
of correctness on every one of k attempts: average `C(s,k)/C(n,k)` over tasks
with s successes in n repeats. QA exact success requires answer F1 of one; use
mean answer F1 as its primary graded measure. Do not confuse `pass^k` with the
probability of at least one success.

Paired 95% bootstrap intervals compare group means of content score and exact
content success, retaining all repeats and
correlated cases within each source paper, scientific family, or candidate set.
Report the number of groups and per-group results. Four controlled families and
four selection sets give limited uncertainty estimates; repetitions and three
candidate orders do not create more independent studies. Selection reports both
all-orders-correct and same-choice consistency, since consistent mistakes are
possible. Compare model blocks separately and interpret provider drift as an
unresolved external source of variation.

## Validity limits and follow-up

Public source material may occur in model pretraining. QASPER is a small text-only
slice of its upstream development release, with local splits. ReviewCritique
assesses existing segments and reasonable experts can disagree. Synthetic reports
are narrow, stylistically regular diagnostics. No track establishes complete
review usefulness or genuine human reading-club preference.

Majority-label and always-criticize controls should accompany interpretation;
balanced critique labels and supported controlled counterparts prevent a blanket
criticism policy from succeeding. Source-free, abstract-only, and oracle-evidence
model ablations remain follow-up experiments and have no results. A human audit
of complete reviews remains useful when available. Choose an architecture only
after content reliability, within-method variation, cost, and latency are known;
no winner follows from benchmark preparation.
