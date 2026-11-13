# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**baseline · ok**

1 model calls · 0 reads · 10.58 s · $0.002430

1 decisions · 0 tool calls · 16572 input tokens (0 cached) · 718 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AGENTLESS presents a simple, non-agentic pipeline for repository-level issue resolution: hierarchical code localization, patch sampling, filtering, and majority-vote ranking. On SWE-bench Lite, it reports 82 of 300 issues resolved at an average cost of $0.34, and it contributes a manual classification of benchmark issues used to define a 252-issue filtered subset. The work makes a useful empirical case that a relatively simple pipeline can be competitive, though its comparative claims and benchmark analysis have important evaluation and reproducibility limits.

- **strength**: The paper gives a concrete, interpretable pipeline and evaluates both localization and repair components, rather than presenting only an end-to-end solve rate.
  - Page 5 · citation: whitespace
  - Quote: "AGENTLESS smartly combines existing techniques to construct an easy-to-understand approach."

- **strength**: The reported results support the practical value of the approach: it resolves 82 of 300 tasks at low reported cost, and the paper includes ablations showing gains from sampling, voting, and filtering.
  - Page 8 · citation: not_found
  - Quote: "Finally, the full AGENTLESS performance is achieved by further applying filtering"

- **limitation**: The comparison is not uniformly reproducible or directly controlled: the paper says baseline results are taken from reported sources, and notes that many closed-source systems lack code or trajectories. This limits confidence in attributing performance differences solely to the methods.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

- **uncertainty**: The filtered benchmark is motivated by manual issue classification, but the supplied paper does not establish how consistently independent reviewers would apply these categories. The authors also state they could not run commercial tools on the modified set, so comparisons there rely on existing submissions rather than new matched evaluations.
  - Page 10 · citation: whitespace
  - Quote: "as we are not able to run commercial tools ourselves on the modified problems"

Unresolved questions:

- How reliable and reproducible are the manual issue classifications, and would independent annotators agree on which issues to exclude?
- How would the relative results change under a common rerun of all systems on SWE-bench Lite-S with matched models, evaluation setup, and cost accounting?
- How sensitive are AGENTLESS's solve rate and cost to its localization and sampling settings, or to other LLMs?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
