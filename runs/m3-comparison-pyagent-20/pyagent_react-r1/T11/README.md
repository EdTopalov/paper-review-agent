# T11: Executable Code Actions Elicit Better LLM Agents

**pyagent_react · ok**

5 model calls · 2 reads · 15.05 s · $0.002655

5 decisions · 4 tool calls · 24435 input tokens (7317 cached) · 884 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

The paper proposes CodeAct, using executable Python as an LLM agent’s action format, and supports it with comparisons across 17 models on atomic API calls and a curated multi-tool benchmark. It also presents an instruction-tuning dataset and agent. The central evidence is promising, especially for complex tool composition, but the benchmark is small and manually constructed; I inspected only pages 1–7, not the later dataset-training results or appendices.

- **strength**: The multi-tool benchmark reports a meaningful advantage for CodeAct on many tested models, including fewer interaction turns; the comparison covers multiple action formats.
  - Page 5 · citation: whitespace
  - Quote: "CodeAct generally has a higher task success rate (12 out of 17 evaluated LLMs), similar to the trend in §2.2."

- **strength**: The framework’s proposed advantage is concrete: executable code can combine operations and use program control flow rather than requiring separate predefined actions.
  - Page 2 · citation: whitespace
  - Quote: "code inherently supports control and data flow, allowing for the storage of intermediate results as variables for reuse and the composition of multiple tools"

- **limitation**: The complex-task evaluation has limited scale and uses manually created task instances and tools, which narrows what can be concluded about performance in broader environments.
  - Page 5 · citation: exact
  - Quote: "It contains 82 human-curated instances"

- **uncertainty**: The inspected pages do not establish whether the reported benchmark gains generalize to other task distributions or tool implementations; the later evaluation details were not inspected.
  - Page 5 · citation: whitespace
  - Quote: "Each domain is accompanied by a unique set of manually crafted tools."

Unresolved questions:

- How robust are the results across independently developed benchmarks, larger task sets, and tools not tailored to each domain?
- Do the CodeActInstruct training results support the claims about improving agent tasks without reducing general capability? I did not inspect those results or the appendices.
- What execution safeguards and operational constraints are used when generated Python code can access packages or external resources?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages invalid arguments: `{"start": 2, "end": 4, "reason": "Inspect the proposed interaction design and benchmark evidence."})Action: read_pages({"start":2,"end":4,"reason":"Inspect the method and initial e` |  | invalid_arguments | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 4}` | Inspect the method and initial evaluation details. | read pages [2, 3, 4] | [event 14](trace.jsonl#L14) |
| 4 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark construction, evaluation procedure, and reported outcomes. | read pages [5, 6, 7] (text truncated by tool) | [event 19](trace.jsonl#L19) |
| 5 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit a balanced assessment based on the abstract and inspected pages 2–7, noting uninspected sections. | review accepted | [event 25](trace.jsonl#L25) |
