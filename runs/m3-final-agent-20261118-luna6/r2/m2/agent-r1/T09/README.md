# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**agent · ok**

7 model calls · 4 reads · 20.91 s · $0.002391

7 decisions · 7 tool calls · 46100 input tokens (36283 cached) · 1647 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

AGENTLESS argues that repository-level issue repair need not rely on autonomous, tool-using LLM agents. Its structured localization-then-repair pipeline is a simple, interpretable baseline that reports strong SWE-bench Lite performance at low cost; manual problem classification and the filtered Lite-S subset are useful evaluation contributions. Evidence is persuasive for this benchmark setting, but comparisons on the filtered subset reuse prior tools’ reported results rather than rerunning commercial systems, and broader generalization remains open.

- **strength**: The paper contributes a concrete, understandable alternative to agentic workflows: hierarchical fault localization followed by candidate patch generation, filtering, and ranking.
  - Page 2 · citation: exact
  - Quote: "AGENTLESS follows a simple two phase process: localization and repair."

- **strength**: The component analysis reports incremental repair gains from candidate sampling and test-based filtering.
  - Page 8 · citation: whitespace
  - Quote: "We can further improve performance to 78 fixes by sampling the LLM multiple times and selecting a patch using majority voting."

- **strength**: The manual classification identifies material benchmark irregularities and motivates a filtered evaluation set, extending the work beyond a single leaderboard score.
  - Page 3 · citation: whitespace
  - Quote: "we built SWE-bench Lite-S, which removes such problematic problems"

- **limitation**: Lite-S comparisons are constrained because commercial systems could not be rerun on the altered subset, so those rows do not constitute a controlled comparison on identical modified tasks.
  - Page 10 · citation: whitespace
  - Quote: "as we are not able to run commercial tools ourselves on the modified problems, we simply exclude the problematic problems in the below evaluation."

Unresolved questions:

- How robust are the results to different repositories, benchmark versions, or software-engineering task distributions beyond SWE-bench Lite?
- How reproducible and stable are the manual problem classifications, and would independent annotators agree on which issues Lite-S excludes?
- Would agent-based systems' relative performance change if they were rerun on the same Lite-S instances under matched models and evaluation conditions?
- Inspection focused on the method overview, selected ablation/results pages, and benchmark analysis; later discussion and any additional implementation details were not examined.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "SWE-bench Lite-S"}` | Locate the paper's evaluation and scope discussion to assess evidence and caveats. | 8 matches on pages [3, 10, 11, 12] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect method details and stated contributions to ground the assessment. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Check benchmark results, comparisons, and evaluation caveats before scoring. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Evidence covers the method, benchmark results, and benchmark filtering; submit a balanced assessment with observed-page quotes. | citation_validation_failed; #2: not_found | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Correct the unverifiable second citation using an exact quote from the inspected page 8 excerpt and resubmit. | citation_validation_failed; #2: not_found | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 8, "end": 8}` | Retrieve an exact passage on repair performance so the observation quote can be verified. | read pages [8] | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.76, "observations": 4}}` | Resubmit with the newly observed exact page 8 wording for the performance evidence. | review accepted | [event 35](trace.jsonl#L35) |
