# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**baseline · ok**

1 model calls · 0 reads · 8.29 s · $0.000711

1 decisions · 0 tool calls · 36934 input tokens (36931 cached) · 683 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

τ-bench introduces a modular benchmark for evaluating language agents in multi-turn interactions with simulated users, API tools, and domain policies. It uses annotated database outcomes to score task completion and proposes pass^k to measure consistency across repeated trials. Results across retail and airline tasks show substantial failures in the tested agents, while the paper also discusses limitations of its simulator and task-curation process.

- **strength**: The benchmark’s combination of user interaction, policy constraints, tools, and final-state evaluation is a substantive contribution, and pass^k makes repeated-trial reliability measurable.
  - Page 4 · citation: whitespace
  - Quote: "the final database is identical to the unique ground truth outcome database"

- **limitation**: The paper itself identifies meaningful limitations in simulated-user fidelity and task curation, including possible bias from tuning prompts against one agent.
  - Page 9 · citation: not_found
  - Quote: "there is also some element of implicit bias during the task curation process since we use the gpt-4-turbo FC agent to tune the user’s system prompt."

- **uncertainty**: The reported retail success rate is inconsistent within the paper: the table gives 61.2%, while the failure-analysis text reports a 65.2% pass^1 rate for 115 tasks. The supplied pages do not explain the discrepancy.
  - Page 7 · citation: whitespace
  - Quote: "out of which 40 tasks have failed (pass^1=65.2%)."

Unresolved questions:

- How well do results transfer to real users, production systems, and domains beyond the two customer-service settings tested?
- How sensitive are pass^k estimates and agent rankings to the choice and behavior of the user-simulation model?
- What accounts for the differing τ-retail pass^1 figures reported on page 7?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
