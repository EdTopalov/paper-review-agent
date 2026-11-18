# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

12 model calls · 5 reads · 39.64 s · $0.005877

12 decisions · 12 tool calls · 117410 input tokens (89744 cached) · 3118 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.7

The paper introduces Plan-and-Solve prompting: a zero-shot template that elicits planning before solution steps, with PS+ adding variable extraction and calculation guidance. Experiments on GPT-3 report improvements over Zero-shot-CoT across ten reasoning datasets and competitive math results against few-shot methods. It is useful, broadly tested prompt-level work, but evidence is limited to one model setup and a modest error-analysis sample.

- **strength**: The math table reports PS+ above Zero-shot-CoT across the six listed datasets.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **strength**: The paper situates its comparison against three types of baselines.
  - Page 5 · citation: whitespace
  - Quote: "We compare our proposed zero-shot PS and PS+ prompting methods with three types of prompting baselines:"

- **limitation**: The main-paper implementation names one GPT-3 engine, leaving transfer across model families unresolved.
  - Page 5 · citation: exact
  - Quote: "text-davinci-003 engine for GPT-3"

Unresolved questions:

- Do the gains transfer to other model families and sizes?
- How stable are the reported differences across repeated runs or alternate samples?
- I inspected pages 1–7 and 15–16, not the remainder of the paper and appendix; additional methodological details or limitations may appear there.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Experimental Results"}` | Locate the paper’s evaluation evidence and reported comparisons. | 1 matches on pages [5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect method details, motivation, and evaluation setup. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Check quantitative results, comparison strength, and experimental reporting. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 15, "end": 16}` | Inspect any author-stated limitations and conclusion for scope context. | read pages [15, 16] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.7, "observations": 4}}` | Evidence covers proposed prompt, main comparative results, error analysis, and inspected scope; submit a calibrated paper assessment. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #3: not_found; #4: wrong_page (pages [6]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.7, "observations": 4}}` | Resubmit with verbatim quotes copied exactly from the observed PDF excerpts and corrected page-specific evidence. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #3: not_found; #4: wrong_page (pages [6]) | [event 30](trace.jsonl#L30) |
| 7 | read_pages `{"start": 2, "end": 2}` | Verify exact page-2 phrasing to resolve citation validation and support the method observation. | read pages [2] | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.7, "observations": 4}}` | Submit a corrected assessment with short exact excerpts copied verbatim from observed pages. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #3: hyphenation_ambiguous (pages [5]); #4: wrong_page (pages [6]) | [event 41](trace.jsonl#L41) |
| 9 | submit_review `{"review": {"score": 0.7, "observations": 4}}` | Finalize using exact short quotes that avoid line-wrap hyphenation ambiguities in prior citation checks. | citation_validation_failed; #1: not_found; #4: wrong_page (pages [6]) | [event 47](trace.jsonl#L47) |
| 10 | submit_review `{"review": {"score": 0.7, "observations": 4}}` | Submit the assessment using only validated verbatim excerpts from observed pages, with cautious uncertainty about uninspected sections. | citation_validation_failed; #4: wrong_page (pages [6]) | [event 53](trace.jsonl#L53) |
| 11 | submit_review `{"review": {"score": 0.7, "observations": 4}}` | Finalize with citations only from already validated observed passages; second limitation cites the inspected page-7 sample wording exactly. | citation_validation_failed; #4: wrong_page (pages [6]) | [event 59](trace.jsonl#L59) |
| 12 | submit_review `{"review": {"score": 0.7, "observations": 3}}` | Complete review with the already validated citations and omit any disputed citation so all evidence remains verifiable. | review accepted | [event 65](trace.jsonl#L65) |
