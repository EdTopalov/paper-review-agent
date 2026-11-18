# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**pyagent_react · ok**

5 model calls · 3 reads · 11.32 s · $0.001961

5 decisions · 4 tool calls · 32471 input tokens (20955 cached) · 624 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

SWE-agent presents an LM-oriented agent-computer interface for repository-level software engineering and evaluates its effects on SWE-bench. Its focused interface design and ablations support the claim that interaction design can substantially affect agent performance, while the main results show useful but still limited issue-resolution rates.

- **strength**: The paper contributes a concrete interface design rationale, linking simpler actions, informative feedback, and guardrails to agent needs.
  - Page 3 · citation: exact
  - Quote: "Environment feedback should be informative."

- **strength**: The empirical case includes a full test-set result and a comparison against an interactive shell-only baseline on the Lite subset.
  - Page 6 · citation: exact
  - Quote: "w/ GPT-4 Turbo 12.47 1.59 18.00 1.67"

- **limitation**: The reported model evidence is limited to two leading language models; transfer to other model families remains uncertain.
  - Page 5 · citation: exact
  - Quote: "All results, ablations, and analysis are based on two leading LMs"

- **uncertainty**: The authors report that agents often fail to recognize dead ends, a behavioral weakness that may constrain improvements beyond interface changes.
  - Page 8 · citation: whitespace
  - Quote: "they rarely recognize dead ends or reset their problem solving approach."

Unresolved questions:

- How well do these interface choices transfer to a broader range of language models and repositories?
- Would the observed performance and failure patterns persist under different budgets or evaluation sets?
- I inspected pages 1–10, not pages 11–25; details and caveats in the uninspected remainder, including appendices, may qualify this assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the interface design and evaluation setup. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect benchmark results and interface ablations. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 5, "end": 7}` | Check quantitative results, ablations, and stated evaluation caveats. | read pages [5, 6, 7] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Submit an evidence-based assessment from inspected design, setup, and results pages. | review accepted | [event 25](trace.jsonl#L25) |
