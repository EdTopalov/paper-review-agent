# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**baseline · ok**

1 model calls · 0 reads · 9.61 s · $0.000493

1 decisions · 0 tool calls · 16572 input tokens (16569 cached) · 655 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.71

AGENTLESS presents a simple, hierarchical localization-and-repair pipeline for repository-level issue fixing, replacing autonomous agent actions with fixed LLM steps, sampled patches, filtering, and voting. Its evaluation reports competitive SWE-bench Lite performance at low cost, adds useful component and dataset analyses, and proposes a filtered benchmark subset. The contribution is practical and clearly motivated; the evidence is promising but bounded by the benchmark and the reported baseline comparisons.

- **strength**: The paper contributes a concrete, interpretable alternative to agent workflows and reports strong results for it on SWE-bench Lite.
  - Page 7 · citation: wrong_page
  - Quote: "AGENTLESS is able to achieve the highest performance of"

- **strength**: The repair ablation gives evidence that sampling and voting, followed by test filtering, each improve the reported solve count.
  - Page 8 · citation: exact
  - Quote: "+ test filtering\n(full AGENTLESS) 82 (27.33%) $0.34"

- **limitation**: The comparison is not uniformly based on experiments conducted by the authors: for baselines, the paper uses reported results, which limits how directly performance and cost comparisons can be interpreted.
  - Page 6 · citation: exact
  - Quote: "For baseline tools, we directly use the reported results"

- **uncertainty**: The modified benchmark comparison excludes commercial tools because the authors could not run them on the filtered set; how their relative performance changes on Lite-S therefore remains unresolved.
  - Page 10 · citation: whitespace
  - Quote: "we are not able to run commercial tools ourselves on the modified problems"

Unresolved questions:

- How robust are the performance and cost results across repeated runs, given the sampling used for patch generation?
- Would the advantage persist with other underlying LLMs or on repository-level benchmarks beyond SWE-bench Lite and Lite-S?
- How would commercial systems compare on Lite-S if evaluated under the same conditions?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
