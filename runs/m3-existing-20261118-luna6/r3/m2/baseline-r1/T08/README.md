# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**baseline · ok**

1 model calls · 0 reads · 6.73 s · $0.000626

1 decisions · 0 tool calls · 36934 input tokens (36931 cached) · 512 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

τ-bench contributes a practical benchmark for evaluating tool-using agents in multi-turn interactions with simulated users, domain policies, and database APIs. Its state-based task scoring and pass^k reliability metric expose shortcomings in task success, policy adherence, and consistency across two customer-service domains. The evidence is informative but bounded by the small, manually curated task sets, synthetic user simulation, and evaluation criteria that do not fully capture rule compliance.

- **strength**: The benchmark combines user interaction, API actions, and domain policy constraints, addressing a specific limitation in prior agent evaluations.
  - Page 2 · citation: whitespace
  - Quote: "τ-bench aims to unify both under realistic settings, while also testing how well agents can follow domain-specific policies in a consistent manner."

- **strength**: Database-state evaluation enables objective scoring despite variation in dialogue, and pass^k directly measures repeated-trial reliability.
  - Page 4 · citation: whitespace
  - Quote: "the agent is successful if the only database write action is return_delivered_order_items(order_id=\"#W2890441\","

- **limitation**: The authors explicitly bound current coverage to two customer-service domains and acknowledge that broader, more complex domains remain future work.
  - Page 5 · citation: whitespace
  - Quote: "For more capable agents in the future, more advanced domains (e.g., medical, tax, or legal) with more complex data and rules can be studied."

- **uncertainty**: The automatic reward may not fully assess policy compliance: the authors note that a successful score need not imply compliant behavior, and propose additional checks as future work.
  - Page 4 · citation: whitespace
  - Quote: "r = 1 might be a necessary but not sufficient condition for a successful episode e.g., the agent might issue the return without explicit user confirmation, which violates the policy."

Unresolved questions:

- How well do the benchmark’s simulated-user behaviors and task outcomes correspond to interactions with real users? The paper acknowledges simulator limitations, but the inspected pages provide no real-user validation.
- How stable are the reported model comparisons across additional tasks and repeated evaluations? Although the paper reports multiple trials and describes a task-level analysis, the inspected main-results pages do not show uncertainty intervals for the aggregate scores.
- Could rule compliance be measured systematically alongside final database state, especially for violations that leave the same final state? The authors identify this as a possible metric extension.
- Assessment is based on the supplied pages; I did not inspect any material beyond them.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
