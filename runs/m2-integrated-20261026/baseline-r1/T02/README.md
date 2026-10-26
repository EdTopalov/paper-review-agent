# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**baseline · ok**

1 model calls · 0 reads · 8.12 s · $0.002152

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

Refl e xion? Refl exion proposes a model-agnostic wrapper that stores language-model reflections after failed trials and feeds them into later attempts, using binary outcome feedback and simple failure heuristics. The paper reports gains over ReAct on AlfWorld and HotPotQA, but the results are proof-of-concept evidence: evaluation is limited in scale and scope, and the paper gives inconsistent HotPotQA performance figures.

- **strength**: The paper presents a straightforward mechanism for turning failed attempts into persistent, task-specific guidance, and demonstrates the approach on both interactive decision-making and search-based QA tasks.
  - Page 4 · citation: normalized
  - Quote: "Finally, we add the reflection to the agent’s memory, reset the environment, and start the next trial."

- **strength**: The AlfWorld experiment reports a substantial improvement across repeated trials, although this is evidence on the selected benchmark tasks rather than broad generalization.
  - Page 5 · citation: normalized
  - Quote: "Given the ability to reflect, the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: HotPotQA performance is reported inconsistently: the abstract gives 51%, while the results section reports 54%. This is a demonstrated reporting discrepancy that makes the headline figure unclear.
  - Page 1 · citation: exact
  - Quote: "We observe success rates of 97% and 51%, respectively"

- **uncertainty**: The supplied evaluation provides limited information about variability or robustness across independent runs; it is unclear how stable the reported gains are under different samples or model settings.
  - Page 5 · citation: whitespace
  - Quote: "we ran the agent in 134 AlfWorld environments across six different tasks"

Unresolved questions:

- How much of the gains persists across independent random seeds, task samples, and alternative base models?
- What are the token, latency, and API-cost tradeoffs of repeated reflection and trial execution compared with a single attempt?
- How sensitive are results to reflection prompt design, memory limits, and the heuristic thresholds?
- Which HotPotQA success rate is intended: 51% in the abstract or 54% in the results section?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes storing a reflection in memory, resetting the environment, and beginning another trial (PDF pp. 3–4). It evaluates ReAct-based Refl exion on AlfWorld and HotPotQA (PDF pp. 5–6), matching the claim’s stated scope.
- Observation 2: **supported** — The results report that Refl exion solved 97% of 134 AlfWorld environments over 12 trials, with four tasks unsolved; the assessment appropriately limits the inference to the selected benchmark tasks (PDF p. 5).
- Observation 3: **supported** — The abstract reports 51% for HotPotQA, while the results section reports 54% (PDF pp. 1, 6). This is a discrepancy in the paper’s reported figures.
- Observation 4: **supported** — The paper reports evaluations on 134 AlfWorld environments and 100 HotPotQA questions, but the supplied text does not describe independent-run variability or robustness across samples or model settings (PDF pp. 5–6). The observation is carefully framed as limited information and uncertainty, not as a demonstrated flaw.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
