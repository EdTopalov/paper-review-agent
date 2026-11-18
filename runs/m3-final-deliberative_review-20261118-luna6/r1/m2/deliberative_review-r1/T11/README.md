# T11: Executable Code Actions Elicit Better LLM Agents

**deliberative_review · ok**

7 model calls · 3 reads · 32.37 s · $0.010938

7 decisions · 4 tool calls · 75914 input tokens (0 cached) · 2916 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes CodeAct, using executable Python as a flexible action format for LLM agents, and compares it with text and JSON actions. It also introduces a 7,139-trajectory instruction-tuning dataset and fine-tuned agents. Reported results show benefits in several tool-use settings, but outcomes vary across models and tasks.

- **strength**: Across 17 evaluated models, CodeAct has the highest success rate for a majority on the multi-turn benchmark. This supports its promise in the evaluated setting, not universal superiority.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)"

- **limitation**: The multi-tool benchmark is modest in size and curated by the authors, which limits how broadly its results alone can establish general performance.
  - Page 5 · citation: exact
  - Quote: "It contains 82 human-curated instances"

- **limitation**: The fine-tuning results are not uniform: the paper reports no M3ToolEval improvement for the LLaMA-2 variant. This is a specific difference, not evidence of general failure.
  - Page 9 · citation: whitespace
  - Quote: "Surprisingly, no improvement is observed for the Llama-2 variant."

- **uncertainty**: The paper identifies overlap between training domains and MINT evaluation and reports in- and out-of-domain results separately. Broader deployment performance is not established by the inspected excerpts.
  - Page 9 · citation: exact
  - Quote: "CodeActAgent has some training domains overlapping with MINT’s evaluation"

Unresolved questions:

- How robust are the action-format and fine-tuning gains on larger or independently constructed benchmarks and in settings beyond those evaluated?
- Which factors explain the different M3ToolEval outcomes for the LLaMA-2 and Mistral CodeActAgent variants?
- Only pages 1–9 were inspected, and pages 2, 3, and 6 were represented by partial extracts. The remaining 20 pages, including appendices and any further discussion of limitations, were not inspected; conclusions about them remain open.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the methods and benchmark setup to verify what CodeAct is compared against, which tasks and models are covered, and whether evaluation supports the claimed success-rate gains.; Check results, analyses, and any limitations or discussion pages for evidence behind the reported performance and claims about instruction tuning and retained general capability; distinguish reported results from untested claims.; Cover the paper’s full scope before assessing it: only page 1 is currently visible, so inspect relevant later pages for supporting evidence and caveats, then provide page-numbe … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 3, 5, 9] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [4, 5, 6] (text truncated by tool) | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [7, 8, 9] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | invalid_phase_output; invalid_ledger_finding; ValueError | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Retained the draft’s score and main assessment. The inspected evidence supports the benchmark and model-specific observations, but not conclusions about the uninspected pages; that coverage gap is stated explicitly. No unsupported criticism was added. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "success rate"}` | Locate reported experimental comparisons and quantitative support for the central performance claim. | 8 matches on pages [1, 2, 3, 5, 9] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 4, "end": 6}` | Inspect experimental methods and comparative results supporting CodeAct claims. | read pages [4, 5, 6] (text truncated by tool) | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 7, "end": 9}` | Inspect CodeActInstruct methods and reported tuning evaluations/caveats to assess claims and evidence. | read pages [7, 8, 9] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
