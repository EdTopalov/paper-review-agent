# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**agent · ok**

5 model calls · 4 reads · 11.77 s · $0.001579

5 decisions · 5 tool calls · 23096 input tokens (13918 cached) · 616 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

AGENTLESS presents a simple, interpretable pipeline for repository-level issue repair: hierarchical code localization followed by sampled patch generation, test filtering, and voting. The evaluated method achieves 82/300 fixes on SWE-bench Lite at an average reported cost of $0.34, and the paper contributes a manual problem classification and filtered Lite-S subset. The combination and evaluation are useful and supported, though the paper’s strongest claims are tied to this benchmark and reported comparisons.

- **strength**: The paper gives a clear, technically concrete localization-and-repair workflow rather than relying on an opaque sequence of autonomous tool actions.
  - Page 5 · citation: exact
  - Quote: "AGENTLESS solves repository-level issues using a simple step-by-step procedure."

- **strength**: The benchmark results support a meaningful performance-cost tradeoff, with ablations showing benefits from sampling/voting and test filtering.
  - Page 8 · citation: exact
  - Quote: "+ test filtering\n(full AGENTLESS) 82 (27.33%) $0.34"

- **strength**: The authors identify benchmark quality concerns and evaluate on a curated subset, while showing AGENTLESS remains competitive but is not the top-ranked method.
  - Page 10 · citation: exact
  - Quote: "AGENTLESS\n GPT-4o 82 (27.33%) 5 71 (28.17%) 5"

- **limitation**: The revised benchmark comparison excludes commercial tools because the authors could not run them on the modified problems, limiting like-for-like validation of Lite-S rankings.
  - Page 10 · citation: whitespace
  - Quote: "as we are not able to run commercial tools ourselves on the modified problems, we simply exclude the problematic problems in the below evaluation."

Unresolved questions:

- How robust is the approach across repositories, benchmarks, model versions, and issue types beyond SWE-bench Lite and Lite-S?
- How sensitive are the results and cost estimates to prompting, sampling settings, and tool/model changes?
- I inspected pages 1–10 and did not inspect the remainder of the paper; additional limitations or evaluation details may therefore be unreviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's stated limitations to assess scope and evidence. | 3 matches on pages [2, 3, 12] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 5}` | Inspect the method and core benchmark results supporting the contribution. | read pages [4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 8}` | Review quantitative benchmark comparisons and evaluation setup. | read pages [7, 8] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 10}` | Inspect benchmark curation findings and reported evaluation caveats. | read pages [9, 10] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Evidence covers the approach, quantitative evaluation, and benchmark curation; submit a balanced reading-club assessment with remaining scope gaps. | review accepted | [event 25](trace.jsonl#L25) |
