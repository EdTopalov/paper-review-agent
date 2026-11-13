# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**pyagent_react · ok**

4 model calls · 2 reads · 16.19 s · $0.002256

4 decisions · 4 tool calls · 23119 input tokens (10520 cached) · 1153 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

InterCode contributes a reusable framework for evaluating language models in interactive coding settings, where executable code actions produce feedback that can inform subsequent actions. Its Bash and SQL environments and comparisons across models and prompting strategies make a useful case for moving beyond static code-generation evaluation. The evidence supports the benchmark’s viability, but the evaluation is preliminary and the stated task coverage is narrow.

- **strength**: The paper reports substantial gains from interaction on SQL, including for GPT-4, supporting the benchmark’s value for studying feedback-driven coding.
  - Page 6 · citation: whitespace
  - Quote: "notable multi-fold increase for GPT-4 (9.1% → 73.7%)"

- **strength**: The authors describe concrete checks that gold commands execute and receive full reward, providing implementation-level validation of the environments and reward functions.
  - Page 5 · citation: exact
  - Quote: "verify that the reward received by the command is1."

- **limitation**: The paper explicitly bounds the available environments and notes that its manually curated CTF set is very small; this is a scope limitation, not evidence that the framework cannot extend further.
  - Page 9 · citation: whitespace
  - Quote: "the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **uncertainty**: The reported reward functions include lexical and record-overlap components. Whether these proxies reliably capture semantic task success beyond the described checks remains unresolved in the inspected pages.
  - Page 5 · citation: whitespace
  - Quote: "Execution output is graded with a simple lexical similarity function."

Unresolved questions:

- How robust are the reported findings to alternative task samples, repeated evaluation runs, and changes to prompt or model settings?
- How well do the reward functions align with human judgments of task completion, especially for outputs with multiple valid forms?
- What are the implementation details and additional caveats in the appendices? I inspected the supplied first page and PDF pages 5–9, not the full paper or appendices, so this assessment may miss evidence elsewhere.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 5, "end": 7}` | Inspect the benchmark environments and reported evaluation results. | read pages [5, 6, 7] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 8, "end": 9}` | Inspect conclusions and stated limitations or scope boundaries. | read pages [8, 9] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | The inspected pages establish the framework, its task construction and reported comparisons, and its stated limitations; submit a qualified assessment. | citation_validation_failed; #1: wrong_page (pages [6]) | [event 17](trace.jsonl#L17) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the citation page for the reported GPT-4 interaction gain and resubmit the review. | review accepted | [event 23](trace.jsonl#L23) |
