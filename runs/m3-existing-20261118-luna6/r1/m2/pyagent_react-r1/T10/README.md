# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**pyagent_react · ok**

8 model calls · 4 reads · 18.87 s · $0.002548

8 decisions · 5 tool calls · 55598 input tokens (42348 cached) · 938 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

SWE-agent makes a substantial, practical contribution by showing that an interface tailored to language-model agents can improve repository-level software issue resolution without changing the underlying model. The paper supports this claim with full-benchmark results and component ablations, while its behavior analysis also identifies a meaningful failure pattern. The contribution is chiefly empirical and system-design focused; the evidence inspected does not establish how broadly the findings transfer beyond the evaluated models and SWE-bench settings.

- **strength**: The paper reports strong issue-resolution results on the full SWE-bench test set and transfer to a second language model.
  - Page 6 · citation: exact
  - Quote: "w/ GPT-4 Turbo 12.47 1.59"

- **strength**: The component ablations provide evidence that interface choices, including linting and file-viewer size, affect benchmark performance.
  - Page 7 · citation: exact
  - Quote: "This intervention improves performance considerably (Without Linting, 15.0% ↓ 3.0)."

- **limitation**: The authors identify a notable behavior-level weakness: agents often persist with editing and fail to change course when stuck.
  - Page 8 · citation: whitespace
  - Quote: "agents rarely deviate from this pattern but they rarely recognize dead ends or reset their problem solving approach."

- **uncertainty**: The inspected benchmark evidence is centered on SWE-bench and SWE-bench Lite; how well the reported interface gains generalize to other software-engineering tasks remains unresolved.
  - Page 6 · citation: exact
  - Quote: "Main results for SWE-agent performance on the full and Lite splits of the SWE-bench"

Unresolved questions:

- Do the ACI gains persist across a broader range of language models, repository types, and software-engineering benchmarks?
- Can the observed tendency to repeat editing patterns and miss dead ends be reduced without sacrificing the interface's performance gains?
- I inspected pages 1–8 and 10–12 only; the remainder of the paper, including any further discussion of limitations or evaluation details, was not inspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the proposed interface and experimental setup. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 15](trace.jsonl#L15) |
| 4 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 19](trace.jsonl#L19) |
| 5 | read_pages `{"start": 10, "end": 12}` | Inspect benchmark results and ablation evidence. | read pages [10, 11, 12] | [event 23](trace.jsonl#L23) |
| 6 | search_paper `{"query": "10.7"}` | Locate quantitative ablation results in the paper. | 1 matches on pages [2] | [event 28](trace.jsonl#L28) |
| 7 | read_pages `{"start": 6, "end": 8}` | Review main benchmark and component ablation results. | read pages [6, 7, 8] | [event 33](trace.jsonl#L33) |
| 8 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Submit an evidence-based assessment using the observed benchmark, ablation, and behavior analysis pages. | review accepted | [event 38](trace.jsonl#L38) |
