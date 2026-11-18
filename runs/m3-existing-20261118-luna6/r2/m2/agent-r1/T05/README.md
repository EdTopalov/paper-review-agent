# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**agent · ok**

5 model calls · 4 reads · 9.21 s · $0.001264

5 decisions · 5 tool calls · 20302 input tokens (13559 cached) · 602 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

WebArena contributes a reproducible, self-hosted web-agent environment spanning four application domains, plus 812 long-horizon natural-language tasks assessed by functional outcomes rather than exact action traces. Its functional evaluations and low baseline success rates make it a useful testbed for agent research, although the benchmark’s chosen sites/tasks and text-based baseline evaluation bound what the results establish.

- **strength**: The work offers an integrated environment with realistic applications, support tools, and external knowledge resources, alongside reproducibility through self-hosting.
  - Page 3 · citation: whitespace
  - Quote: "We achieve reproducibility by having the environment be standalone, not relying on live websites."

- **strength**: The benchmark emphasizes whether goals are achieved, allowing different valid interaction paths, and includes a sizable collection of tasks.
  - Page 2 · citation: whitespace
  - Quote: "Along with WebArena, we release a ready-to-use benchmark with 812 long-horizon web-based tasks"

- **strength**: The paper provides a concrete baseline showing that complex tasks remain difficult for the tested language-model agents.
  - Page 9 · citation: whitespace
  - Quote: "The reasoning agent powered by GPT-4 achieves a relatively modest end-to-end task success rate of 10.63%."

- **limitation**: The implemented environment is deliberately bounded to selected website categories and examples derived from the authors’ browser histories, so realism does not establish broad coverage of web use.
  - Page 3 · citation: whitespace
  - Quote: "We then identified the four most salient categories and implemented one instance per category based on this analysis"

Unresolved questions:

- How robust are task annotations and functional evaluators across the full benchmark, including potentially valid outcomes not represented by their checks?
- How well do results transfer from these self-hosted sites and text/accessibility-tree agents to live websites or multimodal interaction?
- I inspected pages 2–3, 8–9, and 12; details elsewhere in the paper, including complete task distributions and broader evaluation evidence, remain unreviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's explicit scope and limitation discussion to assess benchmark boundaries. | 2 matches on pages [2, 11] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect benchmark design and task construction details supporting the contribution. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 9}` | Review reported evaluation results and failure analysis to gauge supporting evidence. | read pages [8, 9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 12, "end": 13}` | Inspect authors' discussion of benchmark boundaries and broader limitations. | read pages [12, 13] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Evidence covers the environment and benchmark design, task evaluation, baseline results, and conclusion; submit a balanced assessment while noting inspected-section limits. | review accepted | [event 25](trace.jsonl#L25) |
