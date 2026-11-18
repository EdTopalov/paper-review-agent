# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**baseline · ok**

1 model calls · 0 reads · 7.76 s · $0.000564

1 decisions · 0 tool calls · 23863 input tokens (23860 cached) · 650 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

SWE-agent argues that language-model agents benefit from interfaces designed for their interaction patterns, and presents a system for resolving repository-level software issues. Its custom search, file-viewing, editing, and feedback tools improve performance over a shell-only agent on the reported SWE-bench Lite ablations; the system also reports results on the full benchmark and with a second model. The paper combines a practical system contribution with an empirical investigation of interface design.

- **strength**: The paper provides a substantial benchmark evaluation and reports transfer of the interface across two language models.
  - Page 6 · citation: exact
  - Quote: "SWE-agent\nw/ GPT-4 Turbo 12.47 1.59 18.00 1.67\nw/ Claude 3 Opus 10.46 2.59 13.00 2.18"

- **strength**: The Lite ablations support the central claim that interface choices matter, including the value of summarized search and linting.
  - Page 6 · citation: exact
  - Quote: "Summarized\n 18.0\nIterative 12.0 ↓ 6.0"

- **limitation**: The interface ablations are reported on a subset rather than the full benchmark, so their measured effects may not generalize to all tasks.
  - Page 2 · citation: exact
  - Quote: "We perform an ablation study on a subset of 300 SWE-bench test issues"

- **uncertainty**: The evaluation scope is bounded to a particular benchmark and a small set of models; broader applicability to other languages, repositories, or model families remains unclear.
  - Page 5 · citation: whitespace
  - Quote: "We evaluate on the SWE-bench dataset, which includes 2,294 task instances from 12 different repositories of popular Python packages"

Unresolved questions:

- Would the interface advantages persist across a wider range of models, programming languages, and repository types?
- How robust are the ablation results to task selection and run-to-run variation on the 300-instance subset?
- Which interface components provide the most benefit when combined, and do their effects interact?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
