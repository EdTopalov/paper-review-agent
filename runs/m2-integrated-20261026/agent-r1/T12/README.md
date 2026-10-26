# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**agent · ok**

5 model calls · 4 reads · 10.71 s · $0.001680

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

InterCode contributes a practical framework and benchmark formulation for interactive code generation, pairing code actions with execution feedback in containerized environments. Its Bash and SQL implementations and model evaluations demonstrate that the testbed is usable and expose meaningful benefits and failure patterns of interaction, though empirical breadth and task coverage remain limited.

- **strength**: The paper defines a modular interactive coding framework with execution-based feedback and customizable task-specific rewards, supporting extension beyond the supplied environments.
  - Page 4 · citation: whitespace
  - Quote: "InterCode exposes a reward function endpoint that has access to both the interaction history and the execution container, allowing for custom reward function definitions that can incorporate multiple signals."

- **strength**: Reported evaluations show substantial gains from iterative feedback for multiple models, especially on SQL, supporting benchmark viability and the value of interaction.
  - Page 7 · citation: exact
  - Quote: "gpt-4 19.8 7.2 4.6 3.0 9.1 87.5 76.7 66.7 52.4 73.7"

- **limitation**: The implemented benchmark has narrow language and dataset coverage, and the CTF demonstration is too small for broad evaluation.
  - Page 9 · citation: whitespace
  - Quote: "At this time, the number of InterCode based environments is limited to SQL and Bash action spaces and datasets"

- **uncertainty**: The paper says execution is sandboxed, but its own discussion warns the Bash and SQL environments lack strict action-space restrictions; safety of direct transfer is not established.
  - Page 26 · citation: exact
  - Quote: "do not explicitly impose any strict limitations on the action space."

Unresolved questions:

- How well do results generalize to additional programming languages, datasets, and independently authored tasks?
- How robust are benchmark scores to alternative reward designs, particularly where exact outputs or ordering differ despite equivalent solutions?
- What operational safeguards are needed before deploying agents trained or evaluated in these environments on real systems?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — The paper describes a modular construction pipeline and a reward-function endpoint that can use interaction history and container state, enabling custom reward designs (PDF p. 4). The interface and appendix also discuss customization and extension (PDF pp. 14–15).
- Observation 2: **supported** — The reported SQL results show Try Again outperforming Single Turn for every listed model, including GPT-4 rising from 9.1% to 73.7% overall; the paper also reports gains in Bash (PDF pp. 6–7). This supports the qualified claim about interaction and benchmark viability.
- Observation 3: **supported** — The paper explicitly states that its implemented environments are limited to Bash and SQL and that the CTF dataset has only four instances, limiting broad evaluation (PDF p. 9; see also PDF p. 26).
- Observation 4: **supported** — The paper describes Docker containers as execution sandboxes, but warns that Bash and SQL impose no strict action-space limitations and that direct sim-to-real transfer may put real systems at risk (PDF pp. 3–4, 26). The claim accurately distinguishes sandboxed evaluation from unestablished deployment safety.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper's explicit scope limitations to assess benchmark coverage. | 7 matches on pages [9, 13, 14, 26] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 3, "end": 5}` | Inspect benchmark design and experimental results supporting the paper's claims. | read pages [3, 4, 5] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 6, "end": 7}` | Review model evaluation setup and reported benchmark outcomes. | read pages [6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 9, "end": 9}` | Inspect the authors' own stated limitations before judging scope and safety. | read pages [9] | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.73, "observations": 4}}` | Evidence covers framework design, evaluation results, and explicit limitations; submit a scoped assessment. | review accepted | [event 25](trace.jsonl#L25) |
