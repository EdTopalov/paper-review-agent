# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

11 model calls · 4 reads · 37.12 s · $0.004211

11 decisions · 11 tool calls · 99355 input tokens (86024 cached) · 3439 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

Plan-and-Solve prompting asks an LLM to plan subtasks and then execute them, while PS+ adds instructions for variable extraction and intermediate calculations. In GPT-3 experiments, the authors report gains over zero-shot CoT across ten reasoning datasets and competitive arithmetic performance versus few-shot CoT. This is a practical prompt-design contribution, with evidence bounded by the tested model and benchmarks.

- **strength**: The paper clearly identifies the central plan-and-execute intervention.
  - Page 2 · citation: normalized
  - Quote: "we propose Plan-and-Solve (PS) Prompting."

- **strength**: The reported arithmetic results show PS+ above zero-shot CoT on average and close to manual few-shot CoT.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **limitation**: The reported main paper uses one GPT-3 engine; these inspected passages do not establish transfer to other model families.
  - Page 5 · citation: whitespace
  - Quote: "text-davinci-003 engine for GPT-3 in the main paper."

Unresolved questions:

- Are the improvements robust across other model families, sizes, prompt formulations, and independent replications?
- Only pages 2–7 were inspected, not the remainder or appendix; what additional robustness evidence and limitations are reported there?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Experiments"}` | Locate the paper's evaluation section to inspect datasets and reported results. | 4 matches on pages [2, 5, 6] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect experiment setup, quantitative comparisons, and analysis passages. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 3}` | Review the proposed prompt design and its stated motivation and scope. | read pages [2, 3] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers method, setup, cross-task results, and error analysis; submit a balanced paper assessment. | citation_validation_failed; #3: not_found; #4: wrong_page (pages [6]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Resubmit with corrected verbatim citations from pages inspected and preserve explicit uncertainty about the limited inspected material. | citation_validation_failed; #3: hyphenation_ambiguous (pages [5]); #4: wrong_page (pages [6]) | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 5, "end": 5}` | Verify exact wording on the model implementation page for a properly supported scope observation. | read pages [5] | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit final evidence-based review using exact quotations from observed pages. | citation_validation_failed; #3: hyphenation_ambiguous (pages [5]); #4: wrong_page (pages [6]) | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Final submission with only exact, observed quotations and page citations; avoid hyphenated line-break passages. | citation_validation_failed; #1: not_found; #3: hyphenation_ambiguous (pages [5]); #4: wrong_page (pages [6]) | [event 40](trace.jsonl#L40) |
| 9 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit review with exact short quotations copied from inspected page text; state limitations and inspection gap. | citation_validation_failed; #4: wrong_page (pages [6]) | [event 45](trace.jsonl#L45) |
| 10 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit final assessment with citations using exact quotations from observed pages; all claims remain within inspected material. | citation_validation_failed; #4: wrong_page (pages [6]) | [event 50](trace.jsonl#L50) |
| 11 | submit_review `{"review": {"score": 0.72, "observations": 3}}` | Submit concise final review using verified quotations from inspected pages and acknowledge uninspected remainder. | review accepted | [event 55](trace.jsonl#L55) |
