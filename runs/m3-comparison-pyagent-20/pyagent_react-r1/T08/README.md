# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**pyagent_react · ok**

5 model calls · 2 reads · 25.50 s · $0.002385

5 decisions · 4 tool calls · 18270 input tokens (7174 cached) · 1854 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

τ-bench introduces a benchmark for evaluating language agents in multi-turn user interaction with API tools and domain policies. Its task-level database-state comparison and pass^k reliability metric address capabilities that single-step tool-use evaluations do not directly capture. The reported results show substantial difficulty for tested agents, while the benchmark’s simulated users, narrow initial domain coverage, and imperfect correspondence between state-based reward and policy compliance limit the conclusions that can be drawn.

- **strength**: The benchmark combines simulated user interaction, API use, and domain policy following; the authors position this as a contrast with existing single-step tool benchmarks.
  - Page 3 · citation: whitespace
  - Quote: "In contrast, our benchmark focuses on a more realistic setting where the agent has to interact with human users to gather information and authorization."

- **strength**: The paper defines pass^k to assess the probability of consistently succeeding across repeated trials, and reports low success for tested agents.
  - Page 2 · citation: whitespace
  - Quote: "With increasing k, the chance of consistently solving a task drops rapidly, to as low as ∼25% for pass^8 on τ-retail for the same model."

- **limitation**: The stated initial application scope is customer service, with two domains; how well the benchmark transfers to other settings remains open.
  - Page 2 · citation: whitespace
  - Quote: "As a first demonstration, we focus on the realm of customer service and create two different domains where agents need to assist simulated users with diverse requests (τ -retail and τ -airline)."

- **limitation**: The authors acknowledge that the automated state-based reward can miss policy violations, so a successful score is not sufficient evidence of compliant behavior.
  - Page 4 · citation: whitespace
  - Quote: "Note that r = 1 might be a necessary but not sufficient condition for a successful episode e.g., the agent might issue the return without explicit user confirmation, which violates the policy."

Unresolved questions:

- How well do the language-model user simulations represent real users, and do benchmark rankings hold with human users?
- How robust are the reported findings outside the two customer-service domains and the evaluated agent/model configurations?
- What is the practical rate of policy violations that leave the final database in the annotated state, given the stated limitation of the reward?
- I inspected the opening pages and selected benchmark-description and appendix pages, not the full methods, experiments, or limitations discussion; those aspects remain unassessed here.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages invalid arguments: `{"start":2,"end":4,"reason":"Inspect benchmark design and evaluation setup."})Action: read_pages({"start":2,"end":4,"reason":"Inspect benchmark design and evaluation setup."}` |  | invalid_arguments | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design and evaluation setup. | read pages [2, 3, 4] | [event 14](trace.jsonl#L14) |
| 4 | read_pages `{"start": 11, "end": 13}` | Inspect main results and reported failure analysis. | read pages [11, 12, 13] | [event 19](trace.jsonl#L19) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit assessment grounded in the inspected benchmark description and construction pages. | review accepted | [event 25](trace.jsonl#L25) |
