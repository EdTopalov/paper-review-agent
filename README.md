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

| Location | Contents |
|---|---|
| [Source](src/paper_review), [tests](tests) | Agent, tools, evaluation, and offline checks. |
| [Dataset freezer](scripts/freeze_sample.py) | Optional source download and snapshot preparation; existing evaluation inputs are already frozen. |
| [M1](milestones/M1.md) | Original task, architecture, failure map, and evaluation plan. |
| [M2](milestones/M2.md) | Implementation, plan changes, measured results, and failure analysis. |
| [Evaluation data](data/eval/README.md) | Frozen paper versions, provenance, licenses, and sampling limits. |
| [Saved runs](runs/README.md), [failure cases](data/failures) | Readable results, model/tool traces, and annotated decisions. |
| [Sources and licenses](THIRD_PARTY.md) | Attribution and dependency licenses. |
