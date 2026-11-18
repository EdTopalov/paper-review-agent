# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

11 model calls · 5 reads · 27.98 s · $0.004020

11 decisions · 11 tool calls · 83869 input tokens (65903 cached) · 2300 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes zero-shot Plan-and-Solve prompting, with PS+ adding explicit variable extraction and intermediate-calculation guidance. Reported GPT-3 results across several reasoning task types generally improve on Zero-shot-CoT, particularly on math. This is a practical prompting contribution with broad benchmark comparisons, but prompt sensitivity and semantic errors limit its scope.

- **strength**: PS+ improves over Zero-shot-CoT on the two listed commonsense datasets.
  - Page 6 · citation: exact
  - Quote: "Zero-shot-PS+ (ours) 71.9 65.4"

- **strength**: The math table reports a 76.7 average for PS+, the highest listed average.
  - Page 6 · citation: exact
  - Quote: "76.7"

- **limitation**: The authors explicitly identify prompt sensitivity as requiring careful design.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."

Unresolved questions:

- How robust are gains across prompt wording and models beyond the evaluated GPT-3 setting?
- How much variation occurs across repeated runs and other evaluation conditions? I inspected selected main results and limitations, not every experimental detail or appendix.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Table 1"}` | Locate the reported benchmark results to assess empirical support. | 8 matches on pages [5, 13, 14] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 6, "end": 7}` | Inspect core results and experimental setup reported in the main evaluation. | read pages [6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 15, "end": 16}` | Check stated limitations and conclusion for scope and claims. | read pages [15, 16] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "limitations"}` | Search the paper for an explicit discussion of limitations and experimental scope. | 2 matches on pages [9] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 9, "end": 9}` | Read the full limitations passage so scope boundaries are assessed accurately. | read pages [9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | The main results, error analysis, and stated limitations have been inspected; submit an evidence-based assessment. | citation_validation_failed; #4: hyphenation_ambiguous (pages [9]) | [event 31](trace.jsonl#L31) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the rejected limitation quote with an exact observed passage and finalize the assessment. | citation_validation_failed; #4: hyphenation_ambiguous (pages [9]) | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Use the exact error wording from the inspected limitation page and submit the review. | citation_validation_failed; #4: hyphenation_ambiguous (pages [9]) | [event 43](trace.jsonl#L43) |
| 9 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Finalize with validated exact passages from the inspected PDF pages. | citation_validation_failed; #4: hyphenation_ambiguous (pages [9]) | [event 49](trace.jsonl#L49) |
| 10 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit a final evidence-based assessment using short unhyphenated exact excerpts from observed pages. | citation_validation_failed; #4: hyphenation_ambiguous (pages [9]) | [event 55](trace.jsonl#L55) |
| 11 | submit_review `{"review": {"score": 0.72, "observations": 3}}` | Use only exact, short observed result and prompt-sensitivity excerpts; omit the ambiguous hyphenated error quote. | review accepted | [event 61](trace.jsonl#L61) |
