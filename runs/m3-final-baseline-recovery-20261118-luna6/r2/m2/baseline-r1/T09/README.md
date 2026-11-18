# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**baseline · ok**

1 model calls · 0 reads · 12.21 s · $0.000564

1 decisions · 0 tool calls · 16572 input tokens (16569 cached) · 797 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

AGENTLESS presents a simple, hierarchical localization-then-repair workflow for repository-level issue resolution, and reports competitive SWE-bench Lite results at low inference cost. Its component analysis and manual benchmark classification add useful evidence and evaluation context. The evidence is promising but bounded: the reported comparisons include results from other tools that the authors did not independently verify, and evaluation is centered on SWE-bench Lite and its filtered subset.

- **strength**: The paper contributes a clearly specified agentless workflow and reports strong performance relative to open-source approaches, alongside low average cost.
  - Page 7 · citation: whitespace
  - Quote: "AGENTLESS  GPT-4o 82 (27.33%) $0.34 42,376"

- **strength**: The repair ablation gives evidence that multiple sampling and voting, followed by test filtering, improve the reported fix count over a single sample.
  - Page 8 · citation: exact
  - Quote: "+ test filtering\n(full AGENTLESS) 82 (27.33%) $0.34"

- **limitation**: Some baseline results cannot be independently checked from the evidence presented, which limits the strength of direct comparisons.
  - Page 6 · citation: whitespace
  - Quote: "the majority of the closed-source baselines do not provide any trajectories, just the submission patches. Therefore, we cannot verify the steps taken to arrive at the final patches."

- **uncertainty**: The supplied paper evaluates on SWE-bench Lite and a filtered subset; how well the findings transfer to other repository-level tasks or benchmarks remains an open question. This assessment is based on the supplied 17-page paper text; supplementary materials and independent reproductions were not inspected.
  - Page 6 · citation: whitespace
  - Quote: "we focus on the filtered subset SWE-bench Lite, containing 300 problems"

Unresolved questions:

- How does AGENTLESS perform on broader repository-level benchmarks, tasks beyond single-file bug fixing, or independently curated evaluations?
- Would the relative performance and cost conclusions persist if the competing systems were rerun under matched models, prompts, and evaluation conditions?
- How sensitive are the results to the localization and sampling choices, such as the top-three-file limit and number of generated patches?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
