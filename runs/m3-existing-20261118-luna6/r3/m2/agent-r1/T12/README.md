# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**agent · ok**

5 model calls · 4 reads · 9.63 s · $0.001280

5 decisions · 5 tool calls · 23780 input tokens (17367 cached) · 640 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

InterCode makes a useful, clearly specified benchmark contribution by framing coding as interactive environment use with execution feedback, and supplies Bash/SQL implementations plus evaluations showing that interaction and reasoning prompts can improve success. The evidence is promising for the benchmark’s intended role, but the demonstrated task coverage remains narrow and the CTF extension is only a small illustration.

- **strength**: The paper defines an extensible interactive task formulation and a practical construction pipeline, pairing environment execution with customizable reward design.
  - Page 4 · citation: whitespace
  - Quote: "InterCode decomposes the construction of an interactive coding task into three modular parts: (1) environment construction, (2) data collection, and (3) reward design."

- **strength**: Results support the claim that execution feedback can improve task success across the reported model/task settings; the SQL gains are especially large for GPT-4.
  - Page 6 · citation: whitespace
  - Quote: "performance across different levels of task difficulty (SQL) and different file systems (Bash) is superior in the interactive setting for all models, with a notable multi-fold increase for GPT-4 (9.1% → 73.7%)"

- **limitation**: The authors explicitly bound the current breadth of evaluated environments and note that the CTF task has too few instances for a thorough benchmark assessment.
  - Page 9 · citation: whitespace
  - Quote: "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets;"

- **uncertainty**: The paper’s manual trajectory inspection suggests long-context interaction can falter, but the inspected evidence does not establish how broadly or reliably this behavior generalizes.
  - Page 7 · citation: whitespace
  - Quote: "This suggests that as the amount of context and feedback builds up, models are less capable of discerning relevant past history toward future actions."

Unresolved questions:

- How well do the framework and reported benefits extend to additional languages, environments, and datasets beyond Bash and SQL?
- How robust are the results across repeated runs or alternative task/reward designs? I inspected the primary result tables and discussion, not the full experimental setup or all appendix details.
- Can the CTF task support meaningful comparative evaluation once expanded beyond its four manually curated instances?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the authors’ stated scope boundaries and limitations. | 7 matches on pages [9, 13, 14, 26] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 4}` | Inspect benchmark design and experimental evidence for the paper’s central claims. | read pages [3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 7}` | Check reported model evaluations and the strength of empirical support. | read pages [6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 9}` | Read the conclusion and explicit limitations to calibrate contribution and uncertainty. | read pages [9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Evidence covers framework design, benchmark results, and stated scope limitations; submit a calibrated review. | review accepted | [event 25](trace.jsonl#L25) |
