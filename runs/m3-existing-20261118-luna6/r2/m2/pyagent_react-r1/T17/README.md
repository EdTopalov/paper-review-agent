# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**pyagent_react · ok**

4 model calls · 2 reads · 18.33 s · $0.001426

4 decisions · 3 tool calls · 17030 input tokens (11286 cached) · 1190 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.71

The paper proposes Plan-and-Solve prompting, which asks a language model to formulate a plan and then execute it; PS+ adds instructions to identify variables and calculate intermediate results. Reported evaluations show improvements over zero-shot CoT on a range of reasoning datasets, with especially reduced calculation and missing-step errors. The approach is a simple, useful prompting contribution, but the inspected evidence is bounded by model and prompt sensitivity, and semantic errors remain.

- **strength**: The authors report evaluation across multiple reasoning domains and datasets, giving the proposal broader support than a single benchmark result.
  - Page 2 · citation: exact
  - Quote: "We evaluate our proposed prompting on six\nmath reasoning datasets"

- **strength**: In a 100-example GSM8K error analysis, PS+ has lower reported calculation and missing-step error rates than the zero-shot CoT baseline.
  - Page 7 · citation: whitespace
  - Quote: "PS+ prompting achieves the least calculation (5%) and missing-\nstep (7%) errors"

- **limitation**: The paper explicitly reports that semantic misunderstanding remains unresolved; this is a stated scope boundary, not evidence that the method fails on every such case.
  - Page 9 · citation: exact
  - Quote: "the semantic misunderstanding er-\nrors are still remain."

- **limitation**: The authors acknowledge prompt design effort and sensitivity to expression, which complicates treating the approach as a plug-and-play recipe.
  - Page 9 · citation: exact
  - Quote: "The GPT-3 models\nare sensitive to the expressions in prompts"

Unresolved questions:

- How consistently would the gains hold across model families or versions beyond the GPT-3 evaluations reported in the paper?
- How sensitive are the results to prompt wording and evaluation choices across the full set of datasets?
- I inspected the abstract and selected pages on the method, results, and limitations, not the complete paper; details elsewhere on experimental controls, uncertainty, and dataset-specific outcomes remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect the proposed prompt and evaluation design. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 9}` | Inspect benchmark results and comparisons. | read pages [7, 8, 9] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.71, "observations": 4}}` | Submit a balanced assessment based on the abstract and selected method, results, and limitations pages inspected. | review accepted | [event 20](trace.jsonl#L20) |
