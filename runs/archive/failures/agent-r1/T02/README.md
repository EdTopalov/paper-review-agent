# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**agent · ok**

5 model calls · 4 reads · 10.82 s · $0.001227

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Reflexion adds a simple, training-free mechanism for agents to use outcome-triggered verbal reflections as dynamic memory across repeated attempts. Results on AlfWorld and HotPotQA suggest substantial within-task improvement over retries alone, while the WebShop result and reliance on heuristics/reward signals bound the claim; the evidence supports a useful approach rather than broad, reliable autonomous learning.

- **strength**: The AlfWorld comparison is framed to distinguish reflection from mere retries, and shows improvement on 134 tasks.
  - Page 5 · citation: strict match
  - Quote: "the agent used ReAct to solve 97% of the given environments in 12 trials"

- **strength**: On HotPotQA, repeated reflection improved cumulative exact-match success, with retry-only baseline not improving.
  - Page 6 · citation: strict match
  - Quote: "the Reﬂexion agent achieved 32% accuracy in the ﬁrst trials"

- **limitation**: The approach depends on task-specific termination and binary reward machinery, which restricts how frictionlessly it transfers.
  - Page 7 · citation: strict match
  - Quote: "A Reﬂexion agent must have access to a heuristic for termination and a binary reward model."

- **limitation**: A third benchmark yielded little improvement, and the authors report that reflections were not helpful there.
  - Page 10 · citation: strict match
  - Quote: "The agent achieved a 33% → 34% accuracy improvement in the baseline run and a mere33% → 35% accuracy improvement in the Reﬂexion run"

Unresolved questions:

- How robust are the gains across model versions, random seeds, prompt choices, and larger benchmark samples?
- Which components of reflection or memory account for gains, and how sensitive are outcomes to the termination heuristic and reward definition?
- I inspected the abstract, pages 5–7, and pages 10–12; detailed method/implementation and appendix materials were not reviewed, so reproducibility and the full experimental protocol remain uncertain.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The AlfWorld setup compares a reflection run with a retry-only baseline by skipping reflection when the heuristic triggers, explicitly aiming to distinguish learning from probabilistic success over retries (PDF p. 5). The paper reports solving 97% of 134 environments with reflection, supporting the claim at that scope (PDF p. 5).
- Observation 2: **supported** — The paper reports that HotPotQA ReAct-only retries added no correct answers, while the reflection agent improved across consecutive trials and reached 54% cumulative accuracy (PDF pp. 6–7).
- Observation 3: **overstated** — The paper says an agent needs a termination heuristic and binary reward model (PDF p. 7), but does not establish that termination must be task-specific or that these requirements in fact impede transfer. It presents more specific heuristics as an option and gives examples of broadly applicable binary rewards (PDF pp. 7, 10).
- Observation 4: **supported** — On WebShop, the paper reports only a 33%→35% gain for Reﬂexion and says the agent was not generating helpful, intuitive self-reflections (PDF p. 10). The authors characterize this benchmark attempt as inconclusive (PDF p. 10).

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "97% 51% success rate comparison baseline"}` | Locate evaluation results and comparison evidence for the reported benchmark performance. | 0 matches | [event 5](trace.jsonl#L5) |
| 2 | search_paper `{"query": "AlfWorld HotPotQA results Table success"}` | Find the paper's main quantitative evaluation and its surrounding methodological context. | 0 matches | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect experimental setup, result tables, and claims supporting the benchmark outcomes. | response recorded | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 10, "end": 12}` | Review stated limitations and conclusion to accurately characterize scope and unanswered issues. | response recorded | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Evidence covers central method evaluation, benchmark limitations, and conclusion; submit a bounded assessment while noting uninspected details. | review accepted | [event 25](trace.jsonl#L25) |
