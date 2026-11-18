# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**baseline · ok**

1 model calls · 0 reads · 8.17 s · $0.000501

1 decisions · 0 tool calls · 16572 input tokens (16569 cached) · 670 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AGENTLESS presents a straightforward, hierarchical localization-and-repair pipeline that avoids autonomous tool use and planning. On SWE-bench Lite, the authors report 82/300 resolved issues at an average cost of $0.34, with ablations suggesting that patch sampling, voting, and test filtering improve results. The paper also manually classifies benchmark issues and proposes SWE-bench Lite-S. The contribution is useful and supported by benchmark results, though comparisons and conclusions are bounded by the chosen benchmark and the use of previously reported baseline results.

- **strength**: The paper provides a concrete, reproducible-in-principle method and reports both performance and cost, with component-level repair comparisons.
  - Page 8 · citation: not_found
  - Quote: "Starting with just generating a single sample (i.e., using greedy decoding), AGENTLESS can achieve 70 correct fixes"

- **strength**: The authors investigate benchmark quality and create a filtered subset; they also report results on it rather than relying only on the original benchmark.
  - Page 10 · citation: exact
  - Quote: "We refer to our subset of 252 problems as SWE-bench Lite-S."

- **limitation**: Baseline comparisons are not uniformly produced under the paper's own experimental setup, limiting the strength of direct performance and cost comparisons.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

- **uncertainty**: The reported manual benchmark categorization is potentially valuable, but the supplied paper text does not establish how robust or reproducible those judgments are.
  - Page 8 · citation: not_found
  - Quote: "we perform manual classification based on the issue description and ground truth developer patch of each problem."

Unresolved questions:

- How much would the ranking and cost comparison change if open-source baselines were rerun using the same model, evaluation setup, and cost accounting?
- How consistent are the manual issue classifications across independent annotators, and how sensitive are SWE-bench Lite-S results to borderline inclusion decisions?
- Do the localization and repair results generalize beyond this benchmark and GPT-4o setup? The inspected evaluation focuses on SWE-bench Lite and one implementation configuration.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
