# T05: WebArena: A Realistic Web Environment for Building Autonomous Agents

**pyagent_react · ok**

5 model calls · 3 reads · 14.79 s · $0.001620

5 decisions · 4 tool calls · 25702 input tokens (17456 cached) · 831 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

WebArena contributes a self-hostable, interactive web benchmark spanning multiple web domains, with 812 natural-language tasks and programmatic checks intended to assess task outcomes rather than exact action sequences. Its baseline results and failure analysis illustrate the difficulty of long-horizon web interaction. This is a substantial and practically useful evaluation resource; the inspected evidence leaves questions about task representativeness and the robustness of its evaluation and baseline findings.

- **strength**: The benchmark combines several functional web applications with tools and knowledge resources, and supports multiple observation formats and tabs, making the environment a meaningful platform for studying web interaction.
  - Page 3 · citation: whitespace
  - Quote: "We then identified the four most salient categories and implemented one instance per category based on this analysis"

- **strength**: Outcome-oriented evaluation is a useful design choice: checks can accommodate different valid execution paths, and the paper describes annotation procedures that include double annotation for information-seeking answers.
  - Page 8 · citation: exact
  - Quote: "These examples allow us to assess an agent’s ability to avoid making unfounded claims"

- **limitation**: The authors’ category selection draws on browser histories from the authors themselves; the inspected account does not establish how well those histories represent broader users or web tasks.
  - Page 3 · citation: whitespace
  - Quote: "we first conducted an analysis of approximately 200 examples from the authors’ actual web browser histories"

- **uncertainty**: The reported GPT-4 success rate is inconsistent across inspected pages: the results table and abstract give 10.59%, while the page 9 prose gives 10.63%. This is an observed reporting discrepancy; its source is unclear.
  - Page 9 · citation: whitespace
  - Quote: "The reasoning agent powered by GPT-4 achieves a relatively modest end-to-end task success rate of 10.63%."

Unresolved questions:

- How representative are the benchmark tasks and website content of users and web tasks beyond the authors’ browsing-history sample?
- How sensitive are task success and baseline comparisons to the annotation and evaluation checks, model sampling variability, and agent configuration?
- What explains the discrepancy between 10.59% and 10.63% in the reported GPT-4 result?
- I inspected pages 1–4 and 8–12, not the full paper or appendices; details of the complete task inventory, environment implementation, and additional experimental analyses therefore remain unassessed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the benchmark design, task construction, and agent evaluation evidence. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect task validation procedures and benchmark dataset construction. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 11, "end": 12}` | Inspect the paper's stated limitations and interpretation of benchmark results. | read pages [11, 12] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit an evidence-based assessment from the inspected pages, noting the result discrepancy and uninspected portions. | review accepted | [event 25](trace.jsonl#L25) |
