# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**agent · ok**

3 model calls · 2 reads · 9.37 s · $0.001942

3 decisions · 3 tool calls · 14962 input tokens (1500 cached) · 508 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

τ-bench introduces a modular benchmark for evaluating language agents across simulated user dialogue, domain-specific policies, and API/database actions. Its ground-truth state comparison and pass^k reliability metric provide a concrete evaluation framework, and baseline experiments expose substantial weaknesses in tested agents. The work is a useful, well-motivated benchmark contribution, while its synthetic, deliberately simplified domains and simulator-based evaluation bound claims about real-world deployment.

- **strength**: The benchmark unifies tool use, user interaction, and policy adherence, with a measurable outcome based on an annotated target state.
  - Page 4 · citation: whitespace
  - Quote: "the final database is identical to the unique ground truth outcome database"

- **strength**: Experiments show low success rates and quantify how reliability degrades over repeated trials for the tested agents.
  - Page 7 · citation: whitespace
  - Quote: "pass^8 drops to < 25%."

- **limitation**: The authors explicitly simplify domains and focus on two customer-service settings, so transfer to richer real-world domains remains open.
  - Page 6 · citation: whitespace
  - Quote: "Each τ-bench domain’s data schemas, APIs, and rules are simplified compared to real-world domains"

- **uncertainty**: Evaluation depends on simulated users and rule-based outcome checks; the paper itself notes these checks can miss policy violations, so correspondence to human-judged service quality is unresolved.
  - Page 4 · citation: whitespace
  - Quote: "r = 1 might be a necessary but not sufficient condition for a successful episode"

Unresolved questions:

- How well do the user simulator and database-state reward align with judgments from real users and domain experts?
- Do findings and pass^k trends generalize to domains with less simplified policies and higher-stakes decisions?
- I inspected the abstract, benchmark formulation, construction, and initial experimental results, but not the full appendices or later analyses; those may add evidence about validation and failure modes.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction, task domains, and methodological details. | read pages [2, 3, 4] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Review empirical setup and stated benchmark limitations or caveats. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Evidence covers benchmark design, evaluation criteria, limitations in scope, and reported baseline results; submit an independent assessment. | review accepted | [event 16](trace.jsonl#L16) |
