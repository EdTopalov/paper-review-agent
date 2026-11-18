# Paper Review Agent

Review research papers for a reading club using an OpenAI model. The model chooses
which pages to read or search, then returns an absolute score from 0 to 1, a short
assessment, quotations with page numbers, and unresolved questions. Inputs can be
local PDFs or saved page-text snapshots; figures and page layout are not inspected.

## Installation

Use Python 3.12, the tested version. From the repository root:

```shell
python -m venv .venv
```

Activate with `.venv\Scripts\Activate.ps1` in Windows PowerShell or
`source .venv/bin/activate` on Linux/macOS. Then install:

```shell
python -m pip install -r requirements-m2.txt
python -m pip install --no-deps -e .
```

Copy `.env.example` to `.env` and set `OPENAI_API_KEY`. The optional `OPENAI_MODEL`
defaults to `gpt-6-luna`; `--model` overrides it. Local `.env` values take precedence
over environment variables. Keep credentials out of Git. `paper-review models`
lists model IDs accessible to the configured key.

## Usage

Run commands from the repository root with the environment activated:

```shell
paper-review verify
paper-review review data/eval/papers/T01.json --out runs/scratch/example
paper-review review path/to/paper.pdf --out runs/scratch/local-paper
paper-review eval --out runs/my-comparison --workers 3
```

`verify` checks saved input hashes without API calls and reports 20 distinct tasks.
`review` writes a readable `README.md` and one structured event log, `trace.jsonl`,
containing the review or error diagnostic. `eval` compares the
reading agent with a baseline that reviews the full paper in one model call, using
the same 20 saved papers, model, and scoring criteria. Model calls incur API costs.
Use a fresh output directory for each new run. Open `runs/my-comparison/README.md`
for the comparison table and links to each paper's review and decisions, ordered
by absolute score. Audits append to the same task logs and update those pages.

Optional evidence auditing asks a separate model call to judge whether each
review's claims follow from the paper. These judgments are provisional and billed
separately:

```shell
paper-review audit --experiment runs/my-comparison --workers 3
```

## Checks and navigation

```shell
python -m pytest -q
paper-review check runs/m2-integrated-20261026
paper-review summarize runs/m2-integrated-20261026
```

These commands inspect the code and saved results without API calls. `summarize`
rebuilds the readable pages from traces; `check` writes no additional files. Use
`paper-review --help` or `paper-review <command> --help` for options.

## Agent variants (M3)

The three agents are `agent` (native ReAct), `pyagent_react` (the
[PyAgent](https://pyagent.org/) harness with text actions), and
`deliberative_review` (enforced planning, evidence gathering, source-grounded
criticism, and revision). Scripted checks cover phase order, budget limits,
source provenance, and recovery through the shared entry point.
The full-paper one-call `baseline` is a fourth comparison method.
The [M3 report](milestones/M3.md) and [experiment protocol](milestones/M3-protocol.md)
define hypotheses, repetitions, human quality assessment, and limits.
The [short results report and accuracy/cost plot](milestones/M3-results/README.md)
summarize the repeated comparison; the [M2 appendix](milestones/M3-results/M2.md)
keeps full review metrics and per-paper evidence separate.
Select each implementation through the same `paper-review` entry point.

Reading agents have `2 * (max_reads + 3)` ordinary decisions: 16 with the default
five reading actions, or 46 with the benchmark selection cap of 20. Reading caps
are unchanged. Ordinary submissions require matching, observed quotations. At
the decision cap, one final call uses only observed fragments, without tools or
retries: a non-null public-schema answer is accepted with citation diagnostics;
null is a failure. This gives at most 17 or 47 decisions including finalization.

Install V2 in the activated environment, then select it with `--variant`:

```shell
python -m pip install -r requirements-m3.txt
python -m pip install --no-deps -e .
paper-review review data/dev/toy.json --variant pyagent_react --out runs/scratch/v2-dev
paper-review review data/dev/toy.json --variant deliberative_review --out runs/scratch/deliberative-dev
```

The original `eval --variant both` still compares only M2 and baseline. Each
variant's README contains its hypothesis and design. `eval --task-ids T17`
selects a diagnostic case from the unchanged sample. Repeated-run reports include
per-repeat variation, per-paper consistency, costs, and pass^k (success in every
one of k attempts). Full M2 comparison commands are in the experiment protocol.

## Evidence-assessment benchmark

The [frozen benchmark](data/benchmark/v1/README.md) adds 76 test and 26 development
cases for scientific questions, expert-labelled review criticism, controlled
claim appraisal, and paper selection under explicit requirements. Human labels
come from QASPER and ReviewCritique; synthetic targets come from deterministic
study records. All four methods use the same task contracts and source blocks.
Content correctness, citation matching, completion, and cost are scored separately.

Prepare and inspect a run without API calls:

```shell
paper-review benchmark-verify
paper-review benchmark-plan --split test --tracks qasper reviewcritique controlled --model gpt-6-luna --repeats 3 --out runs/scratch/benchmark-plan.json
paper-review benchmark-run --plan runs/scratch/benchmark-plan.json --out runs/benchmark-pending
```

`benchmark-run` validates only unless `--execute` is explicitly supplied. The
[benchmark protocol](milestones/benchmark-protocol.md) defines separate reading
budgets, repetitions, statistics, and saved plans. This suite supplements the
unchanged M2 comparison. The final comparison uses `gpt-6-luna`, three repetitions,
and eight workers per method. These targets do not provide gold ratings for overall paper merit
or human reading-club preference.

## Human assessment and paper selection

Export blinded review packets without API calls:

```shell
paper-review quality-export --experiment runs/my-comparison --out runs/scratch/human-packets
paper-review quality-score --packets runs/scratch/human-packets --labels labels-rater-a.jsonl labels-rater-b.jsonl
```

Follow the [human-label protocol](data/quality/README.md). Empty templates are
unlabelled; missing judgments never become positive quality scores. Keep the
packet's `private/` key away from annotators. Citation validity, claim support,
assessment quality, and completion have separate denominators.

The separate selection pilot compares final candidate reviews against a club brief:

```shell
paper-review select data/dev/toy.json data/dev/selection-negative-result.json --variant deliberative_review --brief "Discuss experimental evidence and uncertainty" --out runs/scratch/selection-dev
```

This command makes paid API calls for each review and one comparative decision.
It writes the chosen paper, trade-offs, ties, uncertainties, and total usage to
`selection.json`, with candidate and selection traces. The supplied development
papers are synthetic. See the [selection pilot protocol](milestones/selection-pilot.md)
for scope and future evaluation; selection is separate from the frozen M2 task.

| Location | Contents |
|---|---|
| [Source](src/paper_review), [tests](tests) | Agent, tools, evaluation, and offline checks. |
| [Dataset freezer](scripts/freeze_sample.py) | Optional source download and snapshot preparation; existing evaluation inputs are already frozen. |
| [M1](milestones/M1.md) | Original task, architecture, failure map, and evaluation plan. |
| [M2](milestones/M2.md) | Implementation, plan changes, measured results, and failure analysis. |
| [M3](milestones/M3.md), [PyAgent](variants/pyagent_react/README.md), [deliberative review](variants/deliberative_review/README.md) | Variant mechanisms, hypotheses, and experiment protocol. |
| [Failure map](milestones/failure-map.md), [human labels](data/quality/README.md) | Observed assessment failures, anticipated risks, and quality-evaluation instructions. |
| [Evaluation data](data/eval/README.md) | Frozen paper versions, provenance, licenses, and sampling limits. |
| [Assessment benchmark](data/benchmark/v1/README.md), [protocol](milestones/benchmark-protocol.md) | Frozen externally labelled and synthetic tasks, offline scoring, and prepared run plans. |
| [Saved runs](runs/README.md), [failure cases](data/failures) | Readable results, model/tool traces, and annotated decisions. |
| [Sources and licenses](THIRD_PARTY.md) | Attribution and dependency licenses. |
