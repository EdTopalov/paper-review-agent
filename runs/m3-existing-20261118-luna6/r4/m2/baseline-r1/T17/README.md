# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**baseline · ok**

1 model calls · 0 reads · 7.84 s · $0.000548

1 decisions · 0 tool calls · 18064 input tokens (18061 cached) · 735 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

The paper proposes Plan-and-Solve prompting, a zero-shot prompting strategy that asks an LLM to devise a plan before solving a problem, and PS+ adds instructions to identify variables and calculate intermediate results. Experiments with GPT-3 across ten datasets show consistent gains over Zero-shot-CoT, with PS+ approaching few-shot CoT on arithmetic tasks. The results make a useful case for prompt design as a practical way to improve reasoning-task accuracy, though the evaluation is limited to one model family and reported benchmark settings.

- **strength**: The evaluation spans arithmetic, commonsense, and symbolic reasoning datasets. PS+ improves on Zero-shot-CoT across the reported datasets, and the paper also compares against few-shot methods on several tasks.
  - Page 6 · citation: exact
  - Quote: "Zero-shot-PS+ (ours) 71.9 65.4"

- **strength**: The prompt variants and error analysis provide some evidence about how prompt content relates to performance, rather than reporting only aggregate accuracy.
  - Page 7 · citation: normalized
  - Quote: "PS+ prompting achieves the least calculation (5%) and missing-step (7%) errors"

- **limitation**: The reported evaluation uses GPT-3, specifically text-davinci-003 in the main paper, so the evidence does not establish whether the gains transfer to other models. The authors also explicitly note that prompts require careful design and semantic misunderstandings remain.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts"

- **uncertainty**: There is an internal discrepancy in the reported Last Letters baseline: the table and accompanying text give different Zero-shot-CoT accuracies. The supplied paper does not explain which value is intended.
  - Page 6 · citation: exact
  - Quote: "Zero-shot-CoT 64.8 96.8"

Unresolved questions:

- How robust are the reported gains across different model families, model sizes, and prompt formulations?
- Would controlled evaluations on additional samples or repeated runs preserve the reported improvements, particularly where the accuracy differences are modest?
- Which Last Letters Zero-shot-CoT result is correct: 64.8% in Table 4 or 65.2% in the accompanying text?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
