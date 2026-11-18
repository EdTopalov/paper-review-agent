# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

6 model calls · 3 reads · 14.13 s · $0.002125

6 decisions · 6 tool calls · 41267 input tokens (31690 cached) · 1260 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper introduces Plan-and-Solve prompting, which asks an LLM to devise a plan and execute it, with PS+ adding detailed guidance to improve reasoning-step quality. Across ten datasets, GPT-3 results generally improve over zero-shot CoT, with especially strong math performance; evidence is useful but limited to one model family and prompt-sensitive evaluations.

- **strength**: The evaluation spans multiple reasoning categories and ten benchmarks.
  - Page 4 · citation: whitespace
  - Quote: "Arithmetic Reasoning: (1) the GSM8K"

- **strength**: PS+ obtains strong aggregate math benchmark performance relative to zero-shot baselines.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **limitation**: The authors note prompt sensitivity as a practical limitation.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."

- **limitation**: Semantic misunderstanding remains outside the method’s demonstrated remedy.
  - Page 9 · citation: normalized
  - Quote: "the semantic misunderstanding er-rors are still remain."

Unresolved questions:

- How robust are the gains across model families beyond the GPT-3 engines evaluated?
- How much do gains depend on prompt selection or tuning on the evaluation tasks?
- Inspection covered the core setup, main results, and stated limitations, but not the full appendices or all error-analysis details.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Table 1"}` | Locate benchmark results to assess empirical support and scope. | 8 matches on pages [5, 13, 14] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 6}` | Read methods and benchmark setup surrounding evaluation details. | read pages [4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 9, "end": 10}` | Inspect stated limitations and methodological boundaries before scoring. | read pages [9, 10] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers core approach, benchmark results, and authors’ stated limitations; submit a balanced assessment while noting remaining inspection gaps. | citation_validation_failed; #1: hyphenation_ambiguous (pages [4]); #4: hyphenation_ambiguous (pages [9]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct citation text to exact observed wording while preserving the assessment. | citation_validation_failed; #1: hyphenation_ambiguous (pages [4]); #4: hyphenation_ambiguous (pages [9]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Resolve citation validation by using exact continuous excerpts from observed pages; submit final scored review. | review accepted | [event 30](trace.jsonl#L30) |
