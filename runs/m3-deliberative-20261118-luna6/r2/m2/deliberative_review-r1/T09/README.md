# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**deliberative_review · ok**

6 model calls · 3 reads · 21.69 s · $0.004717

6 decisions · 4 tool calls · 30963 input tokens (1274 cached) · 2006 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

AGENTLESS presents a transparent, two-phase alternative to interactive software-engineering agents: hierarchical code localization followed by patch generation, filtering, and majority voting. Its reported SWE-bench Lite results and manual construction of a filtered subset make it a useful empirical baseline and raise worthwhile questions about benchmark quality. The inspected evidence is promising, but does not establish the comparative results independently, and substantial portions of the paper were not available for inspection.

- **strength**: The method is described concretely enough to understand its localization and repair pipeline, including patch filtering and selection.
  - Page 5 · citation: whitespace
  - Quote: "We filter out any patches with syntax and regression tests errors, and finally select the patch for submission using classic majority voting."

- **strength**: The evaluation reports a measurable result on a specified 300-problem benchmark and compares against multiple agent approaches, though the supplied excerpts do not include the complete results table.
  - Page 6 · citation: whitespace
  - Quote: "We observe that AGENTLESS is able to solve 82 out of 300 problems (27.33%)."

- **limitation**: The paper identifies potentially problematic benchmark items and excludes them from its filtered evaluation; this is a useful scope clarification, but the supplied evidence does not let us assess the classification procedure in detail.
  - Page 10 · citation: exact
  - Quote: "We refer to our subset of 252 problems as SWE-bench Lite-S."

- **uncertainty**: The authors note that most closed-source baselines lack trajectories and that their steps cannot be verified, limiting the transparency of those comparisons. The available excerpts do not establish how much this affects the headline comparison.
  - Page 6 · citation: whitespace
  - Quote: "Therefore, we cannot verify the steps taken to arrive at the final patches."

Unresolved questions:

- How robust are the reported results to changes in localization, patch sampling, and voting settings? The supplied pages describe the setup but do not provide enough inspected ablation evidence to answer this.
- How were the benchmark issues classified and removed, and how reproducible are the resulting SWE-bench Lite-S judgments?
- What qualifications or limitations are discussed in the uninspected pages? Eight pages are uninspected, and several inspected pages are only partially represented in the supplied excerpts.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the method and experimental sections to verify what AGENTLESS does and whether its localization-and-repair design supports the central performance and cost claims.; Check benchmark setup, baselines, results, and supporting analyses—including SWE-bench Lite-S—to assess comparison fairness and whether the reported evidence supports the claimed advantage.; Inspect the remaining pages for limitations, caveats, and further evidence; only page 1 is currently available, so avoid treating uninspected material as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [3, 10, 11, 12] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [4, 5, 6] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | 3 matches on pages [2, 3, 12] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: approve | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "SWE-bench Lite-S"}` | Inspect result evidence and benchmark analysis beyond supplied first-page excerpt. | 8 matches on pages [3, 10, 11, 12] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 4, "end": 6}` | Inspect method details and experiment setup to evaluate the claimed two-stage approach and evidence. | read pages [4, 5, 6] | [event 16](trace.jsonl#L16) |
| 4 | search_paper `{"query": "limitations"}` | Inspect discussion/conclusion for caveats and counterevidence to central performance claims. | 3 matches on pages [2, 3, 12] | [event 22](trace.jsonl#L22) |
| 6 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 34](trace.jsonl#L34) |
