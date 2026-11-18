# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**pyagent_react · ok**

4 model calls · 3 reads · 23.98 s · $0.002072

4 decisions · 4 tool calls · 22256 input tokens (13936 cached) · 1786 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

τ-bench contributes a practical benchmark for evaluating agents across multi-turn user interaction, API use, and domain-policy following, with a database-state-based task metric and pass^k reliability measure. Its two domains and baseline comparisons expose substantial weaknesses in current agents. The work is valuable and clearly scoped, though its simulated users, limited domain coverage, and partly rule-based evaluation constrain how directly results transfer to deployment.

- **strength**: The benchmark combines simulated conversation, database-backed API actions, and domain policies, and evaluates task outcomes against an annotated target state.
  - Page 3 · citation: whitespace
  - Quote: "The agent interacts with both (1) databases (db) via API tools, and (2) a (simulated) user (user) to complete a task"

- **strength**: The paper provides a reliability metric suited to repeated task execution and reports a marked gap between single-trial success and consistent success.
  - Page 7 · citation: whitespace
  - Quote: "Even for the best-performing gpt-4o function calling agent which has a > 60% average task success, pass^8 drops to < 25%."

- **limitation**: The authors acknowledge that the simulated user can make errors or fail to represent the full range of domain knowledge and reasoning, which may affect task outcomes.
  - Page 9 · citation: normalized
  - Quote: "the user simulation LM might have limited capacity at reasoning, calculation, long-context memorization, or alignment with the instruction prompt"

- **limitation**: The initial evaluation covers only two relatively tractable domains, so evidence for broader real-world applicability remains open.
  - Page 5 · citation: whitespace
  - Quote: "We choose these two domains as they are relatively easy to synthesize data (e.g., products, prices, flights) and craft policies"

Unresolved questions:

- How well do benchmark outcomes correspond to performance with real users and real operational systems, rather than simulated conversations and deterministic APIs?
- Would the observed reliability and policy-following weaknesses persist across a wider range of domains and more complex task distributions?
- How sensitive are agent rankings to the rule-based success criteria and task curation process? The paper notes potential implicit bias from tuning prompts with a gpt-4-turbo function-calling agent.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "pass^k"}` | Locate the benchmark metric and reported reliability results. | 8 matches on pages [1, 2, 4, 5, 6] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect benchmark design, task scope, and evaluation details. | read pages [3, 4, 5] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 7, "end": 9}` | Inspect empirical results and identify the evaluated agents and domains. | read pages [7, 8, 9] | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Submit an evidence-based assessment using the benchmark description, results, and stated limitations inspected. | review accepted | [event 21](trace.jsonl#L21) |
