# T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**agent · ok**

8 model calls · 4 reads · 27.54 s · $0.002865

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.78

τ-bench contributes a modular benchmark for tool agents in simulated multi-turn user interactions under domain policies, using database-state goals and pass^k to measure repeatability. Experiments across multiple models reveal substantial weaknesses in the tested setting. The evidence is useful, but simplified customer-service domains and simulated users limit real-world generalization.

- **strength**: The benchmark provides objective end-state assessment alongside user interaction and tool use.
  - Page 2 · citation: whitespace
  - Quote: "Our evaluation scheme compares the database state at the end of each episode with the ground truth expected state."

- **strength**: Repeated-trial evaluation reveals that reliability falls substantially even for the best-performing tested model.
  - Page 7 · citation: whitespace
  - Quote: "pass^8 drops to < 25%."

- **strength**: The ablation directly removes policy context to test its contribution.
  - Page 8 · citation: whitespace
  - Quote: "we perform an ablation study by remov- ing the domain policy from the FC agent system prompt."

- **limitation**: The benchmark intentionally simplifies its domains relative to real-world settings, limiting external validity.
  - Page 6 · citation: whitespace
  - Quote: "Each τ-bench domain’s data schemas, APIs, and rules are simplified compared to real-world domains"

Unresolved questions:

- How well do simulated users and database-state success correspond to real-user satisfaction and expert judgments?
- Do results generalize to domains beyond retail and airline, and to newer models and agent designs?
- I inspected pages 1–8 only; later discussion, appendices, and detailed task-level evidence remain unreviewed.

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The benchmark evaluates tool-mediated conversations with a simulated user and compares the final database state with a ground-truth outcome; the reward also checks required information in user-facing responses (pp. 2, 4).
- Observation 2: **supported** — The paper reports that for the best-performing tested model, gpt-4o, pass^8 in retail drops below 25% (p. 7).
- Observation 3: **supported** — The authors explicitly remove the domain policy from the function-calling agent’s system prompt and report the resulting pass^1 changes (p. 8).
- Observation 4: **supported** — The paper states that the domains’ schemas, APIs, and rules are simplified relative to real-world domains, and presents this as a benchmark characteristic relevant to generalization (p. 6).

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "pass^k"}` | Inspect the benchmark’s reliability metric and experimental evidence. | 8 matches on pages [1, 2, 4, 5, 6] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Read the benchmark’s design and stated scope beyond the abstract. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 6}` | Check benchmark size, construction choices, and evaluation caveats. | read pages [5, 6] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 7, "end": 8}` | Inspect reported results and whether evaluation reliability is characterized. | read pages [7, 8] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Submit an evidence-grounded assessment based on the abstract and inspected benchmark, methods, and results pages. | citation_validation_failed; #3: hyphenation_ambiguous (pages [8]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Correct the failed quote using an exact verbatim passage from inspected page 8 and resubmit. | citation_validation_failed; #3: hyphenation_ambiguous (pages [8]) | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Use an unambiguous exact citation from the inspected page 8 and finalize the assessment. | citation_validation_failed; #3: hyphenation_ambiguous (pages [8]) | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.78, "observations": 4}}` | Finalize with observations supported by exact unambiguous quotes from inspected pages. | review accepted | [event 40](trace.jsonl#L40) |
