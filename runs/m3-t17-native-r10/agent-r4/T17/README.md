# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

8 model calls · 4 reads · 21.05 s · $0.002614

8 decisions · 8 tool calls · 56044 input tokens (45953 cached) · 1836 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

The paper proposes a two-stage zero-shot prompt: have an LLM devise a plan, then carry it out, with PS+ adding detailed instructions. GPT-3 results across ten reasoning datasets generally improve over Zero-shot-CoT and are competitive with few-shot CoT on arithmetic. This is a useful prompt-design contribution, though evidence is limited to the tested model and benchmarks, and the authors acknowledge prompt sensitivity and unresolved semantic errors.

- **strength**: The method instructs the model to construct and follow a plan.
  - Page 2 · citation: normalized
  - Quote: "Let’s first understand the problem and devise a plan to solve the problem. Then, let’s carry out the plan and solve the problem step by step"

- **strength**: PS+ improves the reported arithmetic average relative to Zero-shot-CoT.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **limitation**: The evaluation uses GPT-3 as its backbone, leaving generalization across model families unresolved.
  - Page 5 · citation: whitespace
  - Quote: "we use the public GPT-3 (Brown et al., 2020) (175B) as the backbone language model"

- **limitation**: The authors explicitly state that semantic misunderstanding errors persist.
  - Page 9 · citation: whitespace
  - Quote: "We will explore how to ad- dress semantic misunderstanding errors by prompt- ing instead of upgrading LLMs in the future."

Unresolved questions:

- Would gains persist across other model families, sizes, and model versions?
- How sensitive are the results to prompt wording and independent prompt selection?
- I inspected the main results and limitations, but not the full appendix; additional prompt variants and complete error-analysis details remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experiments"}` | Locate the paper's experimental results and evaluation setup. | 4 matches on pages [2, 5, 6] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 6}` | Inspect evaluation protocol, main comparisons, and reported results. | read pages [4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Check whether the paper explicitly states scope limitations. | 2 matches on pages [9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect discussion of error analysis, limitations, and stated scope. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Evidence includes the main benchmark results and explicit limitations; submit a balanced paper assessment. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Resubmit with exact verbatim citation text from the inspected results pages. | citation_validation_failed; #1: not_found; #4: not_found | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Correct the two unmatched quotations using exact observed text from pages 2 and 9. | citation_validation_failed; #4: hyphenation_ambiguous (pages [9]) | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Submit assessment with exact limitations sentence avoiding line-break hyphenation ambiguity. | review accepted | [event 40](trace.jsonl#L40) |
