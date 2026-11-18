# T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**pyagent_react · ok**

3 model calls · 1 reads · 48.39 s · $0.002753

3 decisions · 3 tool calls · 12004 input tokens (8720 cached) · 4512 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

SWE-bench introduces a substantial benchmark of real GitHub issue resolution using codebase snapshots and test-based patch evaluation. Its reported scale and low model success rates make it a promising evaluation contribution. This assessment is provisional: only page one was inspected, leaving curation, test validity, experimental controls, and scope limitations uncertain.

- **strength**: The benchmark draws tasks from real issues and corresponding pull requests across multiple Python repositories.
  - Page 1 · citation: exact
  - Quote: "across 12 popular Python repositories."

- **strength**: The abstract reports low success rates for the evaluated models, though the underlying experimental details were not inspected.
  - Page 1 · citation: exact
  - Quote: "Claude 2 and GPT-4 solve a mere4.8% and 1.7% of instances"

- **uncertainty**: The page describes test-based evaluation, but does not establish whether the tests are representative or how issue-to-PR links were validated.
  - Page 1 · citation: exact
  - Quote: "models generate a patch that is evaluated against real tests."

Unresolved questions:

- How were dataset instances, issue-to-PR links, and test-based evaluations curated and validated?
- What experimental settings, comparisons, and analyses support the reported results?
- What limitations and scope boundaries are discussed in the uninspected pages?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | submit_review `{"review": {"score": 0.62, "observations": 3}}` | Submit a provisional assessment using the supplied first page and acknowledge uninspected evidence. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1]); #2: hyphenation_ambiguous (pages [1]) | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 1, "end": 1}` | Inspect page one directly to resolve ambiguous citation matching. | read pages [1] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.62, "observations": 3}}` | Resubmit with short exact excerpts copied from the observed page. | review accepted | [event 16](trace.jsonl#L16) |
