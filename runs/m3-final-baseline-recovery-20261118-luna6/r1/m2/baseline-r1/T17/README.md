# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**baseline · ok**

1 model calls · 0 reads · 8.90 s · $0.000534

1 decisions · 0 tool calls · 18064 input tokens (18061 cached) · 706 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

The paper proposes Plan-and-Solve prompting, which asks a language model to plan a decomposition and then execute it; PS+ adds instructions to identify variables and calculate intermediate results. On ten reasoning datasets, experiments with GPT-3 show improved accuracy over zero-shot CoT, with PS+ competitive with few-shot CoT on arithmetic tasks. The evidence is promising but scoped to one model family and relies on reported accuracy without uncertainty estimates. I inspected the supplied pages, including the main results and appendices; I did not inspect any material beyond them.

- **strength**: The approach is simple to apply and is evaluated across arithmetic, commonsense, and symbolic reasoning rather than only one benchmark type.
  - Page 2 · citation: whitespace
  - Quote: "We evaluate our proposed prompting on six math reasoning datasets"

- **strength**: Reported results show consistent improvements over zero-shot CoT, with PS+ exceeding it on all six arithmetic datasets and both commonsense datasets.
  - Page 5 · citation: not_found
  - Quote: "PS+ prompting consistently outperforms Zero-shot-CoT across all arithmetic reasoning datasets by a large margin."

- **limitation**: The evaluation uses GPT-3 text-davinci-003 as its main backbone, so the evidence does not establish that the gains transfer to other model families.
  - Page 5 · citation: not_found
  - Quote: "we report the results using text-davinci-003 engine for GPT-3 in the main paper."

- **uncertainty**: The reported accuracy comparisons do not provide uncertainty estimates, and the error analysis is based on a randomly sampled set of 100 GSM8K examples; the stability of these findings across samples or runs is unclear.
  - Page 7 · citation: not_found
  - Quote: "we first randomly sample 100 problems from GSM8K"

Unresolved questions:

- How well do PS and PS+ transfer to other language model families and model scales?
- How much do results vary across independent runs or alternative samples, particularly for the error-category analysis?
- Which parts of PS+ account for the gains, and how robust are they to changes in prompt wording?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
