# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**deliberative_review · ok**

6 model calls · 3 reads · 21.09 s · $0.003491

6 decisions · 4 tool calls · 21627 input tokens (1299 cached) · 1893 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

τ-bench proposes a benchmark for evaluating agents in simulated customer-service conversations involving users, APIs, and domain policies. It pairs task-specific goal states with database-based success evaluation and introduces pass^k to measure consistency across repeated trials. The available evidence supports a useful, clearly scoped benchmark contribution, but does not let me fully assess the reported experiments or validation of its simulations and annotations.

- **strength**: The benchmark combines simulated user interaction, API use, and policy following, with manual design and verification as part of its construction.
  - Page 2 · citation: whitespace
  - Quote: "manual schema and API design, LM-assisted generation of data entries, and manual scenario generation and verification"

- **strength**: The evaluation uses an explicit target database state and proposes a metric for consistency across repeated trials.
  - Page 4 · citation: whitespace
  - Quote: "we propose a new metric – pass^k (pass hat k), defined as the chance that all k i.i.d. task trials are successful"

- **limitation**: The authors identify possible ambiguities and missing domain knowledge in simulated-user instructions; these are acknowledged limitations, not evidence that the benchmark fails generally.
  - Page 9 · citation: exact
  - Quote: "the user instruction might contain typos or ambiguities"

- **uncertainty**: The abstract reports low success and consistency for tested agents, but the inspected excerpts do not provide enough experiment detail to assess the breadth or robustness of those findings.
  - Page 1 · citation: whitespace
  - Quote: "pass^8 < 25% in retail"

Unresolved questions:

- How are simulated-user behavior and the manually annotated goal states validated across tasks, and how sensitive are results to simulator choices?
- How broad are the experiments across agent configurations and repeated trials, and how much uncertainty surrounds the reported success and pass^k estimates?
- The supplied excerpts cover only selected portions of the 50-page paper; the experiment details and much of the discussion remain uninspected.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark construction, task domains, simulated-user design, and policy/API setup to determine how well the benchmark supports its claim of realistic tool-agent-user interaction.; Check the evaluation protocol and reported results—especially state comparison and pass^k—for evidence supporting the claims about success and consistency, and look for relevant caveats or limitations elsewhere in the paper.; Inspect the paper’s discussion and experiment details for scope boundaries, validation of simulated users and annotated goals, and any qualifications to the reported findings … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 4, 5, 6] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 3 matches on pages [9, 12, 35] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 4 matches on pages [2, 4, 9] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: approve | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "pass^k"}` | Inspect the paper’s evaluation metric/results and nearby discussion for evidence on consistency and qualifications. | 8 matches on pages [1, 2, 4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "Limitations"}` | Check discussion for explicit scope limitations and counterevidence to broad claims. | 3 matches on pages [9, 12, 35] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "simulated user"}` | Inspect benchmark design and user-simulation validation evidence, including limitations, for the realism assessment. | 4 matches on pages [2, 4, 9] | [event 22](trace.jsonl#L22) |
| 6 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 34](trace.jsonl#L34) |
