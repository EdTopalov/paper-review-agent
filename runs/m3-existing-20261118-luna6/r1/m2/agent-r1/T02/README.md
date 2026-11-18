# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**agent · ok**

4 model calls · 3 reads · 11.57 s · $0.001726

4 decisions · 4 tool calls · 23127 input tokens (12730 cached) · 623 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.65

Reflexion is a simple, model-agnostic trial-to-trial memory and self-reflection wrapper for LLM agents, using binary success feedback and heuristics to trigger reflection. Its AlfWorld and HotPotQA results provide promising evidence that written feedback can improve subsequent attempts, but evaluation is narrow and the authors report little benefit on WebShop.

- **strength**: The paper gives a concrete and lightweight mechanism: store self-reflections and feed them into future attempts, with heuristic triggers intended to detect repetitive or overlong trajectories.
  - Page 3 · citation: normalized
  - Quote: "The reflection loop aims to help the agent correct common cases of hallucination and inefficiency through trial and error."

- **strength**: On 134 AlfWorld environments, the reported success rate rises to 97% over 12 trials, compared with 63% initial accuracy; a no-reflection retry baseline is included to distinguish improvement from simple retries.
  - Page 5 · citation: normalized
  - Quote: "Given the ability to reflect, the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: HotPotQA evaluation uses only 100 questions and exact-match grading; the reported initial ReAct accuracy was slightly higher than Reflexion's, despite Reflexion's later cumulative advantage.
  - Page 6 · citation: normalized
  - Quote: "While the base ReAct agent achieved 34% accuracy and the Reflexion agent achieved 32% accuracy in the first trials"

- **limitation**: The paper reports weak WebShop improvement and unhelpful reflections, indicating that the approach's utility does not transfer uniformly to this tested task.
  - Page 10 · citation: whitespace
  - Quote: "The agent achieved a 33% → 34% accuracy improvement in the baseline run and a mere33% → 35% accuracy improvement in the Reﬂexion run"

Unresolved questions:

- How robust are the gains across random seeds, alternative base models, and substantially larger or more diverse task samples?
- Which aspects of the approach account for the gains—reflection content, persistent memory, heuristic-triggered stopping, or additional attempts—and how sensitive are outcomes to prompt and heuristic choices?
- I inspected pages 1–10 only; the remaining pages, including any further experimental details or appendices, were not reviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect method description and experimental setup to assess contribution and evidence. | read pages [2, 3, 4] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Read benchmark results and reported comparisons to evaluate empirical support. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect stated limitations and conclusion for scope and open questions. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.65, "observations": 4}}` | Sufficient inspected evidence spans method, benchmark outcomes, and limitations; submit independent assessment with explicit scope caveat. | review accepted | [event 20](trace.jsonl#L20) |
