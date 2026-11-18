# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**pyagent_react · ok**

5 model calls · 4 reads · 17.62 s · $0.001834

5 decisions · 5 tool calls · 34681 input tokens (26236 cached) · 1032 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

WebArena contributes a reproducible, self-hostable environment of functional web applications and an 812-task benchmark for evaluating agents on realistic multi-step web tasks. It emphasizes goal-based functional evaluation rather than matching action traces, and its baseline results expose substantial challenges for current agents. The benchmark is a useful research contribution, while the inspected evidence leaves open how representative its curated tasks and sites are of broader web use.

- **strength**: The environment combines multiple web domains, tools, and knowledge resources, and is designed for standalone reproducible use.
  - Page 3 · citation: whitespace
  - Quote: "We achieve reproducibility by having the environment be standalone, not relying on live websites."

- **strength**: The benchmark uses outcome-oriented checks that can accommodate different valid execution paths.
  - Page 2 · citation: whitespace
  - Quote: "This evaluation is not only more reliable [40, 5, 33] than comparing the vanilla action sequences"

- **limitation**: The authors acknowledge that some benchmark tasks cannot be completed in the provided environment and label them accordingly; this is a stated scope constraint, not evidence that the rest of the benchmark is defective.
  - Page 8 · citation: whitespace
  - Quote: "some tasks ( ∼4%) in our benchmark are not possible to complete."

- **uncertainty**: The reported baseline success rates are low, but the inspected results cover a small set of text-based prompting agents and configurations; how alternative observations, agent designs, or evaluation settings compare remains unanswered here.
  - Page 9 · citation: exact
  - Quote: "the actions are not flawless."

Unresolved questions:

- How well do tasks and content sampled from the selected applications represent web tasks beyond these four application domains and the authors’ browsing-history analysis?
- How sensitive are performance conclusions to the selected observation/action interface, model settings, and benchmark evaluation rules?
- I inspected pages 1–11 and a search result for “Limitations”; I did not inspect pages 12–23, including later discussion and appendices, so additional evidence or qualifications may remain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark construction and task design. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 5, "end": 7}` | Inspect task coverage and benchmark evaluation methodology. | read pages [5, 6, 7] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect agent baselines and reported benchmark results. | read pages [8, 9, 10] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "Limitations"}` | Locate the authors’ stated limitations to qualify the assessment. | 2 matches on pages [2, 11] | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Submit a qualified assessment grounded in inspected benchmark, evaluation, and results pages. | review accepted | [event 26](trace.jsonl#L26) |
