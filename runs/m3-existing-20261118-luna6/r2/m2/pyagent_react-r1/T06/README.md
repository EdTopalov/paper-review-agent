# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**pyagent_react · ok**

3 model calls · 1 reads · 33.18 s · $0.002111

3 decisions · 3 tool calls · 14754 input tokens (10190 cached) · 2878 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

SWE-bench makes a substantial contribution by operationalizing real GitHub issue resolution as a patch-generation benchmark across 12 Python repositories. The reported evaluations show low resolution rates and expose retrieval and context-localization challenges. Evidence is useful but bounded by the evaluation setup, including a partial GPT-4 sample and an oracle context that is explicitly imperfect.

- **strength**: The benchmark includes tasks with varied and sometimes extensive code changes, supporting its focus on repository-level engineering rather than only short code completion.
  - Page 4 · citation: exact
  - Quote: "# Files edited 1.7 31"

- **strength**: Results indicate retrieval/context matters; the collapsed-oracle evaluation also reports improved resolution for some models.
  - Page 6 · citation: exact
  - Quote: "Claude 2 from 4.8% to 5.9%."

- **limitation**: The reference-file oracle is useful as a diagnostic but is not a fully comprehensive ideal-context condition; the paper notes that edited files may omit necessary context.
  - Page 4 · citation: whitespace
  - Quote: "edited files alone may not include all the required context to understand exactly how software will behave when interacting with unseen parts of the code."

- **limitation**: GPT-4 evidence is based on a subset rather than the full benchmark, limiting direct interpretation of its reported resolution rate as a full-set estimate.
  - Page 6 · citation: whitespace
  - Quote: "Due to budget constraints we evaluate GPT-4 on a 25% random subset of SWE-bench"

Unresolved questions:

- How sensitive are results to alternative retrieval methods, prompts, and execution budgets beyond the settings summarized here?
- How representative are the task mix and reported rates beyond the selected Python repositories?
- Only the supplied first page and excerpts from pages 4–6 were inspected; other methodology, results, and stated limitations remain unreviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 4, "end": 6}` | Inspect benchmark construction and task validation details. | read pages [4, 5, 6] | [event 6](trace.jsonl#L6) |
| 2 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Use the supplied excerpts from pages 4–6 to assess benchmark evidence and its stated evaluation caveats. | citation_validation_failed; #2: not_found | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Correct the unmatched page 6 citation using an exact excerpt from the supplied text. | review accepted | [event 16](trace.jsonl#L16) |
