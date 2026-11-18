# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**baseline · ok**

1 model calls · 0 reads · 6.84 s · $0.000527

1 decisions · 0 tool calls · 23863 input tokens (23860 cached) · 577 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

SWE-agent presents an LM-oriented agent-computer interface for repository-level software engineering and evaluates it on SWE-bench. Its principal contribution is a set of practical interface design choices—summarized search, file viewing and editing, informative feedback, linting guardrails, and context management—supported by benchmark results and ablations showing improved performance over a shell-only agent. The results are substantial for the tested systems, though the evidence is concentrated on two models and one benchmark.

- **strength**: The paper reports a meaningful improvement over the interactive shell-only baseline on SWE-bench Lite, and evaluates the system on the full test set as well.
  - Page 5 · citation: whitespace
  - Quote: "SWE-agent with GPT-4 Turbo yields the best performance, solving 12.47% (286/2,294) of the full SWE-bench test set and 18.00% (54/300) of the Lite split."

- **strength**: The interface-design contribution is supported by component ablations, including measurable declines when editing and linting are removed.
  - Page 7 · citation: whitespace
  - Quote: "Without SWE-agent’s file editor interface, performance drops to (10.3% ↓ 7.7)."

- **limitation**: The study’s main evidence is bounded to two closed models and SWE-bench, with the component ablations run on the 300-instance Lite subset; broader generality is not established here.
  - Page 5 · citation: exact
  - Quote: "All results, ablations, and analysis are based on two leading LMs"

Unresolved questions:

- How well do these ACI choices transfer to other model families, software tasks, and repository benchmarks beyond the two tested models and SWE-bench?
- How much of the overall gain is attributable to individual interface components versus their interaction with prompts, demonstrations, and other configuration choices?
- The review is based on the supplied pages; detailed appendix material beyond page 25 and any supplementary artifacts were not inspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
