# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**agent · ok**

5 model calls · 4 reads · 10.71 s · $0.001306

5 decisions · 5 tool calls · 21056 input tokens (14490 cached) · 713 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

ReFlexion adds episodic natural-language reflection and bounded working memory to an LLM agent, using a heuristic trigger and binary success feedback to carry lessons across task retries. Its AlfWorld and HotPotQA evaluations suggest meaningful gains over retrying without reflection, but the evidence is limited to two setups and small reported evaluation samples, and does not establish generality across agents or domains.

- **strength**: The paper provides a concrete mechanism for autonomous iteration, connecting observed failures and trajectory context to a retained memory that can guide subsequent trials.
  - Page 3 · citation: normalized
  - Quote: "The reflection loop aims to help the agent correct common cases of hallucination and inefficiency through trial and error."

- **strength**: On the stated AlfWorld evaluation, reflection is associated with substantially higher cumulative task completion than the initial performance; the authors also distinguish learning from simply retrying.
  - Page 5 · citation: normalized
  - Quote: "Given the ability to reflect, the agent used ReAct to solve 97% of the given environments in 12 trials, failing to solve only 4 out of 134 tasks."

- **limitation**: The HotPotQA experiment uses only 100 questions, and the reported result differs across paper passages: the abstract says 51%, while the results passage reports 54%. This makes the precise headline figure uncertain.
  - Page 6 · citation: normalized
  - Quote: "We tested the base agent and Reflexion agent on a 100-question dataset."

- **limitation**: The approach depends on a heuristic and binary reward; the paper itself identifies these as requirements, so the evaluations do not demonstrate turnkey applicability where success signals or failure triggers are difficult to define.
  - Page 7 · citation: normalized
  - Quote: "A Reflexion agent must have access to a heuristic for termination and a binary reward model."

Unresolved questions:

- How robust are the gains to different LLMs, prompt examples, memory limits, and task distributions?
- Would the approach transfer to settings without a readily available binary success signal or hand-designed failure heuristic?
- What accounts for the HotPotQA discrepancy between the abstract's 51% and the results section's 54%?
- I inspected pages 1–7 only; later discussion, appendices, and any further limitations or evaluation details remain unreviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "97%"}` | Locate the reported benchmark results and their experimental context. | 3 matches on pages [1, 2, 5] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect the method description and setup for the reported agent evaluations. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 4, "end": 5}` | Review benchmark methodology, measured outcomes, and any stated limitations. | read pages [4, 5] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 7}` | Inspect HotPotQA evaluation details and discussion of scope or caveats. | read pages [6, 7] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.66, "observations": 4}}` | Evidence covers method, benchmark setup/results, and discussion; submit a calibrated assessment while noting remaining scope gaps. | review accepted | [event 25](trace.jsonl#L25) |
