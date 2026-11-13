# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**baseline · ok**

1 model calls · 0 reads · 5.86 s · $0.002383

1 decisions · 0 tool calls · 16572 input tokens (0 cached) · 624 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AGENTLESS presents a fixed, two-phase localization-and-repair pipeline as a simpler alternative to autonomous software-engineering agents. On SWE-bench Lite, the authors report 82 of 300 issues resolved at an average cost of $0.34, and introduce a manually filtered 252-issue subset, SWE-bench Lite-S. The work offers a clear and useful baseline, with evidence from component comparisons and benchmark analysis, but its evaluation scope and some cross-system comparisons limit how broadly to interpret the results.

- **strength**: The method is clearly specified, and the authors compare repair variants to show the incremental contribution of sampling, voting, and test filtering.
  - Page 8 · citation: exact
  - Quote: "single sample 70 (23.33%) $0.11"

- **strength**: The reported benchmark results support a meaningful cost-performance contribution among the compared open-source approaches.
  - Page 7 · citation: wrong_page
  - Quote: "AGENTLESS is able to achieve the highest performance of"

- **limitation**: The headline comparisons mix the authors' run with results taken from leaderboards or other papers, and the authors note that many commercial systems cannot be independently verified from released trajectories.
  - Page 6 · citation: exact
  - Quote: "For baseline tools, we directly use the reported results"

- **uncertainty**: The authors identify harder cases without location clues as a relative weakness, but the paper does not establish how much more complex search or agent interaction would improve AGENTLESS on those cases.
  - Page 11 · citation: whitespace
  - Quote: "the closed-source agent tools perform better compared to AGENTLESS in the case where no location clue is provided."

Unresolved questions:

- How robust are the results to other LLMs, model versions, and inference settings beyond the reported GPT-4o setup?
- How reproducible are the reported comparisons when all systems are run under the same evaluation setup, model access, and cost accounting?
- How sensitive are SWE-bench Lite-S results to the authors' manual classification and exclusion decisions?
- This assessment relies on the supplied paper text; I have not independently inspected its code, raw outputs, or supplementary materials.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
