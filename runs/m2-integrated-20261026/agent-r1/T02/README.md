# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**agent · ok**

4 model calls · 3 reads · 12.96 s · $0.001207

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

Reflexion adds a practical, training-free loop in which an LLM agent reflects on failed attempts and stores the resulting guidance in dynamic memory, using binary success feedback. The reported gains on AlfWorld and HotPotQA are promising, but evaluations are modest in scale and the approach does not improve meaningfully on WebShop, limiting the strength and breadth of the evidence.

- **strength**: The core design is simple and potentially broadly usable: reflection is stored between trials, while the reward signal is deliberately restricted to success or failure.
  - Page 4 · citation: whitespace
  - Quote: "By limiting the agent’s knowledge to a binary success status within an environment, we force the agent to make meaningful inferences about its performance without external input"

- **strength**: The AlfWorld result is substantial on the tested set and is framed as improvement through learning rather than merely retrying.
  - Page 5 · citation: whitespace
  - Quote: "the agent used ReAct to solve 97% of the given environments in 12 trials, failing to solve only 4 out of 134 tasks."

- **limitation**: The HotPotQA evaluation uses only 100 questions; reported gain over baseline is encouraging but does not establish broad generalization.
  - Page 6 · citation: exact
  - Quote: "We tested the base agent and Reﬂexion agent on a 100-question dataset."

- **limitation**: The authors report little benefit in WebShop and note that tool search quality can limit what reflection and planning can accomplish.
  - Page 10 · citation: whitespace
  - Quote: "The agent achieved a 33% → 34% accuracy improvement in the baseline run and a mere33% → 35% accuracy improvement in the Reﬂexion run"

Unresolved questions:

- How robust are the improvements across larger and more diverse task sets, model versions, and repeated runs?
- How much of the gains depends on prompt examples, trial budget, or the particular reflection heuristic?
- I inspected pages 4–6 and 9–11, not the full paper; detailed prompting, ablations, and other methodological particulars remain unassessed.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes adding reflections to working memory before resetting and trying again (PDF pp. 3–4), and explicitly constrains the agent to binary success/failure feedback (p. 4). Its discussion also presents the approach as broadly applicable, so “potentially” is appropriately qualified (pp. 7, 10).
- Observation 2: **supported** — The evaluation covers 134 AlfWorld environments, and reports solving 97% in 12 trials (PDF p. 5). The authors explicitly characterize the comparison as improved accuracy through self-improved learning rather than success by retry (p. 5).
- Observation 3: **supported** — The HotPotQA evaluation used 100 questions (PDF p. 6). The paper reports improvement over the baseline across trials, but this test size does not itself establish generalization to broader datasets; the assessment appropriately describes that as unestablished rather than as a demonstrated failure (pp. 6–7).
- Observation 4: **supported** — The paper reports only small WebShop gains after four trials and says the agent did not show helpful, intuitive reflections (PDF p. 10). It also notes that successful purchase outcomes may depend on search-engine result quality, which reflection cannot fully address (p. 10).

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper’s explicit scope and limitations discussion. | 2 matches on pages [10] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 6}` | Inspect method and experimental results to assess novelty and evidential support. | read pages [4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 9, "end": 11}` | Read discussion, limitations, and concluding claims to calibrate scope and caveats. | read pages [9, 10, 11] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Evidence covers proposed binary-reward reflection method, benchmark results, and stated failure case; submit a balanced assessment while noting uninspected sections. | review accepted | [event 20](trace.jsonl#L20) |
