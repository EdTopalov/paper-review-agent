# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**pyagent_react · ok**

3 model calls · 2 reads · 18.88 s · $0.001834

3 decisions · 3 tool calls · 17905 input tokens (9806 cached) · 1448 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

SWE-agent makes the case that language-model agents benefit from computer interfaces designed for their needs. It presents repository search, navigation, editing, and informative feedback as a coherent agent-computer interface, and reports improved SWE-bench performance. The inspected pages support the design rationale and reported headline claims, but do not include the detailed results tables or evaluation protocol, so the strength and scope of the empirical evidence remain uncertain.

- **strength**: The paper reports a sizable gain over its Linux-shell baseline in an ablation on a subset of the benchmark, though the underlying table was not inspected.
  - Page 2 · citation: whitespace
  - Quote: "SWE-agent solves 10.7 percentage points more issues than the baseline agent that uses just the default Linux shell."

- **strength**: The interface design is grounded in a clear set of principles, including informative feedback and guardrails against error propagation.
  - Page 3 · citation: exact
  - Quote: "Guardrails mitigate error propagation."

- **uncertainty**: The paper reports an ablation on 300 test issues, but the inspected pages do not establish how representative that subset is or show the ablation results.
  - Page 2 · citation: exact
  - Quote: "We perform an ablation study on a subset of 300 SWE-bench test issues"

Unresolved questions:

- How do the detailed benchmark and ablation results compare across repositories, issue types, and interface components?
- How robust are the reported results to model choice, prompting, and repeated evaluation?
- Pages 5–9, including the detailed experimental results and protocol, were not inspected; the assessment therefore relies on the abstract and inspected pages 2–4, and is provisional.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the interface design and experimental methodology. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 10, "end": 12}` | Inspect benchmark results and ablation evidence. | read pages [10, 11, 12] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.68, "observations": 3}}` | Submit an evidence-based provisional review; detailed results pages were not inspected. | review accepted | [event 16](trace.jsonl#L16) |
