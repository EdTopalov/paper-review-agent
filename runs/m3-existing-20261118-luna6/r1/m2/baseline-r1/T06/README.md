# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**baseline · ok**

1 model calls · 0 reads · 6.47 s · $0.004631

1 decisions · 0 tool calls · 35056 input tokens (0 cached) · 498 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

SWE-bench introduces a large, execution-validated benchmark of repository-level software engineering tasks built from real GitHub issues and merged pull requests, and reports early baselines showing that tested language models solve few tasks. Its core contribution is a practical benchmark and construction/evaluation pipeline, supported by substantial dataset characterization and model experiments; the paper also identifies important constraints in its task selection and test-based measure.

- **strength**: The paper contributes a sizeable benchmark of realistic, multi-file tasks and describes a concrete filtering pipeline to produce the final instances.
  - Page 2 · citation: hyphenation_ambiguous
  - Quote: "Through these stages of filtering, the original 90,000 PRs are filtered down to the 2,294 task instances which comprise SWE-bench."

- **strength**: Execution-based validation provides a meaningful correctness check: task instances must include tests that change from failing to passing with the reference fix.
  - Page 18 · citation: not_found
  - Quote: "we then check that there exists at least one ti where s changes from fail to pass."

- **limitation**: The authors explicitly bound the benchmark’s language coverage to Python, so the reported findings do not establish performance on other languages or domains.
  - Page 9 · citation: exact
  - Quote: "SWE-bench task instances are all in Python"

- **limitation**: Passing the benchmark’s tests is not sufficient evidence of production-quality fixes; the authors acknowledge that this evaluation alone cannot ensure reliability or code quality.
  - Page 9 · citation: whitespace
  - Quote: "relying solely on this method is insufficient to guarantee reliable performance of model generations"

Unresolved questions:

- How well do the benchmark’s issue and test selection criteria represent the broader distribution of software maintenance work, beyond the selected popular Python repositories?
- How stable are model rankings under alternative test suites or human assessment of correctness, maintainability, and completeness?
- I inspected the supplied main text and appendix excerpts, but not the underlying released code or dataset; implementation details and instance-level validity therefore remain unverified.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
