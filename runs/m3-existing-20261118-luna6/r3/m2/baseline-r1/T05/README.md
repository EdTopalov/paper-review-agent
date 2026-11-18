# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**baseline · ok**

1 model calls · 0 reads · 6.73 s · $0.000466

1 decisions · 0 tool calls · 16657 input tokens (16654 cached) · 599 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

WebArena contributes a self-hostable, interactive web environment and an 812-task benchmark for evaluating natural-language web agents through task outcomes rather than exact action traces. Its multi-site setting, varied observation and action interfaces, and programmatic checks make it a useful research testbed. Baseline results and trajectory analysis illustrate the difficulty of these tasks, though the evidence is principally an environment-and-benchmark demonstration with a narrow set of agent baselines.

- **strength**: The benchmark emphasizes whether the intended result was achieved, allowing multiple valid interaction paths instead of requiring one reference action sequence.
  - Page 2 · citation: whitespace
  - Quote: "This evaluation is not only more reliable [40, 5, 33] than comparing the vanilla action sequences [25, 7] but also accommodates a range of potential valid paths to achieve the same goal"

- **strength**: The environment combines several functional web domains with tools and knowledge resources, and is designed to be reproducible through self-hosting.
  - Page 3 · citation: whitespace
  - Quote: "We achieve reproducibility by having the environment be standalone, not relying on live websites."

- **limitation**: The task set has a documented feasibility boundary: some tasks cannot be completed because of missing evidence, permissions, or unsupported functionality, and are labeled N/A.
  - Page 8 · citation: whitespace
  - Quote: "Due to constraints such as inadequate evidence, user permissions (§2.4), or the absence of necessary functional support in the website, some tasks ( ∼4%) in our benchmark are not possible to complete."

- **uncertainty**: The reported baseline comparison covers only two prompting styles and two model versions; the paper does not establish how representative these results are of broader agent approaches. This is a scope of the reported evaluation, not evidence that other methods fail.
  - Page 9 · citation: exact
  - Quote: "We design two LLM-prompt-based web agents as our baselines"

Unresolved questions:

- How stable are success rates across repeated runs, given the paper's use of high temperature and its own discussion of prediction variance?
- How sensitive are benchmark scores to the evaluator choices, particularly the fuzzy-match judgments made by GPT-3.5 and the use of recall-oriented checks?
- How well do the sampled sites, data, and author-authored tasks represent web tasks beyond the included domains and the northeast-US map coverage?
- I inspected the supplied pages and appendix excerpts; I did not independently verify the environment implementation or reproduce the reported experiments.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
