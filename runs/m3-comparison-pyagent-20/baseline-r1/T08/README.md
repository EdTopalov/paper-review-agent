# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**baseline · ok**

1 model calls · 0 reads · 5.61 s · $0.004926

1 decisions · 0 tool calls · 36934 input tokens (0 cached) · 619 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

τ-bench introduces a modular benchmark for evaluating language agents in multi-turn interactions with simulated users, API tools, and domain policies. It contributes an end-state database metric and pass^k for measuring consistency across repeated trials, and reports baseline results across retail and airline tasks. The paper provides useful evidence of weaknesses in tested agents, while its scope and evaluation depend on synthetic domains, LM-simulated users, and a reward that does not capture every policy violation.

- **strength**: The benchmark combines user interaction, tools, and domain rules, and uses repeated trials to assess reliability as well as average task success.
  - Page 2 · citation: whitespace
  - Quote: "We also introduce the metric of pass^k, which measures the consistency and robustness of the agent across k i.i.d. trials."

- **strength**: The experiments provide concrete evidence that tested agents often fail, with results varying across domains and models.
  - Page 7 · citation: not_found
  - Quote: "All models are still far from solving τ-bench, especially the more challenging τ-airline where even gpt-4o solves only 35.2% of the tasks."

- **limitation**: The authors note that the automated reward can mark an episode successful even when the agent violates a policy, so it does not fully measure rule adherence.
  - Page 4 · citation: whitespace
  - Quote: "r = 1 might be a necessary but not sufficient condition for a successful episode"

- **uncertainty**: The evaluation covers two deliberately simplified customer-service domains; how well its tasks and findings transfer to other real-world domains remains unresolved.
  - Page 6 · citation: whitespace
  - Quote: "Each τ-bench domain’s data schemas, APIs, and rules are simplified compared to real-world domains"

Unresolved questions:

- How would agent rankings and pass^k results change with human users or independently validated user simulations?
- How much do findings from these two synthetic customer-service domains generalize to other application areas and less simplified systems?
- How would evaluation results change with systematic checks for policy compliance beyond final database state and required response text?
- This assessment inspected the supplied pages, including the main text and selected appendices/examples; it did not independently validate the benchmark code, data, or all reported experimental details.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
