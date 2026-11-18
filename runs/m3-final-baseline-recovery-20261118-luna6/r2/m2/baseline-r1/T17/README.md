# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**baseline · ok**

1 model calls · 0 reads · 6.34 s · $0.000409

1 decisions · 0 tool calls · 18064 input tokens (18061 cached) · 456 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

The paper proposes Plan-and-Solve prompting: a zero-shot prompt that asks an LLM to plan a multi-step solution and then execute it, with PS+ adding instructions to identify variables and calculate intermediate results. Experiments on ten reasoning datasets using GPT-3 show consistent improvements over Zero-shot-CoT, with results sometimes comparable to few-shot CoT. The work offers a simple, broadly tested prompting recipe, though evidence is limited to one model family and does not isolate the contribution of planning from other prompt changes.

- **strength**: The evaluation spans arithmetic, commonsense, and symbolic reasoning; PS+ improves over Zero-shot-CoT on all reported datasets, while retaining a zero-shot setup.
  - Page 2 · citation: whitespace
  - Quote: "We evaluate our proposed prompting on six math reasoning datasets"

- **strength**: The paper includes targeted error analysis that is consistent with fewer calculation and missing-step errors under PS+, while semantic errors remain similar.
  - Page 7 · citation: normalized
  - Quote: "PS+ prompting achieves the least calculation (5%) and missing-step (7%) errors"

- **limitation**: The prompt variants change several instructions together, so the results do not clearly identify which component—planning, variable extraction, or calculation guidance—drives the improvements.
  - Page 7 · citation: hyphenation_ambiguous
  - Quote: "The above results conclude that LLMs are capable of generating high-quality reasoning text when the prompts include more detailed instructions"

- **uncertainty**: The reported experiments use GPT-3 text-davinci-003 as the main backbone, leaving transfer to other model families unestablished in the inspected results.
  - Page 5 · citation: hyphenation_ambiguous
  - Quote: "We report the results using text-davinci-003 engine for GPT-3 in the main paper."

Unresolved questions:

- How much of the improvement comes from explicitly requesting a plan, versus the additional variable-extraction and calculation instructions in PS+?
- Would the gains persist across other model families, model sizes, and current inference settings?
- The inspected pages include main results and prompt tables, but not the complete appendix material for all claimed supplementary experiments; how robust are the results across prompt wording and repeated evaluations?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
