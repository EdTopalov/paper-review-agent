# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · error**

8 model calls · 4 reads · 19.94 s · $0.002783

8 decisions · 8 tool calls · 54736 input tokens (42791 cached) · 1774 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

Error: `{"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"}`

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experimental results"}` | Locate the paper's reported evaluation results to assess empirical support. | 1 matches on pages [5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect method details and the motivation/error analysis supporting the proposed prompting approach. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Review quantitative comparisons and experimental setup for strength and scope of evidence. | read pages [5, 6] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 7, "end": 8}` | Inspect limitations and error-analysis methodology to distinguish evidence from unresolved questions. | read pages [7, 8] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers method, benchmark results, and error analysis; submit a balanced paper assessment while noting inspection gaps. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #4: not_found | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct invalid quote citations using exact observed wording; retain evidence-based assessment. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #4: not_found | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Replace ambiguous hyphenated and unobserved citation text with exact, short phrases from inspected pages. | citation_validation_failed; #4: wrong_page (pages [6]) | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the last quote to an exact phrase on page 7 and submit the completed assessment. | citation_validation_failed; #4: wrong_page (pages [6]) | [event 40](trace.jsonl#L40) |
| — | run_error | | {"type": "RuntimeError", "status_code": null, "code": "model_decision_budget_exhausted"} | [event 43](trace.jsonl#L43) |
