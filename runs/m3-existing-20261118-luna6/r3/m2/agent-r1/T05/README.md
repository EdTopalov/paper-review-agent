# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**agent · ok**

6 model calls · 4 reads · 11.73 s · $0.001333

6 decisions · 6 tool calls · 24335 input tokens (18822 cached) · 949 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.77

WebArena contributes a self-hostable, functional multi-site web environment and an 812-task benchmark intended to assess whether agents actually complete realistic, long-horizon web tasks. Functional validation and reproducibility are meaningful benchmark-design strengths; baseline results establish a challenging reference point, though the evidence inspected does not establish broad real-world generalization.

- **strength**: The benchmark evaluates task outcomes rather than requiring one exact action trace, and the environment is designed for repeatable evaluation.
  - Page 2 · citation: exact
  - Quote: "We focus on evaluating the functional correctness of these tasks"

- **strength**: The task suite is substantial and explicitly targets varied, multi-step interactions across websites.
  - Page 5 · citation: exact
  - Quote: "We provide a benchmark with 812 test examples"

- **limitation**: The authors’ category selection is grounded in a relatively small, author-specific sample of browsing histories, leaving representativeness unresolved.
  - Page 3 · citation: whitespace
  - Quote: "an analysis of approximately 200 examples from the authors’ actual web browser histories"

- **uncertainty**: The reported low success rate signals difficulty, but the inspected passages do not establish whether the proposed failure explanation is causally supported or how results vary across task subsets.
  - Page 2 · citation: whitespace
  - Quote: "with an end-to-end task success rate of 10.59%"

Unresolved questions:

- How do task success and annotation/evaluator reliability vary across task categories and difficulty levels?
- How robust are results to agents beyond the reported few-shot GPT baselines and to changes in website data or interfaces?
- I inspected pages 1–3 and 5–6 plus a search result; detailed experimental tables, later analysis, and any additional limitations were not reviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "10.59%"}` | Locate the reported benchmark results and nearby evidence. | 2 matches on pages [1, 2] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark design and evaluation details on pages 2–3. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Review task composition, validation, and reported agent performance. | read pages [5, 6] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "limitations"}` | Check whether the authors explicitly state evaluation limitations. | 2 matches on pages [2, 11] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.77, "observations": 4}}` | Sufficient evidence collected on contribution, benchmark setup, and agent results; submit a bounded assessment noting uninspected sections. | citation_validation_failed; #4: wrong_page (pages [2]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.77, "observations": 4}}` | Correct the unsupported quote by citing the directly observed 10.59% result on page 2; preserve the bounded evidence assessment. | review accepted | [event 30](trace.jsonl#L30) |
