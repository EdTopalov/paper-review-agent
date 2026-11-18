# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**baseline · ok**

1 model calls · 0 reads · 9.33 s · $0.000581

1 decisions · 0 tool calls · 23863 input tokens (23860 cached) · 685 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

SWE-agent presents an LM-tailored agent-computer interface for repository-level software engineering and evaluates it on SWE-bench. The paper combines a substantial benchmark result with ablations suggesting that search, editing, feedback, and context-management choices affect task success. Its evidence is promising, though the strongest interface comparisons are on the 300-instance Lite subset and the reported results are tied to a small set of closed models.

- **strength**: The paper reports a sizable result on the full SWE-bench test set, with a second model providing some evidence that the approach transfers beyond GPT-4 Turbo.
  - Page 5 · citation: whitespace
  - Quote: "SWE-agent with GPT-4 Turbo yields the best performance, solving 12.47% (286/2,294) of the full SWE-bench test set"

- **strength**: Ablations on SWE-bench Lite provide evidence that specific interface choices—not only the overall agent system—are associated with performance differences.
  - Page 7 · citation: exact
  - Quote: "This intervention improves performance considerably (Without Linting, 15.0% ↓ 3.0)."

- **limitation**: The main interface ablations are reported on the Lite subset, so the paper does not establish whether those component-level gains hold on the full benchmark.
  - Page 5 · citation: whitespace
  - Quote: "We report our main agent results on the full SWE-bench test set and ablations and analysis on the SWE-bench Lite test set"

- **uncertainty**: The configuration search is based on a small development sample; how robust the selected settings are to a broader range of development tasks is not established in the inspected material.
  - Page 18 · citation: whitespace
  - Quote: "We performed a hyperparameter sweep using a subset of 37 instances sampled randomly from the dev split of SWE-bench."

Unresolved questions:

- Do the observed ACI ablation gains persist on the full SWE-bench test set or under other task distributions?
- How much do results vary across additional model families and repeated runs, beyond the models and pass@k analyses reported here?
- The supplied material includes the main paper and appendix, but this assessment does not independently verify implementation details or benchmark execution.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
