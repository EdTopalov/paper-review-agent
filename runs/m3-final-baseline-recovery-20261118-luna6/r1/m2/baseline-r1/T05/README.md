# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**baseline · ok**

1 model calls · 0 reads · 7.49 s · $0.000399

1 decisions · 0 tool calls · 16657 input tokens (16654 cached) · 464 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

WebArena contributes a self-hostable, interactive web environment and an 812-task benchmark for evaluating agents on realistic, multi-step web tasks. Its central value is the combination of functional websites, varied observation/action interfaces, and outcome-oriented evaluation; baseline results also illustrate how difficult the benchmark is for the tested agents. The paper presents a useful platform and diagnostic study, though its realism and evaluation remain bounded by the selected sites, curated tasks, and partly language-model-based scoring.

- **strength**: The environment combines dynamic, self-hosted applications with tools and knowledge resources, supporting broader web interaction than a static task collection.
  - Page 2 · citation: whitespace
  - Quote: "Our environment comprises four fully operational, self-hosted web applications"

- **strength**: The benchmark emphasizes whether an agent achieved the intended outcome rather than requiring one reference action sequence, and reports 812 tasks.
  - Page 2 · citation: whitespace
  - Quote: "we release a ready-to-use benchmark with 812 long-horizon web-based tasks"

- **limitation**: The benchmark’s coverage is deliberately finite: the platform implements four application domains, and the authors’ category selection draws on a small author-history sample.
  - Page 3 · citation: whitespace
  - Quote: "we first conducted an analysis of approximately 200 examples from the authors’ actual web browser histories"

- **uncertainty**: The reported low success rates demonstrate difficulty for these specific baselines, but the paper does not establish how representative they are of broader agent performance; results cover two LLM families and a limited set of prompting approaches.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3.5 reasoning agent outperforms the direct agent only by successfully completing a marginal number of examples."

Unresolved questions:

- How well do benchmark results transfer to live websites or web applications outside the selected domains and implementations?
- How sensitive are aggregate results to the approximately 4% of tasks labeled unachievable and to the language-model-based fuzzy-match evaluator?
- Would stronger agent designs or alternative observation modalities materially improve success, especially on the failure modes identified by the authors?
- Inspection was limited to the supplied pages; detailed per-category results, full task annotations, and the complete evaluation implementations were not assessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
