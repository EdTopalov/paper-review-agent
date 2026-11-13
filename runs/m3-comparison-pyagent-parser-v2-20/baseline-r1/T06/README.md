# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**baseline · ok**

1 model calls · 0 reads · 6.56 s · $0.004648

1 decisions · 0 tool calls · 35056 input tokens (0 cached) · 532 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

This paper introduces SWE-bench, a benchmark of 2,294 issue-and-pull-request tasks from 12 Python repositories, and evaluates proprietary and fine-tuned language models on repository-level code changes. Its main contribution is a practical construction and test-based evaluation pipeline, paired with baseline results showing that the tested models solve few tasks and struggle particularly with relevant-context selection and complex edits.

- **strength**: The benchmark is built from real repository issues and accepted fixes, with execution-based filtering to ensure tasks have tests that respond to the reference solution.
  - Page 2 · citation: not_found
  - Quote: "We filter out instances without at least one test where its status changes from a fail to pass"

- **strength**: The paper provides a useful baseline comparison and separates patch application from full resolution, making clear that formatting or applying a patch is not equivalent to solving the issue.
  - Page 6 · citation: wrong_page
  - Quote: "The best performing model, Claude 2, only achieves a mere 4.8% pass rate using the “oracle” retrieval context."

- **limitation**: The authors explicitly limit the benchmark to Python in this work, so the reported evidence does not establish coverage of software engineering across languages or domains.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **uncertainty**: The evaluation uses one greedy generation per instance, leaving performance under sampling or multiple attempts unmeasured; the paper itself frames this as its evaluation choice.
  - Page 24 · citation: exact
  - Quote: "we only generate a single patch file per instance."

Unresolved questions:

- How well do the benchmark construction and evaluation results generalize to other programming languages, repository types, and less popular or differently maintained projects?
- How sensitive are model rankings and resolution rates to repeated sampling, alternative prompting, or more capable interactive repository tools?
- To what extent do the task selection criteria and associated tests represent the broader range of real software maintenance work, beyond issues that have merged PRs and suitable executable tests?
- Inspection was limited to the supplied paper text and pages; supplementary implementation details and external follow-up evaluations were not independently checked.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
