# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**deliberative_review · ok**

6 model calls · 3 reads · 22.67 s · $0.004471

6 decisions · 4 tool calls · 29977 input tokens (1299 cached) · 1765 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

τ-bench introduces a modular benchmark for evaluating tool-using agents through simulated user conversations, domain policies, and database-state outcomes, alongside pass^k for measuring repeated-trial consistency. Its two domains and broad model comparisons offer useful evidence that current agents struggle, though the environments are deliberately simplified and the inspected results do not establish generalization to real-world deployments.

- **strength**: Task construction combines designed environments with language-model-generated data and human validation. This supports a concrete, reproducible benchmark design, while the domains remain intentionally simplified.
  - Page 5 · citation: whitespace
  - Quote: "Each domain is created in a three-stage approach with a mix of LM and code runs, and human labeling and checking."

- **strength**: The experiments compare many models and report low task success, with a repeated-trial metric that makes consistency visible. Main results use at least three trials per task; the strongest reported retail pass^8 result is below 25%.
  - Page 7 · citation: exact
  - Quote: "Even for the\nbest-performing gpt-4o function calling agent which has a > 60% average task success, pass^8 drops\nto < 25%."

- **limitation**: The benchmark’s two domains are simplified and selected partly for ease of synthesis. The paper identifies more complex domains as future work, so claims about broad real-world coverage remain open rather than disproved.
  - Page 6 · citation: exact
  - Quote: "Each τ-bench domain’s data schemas, APIs, and rules are simplified\ncompared to real-world domains"

Unresolved questions:

- How well do outcomes and pass^k scores transfer to real users, production APIs, or domains beyond retail and airline?
- How sensitive are the conclusions to the user-simulation model and to the benchmark’s task and policy design?
- I inspected only selected pages and excerpts (notably pages 1–7 and partial page 9); the full limitations discussion, appendices, and remaining results were not inspected, so further qualifications or validation evidence may be present.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark construction and task-generation sections to assess whether the retail and airline environments, policies, APIs, and user simulations substantiate the claimed real-world interaction coverage; note explicit scope boundaries.; Inspect experimental setup and results to verify how agent success and pass^k are measured, what baselines and trial counts support the abstract’s claims, and whether the evidence supports reliability conclusions.; Inspect limitations, analysis, and remaining results for qualifications or evidence relevant to validity and generalizability; onl … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 4, 5, 6] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 3 matches on pages [9, 12, 35] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [5, 6, 7] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: approve | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "pass^k"}` | Locate experimental results and evaluation details needed to assess the paper's central benchmark claims. | 8 matches on pages [1, 2, 4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "Limitations"}` | Locate the paper's stated limitations and scope boundaries before assessing generalizability. | 3 matches on pages [9, 12, 35] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark construction and experimental results for evidence and scope. | read pages [5, 6, 7] | [event 22](trace.jsonl#L22) |
| 6 | submit_review `{"review": {"score": 0.74, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 34](trace.jsonl#L34) |
