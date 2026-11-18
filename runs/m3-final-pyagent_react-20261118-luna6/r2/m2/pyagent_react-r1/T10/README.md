# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**pyagent_react · ok**

5 model calls · 2 reads · 21.31 s · $0.002099

5 decisions · 4 tool calls · 33006 input tokens (24922 cached) · 1679 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

SWE-agent presents an LM-tailored agent-computer interface for repository-level software engineering and reports improved issue resolution on SWE-bench. Its contribution combines concrete tool design with benchmark evaluation and analysis of interface choices; the evidence supports a substantial, task-specific advance, while the inspected material leaves questions about generality and the breadth of component-level evidence.

- **strength**: The paper reports a benchmark result and comparison against a shell-based agent and a retrieval-augmented baseline, supporting the practical relevance of the interface design.
  - Page 2 · citation: whitespace
  - Quote: "When using GPT-4 Turbo as the base LLM, SWE-agent solves 12.5% of the 2,294 SWE-bench test issues"

- **strength**: The design is articulated as actionable principles, including simple actions, informative feedback, and guardrails, rather than only a system description.
  - Page 3 · citation: exact
  - Quote: "Guardrails mitigate error propagation."

- **limitation**: The trajectory analysis identifies a behavioral weakness: the agent often repeats a strategy without recognizing a dead end.
  - Page 8 · citation: whitespace
  - Quote: "agents rarely deviate from this pattern but they rarely recognize dead ends or reset their problem solving approach."

- **uncertainty**: The paper describes a diverse benchmark, but the inspected evidence does not establish transfer beyond that benchmark and repository setting.
  - Page 9 · citation: whitespace
  - Quote: "SWE-bench task instances are diverse, having been collected from real GitHub issues across 12 different repositories."

Unresolved questions:

- How robust are the gains across models, task distributions, and repositories beyond the evaluations described in the inspected pages?
- Which ACI components account for the largest gains, and how sensitive are results to development-set configuration choices?
- How often do dead-end trajectories lead to incorrect patches, and can the interface or agent detect and recover from them?
- Important inspection gap: I reviewed pages 1–4 and 8–10, not the detailed experimental tables and full methodology on intervening pages; component-level results and evaluation controls remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the interface design and benchmark evaluation. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect benchmark results, ablations, and evaluation scope. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit a review grounded in the inspected abstract, design, and analysis pages. | citation_validation_failed; #1: not_found | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the unmatched benchmark citation using the observed page 2 wording. | review accepted | [event 25](trace.jsonl#L25) |
