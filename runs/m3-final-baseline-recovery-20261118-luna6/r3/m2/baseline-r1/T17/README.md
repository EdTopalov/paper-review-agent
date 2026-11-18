# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**baseline · ok**

1 model calls · 0 reads · 9.69 s · $0.000548

1 decisions · 0 tool calls · 18064 input tokens (18061 cached) · 734 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

The paper proposes Plan-and-Solve prompting, which asks an LLM to plan a solution and then execute it, with PS+ adding instructions to extract variables and calculate intermediate results. On ten reasoning datasets, experiments with GPT-3 show improvements over zero-shot CoT, including gains in arithmetic, commonsense, and symbolic reasoning. The evidence is useful and spans several task types, but the central evaluation is limited to one model family and the paper itself notes that semantic misunderstandings persist.

- **strength**: The evaluation covers ten datasets across arithmetic, commonsense, and symbolic reasoning, and reports gains over zero-shot CoT across those task categories.
  - Page 2 · citation: whitespace
  - Quote: "We evaluate our proposed prompting on six math reasoning datasets"

- **strength**: The paper provides some analysis beyond aggregate accuracy, comparing error categories and prompt variants; on the sampled GSM8K problems, PS+ has fewer reported calculation and missing-step errors than zero-shot CoT.
  - Page 7 · citation: normalized
  - Quote: "PS+ prompting achieves the least calculation (5%) and missing-step (7%) errors"

- **limitation**: The reported implementation uses one GPT-3 engine, so the evidence does not establish whether the gains transfer to other model families or model sizes.
  - Page 5 · citation: not_found
  - Quote: "we report the results using text-davinci-003 engine for GPT-3 in the main paper."

- **uncertainty**: The approach does not resolve semantic misunderstanding in the reported scope; how much prompt adaptation can address this error type remains open.
  - Page 9 · citation: hyphenation_ambiguous
  - Quote: "the semantic misunderstanding errors are still remain."

Unresolved questions:

- Do PS and PS+ retain their advantages across other model families, model sizes, and evaluation settings?
- How robust are the results to prompt wording and prompt-selection choices, given the reported sensitivity of GPT-3 to prompt expressions?
- Can prompting reduce semantic misunderstanding errors, or does improvement on those errors require changes beyond prompting?
- This assessment is based only on the supplied paper; the reported experiments and analyses were not independently reproduced.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
