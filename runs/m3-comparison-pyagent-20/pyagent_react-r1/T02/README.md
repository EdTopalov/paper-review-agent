# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**pyagent_react · ok**

4 model calls · 2 reads · 13.05 s · $0.001576

4 decisions · 3 tool calls · 14194 input tokens (5001 cached) · 754 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.67

Reflexion adds episodic textual memory and natural-language self-reflection between attempts, using binary success feedback to improve an LLM agent without updating model parameters. The reported AlfWorld and HotPotQA results suggest useful gains from reflection in these evaluated settings. The work is a clear, practically motivated demonstration, but the evidence is limited to two benchmarks and modest test sets, and the paper itself notes that environment-specific heuristics may be needed.

- **strength**: The paper specifies a simple feedback-and-memory loop: after a trial, the agent generates a reflection from its task, reward, trajectory, and memory.
  - Page 4 · citation: exact
  - Quote: "reflection =LLM(st,r t, [a0,o 0,...,a t,o t],mem )"

- **strength**: On the reported 134 AlfWorld environments, reflection improved cumulative success over repeated trials; the authors distinguish this from simply retrying.
  - Page 5 · citation: exact
  - Quote: "the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: The HotPotQA experiment is limited to a 100-question dataset, so the reported performance does not establish broad generalization across the benchmark.
  - Page 6 · citation: exact
  - Quote: "We tested the base agent and Reﬂexion agent on a 100-question dataset."

- **uncertainty**: The discussion identifies a dependence on a termination heuristic and binary reward model, but the inspected evidence does not establish how robust the approach is when these signals are harder to design.
  - Page 7 · citation: whitespace
  - Quote: "A Reﬂexion agent must have access to a heuristic for termination and a binary reward model."

Unresolved questions:

- How sensitive are the reported improvements to the choice and wording of reflection prompts, memory contents, and trial budget?
- Would the gains persist across larger or more varied task sets and alternative base models?
- How well can the approach work in settings where reliable binary feedback and termination heuristics are unavailable?
- I inspected pages 1 and 4–8; I did not inspect the remaining pages, including the full appendix and any additional implementation details or results.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 4, "end": 6}` | Inspect the method and benchmark evaluation details. | read pages [4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 8}` | Inspect reported caveats and conclusion claims. | read pages [7, 8] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.67, "observations": 4}}` | Submit an evidence-based assessment from the inspected method, results, and discussion pages. | review accepted | [event 21](trace.jsonl#L21) |
