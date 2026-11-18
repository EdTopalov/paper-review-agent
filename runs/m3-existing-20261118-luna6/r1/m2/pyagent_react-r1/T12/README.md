# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**pyagent_react · ok**

3 model calls · 2 reads · 18.67 s · $0.001488

3 decisions · 3 tool calls · 12416 input tokens (6535 cached) · 1375 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

InterCode contributes a reusable framework for interactive code generation, with Bash and SQL environments that convert static tasks into action-and-feedback episodes. The inspected results show that prompting strategy performance varies by task and that more interaction can improve success. This is a useful benchmark and infrastructure contribution, though the evidence reviewed does not establish broad generalization beyond these settings; the authors also note the limited environment and CTF task coverage.

- **strength**: The results show strategy-dependent performance, supporting the value of evaluating interaction rather than treating coding as one static generation step.
  - Page 8 · citation: exact
  - Quote: "SQL 47.3 7.25 46.4 58.7 5.30 6.94 49.1 4.29 16.2"

- **strength**: The paper reports success-rate growth as interaction turns increase, an empirical signal that feedback and additional interaction can matter.
  - Page 8 · citation: exact
  - Quote: "Figure 3: Growth in Success Rate with increase in number of interaction turns across models"

- **limitation**: The authors explicitly bound the current benchmark’s breadth: environments are limited to Bash and SQL, and the manually curated CTF set is very small.
  - Page 9 · citation: whitespace
  - Quote: "Second, the CTF dataset is limited to just four task instances due to our manual curation procedure."

- **uncertainty**: The inspected results support differences between prompting strategies on these datasets, but do not resolve how broadly those findings transfer to other languages or interactive coding tasks.
  - Page 9 · citation: whitespace
  - Quote: "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

Unresolved questions:

- How well do these findings transfer to new environments, programming languages, and task distributions?
- How sensitive are outcomes to task design and success metrics, particularly for SQL answer matching and Bash task completion?
- Important inspection gap: only pages 1 and 8–10 were examined; implementation details, full experimental setup, and other results elsewhere in the paper were not reviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Results"}` | Locate evaluation results and benchmark findings. | 8 matches on pages [1, 9, 13, 17, 19, 21] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 8, "end": 10}` | Inspect the framework description and reported findings. | read pages [8, 9, 10] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Assess the framework using inspected benchmark results and the authors’ stated limitations. | review accepted | [event 16](trace.jsonl#L16) |
