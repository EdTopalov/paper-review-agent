# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**baseline · ok**

1 model calls · 0 reads · 5.79 s · $0.004868

1 decisions · 0 tool calls · 36934 input tokens (0 cached) · 503 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

τ-bench introduces a modular benchmark for evaluating language agents in multi-turn interactions with simulated users and domain-specific API tools and policies. Its central contributions are end-state database evaluation and pass^k, which measures repeated-trial consistency. Experiments across retail and airline tasks show substantial weaknesses in tested agents, while the paper also identifies simulator, curation, and scope limitations.

- **strength**: The benchmark combines user interaction, tool use, and rule following in a single task setup, addressing a clear evaluation target.
  - Page 1 · citation: whitespace
  - Quote: "measure an agent’s ability to interact with (simulated) human users and programmatic APIs while following domain-specific policies"

- **strength**: The pass^k metric captures reliability across repeated stochastic interactions, complementing average task success.
  - Page 4 · citation: whitespace
  - Quote: "pass^k (pass hat k), defined as the chance that all k i.i.d. task trials are successful, averaged across tasks."

- **limitation**: Database-state matching does not itself establish that every policy violation is detected; the authors explicitly note a mismatch between reward and full policy compliance.
  - Page 4 · citation: whitespace
  - Quote: "r = 1 might be a necessary but not sufficient condition for a successful episode"

- **uncertainty**: The paper describes a small initial domain set and hand-curated tasks; how well the benchmark generalizes to other industries and more varied task distributions remains open.
  - Page 5 · citation: exact
  - Quote: "we modularly construct two domains, τ-retail and τ-airline"

Unresolved questions:

- How strongly do simulated-user behavior and its instruction-following errors affect the measured agent rankings and pass^k estimates?
- How would conclusions change with broader domains, larger or systematically sampled task sets, and evaluation of policy violations beyond final database state?
- What are the uncertainty intervals for reported model comparisons and pass^k estimates? The inspected pages include a checklist claiming error bars, but do not show them for the main results.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
