# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

7 model calls · 5 reads · 15.72 s · $0.002795

7 decisions · 7 tool calls · 40124 input tokens (23939 cached) · 1109 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper introduces Plan-and-Solve prompting, which asks a model to devise a plan and execute its subtasks; PS+ adds more detailed instructions. On ten reasoning datasets using GPT-3, it reports gains over zero-shot CoT and competitiveness with few-shot CoT on math. The results support a useful prompting contribution, though the evidence is limited to the tested model and tasks, and the paper acknowledges prompt-design effort and persistent semantic errors. I inspected the abstract, core setup and results, and stated limitations, not the full appendix or every experimental detail.

- **strength**: The math table shows PS+ ahead of zero-shot CoT on the reported average, while remaining slightly below manual few-shot CoT.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **strength**: Prompt variations provide a direct comparison suggesting that including plan instructions matters to the tested prompting results.
  - Page 6 · citation: whitespace
  - Quote: "The reason is that Prompt 3 doesn’t include instructions for devise and complete a plan."

- **limitation**: The reported implementation uses GPT-3, so these results alone do not establish generalization across model families.
  - Page 5 · citation: whitespace
  - Quote: "we use the public GPT-3 (Brown et al., 2020) (175B) as the backbone language model"

- **limitation**: The authors identify prompt design effort and unresolved semantic errors as limitations.
  - Page 9 · citation: whitespace
  - Quote: "Second, the proposed plan-and-solve prompting can help ad-\ndress the calculation errors and missing-reasoning-\nstep errors, but the semantic misunderstanding er-\nrors are still remain."

Unresolved questions:

- Do the gains hold for other LLM families, model sizes, or current prompting/API settings?
- How robust are the results to prompt wording and task-specific design choices?
- What further experimental details in the uninspected appendix affect reproducibility or interpretation?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Experimental Results"}` | Locate the evaluation section to inspect datasets, comparisons, and reported evidence. | 1 matches on pages [5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Read main results tables and surrounding interpretation to assess empirical support. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "Limitations"}` | Check whether the paper explicitly states limitations or scope boundaries. | 2 matches on pages [9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 9}` | Read explicit limitations and conclusion to capture scope and unresolved constraints accurately. | read pages [9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence inspected covers the abstract, dataset/method setup, main results, prompt comparisons, and stated limitations; submit an evidence-grounded assessment while noting not all appendix or methodological details were examined. | citation_validation_failed; #1: not_found; #2: wrong_page (pages [6]); #4: hyphenation_ambiguous (pages [9]) | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 6, "end": 6}` | Retrieve verbatim exact result-table and comparison text to correct citation mismatches. | read pages [6] | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit revised review using exact quotes verified on the inspected pages; note scope of pages inspected and remaining uncertainty. | review accepted | [event 36](trace.jsonl#L36) |
