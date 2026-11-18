# T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering

**agent · ok**

7 model calls · 3 reads · 22.63 s · $0.002567

7 decisions · 7 tool calls · 46123 input tokens (35622 cached) · 1840 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AlphaCodium presents a practical multi-stage, test-driven inference workflow for code generation, combining problem analysis, generated tests, and iterative execution/fixing. On CodeContests it reports gains over direct prompting across several models and splits. It is a useful inference methodology, but the evidence inspected is concentrated on this benchmark; comparisons to prior systems have reproducibility and protocol caveats. I inspected pages 6–10 and searched for pass@5 results; other methodological details and earlier pages were not reviewed closely.

- **strength**: The flow reports substantial direct-prompt improvements; GPT-4 validation pass@5 rises from 19% to 44%.
  - Page 7 · citation: whitespace
  - Quote: "For GPT-4 on the validation set, for example, the pass@5 score improves from 19% to 44% - x2.3 improvement."

- **strength**: Test anchors are intended to prevent fixing code in a way that breaks tests already known to pass.
  - Page 6 · citation: whitespace
  - Quote: "As a result, the test anchors will protect us against an incorrectly fixed code."

- **limitation**: The authors note that prior-work comparisons face evaluation subtleties, so reported cross-work superiority should be interpreted cautiously.
  - Page 7 · citation: exact
  - Quote: "There are subtleties when evaluating results."

Unresolved questions:

- How well does the workflow transfer to code-generation settings beyond CodeContests?
- How much do the individual stages contribute to the observed gains?
- How robust are results to model/API changes and benchmark-level variance?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "pass@5"}` | Locate reported performance results and evaluation details. | 8 matches on pages [1, 2, 7] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 6, "end": 8}` | Inspect evaluation tables, comparison details, and caveats on pages 6–8. | read pages [6, 7, 8] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 9, "end": 10}` | Inspect limitations and concluding scope statements on the final pages. | read pages [9, 10] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence includes the reported benchmark tables, comparison caveats, conclusion, and an appendix example of unsuccessful alternatives. | citation_validation_failed; #3: hyphenation_ambiguous (pages [8]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Resubmit with the exact benchmark scope quote observed on page 8. | citation_validation_failed; #3: hyphenation_ambiguous (pages [8]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Revise the unsupported scope citation to the exact conclusion statement observed on page 8. | citation_validation_failed; #3: hyphenation_ambiguous (pages [8]) | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 3}}` | Remove the ambiguous citation and submit only observations with quotes verified exactly in inspected excerpts. | review accepted | [event 35](trace.jsonl#L35) |
