# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**pyagent_react · ok**

6 model calls · 4 reads · 19.98 s · $0.002301

6 decisions · 6 tool calls · 49741 input tokens (39235 cached) · 1192 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

τ-bench contributes a modular benchmark for evaluating language agents in multi-turn simulated-user interactions with API tools and domain policies. It combines annotated database outcomes with a reliability metric, pass^k, and uses retail and airline tasks to expose low success rates and inconsistency in tested agents. It is a substantial and practically motivated evaluation contribution, though its evidence is bounded by two simplified customer-service domains and an LM-simulated user.

- **strength**: Outcome-based evaluation permits varied dialogue while checking whether the intended database changes occurred; the authors also introduce a consistency-oriented metric.
  - Page 2 · citation: whitespace
  - Quote: "compares the database state at the end of each episode with the ground truth expected state."

- **strength**: Experiments across models and methods show substantial task difficulty, and repeated trials highlight reliability concerns beyond average success.
  - Page 7 · citation: whitespace
  - Quote: "pass^8 drops to < 25%."

- **limitation**: The benchmark deliberately simplifies its domains and currently demonstrates only retail and airline tasks; broader applicability is not established by these experiments.
  - Page 6 · citation: whitespace
  - Quote: "Each τ-bench domain’s data schemas, APIs, and rules are simplified compared to real-world domains"

- **limitation**: The authors acknowledge possible bias in task curation from using a GPT-4-turbo agent to tune user prompts.
  - Page 9 · citation: whitespace
  - Quote: "There is also some element of implicit bias during the task curation process since we use the gpt-4-turbo FC agent to tune the user’s system prompt."

Unresolved questions:

- How well do the benchmark’s user simulations and measured agent rankings transfer to interactions with real users?
- Would the evaluation conclusions hold across additional domains and more systematically varied policy complexity?
- How sensitive are results to choices in task curation and the simulator model?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction and task domains. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect evaluation protocol, baselines, and reported results. | read pages [5, 6, 7] | [event 11](trace.jsonl#L11) |
| 3 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope boundaries and evaluation caveats. | 3 matches on pages [9, 12, 35] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 9, "end": 10}` | Read the discussion of benchmark limitations and future directions. | read pages [9, 10] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Submit an evidence-based assessment of the benchmark, experiments, and stated limitations. | citation_validation_failed; #1: wrong_page (pages [1]); #4: not_found | [event 26](trace.jsonl#L26) |
| 6 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Correct the two quotes that failed citation validation using observed page text. | review accepted | [event 31](trace.jsonl#L31) |
