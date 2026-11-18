# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**agent · ok**

8 model calls · 5 reads · 18.79 s · $0.003958

8 decisions · 8 tool calls · 58666 input tokens (35697 cached) · 1511 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

τ-bench introduces an interactive tool-agent-user benchmark for customer-service tasks, combining simulated users, domain policies, APIs, and annotated database outcomes. Its pass^k metric evaluates repeatable reliability, and experiments reveal substantial success and consistency gaps in tested agents. It is a useful evaluation contribution, bounded by two domains and simulator and annotation caveats.

- **strength**: The benchmark compares episodes to annotated goal states and measures reliability over repeated interactions.
  - Page 2 · citation: whitespace
  - Quote: "Our evaluation scheme compares the database state at the end of each episode with the ground truth expected state."

- **strength**: Experiments show that even the tested strong model has low consistency on repeated retail trials.
  - Page 2 · citation: whitespace
  - Quote: "With increasing k, the chance of consistently solving a task drops rapidly, to as low as ∼25% for pass^8 on τ-retail for the same model."

- **limitation**: The authors acknowledge potential limits of the simulated user model that could affect benchmark behavior.
  - Page 9 · citation: normalized
  - Quote: "the user simulation LM might have limited capacity at reasoning, calculation, long-context memorization, or alignment with the instruction prompt"

- **limitation**: The initial scope is two customer-service domains, so broader application generality remains open.
  - Page 2 · citation: whitespace
  - Quote: "focus on the realm of customer service and create two different domains where agents need to assist simulated users with diverse requests"

Unresolved questions:

- How robust are agent rankings and pass^k scores to changing the user simulator LM or prompt?
- Do findings generalize beyond the two customer-service domains?
- I inspected the initial description, selected method and results passages, and discussion of limitations; I did not inspect the complete experimental tables, appendices, or all task-construction details.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "pass^k"}` | Locate the benchmark metric definition and reported reliability results. | 8 matches on pages [1, 2, 4, 5, 6] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect benchmark design, evaluation rationale, and any stated scope limitations. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Check whether the authors explicitly discuss benchmark limitations or scope boundaries. | 3 matches on pages [9, 12, 35] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 9}` | Inspect reported empirical findings and the authors’ stated limitations. | read pages [8, 9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Evidence covers the core benchmark design, metric, empirical findings, and author-stated limitations; submit a calibrated assessment. | citation_validation_failed; #1: wrong_page (pages [2]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Correct quote-page mismatch using the observed page 2 text; resubmit verified evidence. | citation_validation_failed; #1: wrong_page (pages [2]) | [event 30](trace.jsonl#L30) |
| 7 | read_pages `{"start": 2, "end": 2}` | Verify exact page 2 quotes after citation validation reported a page mismatch. | read pages [2] | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit final assessment with page 2 exact evidence now verified, alongside the method and limitation citations. | review accepted | [event 41](trace.jsonl#L41) |
