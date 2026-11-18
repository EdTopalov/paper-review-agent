# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**baseline · ok**

1 model calls · 0 reads · 7.63 s · $0.000511

1 decisions · 0 tool calls · 16572 input tokens (16569 cached) · 690 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

AGENTLESS presents a fixed, two-phase LLM workflow for repository-level issue repair: hierarchical localization followed by patch generation, filtering, and voting. On SWE-bench Lite, the authors report 82/300 resolved at an average cost of $0.34, with ablations indicating gains from multiple samples, voting, and test filtering. They also manually classify benchmark issues and create a filtered subset, SWE-bench Lite-S. The work offers a clear, useful challenge to the assumption that autonomous agent loops are necessary, though its evaluation is concentrated on one benchmark and some comparisons rely on results reported by others.

- **strength**: The paper gives a concrete and interpretable alternative to tool-using agent loops, and reports strong performance relative to the open-source approaches in its comparison.
  - Page 7 · citation: whitespace
  - Quote: "AGENTLESS  GPT-4o 82 (27.33%) $0.34"

- **strength**: The repair ablation provides evidence that sampling and voting, followed by regression-test filtering, improve the reported solve count over a single greedy sample.
  - Page 8 · citation: exact
  - Quote: "+ test filtering\n(full AGENTLESS) 82 (27.33%) $0.34"

- **limitation**: The evaluation’s cross-system comparisons are not uniformly reproduced by the authors: they state that commercial tools could not be run on the modified benchmark and use reported baseline results. This limits how directly the results establish comparative performance.
  - Page 10 · citation: whitespace
  - Quote: "we are not able to run commercial tools ourselves on the modified problems"

- **uncertainty**: The paper reports that agent-based tools do better on issues without location clues, but leaves open how much richer search or other agent capabilities could improve AGENTLESS on that subset.
  - Page 11 · citation: whitespace
  - Quote: "the closed-source agent tools perform better compared to AGENTLESS in the case where no location clue is provided."

Unresolved questions:

- How robust are the reported results to repeated runs or changes in model version, given the stochastic sampling used for patch generation?
- Would the approach’s relative performance and cost advantages persist on other repository-level benchmarks or on a broader range of programming languages?
- How reproducible are the reported comparisons when competing systems are evaluated under the same setup, especially on SWE-bench Lite-S?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
