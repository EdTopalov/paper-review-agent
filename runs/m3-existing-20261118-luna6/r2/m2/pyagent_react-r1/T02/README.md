# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**pyagent_react · ok**

5 model calls · 4 reads · 14.23 s · $0.001389

5 decisions · 5 tool calls · 24357 input tokens (17486 cached) · 711 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.67

Reflexion adds a natural-language reflection and memory loop to an LLM agent: after failure, it uses the trajectory and binary success signal to form advice that carries into a retry. Results on AlfWorld and HotPotQA suggest that this mechanism can improve performance across trials without model fine-tuning. The contribution is a useful, simple agent design and demonstration, though evaluation is limited in scale and scope and does not establish broad generality.

- **strength**: The paper clearly specifies a lightweight reflection trigger, memory cap, and retry loop, making the proposed mechanism concrete rather than merely motivational.
  - Page 3 · citation: whitespace
  - Quote: "we set a hyperparameter limit of three maximum reﬂections to be stored in the agent’s memory"

- **strength**: On the reported AlfWorld setup, reflection improved cumulative task completion over trials relative to the retry baseline.
  - Page 5 · citation: exact
  - Quote: "Given the ability to reﬂect, the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: The reported HotPotQA evaluation uses only 100 questions, and its first-trial result does not show an initial advantage for Reflexion; broader or more varied evaluation remains an open question, not a demonstrated defect.
  - Page 6 · citation: whitespace
  - Quote: "While the base ReAct agent achieved 34% accuracy and the Reﬂexion agent achieved 32% accuracy in the ﬁrst trials"

Unresolved questions:

- How robust are the reported gains across different LLMs, prompt choices, task samples, and settings beyond these two benchmarks?
- How much of the improvement depends on the particular heuristic, reflection examples, or accumulated memory, and how sensitive is performance to those choices?
- I inspected pages 2–8, including the method, benchmark results, and discussion, but not the remaining pages and appendices; details there may qualify experimental setup or provide further evidence.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "97%"}` | Locate the reported benchmark results and evaluation context. | 3 matches on pages [1, 2, 5] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect the proposed agent mechanism and experimental setup. | read pages [2, 3] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 4, "end": 6}` | Inspect benchmark results, comparisons, and evaluation details. | read pages [4, 5, 6] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 7, "end": 8}` | Check the authors’ discussion of limitations and interpretation. | read pages [7, 8] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.67, "observations": 3}}` | Submit a balanced assessment based on the inspected methods, results, and discussion pages. | review accepted | [event 26](trace.jsonl#L26) |
