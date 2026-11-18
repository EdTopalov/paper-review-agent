# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · error**

8 model calls · 3 reads · 26.75 s · $0.003032

8 decisions · 8 tool calls · 63498 input tokens (52541 cached) · 2324 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

Error: `{"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"}`

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Results"}` | Locate the paper's evaluation results to assess evidence for its prompting contribution. | 8 matches on pages [2, 3, 5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect experimental setup and main quantitative results, including scope of evaluated models and datasets. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 12, "end": 14}` | Inspect the authors' stated limitations and conclusion to ground scope and unresolved questions. | read pages [12, 13, 14] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | The inspected abstract, methods/results, and prompt-analysis tables support an evidence-based assessment; remaining questions concern generality beyond tested conditions. | citation_validation_failed; #1: wrong_page (pages [5]); #2: not_found; #3: not_found; #4: wrong_page (pages [6]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct citation mismatches using exact observed wording from inspected pages and finalize the review. | citation_validation_failed; #3: hyphenation_ambiguous (pages [5]); #4: wrong_page (pages [6]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Resolve remaining citation validation issues by using short exact quotes verified in the page excerpts. | citation_validation_failed; #1: hyphenation_ambiguous (pages [5]); #3: hyphenation_ambiguous (pages [5]); #4: wrong_page (pages [6]) | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Finalize with exact short quotations from the inspected excerpts and retain the same supported evaluation. | citation_validation_failed; #4: wrong_page (pages [6]) | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the final quote to the exact sampled-error wording on page 7 and submit the supported assessment. | citation_validation_failed; #4: wrong_page (pages [6]) | [event 40](trace.jsonl#L40) |
| — | run_error | | {"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"} | [event 43](trace.jsonl#L43) |
