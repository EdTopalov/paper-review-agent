# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

6 model calls · 4 reads · 13.12 s · $0.001765

6 decisions · 6 tool calls · 33500 input tokens (25536 cached) · 1067 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes zero-shot Plan-and-Solve prompting: ask an LLM to devise a decomposition plan and execute it; PS+ adds explicit guidance intended to reduce calculation errors. GPT-3 evaluations across ten math, commonsense, and symbolic datasets report gains over zero-shot CoT and, in some settings, results near few-shot CoT. This is a useful prompting contribution, bounded by prompt sensitivity and persistent semantic errors.

- **strength**: On the six math datasets, PS+ improves the reported average over zero-shot CoT and is competitive with few-shot manual CoT, though not higher on average.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **strength**: On the listed commonsense datasets PS+ exceeds zero-shot CoT, but remains below few-shot manual CoT.
  - Page 6 · citation: exact
  - Quote: "Zero-shot-PS+ (ours) 71.9 65.4"

- **limitation**: The authors identify prompt-design effort and sensitivity to wording as practical limitations.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."

- **limitation**: The authors state that semantic misunderstanding errors remain, and their qualitative error analysis samples only GSM8K problems.
  - Page 9 · citation: whitespace
  - Quote: "We will explore how to ad- dress semantic misunderstanding errors by prompt- ing instead of upgrading LLMs in the future."

Unresolved questions:

- How well does the approach transfer to model families and sizes beyond the evaluated GPT-3 setting?
- Would error-type changes hold across larger samples and the other task families?
- How much do results vary across repeated runs and prompt wording?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Table 1"}` | Locate the primary quantitative results table and datasets. | 8 matches on pages [5, 13, 14] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 6, "end": 7}` | Inspect main results and experimental setup for evidence and qualifications. | read pages [6, 7] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "Limitations"}` | Check whether authors state explicit limitations or scope boundaries. | 2 matches on pages [9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Review conclusion and limitations, including the stated bounds of the method. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers main benchmark comparisons, error analysis, and authors’ stated limitations; submit an evidence-based assessment. | citation_validation_failed; #4: hyphenation_ambiguous (pages [9]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the ambiguous final quote using an exact limitation sentence observed on page 9. | review accepted | [event 30](trace.jsonl#L30) |
