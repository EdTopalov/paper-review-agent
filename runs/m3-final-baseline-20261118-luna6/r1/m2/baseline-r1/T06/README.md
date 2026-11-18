# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**baseline · ok**

1 model calls · 0 reads · 7.50 s · $0.000629

1 decisions · 0 tool calls · 35056 input tokens (35053 cached) · 557 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

Introduces SWE-bench, a benchmark of 2,294 issue-and-codebase tasks from 12 Python repositories, evaluated by applying generated patches and running repository tests. It also reports baseline evaluations and fine-tunes SWE-Llama models, finding low task-resolution rates and analyzing context retrieval, patch quality, and failure patterns. The benchmark offers a consequential, realistic evaluation target, though its construction and evaluation choices constrain what its scores establish.

- **strength**: The paper’s core contribution is a sizeable, execution-validated benchmark built from real issues and accepted fixes, rather than short, self-contained code-generation prompts.
  - Page 2 · citation: hyphenation_ambiguous
  - Quote: "Through these stages of filtering, the original 90,000 PRs are filtered down to the 2,294 task instances which comprise SWE-bench."

- **strength**: The evaluation checks both issue-related tests and preservation tests, and the authors document a reproducible task-construction and validation procedure.
  - Page 20 · citation: not_found
  - Quote: "A task is considered solved if all tests across FAIL TO PASS and PASS TO PASS pass."

- **limitation**: The authors explicitly scope the benchmark to Python, so its results do not directly establish performance on other languages or software domains.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **uncertainty**: The reported model results are baseline evidence under particular retrieval and decoding setups, not a broad estimate of the best achievable performance; the paper says it used simple approaches and invites other methods. I inspected the supplied paper text, but did not independently verify the experimental implementation or inspect every appendix detail.
  - Page 9 · citation: whitespace
  - Quote: "our experiments aim to establish a baseline of the simplest and most straight-forward approaches for this task"

Unresolved questions:

- How well do the benchmark’s task selection and test-based success criterion represent the diversity and quality expectations of real software engineering work, beyond the sampled repositories and merged PRs?
- How would performance change with agentic repository exploration, tool use, or other context-selection methods, rather than the paper’s baseline retrieval and prompt setups?
- How stable are the reported resolution rates to repeated sampling or alternative inference settings, given that models generate a single patch per instance using greedy decoding?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
