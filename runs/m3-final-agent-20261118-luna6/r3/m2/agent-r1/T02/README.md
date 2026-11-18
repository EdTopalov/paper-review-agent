# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**agent · ok**

6 model calls · 5 reads · 10.92 s · $0.002483

6 decisions · 6 tool calls · 30569 input tokens (14500 cached) · 697 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Reflexion adds persistent natural-language reflections to an LLM agent’s memory between task attempts, triggered by simple failure heuristics or unsuccessful outcomes. Results on AlfWorld and HotPotQA suggest that reflection can improve cumulative task completion over repeated trials, offering a practical, training-free mechanism for learning from errors. The evidence is promising but limited to two benchmarks and comparatively small evaluated sets, and the inspected results do not isolate reflection from other trial-to-trial effects comprehensively.

- **strength**: The paper reports strong AlfWorld improvement across repeated attempts and gives a concrete scale and comparator.
  - Page 5 · citation: normalized
  - Quote: "Given the ability to reflect, the agent used ReAct to solve 97% of the given environments in 12 trials, failing to solve only 4 out of 134 tasks."

- **strength**: The HotPotQA experiment reports cumulative gains over a retry baseline, with a defined dataset size and evaluation rule.
  - Page 6 · citation: normalized
  - Quote: "We tested the base agent and Reflexion agent on a 100-question dataset."

- **limitation**: HotPotQA first-trial accuracy is lower for Reflexion, and the comparison involves a sequential multi-trial process rather than a single-run accuracy test.
  - Page 6 · citation: normalized
  - Quote: "While the base ReAct agent achieved 34% accuracy and the Reflexion agent achieved 32% accuracy in the first trials (Fig. 3), the Reflexion agent was able to outperform the base ReAct agent over the course of 7 trials."

- **limitation**: The method’s applicability is conditional on having a usable heuristic and binary reward signal, an important scope constraint the authors acknowledge.
  - Page 7 · citation: whitespace
  - Quote: "A Reﬂexion agent must have access to a heuristic for termination and a binary reward model."

Unresolved questions:

- How robust are the gains across different LLMs, prompt choices, task splits, and random seeds?
- How much of the improvement is attributable specifically to persistent reflection rather than extra attempts or changes in generated trajectories?
- The inspected pages do not include the full appendix or all implementation details, so the reproducibility and prompt-sensitivity assessment remains incomplete.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "97%"}` | Locate the paper’s reported benchmark results and evaluation context. | 3 matches on pages [1, 2, 5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Read the approach and experimental setup to assess contribution and strength of evidence. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 4, "end": 5}` | Inspect benchmark protocols and results to judge how directly the performance claims are supported. | read pages [4, 5] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 7}` | Check HotPotQA quantitative results and any stated methodological limitations. | read pages [6, 7] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 8, "end": 9}` | Inspect the authors’ stated scope boundaries and conclusion to capture caveats and open issues. | read pages [8, 9] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | The inspected pages establish the core method, both benchmark protocols, headline outcomes, and a key caveat; submitting the assessment while noting inspected-text limits. | review accepted | [event 31](trace.jsonl#L31) |
