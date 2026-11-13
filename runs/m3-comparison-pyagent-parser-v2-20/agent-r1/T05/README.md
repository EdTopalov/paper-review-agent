# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**agent · ok**

4 model calls · 2 reads · 11.07 s · $0.001292

4 decisions · 4 tool calls · 11377 input tokens (4926 cached) · 897 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

WebArena contributes a self-hostable web-agent environment and an 812-task benchmark across common web domains, evaluating task completion by functional outcomes rather than a single reference action trace. The paper reports that its tested agents perform poorly, while representativeness and broader generalization remain open questions.

- **strength**: The benchmark combines operational web applications, utility tools, and knowledge resources, with a focus on reproducible evaluation.
  - Page 2 · citation: exact
  - Quote: "WebArena creates websites from four popular categories with functionality and data mimicking\ntheir real-world equivalents."

- **strength**: Tasks are evaluated by whether execution achieves the goal, accommodating alternate valid paths.
  - Page 2 · citation: exact
  - Quote: "We focus on evaluating the functional correctness of these tasks"

- **strength**: The authors report low success for their strongest evaluated agent.
  - Page 1 · citation: exact
  - Quote: "only achieves an end-to-end task success rate of 10.59%."

- **limitation**: The selection of website categories was informed by an author-specific browser-history sample, constraining claims of broad representativeness.
  - Page 3 · citation: whitespace
  - Quote: "we first conducted an analysis of approximately 200 examples from the authors’ actual web browser histories."

Unresolved questions:

- How well do the benchmark tasks and applications generalize beyond the selected domains and author-derived browsing-history sample?
- How robust are the reported success rates to changes in task mix, evaluation criteria, or agent interaction strategies?
- I inspected the abstract and pages 2–3, plus search excerpts from pages 2 and 11; I did not inspect the full experimental results, detailed task construction, or complete limitations discussion.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper’s stated limitations to assess scope and caveats. | 2 matches on pages [2, 11] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect problem framing and benchmark design evidence on pages 2–3. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Evidence covers the benchmark’s contribution, task scope, validation approach, and some stated capability gaps; submit a qualified assessment. | citation_validation_failed; #3: wrong_page (pages [2]) | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Correct the page attribution for the reported success rate using the observed abstract, and submit the evidence-based review. | review accepted | [event 22](trace.jsonl#L22) |
