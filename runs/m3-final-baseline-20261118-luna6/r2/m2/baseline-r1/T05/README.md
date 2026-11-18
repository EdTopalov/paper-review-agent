# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**baseline · ok**

1 model calls · 0 reads · 7.69 s · $0.000513

1 decisions · 0 tool calls · 16657 input tokens (16654 cached) · 693 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

WebArena contributes a self-hostable, interactive web environment and an 812-task benchmark for evaluating agents on realistic, multi-step web tasks. Its functional outcome checks and baseline/error analysis make it a useful platform for studying agent capabilities, though the reported baseline evidence is limited and some evaluation judgments rely on an LM.

- **strength**: The environment combines several functional web applications, tools, and knowledge resources in a reproducible setup, supporting tasks that span sites and pages.
  - Page 2 · citation: whitespace
  - Quote: "four fully operational, self-hosted web applications"

- **strength**: The benchmark evaluates task outcomes rather than requiring agents to reproduce one reference action sequence, accommodating different valid ways to complete a task.
  - Page 2 · citation: exact
  - Quote: "accommodates a range of potential valid paths to achieve the same goal"

- **limitation**: The fuzzy-match evaluator uses GPT-3.5 to judge answer entailment, so results for those tasks depend partly on a model-based evaluation decision.
  - Page 7 · citation: not_found
  - Quote: "we use gpt-3.5-turbo-0613 to assess whether ˆa could entail each of the key concepts in a∗"

- **uncertainty**: The reported GPT-4 success rate is inconsistent within the paper: the abstract and table give 10.59%, while the results text gives 10.63%. The supplied text does not resolve which figure is intended.
  - Page 9 · citation: whitespace
  - Quote: "achieves a relatively modest end-to-end task success rate of 10.63%"

Unresolved questions:

- How stable are the results across repeated runs, given the stated high sampling temperature, and what is the source of the 10.59% versus 10.63% discrepancy?
- How well do the author-guided, author-contributed task intents represent tasks encountered by a broader population of web users?
- How sensitive are benchmark scores to the LM-based fuzzy-match evaluator, and how often do its judgments disagree with independent human assessment?
- Inspection was based on the supplied PDF text; figures and some implementation details in appendices were not independently examined.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
