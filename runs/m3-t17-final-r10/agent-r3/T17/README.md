# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

9 model calls · 5 reads · 24.91 s · $0.004028

9 decisions · 9 tool calls · 62884 input tokens (41883 cached) · 2024 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

The paper proposes Plan-and-Solve prompting: ask a model to devise a decomposition plan, then carry it out, with PS+ adding detailed guidance. On ten arithmetic, commonsense, and symbolic datasets using GPT-3, reported results generally improve over zero-shot CoT; PS+ is competitive with few-shot approaches on arithmetic. This simple prompting contribution has broad benchmark coverage, while the authors acknowledge prompt-design effort and unresolved semantic misunderstanding errors. Inspection focused on the method, selected main results, and stated limitations; the full appendix and all analyses were not inspected.

- **strength**: PS+ makes the method's more detailed guidance concrete by requiring intermediate calculations and attention to commonsense.
  - Page 2 · citation: whitespace
  - Quote: "calculate intermediate results (pay atten- tion to calculation and commonsense)"

- **strength**: Reported PS+ arithmetic results surpass zero-shot CoT on each listed dataset, and the average is above Auto-CoT.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **limitation**: The authors acknowledge that prompt design requires care because GPT-3 is sensitive to prompt wording.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."

- **limitation**: Semantic misunderstanding remains unresolved by the proposed approach, according to the authors.
  - Page 9 · citation: whitespace
  - Quote: "the semantic misunderstanding er- rors are still remain."

Unresolved questions:

- How robust are PS/PS+ to wording changes and transfer beyond the evaluated GPT-3 models?
- Would repeated runs or uncertainty estimates alter reported margins, particularly smaller differences?
- How much of PS+ gains derive from planning itself versus its additional detailed instructions?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "Experiments"}` | Locate the evaluation section to inspect datasets, comparisons, and reported evidence. | 4 matches on pages [2, 5, 6] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 6}` | Inspect experimental setup, main quantitative comparisons, and supplementary result analysis. | read pages [4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "Limitations"}` | Check whether the paper explicitly discusses limitations or scope boundaries. | 2 matches on pages [9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 9}` | Read the explicit limitations verbatim to judge scope and cite stated weaknesses. | read pages [9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Evidence covers the proposed prompt, reported cross-task comparisons, and the authors' stated limitations; submit an independently grounded assessment. | citation_validation_failed; #1: not_found | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Correct the first quotation to match the observed page text exactly; all other cited evidence was verified. | citation_validation_failed; #1: not_found | [event 30](trace.jsonl#L30) |
| 7 | read_pages `{"start": 2, "end": 2}` | Retrieve exact displayed page wording for the prompting description to repair the citation. | read pages [2] | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Use the exact page-2 wording from the newly read text and submit the evidence-grounded review. | citation_validation_failed; #1: not_found | [event 41](trace.jsonl#L41) |
| 9 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | The citation checker rejected the page-2 excerpt, so cite only the exact PS+ wording newly observed there and retain already validated evidence. | review accepted | [event 47](trace.jsonl#L47) |
