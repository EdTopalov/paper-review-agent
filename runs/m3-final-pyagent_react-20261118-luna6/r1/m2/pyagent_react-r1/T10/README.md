# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**pyagent_react · ok**

6 model calls · 3 reads · 15.23 s · $0.002551

6 decisions · 5 tool calls · 48552 input tokens (35660 cached) · 1166 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

SWE-agent studies how an LM-facing agent-computer interface affects autonomous software engineering. Its repository search, file-viewing/editing, feedback, linting, and context-management choices are evaluated on SWE-bench, with interface ablations indicating that several design choices materially affect issue resolution. The work offers a concrete system and useful behavioral analysis; the evidence inspected is centered on a particular benchmark, model setup, and interface design.

- **strength**: The paper reports a substantial benchmark result and evaluates transfer to a second language model, alongside a comparison to shell-only interaction.
  - Page 2 · citation: whitespace
  - Quote: "SWE-agent solves 10.7 percentage points more issues than the baseline agent that uses just the default Linux shell."

- **strength**: The Lite-split ablations provide evidence that interface details, including editing and linting, are associated with performance differences.
  - Page 7 · citation: exact
  - Quote: "Without Linting, 15.0% ↓ 3.0"

- **strength**: The paper examines agent trajectories and identifies a potentially important failure pattern: agents may persist in an ineffective approach.
  - Page 8 · citation: whitespace
  - Quote: "agents rarely deviate from this pattern but they rarely recognize dead ends or reset their problem solving approach."

- **uncertainty**: The ACI was developed using a fixed underlying model; the passages inspected do not establish how broadly the findings generalize beyond the evaluated setups.
  - Page 3 · citation: exact
  - Quote: "we keep the language model fixed"

Unresolved questions:

- How well do these ACI gains generalize to other models, codebases, benchmarks, or software-engineering tasks?
- How sensitive are the reported results to the particular development-set selection and ACI configuration process?
- What interventions can reliably help agents detect dead ends and change strategy?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the proposed interface and benchmark evaluation details. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 10, "end": 12}` | Inspect benchmark results and interface ablations. | read pages [10, 11, 12] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 6, "end": 8}` | Review quantitative results, ablations, and stated evaluation boundaries. | read pages [6, 7, 8] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Submit an evidence-based assessment using observed method, benchmark, ablation, and behavior passages. | citation_validation_failed; #4: hyphenation_ambiguous (pages [3]) | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.75, "observations": 4}}` | Resubmit with a short exact quotation from the inspected page to resolve citation validation. | review accepted | [event 30](trace.jsonl#L30) |
