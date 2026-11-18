# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**baseline · ok**

1 model calls · 0 reads · 7.69 s · $0.000542

1 decisions · 0 tool calls · 18064 input tokens (18061 cached) · 723 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

The paper proposes Plan-and-Solve prompting, which asks a language model to make a plan and then execute it; PS+ adds instructions such as extracting variables and checking intermediate calculations. On ten reasoning datasets, experiments with GPT-3 report gains over zero-shot CoT, with PS+ approaching few-shot CoT on arithmetic tasks. The work offers a simple, practical prompting strategy and evidence across several task types, while its results are limited to one model family and prompt-sensitive evaluations.

- **strength**: The evaluation spans ten datasets across arithmetic, commonsense, and symbolic reasoning, and reports consistent PS+ improvements over zero-shot CoT on the included tasks.
  - Page 5 · citation: normalized
  - Quote: "PS+ prompting (i.e., PS prompting with more detailed instructions) consistently outperforms Zero-shot-CoT across all arithmetic reasoning datasets by a large margin."

- **strength**: The paper probes possible mechanisms with an error analysis, reporting fewer calculation and missing-step errors for PS+ in its GSM8K sample, while semantic errors remain comparable.
  - Page 7 · citation: not_found
  - Quote: "PS+ prompting achieves the least calculation (5%) and missing-step (7%) errors, and semantic understanding errors comparable to Zero-shot-CoT."

- **limitation**: The authors identify prompt design as a practical constraint: performance depends on carefully chosen wording, making it harder to treat the method as a fixed, general recipe.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."

- **uncertainty**: The reported study uses text-davinci-003 for its main results, so the supplied evidence does not establish whether the gains transfer to other model families or current systems.
  - Page 5 · citation: hyphenation_ambiguous
  - Quote: "We report the results using text-davinci-003 engine for GPT-3 in the main paper."

Unresolved questions:

- How robust are the gains across other model families, model sizes, and prompt formulations?
- Would the reported differences persist across repeated runs or alternative evaluation samples? The supplied paper reports accuracy results, but the inspected material does not establish uncertainty estimates.
- The evidence inspected covers the supplied pages, including the main results and appendix examples; it does not include independent replications or experiments beyond those reported.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
