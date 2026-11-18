# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**baseline · ok**

1 model calls · 0 reads · 7.19 s · $0.002556

1 decisions · 0 tool calls · 18064 input tokens (0 cached) · 597 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

The paper proposes zero-shot Plan-and-Solve prompting, which asks an LLM to make a plan and execute it, with PS+ adding instructions to identify variables and calculate intermediate results. On ten reasoning datasets using GPT-3, the reported results generally improve on Zero-shot-CoT; PS+ is competitive with few-shot CoT on arithmetic tasks. The approach is simple and supported by broad benchmark comparisons, but evidence is limited to a particular model setup and does not establish why the prompting changes work or how well they generalize.

- **strength**: The evaluation covers ten datasets across arithmetic, commonsense, and symbolic reasoning, and reports consistent PS+ gains over Zero-shot-CoT in the presented comparisons.
  - Page 2 · citation: whitespace
  - Quote: "We evaluate our proposed prompting on six math reasoning datasets"

- **strength**: The paper probes error categories on a sampled GSM8K subset, offering some evidence that PS+ reduces calculation and missing-step errors, while not improving semantic-error rates.
  - Page 7 · citation: normalized
  - Quote: "PS+ prompting achieves the least calculation (5%) and missing-step (7%) errors"

- **limitation**: The authors explicitly note that the method does not resolve semantic misunderstanding, an important boundary on the claimed error-mitigation benefit.
  - Page 9 · citation: hyphenation_ambiguous
  - Quote: "the semantic misunderstanding errors are still remain."

- **uncertainty**: The reported implementation uses text-davinci-003, so the supplied results do not establish whether the gains transfer to other models or model families.
  - Page 5 · citation: hyphenation_ambiguous
  - Quote: "We report the results using text-davinci-003 engine for GPT-3 in the main paper."

Unresolved questions:

- Do the gains persist across model families, model sizes, and newer model versions, rather than this GPT-3 setup?
- How robust are the results to prompt wording and benchmark sampling? The paper reports prompt variants, but broader replication or uncertainty estimates are not provided in the inspected pages.
- Would the error reductions persist under independent labeling or a larger error-analysis sample? The paper describes a randomly sampled set of 100 GSM8K examples.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
