# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**baseline · ok**

1 model calls · 0 reads · 8.05 s · $0.000508

1 decisions · 0 tool calls · 16572 input tokens (16569 cached) · 684 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

AGENTLESS presents a simple, fixed localization-then-repair pipeline for repository-level issue resolution, using hierarchical code localization, multiple patch samples, filtering, and majority voting. On SWE-bench Lite, it reports 82 of 300 issues resolved at an average cost of $0.34, and introduces SWE-bench Lite-S after manually excluding issues judged problematic. The work makes a useful empirical case for a lightweight alternative to autonomous agents, though the strength of its comparative claims is limited by reliance on reported baseline results and evaluation on a single benchmark setup.

- **strength**: The paper provides component-level evidence that sampling and voting improve results over a single greedy patch, with test filtering adding a further improvement.
  - Page 8 · citation: exact
  - Quote: "single sample 70 (23.33%) $0.11"

- **limitation**: The baseline comparison is not uniformly based on experiments run by the authors, which limits how directly the headline ranking can be compared across systems.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

- **uncertainty**: The authors did not evaluate commercial tools on the filtered benchmark themselves, so the Lite-S comparison inherits the uncertainty of carrying over their original results.
  - Page 10 · citation: whitespace
  - Quote: "we are not able to run commercial tools ourselves on the modified problems"

Unresolved questions:

- How robust are the reported solve rate and cost to changes in model, prompt design, and sampling budget? The experiments described here use GPT-4o and SWE-bench Lite variants.
- How reproducible and reliable is the manual classification used to construct SWE-bench Lite-S, including agreement between annotators and the effect of alternative exclusion criteria?
- I inspected the supplied 17-page paper text, including its experimental setup and analyses; I did not independently verify the reported runs, baseline measurements, or dataset classifications.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
