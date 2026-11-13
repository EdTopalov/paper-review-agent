# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**pyagent_react · ok**

3 model calls · 2 reads · 8.93 s · $0.001511

3 decisions · 3 tool calls · 12267 input tokens (3132 cached) · 676 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.64

Reflexion adds written self-reflection to an LLM agent’s working memory between task attempts, using binary success feedback and task-specific termination heuristics rather than updating model parameters. The paper reports improved multi-trial performance on AlfWorld and HotPotQA. This is a useful, concrete agent-design demonstration, but the evaluation is limited in scale and scope, and the evidence does not isolate reflection from other retry-related effects across broad settings.

- **strength**: The AlfWorld experiment reports a substantial improvement over successive trials, with 97% success on 134 environments; the authors appropriately frame the comparison as learning through self-improvement rather than a state-of-the-art accuracy comparison.
  - Page 5 · citation: exact
  - Quote: "the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: The HotPotQA evidence comes from a 100-question dataset and uses exact match as its binary reward, so conclusions are bounded by this evaluation setup and grading choice.
  - Page 6 · citation: exact
  - Quote: "We tested the base agent and Reﬂexion agent on a 100-question dataset."

- **uncertainty**: The paper defines AlfWorld hallucination and inefficient planning using specific action-count heuristics. Whether those operational definitions capture broader failure modes is not established by the inspected evidence.
  - Page 7 · citation: whitespace
  - Quote: "we deﬁned hallucination as the occurrence of two or more consecutive identical actions"

- **uncertainty**: The abstract reports 51% HotPotQA success, while the results passage reports 54%; the inspected pages do not explain this difference.
  - Page 1 · citation: exact
  - Quote: "We observe success rates of 97% and 51%, respectively"

Unresolved questions:

- How robust are the reported gains to different LLMs, prompts, task distributions, and larger evaluation sets?
- How much of the improvement is attributable specifically to written reflection and memory, rather than additional attempts or other aspects of the trial procedure?
- What explains the discrepancy between the abstract’s 51% HotPotQA rate and the results section’s 54% rate?
- Inspection was limited to pages 1 and 4–8; later discussion and appendices, including fuller methodological details, were not reviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 4, "end": 6}` | Inspect the agent design and reported benchmark evidence. | read pages [4, 5, 6] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 7, "end": 8}` | Inspect the remaining evaluation claims and discussion of limitations. | read pages [7, 8] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.64, "observations": 4}}` | Assess the reported trials, task scope, and stated operational definitions from the inspected pages. | review accepted | [event 17](trace.jsonl#L17) |
