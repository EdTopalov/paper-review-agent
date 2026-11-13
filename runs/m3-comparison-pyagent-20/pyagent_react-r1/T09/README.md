# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**pyagent_react · ok**

4 model calls · 2 reads · 12.55 s · $0.002092

4 decisions · 4 tool calls · 17625 input tokens (5200 cached) · 975 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AGENTLESS proposes a transparent, non-agentic pipeline that hierarchically localizes code and then generates and filters repair patches. Its benchmark results and component analysis make a useful case that a relatively simple workflow can perform competitively. The paper also identifies problems in SWE-bench Lite and evaluates a filtered subset, though that subset and the reported comparisons leave questions about evaluation scope.

- **strength**: The paper reports competitive performance and low cost on SWE-bench Lite, and its component comparisons provide useful evidence about how sampling, voting, and test filtering contribute.
  - Page 1 · citation: exact
  - Quote: "27.33%) and lowest cost ($0.34)"

- **strength**: The repair ablation shows gains from multiple samples and majority voting, followed by a further improvement from test filtering.
  - Page 8 · citation: exact
  - Quote: "+ test filtering\n(full AGENTLESS) 82 (27.33%) $0.34"

- **limitation**: The authors’ own classification identifies potentially consequential benchmark issues, including insufficient information and exact or misleading proposed solutions; these complicate interpreting raw solve rates as capability.
  - Page 9 · citation: whitespace
  - Quote: "there is a non-trivial percentage (9.3%) of problems which do not contain enough information."

- **uncertainty**: The filtered comparison excludes commercial tools because the authors could not run them on the modified benchmark, so their performance on SWE-bench Lite-S is not directly measured here.
  - Page 10 · citation: whitespace
  - Quote: "we are not able to run commercial tools ourselves on the modified problems"

Unresolved questions:

- How robust are the reported results across model versions, sampling choices, and repositories beyond the evaluated benchmark?
- How would commercial systems perform on SWE-bench Lite-S under a controlled evaluation?
- I inspected the abstract, method pages 3–5, and evaluation pages 8–10; other parts of the paper, including any further experimental details or limitations, were not inspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages invalid arguments: `{"start": 3, "end": 5, "reason": "Inspect the method and benchmark results."})Action: read_pages({"start":3,"end":5,"reason":"Inspect the method and benchmark results."})Action: se` |  | invalid_arguments | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect the method and benchmark results. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect benchmark comparisons and evaluation details. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit an evidence-based assessment using the inspected method and evaluation pages. | review accepted | [event 21](trace.jsonl#L21) |
