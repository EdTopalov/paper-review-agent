# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · error**

8 model calls · 3 reads · 28.25 s · $0.002833

8 decisions · 8 tool calls · 53859 input tokens (42483 cached) · 2023 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

Error: `{"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"}`

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "ten datasets"}` | Locate the paper's evaluation results and dataset scope. | 2 matches on pages [1, 8] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect method definition and experimental setup details. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 8}` | Check reported outcomes, experimental comparisons, and stated scope. | read pages [6, 7, 8] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Sufficient evidence gathered on method, benchmark results, and evaluation scope; submit a balanced assessment. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #3: wrong_page (pages [6]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct citation mismatch using verbatim excerpts on the observed pages and finalize assessment. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #3: wrong_page (pages [6]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Resubmit with exact simple quotes from observed evidence; all observations cite the supplied PDF excerpts. | citation_validation_failed; #1: not_found; #2: hyphenation_ambiguous (pages [6]); #3: wrong_page (pages [6]) | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Finalize using exact, short quotes verified from the observed excerpts; ensure each citation is page-correct. | citation_validation_failed; #2: hyphenation_ambiguous (pages [6]); #3: wrong_page (pages [6]) | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct page citations with exact, uncomplicated phrases copied from the excerpts and submit the completed assessment. | citation_validation_failed; #3: wrong_page (pages [6]) | [event 40](trace.jsonl#L40) |
| — | run_error | | {"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"} | [event 43](trace.jsonl#L43) |
