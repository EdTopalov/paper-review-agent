# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**baseline · ok**

1 model calls · 0 reads · 9.67 s · $0.002186

1 decisions · 0 tool calls · 14416 input tokens (0 cached) · 769 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

Re:flexion adds a natural-language memory of failure and an LLM-generated reflection between task attempts, using binary success feedback and simple heuristics rather than policy training. The reported results suggest that this approach can improve repeated-attempt performance on AlfWorld and HotPotQA, while the WebShop result is inconclusive. The contribution is a practical, relatively simple method with illustrative examples, but the evidence is limited to the reported experiments and leaves the generality and reliability of the gains uncertain.

- **strength**: The paper gives a concrete, minimally specified mechanism for using failure feedback across trials, and reports substantial cumulative gains on two benchmarks. The supplied examples illustrate how remembered task-specific information can change a later attempt.
  - Page 4 · citation: normalized
  - Quote: "Finally, we add the reflection to the agent’s memory, reset the environment, and start the next trial."

- **limitation**: The reported HotPotQA figures are inconsistent: the abstract says 51% and a 17-point gain, while the results section reports 54% and a 20-point gain. This makes the exact headline result unclear in the supplied paper.
  - Page 6 · citation: whitespace
  - Quote: "Reﬂexion agent achieved 32% accuracy in the ﬁrst trials"

- **uncertainty**: The experiments demonstrate cumulative performance over retries, but the supplied report does not establish how much of the gain is robust across random seeds or alternative task samples. The authors frame the comparison as learning rather than retry success, but the reported results alone do not resolve that uncertainty.
  - Page 5 · citation: whitespace
  - Quote: "we wanted to distinguish learning curves from self-improvement to simple probabilistic success over time."

- **strength**: The authors report a meaningful boundary on the approach: their WebShop test showed little improvement and they identify tool/search quality as a possible constraint. This qualifies the broader applicability claim rather than presenting the method as uniformly effective.
  - Page 10 · citation: whitespace
  - Quote: "it highlights the ability of a Reﬂexion agent to optimize reasoning trace and action execution but not complete awareness of the quality of the tools that it may be using."

Unresolved questions:

- Which HotPotQA result is intended—51% with a 17-point gain or 54% with a 20-point gain—and what accounts for the discrepancy?
- How stable are the reported gains across repeated runs, different task samples, and changes to the prompt examples or reflection-memory limit?
- The assessment here is based on the supplied paper text and figures; experimental logs and implementation details were not independently inspected. How much of the measured improvement depends on the specific heuristics, prompts, and benchmark setup?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
