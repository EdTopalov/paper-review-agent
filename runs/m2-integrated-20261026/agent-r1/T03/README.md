# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**agent · ok**

6 model calls · 5 reads · 16.24 s · $0.002759

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

AutoGen presents a flexible infrastructure for building LLM applications as conversations among customizable agents that can combine models, tools, and human participation. Its contribution is a practical, general-purpose framework demonstrated across diverse workflows; evidence is promising but largely illustrative and task-specific rather than a broad validation of general performance.

- **strength**: The framework’s central value is composable, varied agent interaction, with concrete application examples spanning multiple task families.
  - Page 9 · citation: exact
  - Quote: "We present six examples of diverse applications built using AutoGen."

- **strength**: Some empirical support goes beyond demonstrations: the MiniWob++ comparison reports performance across twelve task types and ten instances per task.
  - Page 16 · citation: exact
  - Quote: "For each clicking task, we reported the success rate for ten different instances."

- **limitation**: The math comparison is very small and qualitative, so its results provide only weak grounds for broad claims of competitiveness.
  - Page 10 · citation: whitespace
  - Quote: "We use two level-5 problems from the MATH dataset for the qualitative evaluation and test on each problem for 3 times."

- **uncertainty**: The report itself identifies optimal workflow design as unresolved, including when multi-agent workflows help and how to choose cost-effective configurations.
  - Page 23 · citation: exact
  - Quote: "For a given task, what is the optimal (e.g., cost-effective) multi-agent workflow?"

Unresolved questions:

- How reliably do the framework’s benefits generalize across tasks, model backends, and larger independent evaluations?
- What workflow choices provide consistent gains relative to simpler pipelines, and at what cost?
- I inspected framework descriptions, selected math and MiniWob++ evidence, and future-work discussion; I did not inspect the full report or all application evaluations, so evidence beyond these passages may affect the assessment.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper presents six diverse application examples and describes varied agent roles and conversation patterns (PDF pp. 2, 8–9).
- Observation 2: **supported** — The MiniWob++ comparison covers twelve clicking tasks, and reports success rates over ten instances for each task (PDF pp. 15–16).
- Observation 3: **overstated** — The initial comparison is indeed qualitative and limited to two MATH problems tested three times each (PDF pp. 10–11). But the paper also reports a follow-up quantitative evaluation on 12 level-5 problems, with one trial per problem, so describing the math comparison overall as very small and qualitative omits relevant evidence (PDF p. 11).
- Observation 4: **supported** — The paper explicitly lists unresolved questions about which tasks benefit from multi-agent workflows and what workflow is optimal and cost-effective (PDF p. 23).

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "evaluation"}` | Locate the paper’s evidence and evaluation discussion to assess support for its claimed framework benefits. | 8 matches on pages [9, 10, 11, 12] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 8, "end": 10}` | Inspect framework design and the math evaluation setup and reported results. | read pages [8, 9, 10] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 15, "end": 17}` | Check whether later sections report broader quantitative evidence or explicit limitations for the showcased applications. | read pages [15, 16, 17] | [event 15](trace.jsonl#L15) |
| 4 | search_paper `{"query": "limitations"}` | Check for explicit scope boundaries or limitations before finalizing the review. | 7 matches on pages [3, 4, 7, 15, 20, 24] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 23, "end": 24}` | Read the paper’s discussion of risks and scope to cite a relevant caveat accurately. | read pages [23, 24] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Evidence inspected supports a framework contribution but only narrow selected evaluations; submit an absolute assessment with that limitation stated. | review accepted | [event 31](trace.jsonl#L31) |
