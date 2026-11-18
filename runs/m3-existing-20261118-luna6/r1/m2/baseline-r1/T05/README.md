# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**baseline · ok**

1 model calls · 0 reads · 8.96 s · $0.002338

1 decisions · 0 tool calls · 16657 input tokens (0 cached) · 512 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

WebArena contributes a self-hostable, stateful web environment and an 812-task benchmark for evaluating agents on realistic, multi-step web tasks. Its functional outcome checks and reported baseline results make it a useful testbed for agent research, while the low GPT-4 success rate and error analysis illustrate the difficulty of the benchmark. The paper’s evidence chiefly establishes the environment and benchmark’s utility as an evaluation resource; it does not establish that benchmark performance predicts success on live websites.

- **strength**: The benchmark targets outcome correctness rather than exact action-sequence imitation, and its programmatic checks allow valid alternative execution paths.
  - Page 2 · citation: exact
  - Quote: "accommodates a range of potential valid paths to achieve the same goal"

- **strength**: The environment is designed for repeatable evaluation by avoiding dependence on changing live websites and providing a deterministic reset mechanism.
  - Page 3 · citation: whitespace
  - Quote: "We achieve reproducibility by having the environment be standalone, not relying on live websites."

- **limitation**: The reported baseline comparison is narrow: it covers two prompting styles and two model versions, and reasoning gives only a small reported improvement for GPT-3.5.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3.5 reasoning agent outperforms the direct agent only by successfully completing a marginal number of examples."

- **uncertainty**: The paper acknowledges that some tasks cannot be completed because of the environment’s evidence, permission, or feature constraints; the extent to which this affects benchmark-level comparisons is not resolved in the inspected material.
  - Page 8 · citation: whitespace
  - Quote: "some tasks ( ∼4%) in our benchmark are not possible to complete."

Unresolved questions:

- How well do scores on this sampled, self-hosted environment transfer to agents operating on live websites with different interfaces, data, and changing site behavior?
- How sensitive are the baseline success rates to run-to-run variation, given the reported high sampling temperature?
- How robust are the language-model-based fuzzy-match evaluations to incorrect or unsupported answers?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
