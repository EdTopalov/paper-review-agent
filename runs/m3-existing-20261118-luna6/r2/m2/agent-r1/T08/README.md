# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**agent · ok**

4 model calls · 3 reads · 9.45 s · $0.001330

4 decisions · 4 tool calls · 19078 input tokens (11802 cached) · 630 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

τ-bench contributes a modular benchmark for evaluating language agents in multi-turn user interaction with API tools and domain policies. It pairs simulated conversations with annotated database outcomes, adds pass^k to measure consistency across stochastic trials, and reports substantial failure and reliability gaps for tested agents. Its evidence is useful for controlled benchmark evaluation, while conclusions remain bounded by two simplified customer-service domains and LM-simulated users.

- **strength**: The benchmark combines tool interaction, user dialogue, policy adherence, and state-based scoring in a coherent evaluation setup.
  - Page 4 · citation: whitespace
  - Quote: "The reward of a task episode r = raction × routput ∈ {0, 1} is based on (1) whether the final database is identical to the unique ground truth outcome database (raction), and (2) whether the agent’s responses to the user contain all necessary information (routput)."

- **strength**: Repeated trials and pass^k expose a reliability dimension beyond average task success; the reported gpt-4o results illustrate this sharply.
  - Page 2 · citation: whitespace
  - Quote: "With increasing k, the chance of consistently solving a task drops rapidly, to as low as ∼25% for pass^8 on τ-retail for the same model."

- **limitation**: The initial benchmark is deliberately narrow in domain coverage, so performance evidence does not establish generalization to other high-stakes or operational settings.
  - Page 5 · citation: exact
  - Quote: "we modularly construct two domains, τ-retail and τ-airline."

- **uncertainty**: The evaluation depends on simulated users and annotated outcomes; how well these approximate real users and real-world success criteria remains an open question in the inspected material.
  - Page 3 · citation: whitespace
  - Quote: "We use a language model (gpt-4-0613) to simulate a human user interacting with the agent."

Unresolved questions:

- How well do the benchmark’s simulated-user interactions and objective state-based rewards correlate with judgments from real users and domain experts?
- Do the reported reliability and success patterns persist in additional domains and with agents beyond the tested model/method configurations?
- I inspected pages 1–6 and selected passages only; later experimental tables, detailed failure analysis, and appendices were not examined, so the full breadth of empirical support and implementation details remains unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "pass^k"}` | Locate benchmark results and reliability metric evidence. | 8 matches on pages [1, 2, 4, 5, 6] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design, scoring details, and stated evaluation caveats. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Inspect task scale, construction choices, and benchmark limitations. | read pages [5, 6] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Submit an evidence-grounded assessment after inspecting the benchmark design, metric, construction, and scope. | review accepted | [event 20](trace.jsonl#L20) |
