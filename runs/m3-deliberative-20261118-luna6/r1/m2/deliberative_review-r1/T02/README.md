# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**deliberative_review · ok**

8 model calls · 4 reads · 38.10 s · $0.009222

8 decisions · 5 tool calls · 60667 input tokens (0 cached) · 3303 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.7

Reflexion adds persistent natural-language reflections to an LLM agent’s memory so it can use feedback from failed attempts on later trials. The reported AlfWorld and HotPotQA results show cumulative gains over retrying without reflection, offering a useful demonstration of trial-and-error learning. The evidence is promising but is limited to the inspected evaluations, and the inspected text does not isolate the effects of reflection, memory, and other design choices.

- **strength**: The method provides a concrete trigger for reflection: repeated action-observation cycles or a trial action limit. Reflections are added to memory for subsequent trials.
  - Page 3 · citation: whitespace
  - Quote: "repeat is a simple function that determines the number of repetitive action cycles that yield the same observation(s)."

- **strength**: On 134 AlfWorld environments, the reported cumulative success reaches 97% after 12 trials. The authors characterize this as improvement through learning across attempts, rather than a single-trial comparison.
  - Page 5 · citation: exact
  - Quote: "Given the ability to reﬂect, the agent used ReAct to solve 97% of the given environments in 12 trials,"

- **limitation**: On the 100-question HotPotQA evaluation, Reflexion began below the baseline in the first trial; its reported advantage emerged over repeated trials. This qualifies the headline improvement without negating it.
  - Page 6 · citation: whitespace
  - Quote: "While the base ReAct agent achieved 34% accuracy and the Reﬂexion agent achieved 32% accuracy in the ﬁrst trials (Fig. 3), the Reﬂexion agent was able to outperform the base ReAct agent over the course of 7 trials."

- **limitation**: The reported WebShop attempt did not show a clear advantage, and the authors note that search-engine result quality could constrain success. This is a concrete qualification on the method’s demonstrated scope, not evidence that Reflexion cannot help in other settings.
  - Page 10 · citation: whitespace
  - Quote: "The agent achieved a 33% → 34% accuracy improvement in the baseline run and a mere33% → 35% accuracy improvement in the Reﬂexion run"

Unresolved questions:

- Do controlled ablations separate the effects of persistent memory, reflection text, and the heuristic trigger? The inspected pages describe these components and report combined results, but do not establish their individual contributions.
- How robust are the reported gains across different models, prompts, and task samples?
- Pages 11–17 were not inspected; they may contain additional results, qualifications, or analyses relevant to these questions.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the method and task setup to identify what Reflexion changes—especially the reflection heuristic, memory, and use of feedback—and whether the evaluation supports claims about those components.; Check the full results and comparison details for AlfWorld and HotPotQA, including baselines, trial counts, and any ablations or examples that qualify the reported success rates.; Review discussion and limitations, then select 2–4 observations grounded in exact page-quoted text; explicitly note that only page 1 is currently inspected and avoid treating uninspected material as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2, 4] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [2, 3, 4] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [5, 6, 7] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The draft appropriately discloses that pages 8–17 were not inspected, but the review obligations specifically call for checking the full results and discussion. The current evidence cannot establish whether later pages add qualifications, ablations, or limitations.; The final observation’s quote about using a simple heuristic does not directly support its claim that the inspected pages do not isolate the contributions of memory and reflection.; Target: Do pages 8–17 report ablations or additional results and limitations that qualify the claims about Reflexi … | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | read pages [8, 9, 10] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | Draft revised; Changes: Updated the review to incorporate the observed pages 8–10, including the illustrative trajectories and WebShop qualification. Replaced the prior uncertainty observation whose quotation did not substantiate its claim with a directly supported WebShop limitation. The critic’s concern about uninspected pages remains valid for pages 11–17; no claims are made about their contents. | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "AlfWorld"}` | Find evaluation/results pages and inspect supporting evidence for method and benchmark claims. | 8 matches on pages [1, 2, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 2, "end": 4}` | Inspect method and initial evaluation setup and reported claims. | read pages [2, 3, 4] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 5, "end": 7}` | Inspect evaluation results and comparisons to assess evidence for reported gains. | read pages [5, 6, 7] | [event 22](trace.jsonl#L22) |
| 7 | read_pages `{"start": 8, "end": 10}` | Check subsequent results, ablations, and limitations. | read pages [8, 9, 10] | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.7, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 45](trace.jsonl#L45) |
