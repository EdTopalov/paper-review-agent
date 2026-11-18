# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**agent · ok**

5 model calls · 4 reads · 9.89 s · $0.001383

5 decisions · 5 tool calls · 23505 input tokens (15998 cached) · 601 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.63

Reflexion adds a memory-writing self-reflection step between failed trials to a language-model agent, using heuristic failure detection and binary success feedback. On the reported AlfWorld and HotPotQA evaluations, it improves cumulative task completion over retry-only ReAct baselines, illustrating a useful training-free approach to trial-and-error adaptation. The results support a promising demonstration, but the evaluation is relatively narrow and does not establish robustness beyond the tested setups.

- **strength**: The agent’s reflection and retained memory are concrete additions intended to correct failures across trials, and the paper reports strong AlfWorld cumulative performance.
  - Page 3 · citation: whitespace
  - Quote: "In practice, we set a hyperparameter limit of three maximum reﬂections to be stored in the agent’s memory"

- **strength**: The paper describes a controlled retry-only baseline and reports improved performance over repeated trials on the AlfWorld sample.
  - Page 5 · citation: exact
  - Quote: "Given the ability to reﬂect, the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: The evaluation is small relative to the full benchmark and conclusions are appropriately framed as a demonstration of improvement, not state-of-the-art accuracy.
  - Page 5 · citation: whitespace
  - Quote: "we ran the agent in 134 AlfWorld environments across six different tasks"

- **uncertainty**: HotPotQA performance is measured on 100 questions using exact match, and the paper notes semantic grading alternatives would require subjective human review; robustness to other datasets or scoring was not established in the inspected pages.
  - Page 6 · citation: exact
  - Quote: "We tested the base agent and Reﬂexion agent on a 100-question dataset."

Unresolved questions:

- How sensitive are outcomes to prompt examples, model choice, heuristic thresholds, and memory capacity?
- Would the gains persist across more seeds, larger or independently sampled benchmark sets, and metrics beyond exact match?
- I inspected pages 1–8 only; later material, including any further discussion or appendices, was not assessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "97%"}` | Locate reported benchmark results and supporting evaluation details. | 3 matches on pages [1, 2, 5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect method description and experimental setup/results. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Check benchmark sample sizes, comparison conditions, and stated scope. | read pages [5, 6] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 7, "end": 8}` | Inspect caveats, conclusion, and additional evidence for assessment. | read pages [7, 8] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.63, "observations": 4}}` | Evidence covers method, benchmark results, and explicit scope caveats; submit a balanced assessment. | review accepted | [event 25](trace.jsonl#L25) |
