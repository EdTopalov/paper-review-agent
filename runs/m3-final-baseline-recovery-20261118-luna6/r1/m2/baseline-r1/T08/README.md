# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**baseline · ok**

1 model calls · 0 reads · 7.67 s · $0.000613

1 decisions · 0 tool calls · 36934 input tokens (36931 cached) · 487 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

τ-bench introduces a modular benchmark for evaluating language agents in multi-turn interactions with simulated users and API tools under domain-specific policies. It contributes an end-state database evaluation method and pass^k reliability metric, and reports substantial weaknesses in tested agents across retail and airline tasks. The work is a useful, practically motivated benchmark contribution, though its evidence is bounded by two simplified customer-service domains and LM-based simulation and annotation choices.

- **strength**: The benchmark combines conversational interaction, tool use, and policy adherence, with outcome checks that can tolerate varied dialogue trajectories.
  - Page 4 · citation: whitespace
  - Quote: "the final database is identical to the unique ground truth outcome database"

- **strength**: The repeated-trial metric captures a reliability dimension that average task success alone does not represent; reported results show a steep drop for the strongest tested retail agent.
  - Page 7 · citation: whitespace
  - Quote: "pass^8 drops to < 25%"

- **limitation**: The initial evaluation scope is deliberately narrow; its findings should not automatically be generalized to other domains or deployment settings.
  - Page 5 · citation: exact
  - Quote: "we modularly construct two domains, τ-retail and τ-airline."

- **uncertainty**: Reliability estimates depend on a simulated-user setup, and the authors acknowledge that simulator reasoning, memory, and instruction alignment can be imperfect; how well those variations reflect real users remains unsettled.
  - Page 9 · citation: normalized
  - Quote: "the user simulation LM might have limited capacity at reasoning, calculation, long-context memorization, or alignment with the instruction prompt"

Unresolved questions:

- How do the benchmark rankings and pass^k trends change with human users or independently validated user-simulation models?
- Would the evaluation conclusions hold in additional domains with different policies and action structures?
- How sensitive are results to task curation choices, especially the use of a GPT-4-turbo agent to iteratively tune user instructions?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
