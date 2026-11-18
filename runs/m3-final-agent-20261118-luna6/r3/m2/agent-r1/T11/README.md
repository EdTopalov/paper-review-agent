# T11: Executable Code Actions Elicit Better LLM Agents

**agent · ok**

7 model calls · 4 reads · 20.03 s · $0.002494

7 decisions · 7 tool calls · 51042 input tokens (40057 cached) · 1484 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

The paper proposes CodeAct, using executable Python as a unified action format for LLM agents, and supports its case with comparisons across 17 models, a curated complex-tool benchmark, and an instruction-tuned agent. Its central insight is that code’s control/data flow and existing software ecosystem can make multi-tool tasks more composable and efficient. The evidence is promising; however, the inspected pages do not establish broad real-world generality or safety.

- **strength**: Code’s control and data flow offer a concrete mechanism for composing tools and reusing intermediate results in complex tasks.
  - Page 2 · citation: whitespace
  - Quote: "code inherently supports control and data flow, allowing for the storage of intermediate results as variables for reuse and the composition of multiple tools"

- **strength**: On the paper’s curated complex-tool evaluation, CodeAct reportedly improves success while reducing action count.
  - Page 3 · citation: whitespace
  - Quote: "CodeAct achieves up to a 20% absolute improvement over baselines on the success rate of solving the problems while requiring up to 30% fewer actions."

- **limitation**: The authors identify hallucinated assumptions about program state as a practical weakness of their agent prototype.
  - Page 10 · citation: whitespace
  - Quote: "it may suffer from hallucination commonly seen in LLMs (e.g., imagine the content of a variable without actually printing it out)"

- **uncertainty**: The inspected pages do not establish how broadly the benchmark gains transfer beyond curated tasks; full benchmark construction and results tables were not inspected.
  - Page 3 · citation: whitespace
  - Quote: "Problems in this benchmark often require intricate coordination and composition of multiple tools."

Unresolved questions:

- How representative and reproducible are the curated M3ToolEval tasks and their reported gains?
- How robust is CodeAct under execution limits, unsafe or malicious code, and diverse real-world environments?
- What are the complete results and evaluation details for CodeActInstruct and CodeActAgent?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "20%"}` | Locate quantitative evaluation claims and their context. | 2 matches on pages [1, 3] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark setup, comparative results, and framing of the main contribution. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 10, "end": 12}` | Check finetuning evaluation and stated limitations or constraints. | read pages [10, 11, 12] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Evidence covers the framework, core comparative results, and explicit limitations; submit an independent assessment while noting evaluation details not inspected. | citation_validation_failed; #4: wrong_page (pages [4]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Correct the benchmark-coverage citation to an exact observed quote on page 3 and submit the assessment. | citation_validation_failed; #4: wrong_page (pages [4]) | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 3, "end": 3}` | Verify exact benchmark phrasing and page placement for the unresolved evaluation-scope observation. | read pages [3] | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Use the exact inspected page-3 sentence for the benchmark scope caveat and finalize review. | review accepted | [event 35](trace.jsonl#L35) |
