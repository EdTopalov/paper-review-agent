# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**pyagent_react · ok**

6 model calls · 4 reads · 17.36 s · $0.001915

6 decisions · 5 tool calls · 38215 input tokens (28330 cached) · 793 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

τ-bench contributes a modular benchmark for evaluating tool-using agents in multi-turn, simulated customer-service conversations, where agents must both follow domain policies and reach annotated database outcomes. Its repeated-trial pass^k metric makes consistency visible alongside average task success. Results across two domains and multiple models show substantial difficulty, while the paper also identifies meaningful limits in simulator fidelity, task curation, and rule-based evaluation.

- **strength**: The benchmark combines user interaction, API use, domain policies, and state-based evaluation in a concrete task setup.
  - Page 3 · citation: whitespace
  - Quote: "The agent interacts with both (1) databases (db) via API tools, and (2) a (simulated) user (user) to complete a task"

- **strength**: The multi-model experiments establish that the benchmark challenges the tested baselines, and repeated trials reveal reliability beyond single-run success.
  - Page 7 · citation: whitespace
  - Quote: "Even for the best-performing gpt-4o function calling agent which has a > 60% average task success, pass^8 drops to < 25%."

- **limitation**: The paper acknowledges that its objective reward can miss policy violations, so database-state success does not fully establish correct interaction.
  - Page 4 · citation: whitespace
  - Quote: "r = 1 might be a necessary but not sufficient condition for a successful episode e.g., the agent might issue the return without explicit user confirmation, which violates the policy."

- **limitation**: The authors identify simulator weaknesses and possible curation bias, which qualify how confidently results transfer to real user interactions.
  - Page 9 · citation: whitespace
  - Quote: "There is also some element of implicit bias during the task curation process since we use the gpt-4-turbo FC agent to tune the user’s system prompt."

Unresolved questions:

- How well do the findings generalize beyond the two simplified customer-service domains to other real-world settings and user populations?
- How much would benchmark rankings or measured reliability change with real human users or independent assessments of policy compliance?
- I inspected the benchmark description, selected construction and results pages, and the stated limitations; I did not inspect the full appendices, complete task set, or all reported trajectories.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the benchmark design and task construction. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 9, "end": 11}` | Inspect experimental results and benchmark evaluation. | read pages [9, 10, 11] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 5, "end": 8}` | Review reported agent results and evaluation details. | invalid_page_range | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 5, "end": 7}` | Inspect reported agent results and evaluation details. | read pages [5, 6, 7] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Submit an evidence-grounded assessment using inspected benchmark, results, and limitations pages. | review accepted | [event 30](trace.jsonl#L30) |
