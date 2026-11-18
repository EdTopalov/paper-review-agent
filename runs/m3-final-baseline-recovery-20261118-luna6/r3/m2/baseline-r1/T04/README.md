# T04: AgentBench: Evaluating LLMs as Agents

**baseline · ok**

1 model calls · 0 reads · 7.24 s · $0.000649

1 decisions · 0 tool calls · 36072 input tokens (36069 cached) · 576 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AgentBench introduces an eight-environment benchmark and evaluation toolkit for interactive LLM agents, then evaluates 25 models. Its breadth, practical task interfaces, and reported comparison across commercial and open models make it a useful contribution; the evidence is qualified by small standard test splits and acknowledged uncertainty in some evaluation procedures.

- **strength**: The benchmark’s breadth is a substantive contribution: it combines varied interactive settings and reports results across 25 models.
  - Page 3 · citation: hyphenation_ambiguous
  - Quote: "We introduce the concept of evaluating LLMs as agents, and present AgentBench, a comprehensive benchmark to standardize the evaluation."

- **strength**: The paper gives concrete construction and checking procedures for several environments, including executable OS tasks, supporting reproducibility and varied task types.
  - Page 5 · citation: wrong_page
  - Quote: "we curate 144 high-quality diverse OS evaluation samples accompanied with testing interactive environments and corresponding checking pipelines"

- **limitation**: The paper explicitly notes that automatic evaluation of lateral-thinking puzzles can overestimate some models, which weakens confidence in those metrics.
  - Page 30 · citation: whitespace
  - Quote: "automatic evaluation sometimes more tolerate for the agent, which make SGA and QR seem better than human evaluation"

- **uncertainty**: The main test split is modest relative to the breadth of the benchmark; how stable the model rankings are under larger or repeated test samples is not established in the inspected material.
  - Page 13 · citation: exact
  - Quote: "the total number of problems in Dev and Test are a bit small—289 and 1,141 respectively."

Unresolved questions:

- How much would the reported rankings and overall score change with larger test splits, repeated runs, or uncertainty estimates?
- How well do the benchmark’s tasks and model rankings predict performance in less simulated, real-world agent deployments?
- The supplied material includes descriptions of LTP human validation but not its detailed results; how large is the gap between automatic and human assessment?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
