# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**baseline · ok**

1 model calls · 0 reads · 7.85 s · $0.000521

1 decisions · 0 tool calls · 16572 input tokens (16569 cached) · 710 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AGENTLESS shows that a fixed, hierarchical localization-and-repair pipeline can be a competitive, low-cost alternative to autonomous agents on SWE-bench Lite. Its contribution is a practical system and a benchmark-quality analysis, supported by a reported 27.33% solve rate, component comparisons, and a filtered 252-problem subset. The evidence is useful but bounded: comparisons rely partly on previously reported results, and the evaluation centers on one benchmark and one model setup.

- **strength**: The paper reports a strong result for its simple approach: 82 of 300 issues resolved at an average cost of $0.34, with performance competitive against the listed open-source systems.
  - Page 7 · citation: whitespace
  - Quote: "AGENTLESS  GPT-4o 82 (27.33%) $0.34 42,376"

- **strength**: The repair ablation gives evidence that sampling and majority voting improve the single-sample result, while test filtering adds a further gain.
  - Page 8 · citation: exact
  - Quote: "+ multiple samples\n& maj. voting 78 (26.00%) $0.34\n+ test filtering\n(full AGENTLESS) 82 (27.33%) $0.34"

- **limitation**: Some baseline comparisons are not direct replications: the paper uses results reported elsewhere, limiting control over differences in setup and verification.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

- **uncertainty**: The filtered benchmark comparison is informative, but the paper says commercial tools were not run on the modified set; how those systems would perform under the same conditions remains unresolved.
  - Page 10 · citation: whitespace
  - Quote: "as we are not able to run commercial tools ourselves on the modified problems, we simply exclude the problematic problems in the below evaluation."

Unresolved questions:

- How robust are the performance and cost results across other LLMs, model versions, and repository-level benchmarks?
- Would controlled reruns of all baselines on the same environment and SWE-bench Lite-S change the comparative conclusions?
- How consistent and reproducible are the manual classifications used to construct SWE-bench Lite-S?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
