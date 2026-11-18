# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**baseline · ok**

1 model calls · 0 reads · 5.11 s · $0.000572

1 decisions · 0 tool calls · 36934 input tokens (36931 cached) · 405 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

τ-bench contributes a modular benchmark for evaluating language agents in multi-turn interactions with simulated users, API tools, and domain policies. Its state-based task scoring and pass^k metric target both task completion and consistency; experiments across two customer-service domains show substantial failures among tested agents and provide a structured failure analysis. The work is useful and well-motivated, though its evidence is bounded by synthetic domains, LM-based simulation, and a small task set.

- **strength**: The benchmark combines user interaction, tool use, policy adherence, and end-state evaluation in a coherent setup.
  - Page 2 · citation: whitespace
  - Quote: "Our evaluation scheme compares the database state at the end of each episode with the ground truth expected state."

- **strength**: The reliability metric is tailored to repeated performance on the same task, complementing average success.
  - Page 5 · citation: exact
  - Quote: "pass^k = Etask"

- **limitation**: The initial empirical scope is deliberately narrow: two customer-service domains, with a modest number of annotated tasks.
  - Page 5 · citation: exact
  - Quote: "Tasks 115 50"

- **uncertainty**: Reported success may depend on the behavior and capabilities of the user simulator; the paper recognizes this as a limitation, but the inspected results do not establish how well benchmark rankings generalize to real users.
  - Page 9 · citation: normalized
  - Quote: "the user simulation LM might have limited capacity at reasoning, calculation, long-context memorization, or alignment with the instruction prompt"

Unresolved questions:

- How stable are model comparisons when the user simulator model, prompting, and sampling settings change?
- Do agent rankings and failure patterns generalize to additional domains or interactions with human users?
- How often does database-state success disagree with broader judgments of policy compliance or user satisfaction?
- The inspected pages do not include supplemental materials beyond the supplied excerpt; additional experimental details and analyses may affect assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
