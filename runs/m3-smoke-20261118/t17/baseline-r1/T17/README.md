# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**baseline · ok**

1 model calls · 0 reads · 11.03 s · $0.002568

1 decisions · 0 tool calls · 18064 input tokens (0 cached) · 621 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

The paper proposes Plan-and-Solve (PS) prompting, which asks a language model to plan a solution before carrying out its steps; PS+ adds instructions to extract variables and calculate intermediate results. Tests across ten reasoning datasets show gains over zero-shot chain-of-thought prompting on the reported GPT-3 setup, with some results approaching few-shot CoT. The evidence is useful but scoped to one model family and leaves robustness to prompt and model changes unresolved.

- **strength**: Evaluation spans arithmetic, commonsense, and symbolic reasoning, and PS+ improves over zero-shot CoT on the reported datasets. The breadth is a notable strength, though performance varies by task and does not establish generality beyond the evaluated setup.
  - Page 2 · citation: whitespace
  - Quote: "We evaluate our proposed prompting on six math reasoning datasets"

- **strength**: The authors compare prompt variants and report a small error analysis, offering some evidence about what the added instructions may change. These analyses are limited in scale and do not by themselves establish the proposed explanation for the accuracy gains.
  - Page 7 · citation: normalized
  - Quote: "PS+ prompting achieves the least calculation (5%) and missing-step (7%) errors"

- **limitation**: The main experiments use GPT-3 text-davinci-003, so the paper does not establish whether the gains transfer to other model families or versions.
  - Page 5 · citation: hyphenation_ambiguous
  - Quote: "We report the results using text-davinci-003 engine for GPT-3 in the main paper."

- **uncertainty**: The authors acknowledge that prompt wording matters. Although the appendix reports multiple prompt variants, the evidence leaves open how reliably the method works under a fixed prompt-selection procedure on new tasks.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts"

Unresolved questions:

- Do the gains hold across other model families, model sizes, and API versions?
- How much do results depend on prompt selection or tuning on the evaluated datasets, and would a prespecified prompt perform similarly on new tasks?
- How stable are the reported accuracy differences across repeated evaluation runs or alternative test samples?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
