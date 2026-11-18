# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**agent · ok**

5 model calls · 4 reads · 10.25 s · $0.001670

5 decisions · 5 tool calls · 28889 input tokens (19505 cached) · 635 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

AGENTLESS presents a deliberately simple, interpretable alternative to autonomous software-engineering agents: hierarchical code localization followed by sampled patch generation, regression-test filtering, and majority selection. On SWE-bench Lite it reports 27.33% resolved at $0.34 per issue, and evaluates a manually filtered 252-issue subset. The combination is a substantial, well-supported baseline contribution, though comparative conclusions rely partly on reported results from other systems rather than uniformly reproduced runs.

- **strength**: The paper’s clear two-phase design is a useful contribution and its repair ablation supports the value of sampling and selection beyond a single generation.
  - Page 5 · citation: exact
  - Quote: "AGENTLESS solves repository-level issues using a simple step-by-step procedure."

- **strength**: Reported benchmark results support competitive performance and low average inference cost, and the component comparison provides some empirical support for the design.
  - Page 8 · citation: whitespace
  - Quote: "We can further improve performance to 78 fixes by sampling the LLM multiple times and selecting a patch using majority voting."

- **strength**: The manual benchmark audit identifies concrete issue-description problems and supplies a filtered evaluation set, adding value beyond the proposed system.
  - Page 9 · citation: whitespace
  - Quote: "there is a non-trivial percentage (9.3%) of problems which do not contain enough information."

- **limitation**: Comparisons are not fully controlled: the authors state that most closed-source baselines provide neither source nor trajectories, and they use reported results; modified-benchmark commercial systems could not be rerun.
  - Page 10 · citation: whitespace
  - Quote: "we are not able to run commercial tools ourselves on the modified problems"

Unresolved questions:

- Would the comparative ranking hold if all baselines were rerun under the same model versions, evaluation setup, and cost accounting?
- How sensitive are the results to the manual issue classifications and the selected localization, sampling, and filtering settings?
- How well does the approach generalize beyond SWE-bench Lite and GPT-4o? The inspected pages do not establish this.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "SWE-bench Lite-S"}` | Locate the paper's evaluation and benchmark discussion for evidence. | 8 matches on pages [3, 10, 11, 12] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 6}` | Inspect method design and primary experimental results to assess contribution and evidence. | read pages [4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 8}` | Read comparative results and any cost or localization analyses supporting the headline claims. | read pages [7, 8] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 10}` | Inspect benchmark audit details and filtered-set results, including the authors' stated caveats. | read pages [9, 10] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Evidence covers method, reported benchmark outcomes, ablations, and authors' benchmark audit; submit an independent assessment while noting uninspected areas. | review accepted | [event 25](trace.jsonl#L25) |
