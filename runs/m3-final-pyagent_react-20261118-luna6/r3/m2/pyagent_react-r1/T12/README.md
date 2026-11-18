# T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback

**pyagent_react · ok**

6 model calls · 3 reads · 30.92 s · $0.002581

6 decisions · 6 tool calls · 36225 input tokens (28697 cached) · 2707 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

InterCode formalizes interactive coding as an agent loop in which code actions alter an execution environment and generate observations. The paper contributes a modular Docker-based framework and Bash/SQL environments, then uses them to compare models and prompting strategies. The reported results show meaningful gains from interaction in several settings, while also surfacing persistent failure modes. This is a substantial benchmark contribution, though the inspected evidence does not establish broad task representativeness or settle evaluation validity beyond the described setup.

- **strength**: The framework gives interactive coding a clear task formalization, with explicit actions, observations, rewards, and success metrics.
  - Page 4 · citation: whitespace
  - Quote: "The InterCode benchmark formalizes interactive coding with execution feedback as a partially observable Markov decision process (POMDP)"

- **strength**: The paper reports sizable interactive-setting improvements, including a large SQL gain for GPT-4.
  - Page 6 · citation: exact
  - Quote: "(9.1% → 73.7%)"

- **limitation**: The Bash dataset is substantially filtered and edited to ground tasks and support utilities, so results apply to this curated task set rather than unmodified NL2Bash.
  - Page 5 · citation: exact
  - Quote: "The resulting 200 commands are grouped into 4 disjoint sets"

- **uncertainty**: The authors report plateauing and repeated actions in later turns, demonstrating a failure mode of evaluated agents rather than a defect in the benchmark itself.
  - Page 7 · citation: whitespace
  - Quote: "task episode trajectories often reveal repetition of earlier actions"

Unresolved questions:

- How sensitive are the results to the reward definitions, particularly lexical similarity for Bash output and ordering-sensitive SQL scoring?
- How well do the curated tasks and observed gains generalize to other languages, execution environments, and interactive coding domains?
- I inspected the supplied first page and pages 4–8; the remaining paper, including appendices and additional methodological details, was not inspected, so further limitations and validation evidence may remain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experimental results"}` | Locate benchmark outcome discussion and evidence. | 0 matches | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 4, "end": 6}` | Inspect benchmark setup and reported evaluation details. | read pages [4, 5, 6] | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 7, "end": 8}` | Inspect reported model outcomes and evaluation caveats. | read pages [7, 8] | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Assess the framework and reported benchmark evidence from the inspected pages; state remaining inspection gaps. | citation_validation_failed; #2: wrong_page (pages [6]) | [event 21](trace.jsonl#L21) |
| 5 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the previously mismatched citation to quote text observed on page 7. | citation_validation_failed; #2: wrong_page (pages [6]) | [event 26](trace.jsonl#L26) |
| 6 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the performance citation to its observed page 6 location. | review accepted | [event 31](trace.jsonl#L31) |
