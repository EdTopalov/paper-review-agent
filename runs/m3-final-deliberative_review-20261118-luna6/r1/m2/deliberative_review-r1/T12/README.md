# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**deliberative_review · ok**

7 model calls · 3 reads · 115.50 s · $0.007937

7 decisions · 4 tool calls · 51971 input tokens (0 cached) · 2900 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

InterCode introduces a reusable framework for evaluating coding agents in interactive environments with execution feedback, demonstrated through Bash and SQL tasks adapted from existing datasets. Reported results show gains over single-turn coding in the tested settings, while strategy comparisons indicate that benefits depend on the task. This is a useful benchmark contribution, though the inspected experiments cover only two environments and leave broader safety, reproducibility, and extensibility claims unverified.

- **strength**: The framework makes task construction modular and supports execution-based assessment, with Bash and SQL implementations and environment-specific reward designs.
  - Page 4 · citation: whitespace
  - Quote: "This workflow allows for the safe execution of transition functions, flexible reward design, and convenient adaptation of existing instructions to an interactive setting."

- **strength**: The reported comparisons show higher success rates in the interactive setting for the listed models on both datasets; the paper reports this result in its discussion of the tables.
  - Page 6 · citation: whitespace
  - Quote: "performance across different levels of task difficulty (SQL) and different file systems (Bash) is superior in the interactive setting for all models"

- **limitation**: The empirical demonstrations use two environments derived from existing datasets. Bash instructions were filtered and adapted to supported utilities and custom file systems; this limits the demonstrated scope but does not show that the framework cannot support other tasks.
  - Page 5 · citation: exact
  - Quote: "The resulting 200 commands are grouped into 4 disjoint sets"

- **uncertainty**: The paper describes Docker as a sandbox and reports validation scripts, but the inspected passages do not establish containment effectiveness or reproducibility in practice. Most of the 29-page paper was not inspected, including material that may address these questions.
  - Page 4 · citation: whitespace
  - Quote: "InterCode uses Docker [31] virtual containers as a general-purpose execution sandbox."

Unresolved questions:

- How robust are the benchmark results to alternative reward designs, especially where exact output matching or lexical similarity may not capture semantic correctness?
- Do the safety and reproducibility claims hold under broader threat models and across independently configured Docker-equipped machines?
- How well does the framework and its conclusions transfer to additional programming languages, tasks, and datasets? The inspected experimental material covers Bash and SQL.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the benchmark design and task construction for Bash and SQL, including how static datasets are converted into interactive episodes and what constitutes success.; Check the experimental results and comparisons across models and prompting strategies to determine whether the claimed benefits of interaction are supported by evidence.; Inspect evaluation protocols, environment safety and reproducibility details, and stated limitations elsewhere in the paper; only page 1 is currently available, so these claims and the full scope remain unverified. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [4, 6, 7] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [3, 4, 5] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [6, 7, 8] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The second observation’s quote is found on PDF page 6, not page 7. Correct the page citation to 6; the claim itself is supported by the reported results.; Target: Correct the page number for the quote in observation 2 to page 6. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Corrected observation 2’s citation from page 7 to page 6, where the quoted sentence appears. The critic’s page-number concern is supported; no score change was warranted. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "success"}` | Inspect benchmark task construction, success criteria, and results evidence relevant to the stated contribution. | 8 matches on pages [4, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 3, "end": 5}` | Inspect task construction, reward/success definition, environment and evaluation design. | read pages [3, 4, 5] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 6, "end": 8}` | Inspect experimental protocols/results and discussion of limitations or failure modes, checking whether interactive benefits are backed by comparisons. | read pages [6, 7, 8] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
