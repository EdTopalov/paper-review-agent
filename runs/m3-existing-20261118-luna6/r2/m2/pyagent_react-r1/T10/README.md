# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**pyagent_react · ok**

5 model calls · 4 reads · 13.28 s · $0.002197

5 decisions · 5 tool calls · 45176 input tokens (33506 cached) · 808 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

SWE-agent presents a tailored agent-computer interface for repository-level software engineering and shows that interface choices affect issue-resolution performance. Its SWE-bench results and Lite-split ablations provide meaningful empirical support, while conclusions are bounded by the evaluated models, benchmark, and development choices.

- **strength**: The paper reports a strong benchmark result and transfer to a second evaluated model, with the full-set result supported by automatic test-based resolution scoring.
  - Page 2 · citation: whitespace
  - Quote: "When using GPT-4 Turbo as the base LLM, SWE-agent solves 12.5% of the 2,294 SWE-bench test issues"

- **strength**: The Lite ablations show performance changes associated with interface components, including editing and linting, rather than relying only on the aggregate system comparison.
  - Page 7 · citation: exact
  - Quote: "This intervention improves performance considerably (Without Linting, 15.0% ↓ 3.0)."

- **limitation**: The authors say initial design decisions used a small set of hand-picked easier development examples, which limits how representative that design process is shown to be.
  - Page 5 · citation: whitespace
  - Quote: "qualitative analysis of system behavior on small set of hand-picked easier examples from the development split of SWE-bench."

- **uncertainty**: The reported model evidence centers on two large-context models; the paper does not establish how well the ACI transfers across a broader range of models in the inspected results.
  - Page 5 · citation: exact
  - Quote: "All results, ablations, and analysis are based on two leading LMs"

Unresolved questions:

- How robust are the ACI benefits across more models, repositories, and task types beyond the reported benchmark and two evaluated models?
- How sensitive are the comparisons to the selected prompts, budgets, and evaluation setup?
- I inspected pages 1–10 only, not the remainder of the paper or appendices; further methodological details and limitations there may affect this assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the interface design and experimental methods. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark results, comparison setup, and interface ablations. | read pages [5, 6, 7] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect agent behavior analysis and stated limitations or broader evaluation caveats. | read pages [8, 9, 10] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "budget constraints"}` | Check the paper's explicit evaluation constraints and caveats. | 1 matches on pages [5] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Submit an evidence-based assessment using inspected pages 1–10 and disclose uninspected material. | review accepted | [event 26](trace.jsonl#L26) |
