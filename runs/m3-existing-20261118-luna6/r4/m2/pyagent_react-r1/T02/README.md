# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**pyagent_react · ok**

5 model calls · 4 reads · 13.73 s · $0.001770

5 decisions · 5 tool calls · 34139 input tokens (25537 cached) · 879 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Reflexion adds a practical trial-to-trial loop in which an LLM reflects on failed trajectories and stores advice in dynamic memory, using a heuristic trigger and binary success feedback. The paper reports substantial cumulative gains on AlfWorld and HotPotQA, with illustrative examples of changed behavior. Evidence is promising but limited to a small set of benchmarks and trials, and the paper itself reports little benefit on WebShop. I inspected pages 1–11 only; the appendices and remaining pages were not reviewed.

- **strength**: The method is clearly specified as a lightweight, model-agnostic addition to an existing agent loop, with a defined reflection trigger and memory limit.
  - Page 3 · citation: whitespace
  - Quote: "In practice, we set a hyperparameter limit of three maximum reﬂections to be stored in the agent’s memory"

- **strength**: On the reported AlfWorld evaluation, Reflexion substantially increased cumulative task completion over repeated trials.
  - Page 5 · citation: exact
  - Quote: "the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: The authors report a third benchmark where Reflexion yielded only a small improvement, showing that gains do not extend uniformly across the tested tasks.
  - Page 10 · citation: whitespace
  - Quote: "The agent achieved a 33% → 34% accuracy improvement in the baseline run and a mere33% → 35% accuracy improvement in the Reﬂexion run"

- **uncertainty**: HotPotQA improvement is reported with inconsistent summary figures in the inspected text, making the exact headline gain unclear.
  - Page 6 · citation: whitespace
  - Quote: "Reﬂexion agent achieved 32% accuracy in the ﬁrst trials"

Unresolved questions:

- What explains the difference between the abstract’s HotPotQA result of 51% and the page 6 result of 54%, and between the stated gains of 17% and 20%?
- How robust are the reported gains across random seeds, different base models, and broader task samples?
- What do the uninspected pages and appendices add about prompts, implementation details, and experimental variability?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the proposed reflection loop and experimental setup. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark results and comparison details. | read pages [5, 6, 7] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 8, "end": 9}` | Inspect stated scope boundaries and additional evaluation details. | read pages [8, 9] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 10, "end": 11}` | Check the paper's concluding claims and explicit limitations. | read pages [10, 11] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit an evidence-based assessment from the inspected pages, noting unresolved scope and reporting uncertainty. | review accepted | [event 26](trace.jsonl#L26) |
