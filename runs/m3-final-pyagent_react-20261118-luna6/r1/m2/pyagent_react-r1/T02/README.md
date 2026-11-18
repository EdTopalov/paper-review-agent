# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**pyagent_react · ok**

5 model calls · 4 reads · 17.80 s · $0.001751

5 decisions · 5 tool calls · 34176 input tokens (25563 cached) · 838 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Reflexion adds an autonomous reflection-and-memory loop to an existing LLM agent: failure signals prompt the agent to summarize a trajectory, retain the reflection, and retry. The paper presents promising improvements over retrying alone on AlfWorld and HotPotQA, alongside an unsuccessful WebShop result. Its contribution is a simple, interpretable mechanism with concrete examples, but the evidence is bounded by selected benchmarks, modest evaluation samples, and task-dependent failure signals.

- **strength**: The method is clearly specified as a lightweight addition to an agent, using a heuristic to trigger reflection and storing a limited number of reflections for later trials.
  - Page 3 · citation: whitespace
  - Quote: "we set a hyperparameter limit of three maximum reﬂections to be stored in the agent’s memory"

- **strength**: The AlfWorld experiment reports substantial cumulative improvement over the initial run, and includes a concrete example of a reflection changing the next trial’s behavior.
  - Page 5 · citation: exact
  - Quote: "the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: The main benchmark evidence is limited in scale: AlfWorld uses 134 environments and HotPotQA uses 100 questions, so the reported gains do not by themselves establish broad generalization.
  - Page 6 · citation: exact
  - Quote: "We tested the base agent and Reﬂexion agent on a 100-question dataset."

- **uncertainty**: Performance appears dependent on benchmark-specific signals and the quality of the environment’s tools; the WebShop attempt showed little improvement, and its proposed explanation is not isolated experimentally.
  - Page 10 · citation: whitespace
  - Quote: "the chance of a successful item purchase for an agent in a WebShop environment was not necessarily dependent on the agent’s ability to plan and execute a correct sequence of actions"

Unresolved questions:

- How robust are the reported gains across different models, prompts, and task samples? I did not inspect the appendices or full experimental logs.
- Can reflection improve performance when the failure signal is noisy, delayed, or expensive to obtain?
- How much of the gains comes from reflection itself versus repeated sampling and accumulated task-specific memory?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the method and how reflection updates agent memory. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark results, comparisons, and evaluation details. | read pages [5, 6, 7] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 8, "end": 9}` | Inspect stated limitations and concluding claims to calibrate scope. | read pages [8, 9] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 10, "end": 11}` | Check concluding discussion for explicit limitations and broader claims. | read pages [10, 11] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit a balanced assessment grounded in the inspected method, results, and limitations pages. | review accepted | [event 26](trace.jsonl#L26) |
