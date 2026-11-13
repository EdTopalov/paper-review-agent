# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**baseline · ok**

1 model calls · 0 reads · 7.28 s · $0.002416

1 decisions · 0 tool calls · 16657 input tokens (0 cached) · 668 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

WebArena contributes a self-hosted, interactive web environment spanning several common website types, paired with 812 natural-language tasks and functional-outcome evaluation. Baseline results expose substantial difficulty for the tested agents and motivate research on reliable long-horizon web interaction. The environment and benchmark are a useful research contribution, though the evidence here is mainly an initial evaluation of a narrow set of text-based agents.

- **strength**: The work combines dynamic, self-hosted websites with long-horizon tasks and checks task outcomes rather than requiring agents to reproduce a single action sequence.
  - Page 2 · citation: exact
  - Quote: "We focus on evaluating the functional correctness of these tasks"

- **strength**: The benchmark has meaningful breadth across task instances, with explicit attention to cases that cannot be completed in the environment.
  - Page 8 · citation: whitespace
  - Quote: "some tasks ( ∼4%) in our benchmark are not possible to complete"

- **limitation**: The reported agent evidence is limited to direct and reasoning prompt-based baselines with two model families; the result does not establish how broader agent designs would perform.
  - Page 9 · citation: exact
  - Quote: "We design two LLM-prompt-based web agents as our baselines"

- **uncertainty**: The reported GPT-4 success rate is inconsistent within the paper: the table and abstract give 10.59%, while the main-results prose gives 10.63%. The supplied text does not resolve which figure is intended.
  - Page 9 · citation: whitespace
  - Quote: "achieves a relatively modest end-to-end task success rate of 10.63%"

Unresolved questions:

- How robust are the task annotations and programmatic evaluators across alternative valid completions, especially for tasks scored using fuzzy matching?
- How well do the benchmark and findings generalize beyond the selected applications, data snapshots, and northeast-US map coverage?
- What explains the discrepancy between the GPT-4 success rates reported in the table/abstract and the main-results prose?
- The inspected paper reports baseline outcomes but does not provide, in the supplied pages, broader comparisons across agent architectures or modalities.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
