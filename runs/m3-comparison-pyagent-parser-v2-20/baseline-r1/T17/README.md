# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**baseline · ok**

1 model calls · 0 reads · 6.91 s · $0.002582

1 decisions · 0 tool calls · 18064 input tokens (0 cached) · 649 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

The paper proposes Plan-and-Solve prompting, a zero-shot prompting method that asks an LLM to plan subtasks before solving them, and PS+, which adds instructions to extract variables and calculate intermediate results. Across ten reasoning datasets, the reported results generally improve on Zero-shot-CoT, with especially strong gains on several arithmetic tasks. The contribution is simple and practically useful, though the evidence is concentrated on one GPT-3 engine and the approach does not resolve semantic misunderstanding errors.

- **strength**: The evaluation spans ten datasets across arithmetic, commonsense, and symbolic reasoning, and reports improvements over Zero-shot-CoT in each category. On arithmetic tasks, PS+ also exceeds Zero-shot-CoT on all six datasets in the reported table.
  - Page 5 · citation: normalized
  - Quote: "PS+ prompting (i.e., PS prompting with more detailed instructions) consistently outperforms Zero-shot-CoT across all arithmetic reasoning datasets by a large margin."

- **limitation**: The experiments use text-davinci-003 as the main model, so the evidence does not establish that the gains generalize to other model families or current model versions.
  - Page 5 · citation: hyphenation_ambiguous
  - Quote: "We report the results using text-davinci-003 engine for GPT-3 in the main paper."

- **limitation**: The paper reports that semantic misunderstanding errors remain, limiting the method’s demonstrated ability to address the full set of identified failure modes.
  - Page 9 · citation: not_found
  - Quote: "the proposed plan-and-solve prompting can help address the calculation errors and missing-reasoning-step errors, but the semantic misunderstanding errors are still remain."

- **uncertainty**: The error analysis samples 100 GSM8K problems and classifies error types, but the excerpt does not establish how reliable or reproducible those classifications are.
  - Page 7 · citation: hyphenation_ambiguous
  - Quote: "Subsequently, we analyze and determine the error types of all these problems as shown in Table 6."

Unresolved questions:

- Do PS and PS+ retain their gains across other model families, model sizes, and newer model versions?
- How sensitive are the reported results to prompt wording and to independent judgments of error categories?
- Can prompting reduce semantic misunderstanding errors, or are these errors largely unaffected by plan-and-solve instructions?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
