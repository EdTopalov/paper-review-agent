# T11: Executable Code Actions Elicit Better LLM Agents

**pyagent_react · ok**

4 model calls · 3 reads · 12.73 s · $0.001841

4 decisions · 4 tool calls · 33491 input tokens (23506 cached) · 716 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

The paper proposes CodeAct, using executable Python as a unified action interface for LLM agents, and provides benchmark comparisons plus an instruction-tuned agent and dataset. Results are promising, especially for complex multi-tool interactions, but the evidence is bounded by a small, curated benchmark and the authors characterize the trained agent as an early prototype.

- **strength**: On the curated multi-tool benchmark, CodeAct is reported to improve success and reduce interaction turns for most evaluated models.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs)"

- **strength**: The evaluation covers a broad set of 17 models and compares CodeAct against JSON and text action formats, making the central interface claim directly testable in the reported setup.
  - Page 5 · citation: whitespace
  - Quote: "We measure the success rate by calculating the percentage of the model proposed answers that match the ground-truth solutions."

- **limitation**: The complex-task benchmark is modest in size and relies on human-curated instances, limiting how broadly its results establish generality.
  - Page 5 · citation: exact
  - Quote: "It contains 82 human-curated instances"

- **limitation**: The authors identify practical limitations in the trained agent, including hallucinations; this is a stated scope caveat rather than evidence that the interface comparison itself fails.
  - Page 10 · citation: exact
  - Quote: "CodeActAgent is an initial prototype of an autonomous agent and still has several practical limitations."

Unresolved questions:

- How robust are the benchmark findings on larger, independently constructed tasks and beyond the tested toolsets?
- How do CodeAct agents perform under stronger safety constraints and on consequential real-world tasks?
- I inspected the abstract, pages 4–6, and pages 9–10, but not the full appendices or all experimental details; further uncertainty remains about implementation and evaluation particulars.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 4, "end": 6}` | Inspect the proposed interaction method and benchmark evidence. | read pages [4, 5, 6] (text truncated by tool) | [event 6](trace.jsonl#L6) |
| 2 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope boundaries and caveats. | 3 matches on pages [10] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 9, "end": 10}` | Inspect training-data and limitations discussion for important qualifications. | read pages [9, 10] | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit a balanced assessment based on observed benchmark results, evaluation scope, and stated limitations. | review accepted | [event 21](trace.jsonl#L21) |
