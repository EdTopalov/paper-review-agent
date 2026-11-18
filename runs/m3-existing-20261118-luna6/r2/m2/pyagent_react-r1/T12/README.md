# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**pyagent_react · ok**

5 model calls · 3 reads · 19.72 s · $0.002116

5 decisions · 5 tool calls · 37670 input tokens (28086 cached) · 1275 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

InterCode contributes a reusable, Docker-based framework for evaluating coding agents through iterative code execution and feedback, instantiated with Bash and SQL tasks. Experiments across models and prompting strategies show that interactive execution can improve task success, while also exposing task- and strategy-dependent performance. It is a useful benchmark and research-infrastructure contribution, though demonstrated task coverage and dataset and reward choices constrain how broadly the results generalize.

- **strength**: The framework gives a clear interactive task formulation and supports flexible reward design beyond its default exact-match approach.
  - Page 4 · citation: whitespace
  - Quote: "InterCode exposes a reward function endpoint that has access to both the interaction history and the execution container, allowing for custom reward function definitions that can incorporate multiple signals."

- **strength**: The reported experiments provide concrete evidence that feedback can improve success rates, including across SQL difficulty levels.
  - Page 6 · citation: whitespace
  - Quote: "performance across different levels of task difficulty (SQL) and different file systems (Bash) is superior in the interactive setting for all models"

- **limitation**: The authors explicitly bound the current benchmark’s breadth: its implemented environments are Bash and SQL, and its CTF set is very small.
  - Page 9 · citation: whitespace
  - Quote: "the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **uncertainty**: The evidence inspected does not establish how robust results are to alternative reward specifications or broader task populations; the authors describe the CTF collection as manually curated and limited.
  - Page 9 · citation: whitespace
  - Quote: "the CTF dataset is limited to just four task instances due to our manual curation procedure."

Unresolved questions:

- How sensitive are model rankings and success rates to alternative reward functions, especially where output similarity or exact ordering affects scoring?
- Do the observed benefits of interaction persist on larger and more diverse tasks beyond the two implemented environments?
- I inspected pages 1–9, not the remaining paper or appendices; further methodological details, prompts, and analyses may qualify this assessment.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the framework design and benchmark construction. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect evaluation results and experimental comparisons. | read pages [5, 6, 7] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 8, "end": 9}` | Inspect strategy results and stated limitations. | read pages [8, 9] | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit an evidence-based assessment using the inspected framework, results, and limitations pages. | citation_validation_failed; #2: wrong_page (pages [6]) | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the page number for the verified interactive-results quotation. | review accepted | [event 26](trace.jsonl#L26) |
