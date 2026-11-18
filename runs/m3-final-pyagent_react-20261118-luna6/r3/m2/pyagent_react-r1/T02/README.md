# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**pyagent_react · ok**

4 model calls · 2 reads · 13.32 s · $0.001028

4 decisions · 3 tool calls · 14585 input tokens (10144 cached) · 743 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Reflexion adds a lightweight test-time mechanism for agents to reflect on failures and carry those reflections in dynamic memory across task retries, without model fine-tuning. Its evaluations show notable gains across trials in AlfWorld and HotPotQA, making the approach a useful, accessible demonstration of memory-based self-improvement. Evidence is promising but bounded by modest evaluation sets and task-specific setups; the results do not establish broad generality.

- **strength**: The AlfWorld study reports improvement over repeated trials when reflection is available, and distinguishes this from simple retrying.
  - Page 5 · citation: exact
  - Quote: "Given the ability to reﬂect, the agent used ReAct to solve 97% of the given environments in 12 trials,"

- **strength**: On HotPotQA, the reflective agent improves across trials while the retry baseline does not add correct answers.
  - Page 6 · citation: exact
  - Quote: "Reﬂexion enabled the agent to successfully answer 54% of the questions from the dataset,"

- **limitation**: The evaluated HotPotQA set is limited to 100 questions, so the measured gain has a bounded evaluation scope.
  - Page 6 · citation: exact
  - Quote: "We tested the base agent and Reﬂexion agent on a 100-question dataset."

- **uncertainty**: The authors identify task-level requirements for applying the approach; how performance depends on the quality and transferability of heuristics and binary rewards remains open.
  - Page 7 · citation: whitespace
  - Quote: "A Reﬂexion agent must have access to a heuristic for termination and a binary reward model."

Unresolved questions:

- How robust are the gains across larger and more varied tasks, models, and environments?
- How sensitive is improvement to reflection prompt design, memory contents, and the choice of termination heuristic and reward signal?
- I inspected pages 4–8, focusing on method details, evaluation, and discussion; other portions of the paper, including the full setup and appendices, were not inspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 4, "end": 6}` | Inspect the method and evaluation evidence. | read pages [4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 8}` | Inspect discussion and limitations. | read pages [7, 8] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit an evidence-based assessment using inspected method, results, and discussion pages. | review accepted | [event 20](trace.jsonl#L20) |
