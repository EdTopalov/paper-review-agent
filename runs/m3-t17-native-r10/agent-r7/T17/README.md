# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

8 model calls · 4 reads · 23.89 s · $0.002825

8 decisions · 8 tool calls · 56658 input tokens (46232 cached) · 2170 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

The paper proposes a simple zero-shot Plan-and-Solve prompting strategy: ask an LLM to devise a plan and execute it, with PS+ adding instructions to extract variables and calculate intermediate results. On GPT-3, reported results improve over Zero-shot-CoT across the evaluated math, commonsense, and symbolic datasets, with PS+ approaching few-shot CoT on average for arithmetic. The evidence supports a useful prompting contribution, though it is bounded to the evaluated model and benchmarks, and prompt wording changes multiple things at once.

- **strength**: The method is clearly introduced as a way to address missing reasoning steps.
  - Page 2 · citation: normalized
  - Quote: "To address the issue of Zero-shot-CoT caused by missing reasoning steps, we propose Plan-and-Solve (PS) Prompting."

- **strength**: Reported performance gains are broad across the tested dataset categories, including gains on both commonsense tasks and both symbolic tasks.
  - Page 6 · citation: exact
  - Quote: "Zero-shot-PS+ (ours) 71.9 65.4"

- **limitation**: The main evaluation uses a single GPT-3 engine and greedy decoding for the standard experiments, so the evidence does not establish generality across model families or decoding settings.
  - Page 5 · citation: whitespace
  - Quote: "the public GPT-3 (Brown et al., 2020) (175B) as the backbone language model"

- **uncertainty**: The prompt comparison supports the utility of detailed instructions but does not isolate the causal contribution of planning from other simultaneous instruction changes.
  - Page 7 · citation: whitespace
  - Quote: "calculate intermediate variables (pay attention to correct numerical calculation and commonsense), solve the problem step by step, and show the answer."

Unresolved questions:

- How well does PS/PS+ transfer to other model families, model sizes, or current LLMs?
- Which individual PS+ instruction accounts for the observed improvements when tested in controlled, one-factor-at-a-time comparisons?
- How robust are the measured gains across repeated runs or alternative benchmark samples? I inspected pages 2–7, not the full paper, appendix, or later discussion, so other relevant qualifications may remain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experimental results"}` | Locate the results section to inspect evaluation evidence and comparisons. | 1 matches on pages [5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Read the reported results and adjacent discussion for concrete performance claims. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 3}` | Inspect the proposed prompt formulation and methods for the paper’s core contribution. | read pages [2, 3] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | The core method, cross-dataset results, and a prompt comparison have been inspected; submit a qualified assessment noting remaining limits. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #3: hyphenation_ambiguous (pages [5]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Correct two citation strings that failed exact validation by using directly observed, verbatim excerpts; retain the evidence-based assessment. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1, 2]); #3: hyphenation_ambiguous (pages [5]) | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 5, "end": 5}` | Verify an exact quotation from the inspected implementation details to replace the failed citation. | read pages [5] | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Citations now use exact text from observed pages; submit the final review with appropriately scoped uncertainty. | citation_validation_failed; #3: hyphenation_ambiguous (pages [5]) | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Replace the final failed quotation with an exact, unhyphenated excerpt from page 5 and complete the assessment. | review accepted | [event 40](trace.jsonl#L40) |
