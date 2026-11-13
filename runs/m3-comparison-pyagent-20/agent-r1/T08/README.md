# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**agent · ok**

3 model calls · 2 reads · 7.44 s · $0.001206

3 decisions · 3 tool calls · 9175 input tokens (1500 cached) · 483 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

τ-bench offers a useful, modular benchmark for evaluating tool agents in user-facing dialogues with domain policies, and introduces pass^k to expose consistency beyond single-trial success. Its measured performance gaps are informative, though the two deliberately simplified domains and LM-simulated users limit how directly results transfer to real deployments.

- **strength**: The benchmark combines dialogue, API use, policy following, and a database-state-based success criterion, making its evaluation concrete and reproducible within the supplied environment.
  - Page 6 · citation: whitespace
  - Quote: "By ensuring that only one database outcome is possible based on domain policies and user desires, subjective and noisy human judgments can be replaced by simple and objective database state comparisons."

- **strength**: The evaluation adds a useful reliability perspective, and results show that even the strongest tested model has substantial difficulty, especially in airline tasks.
  - Page 7 · citation: whitespace
  - Quote: "Even for the best-performing gpt-4o function calling agent which has a > 60% average task success, pass^8 drops to < 25%."

- **limitation**: The authors explicitly scope the domains as simplified, so the benchmark does not itself establish performance in full real-world systems.
  - Page 6 · citation: whitespace
  - Quote: "Each τ-bench domain’s data schemas, APIs, and rules are simplified compared to real-world domains"

Unresolved questions:

- How robust are benchmark conclusions to changes in the simulated-user model and its instruction-generation assumptions?
- Do results generalize to additional domains or less simplified operational APIs and policies?
- I inspected the opening page and pages 5–7, plus search results for limitations; I did not inspect the full methods, appendices, or all task annotations, so detailed construction and statistical uncertainty remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Limitations"}` | Check the paper's explicit scope limitations before assessing the benchmark. | 3 matches on pages [9, 12, 35] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark construction, evaluation metric, and reported empirical results. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.74, "observations": 3}}` | Evidence covers benchmark design, reported scores, and a stated simplification boundary; submit a balanced assessment while noting limited inspection. | review accepted | [event 16](trace.jsonl#L16) |
