# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**pyagent_react · ok**

5 model calls · 4 reads · 14.07 s · $0.001831

5 decisions · 5 tool calls · 34135 input tokens (24794 cached) · 832 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

Reflexion adds a lightweight, trial-to-trial memory and language-model reflection loop to an acting agent, triggered by simple failure heuristics or task failure. In reported AlfWorld and HotPotQA evaluations, agents with reflection improve over retry-only ReAct baselines; the paper also reports little benefit on WebShop. The approach is promising and clearly illustrated, but the evidence is limited to a small set of tasks and experiments, and the WebShop result underscores that reflection cannot compensate for tool-quality constraints.

- **strength**: The proposed loop is a concrete, model-agnostic design: it uses a heuristic to trigger reflection, stores reflections in working memory, and retries without updating model parameters.
  - Page 3 · citation: whitespace
  - Quote: "In this study, we do not learn a policy over a state space."

- **strength**: The AlfWorld comparison reports substantial cumulative gains over retry-only ReAct across 134 environments, with a stopping rule based on consecutive-trial improvement.
  - Page 5 · citation: exact
  - Quote: "Given the ability to reﬂect, the agent used ReAct to solve 97% of the given environments in 12 trials"

- **uncertainty**: The paper reports different headline HotPotQA outcomes in its abstract and results section; the inspected passages do not explain the discrepancy.
  - Page 6 · citation: exact
  - Quote: "Reﬂexion enabled the agent to successfully answer 54% of the questions from the dataset"

- **limitation**: The WebShop experiment shows a near-flat outcome and unhelpful reflections; the authors suggest search-result quality may limit what reflection can improve.
  - Page 10 · citation: whitespace
  - Quote: "The agent achieved a 33% → 34% accuracy improvement in the baseline run and a mere33% → 35% accuracy improvement in the Reﬂexion run"

Unresolved questions:

- How robust are the gains across random seeds, model choices, and broader task samples? The inspected results describe 134 AlfWorld environments and 100 HotPotQA questions, but do not establish broader generalization.
- Would the reported improvements persist with alternative reflection prompts, memory policies, or evaluation criteria beyond the reported setup?
- How should the HotPotQA result be reconciled between the abstract’s 51% and the results section’s 54%?
- I inspected pages 1–11 only; the appendix and remaining pages were not reviewed, so I cannot assess their additional experimental details or prompt examples.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the method and task setup. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect benchmark results and evaluation details. | read pages [5, 6, 7] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 8, "end": 9}` | Inspect stated limitations and conclusions. | read pages [8, 9] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 10, "end": 11}` | Check discussion of scope and concluding claims. | read pages [10, 11] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit a review grounded in the inspected abstract, method, results, and limitations. | review accepted | [event 26](trace.jsonl#L26) |
