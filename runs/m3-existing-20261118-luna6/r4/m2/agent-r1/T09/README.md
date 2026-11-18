# T09: Agentless: Demystifying LLM-based Software Engineering Agents

**agent · ok**

7 model calls · 5 reads · 15.96 s · $0.004090

7 decisions · 7 tool calls · 54379 input tokens (28766 cached) · 1245 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.74

AGENTLESS shows that a compact, staged localization-and-repair pipeline can be competitive with more elaborate software-engineering agents on SWE-bench Lite at low reported inference cost. Its contribution is a clear baseline and a critique of benchmark quality, more than a novel standalone algorithm. Evidence is useful but limited to one model and benchmark family, with some comparisons based on reported results for tools the authors could not independently run.

- **strength**: The authors explicitly frame their contribution as combining known techniques into an accessible agentless pipeline.
  - Page 5 · citation: exact
  - Quote: "none of the techniques used by AGENTLESS in isolation are revolutionary, but in-"

- **strength**: The reported result is 82/300 resolved at $0.34 average cost. Comparisons require caution because baseline results are drawn from official leaderboards or papers, and the paper notes some commercial tools were not independently reproducible.
  - Page 7 · citation: exact
  - Quote: "AGENTLESS\n GPT-4o 82 (27.33%) $0.34 42,376"

- **strength**: The authors classify benchmark issues and construct a filtered 252-problem subset, excluding cases they deem unreasonable; independent validation of the classification is not established in the passages inspected.
  - Page 10 · citation: exact
  - Quote: "We refer to our subset of 252 problems as SWE-bench Lite-S."

- **limitation**: The paper reports a comparative weakness on issues with no location clues, providing a specific boundary for the simple approach.
  - Page 11 · citation: whitespace
  - Quote: "the closed-source agent tools perform better compared to AGENTLESS in the case where no location clue is provided."

Unresolved questions:

- How robust are the findings across other LLMs, model versions, and repository-level benchmarks? The inspected implementation uses GPT-4o and evaluation focuses on SWE-bench Lite.
- How comparable are reported baseline results when the authors could not independently run some closed-source tools?
- How reliable is the manual benchmark categorization across annotators? I inspected the classification and filtered-set discussion, not evidence of inter-rater validation or a complete annotation protocol.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Find the paper’s stated scope and limitations to assess caveats. | 3 matches on pages [2, 3, 12] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 4, "end": 6}` | Inspect method details and evaluation setup to substantiate contribution and evidence. | read pages [4, 5, 6] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 7, "end": 9}` | Review comparative results and benchmark curation evidence. | read pages [7, 8, 9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 10, "end": 11}` | Inspect benchmark filtering and manual classification methodology and limitations. | read pages [10, 11] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Evidence covers method, benchmark comparisons, and the filtered-set rationale; submit a qualified assessment. | citation_validation_failed; #1: hyphenation_ambiguous (pages [5]); #2: not_found | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 5, "end": 7}` | Retrieve exact citable text for the method contribution and benchmark result after citation validation flagged mismatches. | read pages [5, 6, 7] | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.74, "observations": 4}}` | Resubmit the assessment using exact quotes from the pages just inspected. | review accepted | [event 36](trace.jsonl#L36) |
