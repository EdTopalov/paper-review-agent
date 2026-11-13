# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**baseline · ok**

1 model calls · 0 reads · 5.52 s · $0.002573

1 decisions · 0 tool calls · 18064 input tokens (0 cached) · 631 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

The paper proposes Plan-and-Solve prompting, which asks an LLM to plan a multi-step solution before carrying it out; PS+ adds instructions to identify variables and calculate intermediate results. Tests on ten reasoning datasets using GPT-3 show consistent gains over zero-shot CoT, with PS+ competitive with few-shot CoT on arithmetic tasks. The results are useful evidence for a simple prompting approach, but the evaluation is limited to one model family and the paper itself notes prompt sensitivity and persistent semantic errors.

- **strength**: The reported benchmark results show PS+ outperforming zero-shot CoT across arithmetic, commonsense, and symbolic tasks, with larger gains on several arithmetic datasets.
  - Page 6 · citation: not_found
  - Quote: "PS+ prompting consistently outperforms Zero-shot-CoT across all arithmetic reasoning datasets by a large margin."

- **strength**: The paper compares prompting variants and reports an error analysis, offering some evidence about how added instructions relate to performance rather than presenting only aggregate accuracy.
  - Page 7 · citation: normalized
  - Quote: "PS+ prompting achieves the least calculation (5%) and missing-step (7%) errors"

- **limitation**: The evaluation uses GPT-3, so the supplied evidence does not establish whether the gains generalize to other model families or later models.
  - Page 5 · citation: whitespace
  - Quote: "we use the public GPT-3 (Brown et al., 2020) (175B) as the backbone language model"

- **uncertainty**: The authors acknowledge prompt sensitivity; it remains unclear how robust the reported gains are to prompt wording and how much prompt selection contributes to the results.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts"

Unresolved questions:

- Do the improvements transfer to different model families, sizes, and current instruction-tuned models?
- How robust are the results to prompt wording and selection, particularly where the appendix tests multiple prompt variants?
- Would the error reductions hold on larger or independently sampled sets? The reported error analysis is based on 100 GSM8K examples.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
