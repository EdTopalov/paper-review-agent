# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**baseline · ok**

1 model calls · 0 reads · 8.23 s · $0.000613

1 decisions · 0 tool calls · 36934 input tokens (36931 cached) · 486 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

τ-bench introduces a benchmark for evaluating tool-using agents in multi-turn interactions with simulated users, domain APIs, and policy documents. Its end-state database evaluation and pass^k metric target task completion and repeatability; results across retail and airline tasks show substantial failures in current function-calling agents. The work is a useful, concrete evaluation contribution, though its scope and conclusions are bounded by two constructed domains, LM-based user simulation, and a small curated task set.

- **strength**: The benchmark combines user interaction, API use, and policy following, with a state-based reward intended to accommodate varied dialogue paths.
  - Page 4 · citation: whitespace
  - Quote: "the final database is identical to the unique ground truth outcome database"

- **strength**: The reliability metric and repeated trials make consistency an explicit target beyond average success.
  - Page 5 · citation: whitespace
  - Quote: "pass^k can capture the reliability of the agent at handling variations in conversations"

- **limitation**: The paper identifies meaningful simulator and curation limitations, including ambiguous instructions, user-model capability, and possible selection bias from tuning with a particular agent.
  - Page 9 · citation: not_found
  - Quote: "there is also some element of implicit bias during the task curation process"

- **uncertainty**: The results are based on two customer-service domains and 115 retail and 50 airline tasks; how well performance generalizes to broader or higher-stakes domains remains open.
  - Page 5 · citation: exact
  - Quote: "we modularly construct two domains, τ-retail and τ-airline"

Unresolved questions:

- How closely do simulator-generated interactions and benchmark task outcomes reflect real user interactions and operational customer-service settings?
- Would the reported reliability and model comparisons hold across additional domains, substantially larger task sets, and different user simulators?
- How sensitive are pass^k estimates and model rankings to choices such as simulator model, sampling settings, and task curation?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
