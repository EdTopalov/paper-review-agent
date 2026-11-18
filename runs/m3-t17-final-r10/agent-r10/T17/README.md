# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

6 model calls · 4 reads · 14.86 s · $0.001699

6 decisions · 6 tool calls · 32404 input tokens (24532 cached) · 977 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper introduces zero-shot Plan-and-Solve prompting: ask an LLM to make a subtask plan, execute it, and extract an answer, with PS+ adding more detailed guidance. Across ten benchmarks using GPT-3 text-davinci-003, PS+ generally improves on Zero-shot-CoT and is competitive with few-shot CoT on math, while the authors acknowledge prompt-design effort and unresolved semantic misunderstandings.

- **strength**: Broad benchmark comparisons show gains over Zero-shot-CoT across task categories, though gains vary by benchmark.
  - Page 6 · citation: exact
  - Quote: "Zero-shot-PS+ (ours) 71.9 65.4"

- **strength**: On arithmetic reasoning, PS+ is reported slightly below manual few-shot CoT and above Auto-CoT on average.
  - Page 5 · citation: normalized
  - Quote: "PS+ prompting yields an aver-age accuracy (76.7%) slightly lower than Manual-CoT (77.6%) but higher than Auto-CoT (75.9%)."

- **limitation**: Prompt design remains effortful because the authors report sensitivity to prompt expressions.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."

- **limitation**: Semantic misunderstanding errors remain unresolved by the proposed approach.
  - Page 9 · citation: normalized
  - Quote: "but the semantic misunderstanding er-rors are still remain."

Unresolved questions:

- How robust are results to alternative prompt wording, model families, and later model versions? The reported evaluation uses GPT-3, and the paper identifies prompt sensitivity.
- How stable are the accuracy differences across repeated runs or independent evaluation? I inspected the main results and limitations, but not the full appendix or all analysis details.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experimental results"}` | Locate reported evaluation outcomes and datasets to assess supporting evidence. | 1 matches on pages [5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 6}` | Inspect method setup and adjacent experimental results, including comparison details. | read pages [4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Check the paper’s stated scope and limitations before final assessment. | 2 matches on pages [9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Read discussion and limitations pages to distinguish stated boundaries from unresolved evidence gaps. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence covers the approach, benchmark comparisons, and explicitly stated limitations; submit a calibrated independent assessment. | citation_validation_failed; #2: not_found; #4: hyphenation_ambiguous (pages [9]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct two citations using exact observed wording on pages 5 and 9, then finalize the review. | review accepted | [event 30](trace.jsonl#L30) |
