# Version 2: Paper Review Agent on PyAgent

Variant ID: **`pyagent_react`**. The original M2 version remains available as
**`agent`**; **`baseline`** is the separate full-paper, one-call comparison.
This variant uses [PyAgent from pyagent.org](https://pyagent.org/), specifically
`pyagent-patterns==0.3.0` from
[pyagent-core/pyagent](https://github.com/pyagent-core/pyagent).

## Why a second version

In M2, the custom loop in `runner.py` exposes tools through native function
calling. Here, the ready-made `ReAct` loop manages conversation history, executes
the selected tool, and returns its observation to the model. The project adapter
retains JSON validation, reading limits, citation checks, tracing, and accounting
for actual API requests.

The experiment jointly changes the execution engine and action serialization:
PyAgent parses `Action: tool_name(<JSON>)` text, whereas M2 uses API tool schemas.
The model, assessment rubric, evidence tools, and acceptance rules stay the same,
so measured differences reflect the harness and protocol together.

## Hypothesis

**Prediction.** Replacing M2's custom loop with PyAgent ReAct will preserve the
number of completed reviews with verified, observed citations without increasing
mean API cost per paper, when the model and execution limits are held constant.

**Rationale.** Both variants start from the same first page and let the model
choose among the same three evidence tools. Citation acceptance is enforced by
the same project code. Moving the reading loop to PyAgent should therefore
preserve the evidence contract. This tests whether a reusable harness can support
the existing reviewer without a quality or cost regression; it does not assume
that changing the harness improves the model's understanding of a paper.

**Main risk.** Text actions lack the API-level format constraints of native
function calling. Malformed JSON, missing actions, or incorrect tool names may
consume decision steps and increase cost. The adapter also has to preserve page
identity and observed evidence across multiple tool calls.

**Cases and expected trace evidence.** Multi-page reads and citation repairs are
the main stress cases. After a rejected citation, a successful recovery should
show a source read or a corrected quotation/page followed by an accepted
submission. After an empty search or invalid page range, the next action should
use a revised query or valid range. A repeated unchanged submission until budget
exhaustion would count against the hypothesis. The M2
[F05 trace](../../data/failures/F05.json) is a concrete example to inspect; the
port does not introduce a new repair strategy and may reproduce that failure.
Accepted submissions should stop without an extra model request.

**Comparison.** Run `agent` and `pyagent_react` on the same frozen papers with the
same model, rubric, initial context, reading and decision budgets, output-token
limit, timeout, and retry policy. Use `baseline` as the full-paper reference.
Compare verified-review completion, action-format errors, rejected submissions,
budget exhaustion, model calls, input/output tokens, mean USD, and latency.
Include failed attempts in cost averages. Repeated runs reveal whether observed
differences exceed variation within a variant.

**Decision rule.** The hypothesis is supported if PyAgent completes at least as
many reviews with verified, observed citations as M2 and its mean cost is no
higher. A lower completion count or higher mean cost fails this criterion, even
if another metric improves. Report latency and recovery behavior alongside this
decision. Citation verification measures text fidelity; claim support requires
separate inspection or evidence auditing.

## How one task runs

1. The shared command loads a PDF or JSON snapshot through `Paper.load()`.
2. It creates task-local state containing the paper, observed excerpts, counters,
   and an accepted-review field. State is not shared between papers.
3. The model receives the same assessment rubric, metadata, and first page as M2.
4. PyAgent requests one action. The adapter uses the existing Responses API and
   `ModelCalls`; model, timeout, retries, and output-token limit are shared with M2.
5. The tool wrapper parses the argument string as JSON and validates it against
   the shared schema. Invalid arguments and reading errors become observations.
6. Searches and page reads add excerpts shown to the model to the evidence ledger.
7. `submit_review` validates the format, score, quotations on the cited pages, and
   whether those quotations appeared in observed excerpts. Errors are returned to
   the model; a valid submission is stored in `accepted_review`.
8. After acceptance, the adapter stops PyAgent before another API request. A
   submission accepted on the final step is also retained.
9. The shared runner writes `run_end` and generates a readable `README.md`.

PyAgent executes its actual ReAct loop. The completion adapter does not copy the
library loop, fabricate model responses, or request confirmation of an already
accepted review. The library's generic instruction to produce an extended
`Thought` is replaced with the shared rubric and a concise action protocol; each
action's purpose is supplied in `reason`.

## Tools and limits

| Tool | Behavior |
|---|---|
| `search_paper` | Literal keyword/phrase search within the current paper, without web search. |
| `read_pages` | Read one to three consecutive pages, preserving each page's number. |
| `submit_review` | Submit and validate a review; invalid citations require correction. |

Example text action:

```text
Action: read_pages({"start": 2, "end": 3, "reason": "Inspect the experimental setup"})
```

Default settings allow five reading actions and eight model decisions
(`max_reads + 3`). Empty searches and invalid page ranges consume a reading
action, as in M2. Once the reading budget is exhausted, code blocks further reads
and the instructions expose only review submission. API retry attempts are
counted separately from decisions.

A returned `PyAgent.Result`, `FINISH` text, or an exhausted step budget **does not
mean success without an accepted review**. The library's internal completion
marker is not an alternative to `submit_review`. If no review has been accepted,
the run saves an error diagnostic. Invalid citations are not accepted to increase
the completion rate.

The review format is shared: a score in [0, 1], a summary, two to four observations
with claim/page/quote fields, and unresolved questions. Images and original PDF
layout are not inspected. A verified citation establishes a text match, not that
the text supports the claim.

## Installation and execution

From the repository root, with a Python 3.12 environment activated:

```shell
python -m pip install -r requirements-m3.txt
python -m pip install --no-deps -e .
```

As in M2, `.env` contains `OPENAI_API_KEY` and optionally `OPENAI_MODEL`. Use the
same explicit model for all variants in a comparison.

```shell
# Verify frozen inputs without API calls
paper-review verify

# Development fixture; API calls incur costs
paper-review review data/dev/toy.json --variant pyagent_react --out runs/scratch/v2-dev

# One paper from the frozen sample
paper-review review data/eval/papers/T01.json --task-id T01 --variant pyagent_react --out runs/scratch/v2-T01

# M2 through the same entry point
paper-review review data/eval/papers/T01.json --task-id T01 --variant agent --out runs/scratch/v1-T01

# Compare all three methods on the same 20 papers: 60 runs with repeats=1
paper-review eval --variants agent pyagent_react baseline --workers 3 --out runs/m3-pyagent-comparison

# Check traces and rebuild reports without API calls
paper-review check runs/m3-pyagent-comparison
paper-review summarize runs/m3-pyagent-comparison
python -m pytest -q
```

Use a fresh output directory for each new `review` run. Set repetitions with
`eval --repeats N`. The existing `--variant both` retains its meaning of
`agent + baseline`; use `--variants` to compare all three methods.

## Outputs and reproducibility

Each task produces `README.md` and `trace.jsonl`. An experiment also produces a
combined `README.md`, `experiment.json`, and `source.zip`; task results are stored
under `<variant>-r<repeat>/<task-id>/`. A successful single-paper run prints:

```json
{"status": "ok", "report": "runs/scratch/v2-dev/README.md"}
```

Every new event contains `task_id` and `variant`. Restore full requests with
`paper_review.trace.read_events()`. Metadata records the PyAgent version, variant
protocol, configuration, and input/source hashes. Accounting uses API usage,
including retries, rather than PyAgent's character-based token estimates.

The main metrics are completion, verification of all citations, first submissions,
rejected submissions, steps, tool/API calls, tokens, USD, and latency per task.
Mean costs include failed attempts. If evidence auditing is used, retain the M2
judge model and rubric, and separately report agreement with manual labels.
Audits incur additional API costs.

Experiment reports contain the per-task results and aggregate measurements for
the selected variants. The shared [comparison index](../../milestones/M3.md)
links variant documentation; this README owns the hypothesis and design details
for `pyagent_react`.

## Sources

- [PyAgent ReAct](https://github.com/pyagent-core/pyagent/blob/main/packages/pyagent-patterns/src/pyagent_patterns/advanced/react.py), MIT.
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629).
- [Project licenses](../../THIRD_PARTY.md).
