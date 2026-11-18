# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**pyagent_react · ok**

8 model calls · 4 reads · 23.29 s · $0.003328

8 decisions · 7 tool calls · 77654 input tokens (63187 cached) · 1776 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

InterCode contributes a practical framework for evaluating interactive code generation with execution feedback, plus Bash and SQL benchmark environments adapted from existing datasets. The paper demonstrates that interaction and prompting strategies can materially affect measured task success, while also identifying narrow environment coverage and a very small CTF example as scope limits.

- **strength**: The framework gives a clear interactive task formulation and supports execution-based reward design beyond exact matching.
  - Page 4 · citation: whitespace
  - Quote: "InterCode exposes a reward function endpoint that has access to both the interaction history and the execution container"

- **strength**: Evaluations across several models show substantial gains from multi-turn feedback, especially on SQL, supporting the benchmark’s ability to reveal interactive behavior.
  - Page 6 · citation: whitespace
  - Quote: "From Table 2 and Table 3, we observe that performance across different levels of task difficulty (SQL) and different file systems (Bash) is superior in the interactive setting for all models"

- **limitation**: The authors explicitly limit the evaluated environment set to Bash and SQL and describe the CTF data as small; these are scope boundaries that constrain broad generalization, not evidence that the framework fails.
  - Page 9 · citation: whitespace
  - Quote: "the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **uncertainty**: Reported results establish performance on these benchmark settings, but the inspected passages do not establish how robust the findings are to alternative datasets or reward definitions.
  - Page 5 · citation: whitespace
  - Quote: "A max score of 1 is achieved only if the correct file paths are changed, the changes are correct, and the latest execution output matches the gold command output exactly."

Unresolved questions:

- How well do the findings transfer to additional programming languages, environments, and task sources?
- How sensitive are success rates and model comparisons to alternative reward functions and evaluation criteria?
- What evidence would a larger and more systematically curated CTF benchmark provide?
- I inspected pages 2–9 and 10–12; I did not inspect the appendices or all intervening pages, so details there may qualify these observations.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the benchmark design and evaluation evidence. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 10, "end": 12}` | Inspect reported model performance and comparisons. | read pages [10, 11, 12] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 5, "end": 7}` | Inspect experimental methods, results, and stated evaluation scope. | read pages [5, 6, 7] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 8, "end": 9}` | Inspect further findings and discussion of benchmark limitations. | read pages [8, 9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit an evidence-based assessment from the inspected benchmark, evaluation, and discussion pages. | citation_validation_failed; #2: not_found | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Replace the unverifiable numeric quote with an exact sentence observed on page 7. | citation_validation_failed; #2: wrong_page (pages [6]) | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the second citation to page 6, where the observed performance statement appears. | review accepted | [event 40](trace.jsonl#L40) |
