# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**baseline · ok**

1 model calls · 0 reads · 7.97 s · $0.000518

1 decisions · 0 tool calls · 18064 input tokens (18061 cached) · 675 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

The paper introduces Plan-and-Solve prompting, which asks a language model to plan a solution and then execute it, with PS+ adding instructions to extract variables and calculate intermediate results. On ten reasoning datasets using GPT-3, the authors report that PS+ improves over zero-shot CoT and is competitive with few-shot CoT on arithmetic tasks. The contribution is a simple, practical prompting strategy supported by broad benchmark comparisons, though the evidence is limited to one model family and leaves the source of the gains uncertain.

- **strength**: The evaluation spans ten datasets in arithmetic, commonsense, and symbolic reasoning, and reports improvements over zero-shot CoT across these task types.
  - Page 2 · citation: whitespace
  - Quote: "We evaluate our proposed prompting on six math reasoning datasets"

- **strength**: The authors include analysis beyond aggregate accuracy: a 100-example GSM8K error analysis reports fewer calculation and missing-step errors for PS+ than for zero-shot CoT, while semantic errors remain similar.
  - Page 7 · citation: normalized
  - Quote: "PS+ prompting achieves the least calculation (5%) and missing-step (7%) errors"

- **limitation**: The paper reports using GPT-3 text-davinci-003 for its main results, so the supplied evidence does not establish whether the gains generalize to other model families.
  - Page 5 · citation: not_found
  - Quote: "we report the results using text-davinci-003 engine for GPT-3 in the main paper."

- **uncertainty**: Prompt variants produce different accuracies, but the experiments do not isolate which instruction components cause the gains; the authors also acknowledge that prompt wording requires care.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts"

Unresolved questions:

- Do the results generalize to other model families and newer model versions?
- How much of PS+’s benefit comes from planning, variable extraction, calculation instructions, or their combination?
- How robust are the reported gains to prompt wording and evaluation variation?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
