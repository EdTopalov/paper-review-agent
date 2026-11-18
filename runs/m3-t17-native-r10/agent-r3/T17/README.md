# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · error**

8 model calls · 4 reads · 22.11 s · $0.003123

8 decisions · 8 tool calls · 67150 input tokens (54203 cached) · 1976 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

Error: `{"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"}`

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "results"}` | Locate the paper's experimental results and comparison evidence. | 8 matches on pages [2, 3, 5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect experimental setup, reported comparisons, and adjacent discussion. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 9}` | Check stated limitations and conclusion to contextualize scope and evidence. | read pages [8, 9] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers the proposal, main benchmark results, qualitative error analysis, and author-stated limitations; submit a grounded reading-club assessment. | citation_validation_failed; #1: hyphenation_ambiguous (pages [8]); #2: not_found; #4: not_found | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct citation text to exact observed page wording and finalize assessment. | citation_validation_failed; #1: hyphenation_ambiguous (pages [8]); #2: not_found; #4: hyphenation_ambiguous (pages [9]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Use short exact quotations from observed pages to resolve citation verification and complete the review. | citation_validation_failed; #1: not_found; #4: hyphenation_ambiguous (pages [9]) | [event 30](trace.jsonl#L30) |
| 7 | read_pages `{"start": 6, "end": 7}` | Check exact page wording for short quotations supporting accuracy and error-analysis observations. | read pages [6, 7] | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Finalize with verified quotations from the observed results and limitations pages. | citation_validation_failed; #4: hyphenation_ambiguous (pages [9]) | [event 40](trace.jsonl#L40) |
| — | run_error | | {"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"} | [event 43](trace.jsonl#L43) |
