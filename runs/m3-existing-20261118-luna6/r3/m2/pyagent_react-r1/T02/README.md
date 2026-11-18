# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**pyagent_react · ok**

6 model calls · 4 reads · 14.43 s · $0.001742

6 decisions · 5 tool calls · 36187 input tokens (27568 cached) · 779 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.7

Refl exion adds an LLM-generated reflection to a retrying agent’s working memory after a binary failure signal and simple failure heuristics. The paper’s main contribution is a practical, model-update-free mechanism for carrying lessons across trials, with promising results on two different task types. Evidence is bounded by benchmark and model choices, and the authors report little improvement on WebShop.

- **strength**: The method is clearly specified: a heuristic triggers reflection on the task, trajectory, reward, and existing memory, then stores the reflection for the next trial.
  - Page 4 · citation: exact
  - Quote: "Finally, we add the reﬂection to the agent’s memory, reset the environment, and start the next trial."

- **strength**: In 134 AlfWorld environments, the reported ReAct agent with reflection solved substantially more tasks over trials than its starting performance; this supports cross-trial learning in that setup.
  - Page 5 · citation: whitespace
  - Quote: "Given the ability to reﬂect, the agent used ReAct to solve 97% of the given environments in 12 trials, failing to solve only 4 out of 134 tasks."

- **limitation**: The HotPotQA evidence is a 100-question evaluation using exact match; the authors report that semantic grading was not used because it required subjective human grading.
  - Page 6 · citation: exact
  - Quote: "We tested the base agent and Reﬂexion agent on a 100-question dataset."

- **limitation**: The reported WebShop result shows only a one-point accuracy gain over baseline, and the authors say the agent did not generate helpful reflections. This limits evidence for broad applicability, though they also note dependence on search quality.
  - Page 10 · citation: whitespace
  - Quote: "The agent achieved a 33% → 34% accuracy improvement in the baseline run and a mere33% → 35% accuracy improvement in the Reﬂexion run"

Unresolved questions:

- How robust are the gains across random seeds, larger held-out samples, and different underlying language models?
- How much of the measured improvement depends on the hand-written heuristics and few-shot reflection examples, rather than reflection and memory as a general mechanism?
- Can the approach reliably improve tasks where success signals are noisy or tool quality, rather than planning, is the main bottleneck?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the proposed method and its memory and reflection mechanism. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark results and reported evaluation conditions. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect the authors’ stated scope, limitations, and concluding claims. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 10, "end": 11}` | Check the paper’s conclusion and explicit limitations. | read pages [10, 11] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.7, "observations": 4}}` | Submit an evidence-based assessment using inspected method, results, and limitations pages. | review accepted | [event 30](trace.jsonl#L30) |
