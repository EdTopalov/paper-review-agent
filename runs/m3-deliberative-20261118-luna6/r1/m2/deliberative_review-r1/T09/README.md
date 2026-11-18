# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**deliberative_review · ok**

8 model calls · 3 reads · 44.49 s · $0.009822

8 decisions · 5 tool calls · 61217 input tokens (0 cached) · 4359 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AGENTLESS demonstrates that hierarchical code localization followed by sampled patch generation, regression-test filtering, and majority voting can solve repository-level SWE-bench Lite issues with a relatively simple pipeline. Its reported results support the effectiveness and low cost of this design, while manual benchmark analysis identifies potentially consequential issue-description problems. The evidence is bounded by the benchmark and GPT-4o setup, and baseline comparisons partly rely on results the authors did not reproduce. Six pages were not inspected, and the supplied Lite-S results are incomplete.

- **strength**: The repair ablation reports gains from sampling and majority voting over one sample, with test filtering adding further fixes.
  - Page 8 · citation: whitespace
  - Quote: "We can further improve performance to 78 fixes by sampling the LLM multiple times and selecting a patch using majority voting."

- **strength**: The manual benchmark analysis finds that some issue descriptions lack information needed to solve the task, supporting the authors’ concern about benchmark quality. The supplied excerpts do not establish classification reliability or show the full Lite-S results.
  - Page 9 · citation: whitespace
  - Quote: "there is a non-trivial percentage (9.3%) of problems which do not contain enough information."

- **limitation**: Baseline comparisons are not uniformly reproduced: the paper uses results from official or published sources. This limits direct comparability, though it does not invalidate the authors’ reported run.
  - Page 6 · citation: whitespace
  - Quote: "For baseline tools, we directly use the reported results either from the official leaderboard [29] or from the tool’s official paper/repository."

Unresolved questions:

- How reliable and reproducible are the manual issue classifications and exclusion decisions, and how do results compare across all 252 SWE-bench Lite-S issues?
- How well does the approach generalize beyond SWE-bench Lite and the reported GPT-4o implementation?
- How sensitive are results and costs to choices such as sample count, localization prompts, and regression-test availability?
- What further limitations or validation are discussed on the six uninspected pages?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the methods and results pages for how localization and repair are implemented, and whether the reported SWE-bench Lite solve rate and cost are supported by clearly specified evaluation procedures and comparisons.; Check the paper’s treatment of SWE-bench Lite-S: how issues were classified or excluded, and whether results on this subset support the claims about misleading descriptions or ground-truth patches.; Inspect the remaining pages for limitations, experimental scope, and relevant ablations or validation; only page 1 is currently available, so avoid treating uninspected ma … | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [3, 10, 11, 12] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [4, 5, 6] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [7, 8, 9] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The first observation claims component-level performance improvements, but its page 5 quote only describes the overall procedure. Cite the component results on page 8 instead.; The second observation cites page 9, but its quoted text appears on page 8 in the supplied source. Correct the page citation and ensure the quote supports the claim about classification.; The inspected excerpts do not include the complete Lite-S results or all remaining pages. Keep claims about those materials explicitly qualified. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Updated the first observation to cite the page 8 repair ablation, and used a verbatim page 9 classification quotation. Kept claims about the incomplete Lite-S results and uninspected pages qualified; no score change was warranted. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |
| 8 | revise | Draft revised; Changes: Corrected the first observation to cite the page 8 ablation evidence and replaced the second quote with an exact page 9 passage. Kept the Lite-S assessment qualified because its supplied results are incomplete, and explicitly noted the uninspected pages. | [event 42](trace.jsonl#L42) · [event 45](trace.jsonl#L45) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "SWE-bench Lite-S"}` | Locate the subset construction and evaluation evidence for the paper’s benchmark claims. | 8 matches on pages [3, 10, 11, 12] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 4, "end": 6}` | Inspect core Agentless method details and experimental setup. | read pages [4, 5, 6] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 7, "end": 9}` | Inspect main results and benchmark issue auditing evidence/counterevidence. | read pages [7, 8, 9] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.72, "observations": 3}}` | Submit after the enforced critique and source validation. | citation_validation_failed; #2: wrong_page (pages [8]) | [event 39](trace.jsonl#L39) |
| 8 | submit_review `{"review": {"score": 0.72, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 47](trace.jsonl#L47) |
