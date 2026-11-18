# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**deliberative_review · ok**

7 model calls · 3 reads · 33.22 s · $0.007370

7 decisions · 4 tool calls · 47146 input tokens (0 cached) · 2972 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

τ-bench introduces a benchmark for language agents in simulated user conversations requiring API use, domain-policy adherence, and task completion. It evaluates outcomes against annotated database states and proposes pass^k to measure success across repeated trials. Experiments across retail and airline tasks report low success and inconsistent behavior for tested agents. This is a useful evaluation contribution, but its domains are simplified and the inspected evidence does not establish generalization to real deployments.

- **strength**: The benchmark combines simulated dialogue, tools, and policies, and evaluates task outcomes through database-state comparisons.
  - Page 6 · citation: whitespace
  - Quote: "By ensuring that only one database outcome is possible based on domain policies and user desires, subjective and noisy human judgments can be replaced by simple and objective database state comparisons."

- **strength**: Repeated-trial results directly illustrate the reliability challenge: even the strongest reported agent has a low chance of succeeding on every trial.
  - Page 7 · citation: whitespace
  - Quote: "Even for the best-performing gpt-4o function calling agent which has a > 60% average task success, pass^8 drops to < 25%."

- **limitation**: The authors characterize the domains as simplified relative to real-world settings. This is a scope boundary, not by itself evidence that the benchmark is invalid.
  - Page 6 · citation: whitespace
  - Quote: "Each τ-bench domain’s data schemas, APIs, and rules are simplified compared to real-world domains"

- **uncertainty**: The paper flags manual annotation and curation as challenges. The supplied excerpts do not establish how independently validated annotations or user simulations are; inspection was limited to excerpts from pages 1–9 of the 50-page PDF, including partial excerpts on pages 2 and 4.
  - Page 9 · citation: whitespace
  - Quote: "The manual annotation process for the benchmark is difficult and requires a deep understanding of both the domain and agent capabilities."

Unresolved questions:

- How robust are task outcomes and user simulations to independent annotation or alternative user simulators?
- Do the reported findings transfer to additional domains, real users, or production systems?
- What additional validation or implementation details appear in the uninspected pages and appendices?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark design and task construction to assess whether the simulated user, APIs, policies, and goal-state evaluation support the claimed real-world interaction setting.; Check the experimental results and analysis for evidence behind the reported success and pass^k reliability claims, including baselines and domain-specific findings.; Review limitations and remaining paper sections for scope boundaries or additional validation; only page 1 is currently available, so avoid treating uninspected material as missing support. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 4, 5, 6] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [5, 6] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [7, 8, 9] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: Observation 2’s quote supports the airline success-rate claim but not its claim about pass^k reliability. Replace it with a quote that directly supports the repeated-trial claim, or separate the claims and cite supporting text for each.; Target: Observation 2: use the page 7 passage stating that pass^8 drops below 25% to support the reliability claim. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Replaced observation 2’s airline-success quote with the page 7 passage that directly supports the pass^8 reliability claim. Retained the score and clarified the inspected-page gaps; no unsupported criticism was added. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "pass^k"}` | Locate experimental results and reliability analysis to substantiate claims. | 8 matches on pages [1, 2, 4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Inspect benchmark construction, user simulation/evaluation caveats, and evidence around design claims. | read pages [5, 6] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 7, "end": 9}` | Inspect experimental tables, reliability analysis, and reported limitations to support an independent assessment. | read pages [7, 8, 9] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
