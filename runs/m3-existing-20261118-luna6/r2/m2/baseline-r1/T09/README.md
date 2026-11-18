# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**baseline · ok**

1 model calls · 0 reads · 9.27 s · $0.000531

1 decisions · 0 tool calls · 16572 input tokens (16569 cached) · 731 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

AGENTLESS presents a deliberately non-agentic approach to repository-level issue fixing: hierarchical code localization followed by patch generation, filtering, and voting. On SWE-bench Lite, the authors report 82 of 300 issues resolved at an average cost of $0.34, and introduce a manually curated 252-issue subset, SWE-bench Lite-S, after excluding issues they classify as problematic. The paper offers a useful empirical challenge to the assumption that more autonomous agent interaction is always necessary, though the scope of its comparisons and evaluation leaves important questions about reproducibility and generality.

- **strength**: The paper contributes a clear, interpretable pipeline and a useful baseline for testing whether autonomous tool use is needed for this task.
  - Page 5 · citation: whitespace
  - Quote: "AGENTLESS smartly combines existing techniques to construct an easy-to-understand approach."

- **strength**: The authors report component-level results that help explain performance: multiple samples and voting improve the single-sample result, with test filtering adding further fixes.
  - Page 8 · citation: exact
  - Quote: "+ test filtering\n(full AGENTLESS) 82 (27.33%) $0.34"

- **limitation**: The comparison is not uniformly reproduced by the authors: many baseline figures are taken from prior reports, and the paper notes missing source code or trajectories for some systems. This limits how directly the headline comparisons can be interpreted.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

- **uncertainty**: The reported evaluation centers on SWE-bench Lite and a single configured model, GPT-4o. The paper does not establish from the inspected results how well the approach generalizes to other models, benchmarks, or repository-level task types.
  - Page 6 · citation: exact
  - Quote: "We implement AGENTLESS using GPT-4o (gpt-4o-2024-05-13) [45]."

Unresolved questions:

- How would AGENTLESS compare with agent-based systems under a matched setup using the same model, inference budget, evaluation environment, and reproducible runs?
- How sensitive are the results to the choice of LLM and to the localization and patch-sampling settings?
- Would the reported performance and cost pattern persist on the full SWE-bench dataset or other repository-level benchmarks?
- The supplied paper reports manual classification and filtering for SWE-bench Lite-S; what is the inter-rater agreement or other validation for those classifications?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
