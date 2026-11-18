# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**pyagent_react · ok**

8 model calls · 4 reads · 31.88 s · $0.003346

8 decisions · 8 tool calls · 69101 input tokens (56550 cached) · 2424 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

CAMEL presents a practical role-playing and inception-prompting framework for generating task-oriented conversations between LLM agents, releases associated datasets and tools, and analyzes cooperation failures and prompt variations. Its main value is a reusable research setup and descriptive study, rather than strong evidence that agents reliably complete real-world tasks. I inspected the introduction, method, and selected experiment and conclusion pages; I did not inspect the full paper, supplementary materials, or the complete figures and dataset contents.

- **strength**: The framework specifies an idea-to-task step followed by autonomous cooperation between assigned agent roles, making the proposed setup concrete.
  - Page 4 · citation: whitespace
  - Quote: "After the multi-agent system receives a preliminary idea and the role assignment from human users, a task-speciﬁer agent will provide a detailed description"

- **strength**: The authors compare prompt variations and discuss their effects on conversation termination outcomes.
  - Page 12 · citation: whitespace
  - Quote: "We design Prompt V2 which modiﬁes the original AI society prompt by removing the assistant response format"

- **limitation**: The authors identify a central evaluation gap: generated conversation volume does not establish that tasks were successfully completed, and robust evaluation would require domain expertise.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **uncertainty**: The datasets are large, but the inspected evidence does not establish the correctness or usefulness of generated task solutions.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations."

Unresolved questions:

- How often do conversations produce correct, usable task outcomes when assessed independently by domain experts?
- Do the observed cooperation patterns and prompt-ablation effects hold across other model families, model versions, and settings with more than two agents?
- What are the dataset quality, duplicate-rate, and coverage characteristics beyond the summaries and figures inspected here?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | ` line with JSON, and no prose outside that. We need continue the reading loop with `read_pages` and a short observable purpose in `reason`. Since the first page is supplied and the total budget is five tool calls, a sensible next move is to inspect pages 2-4 for motivation and framework details. But the ideal reading sequence should prioritize methods and experiments over repeating the intro; still, pages 2-4 may include related work and contributions. Let's request pages 2-4. invalid arguments: `` |  | unknown_tool | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 2, "end": 4}` | Inspect the framework motivation and proposed method. | read pages [2, 3, 4] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 5, "end": 7}` | Inspect prompt design and evaluation procedure. | read pages [5, 6, 7] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 8, "end": 10}` | Inspect reported experiments, dataset scale, and findings. | read pages [8, 9, 10] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 11, "end": 13}` | Inspect experiment outcomes and stated scope limitations. | read pages [11, 12, 13] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.62, "observations": 4}}` | Submit a supported assessment using the inspected method and experiment pages. | citation_validation_failed; #4: not_found | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.62, "observations": 4}}` | Resubmit with verbatim excerpts copied from inspected pages. | citation_validation_failed; #2: not_found | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.62, "observations": 4}}` | Correct the prompt-ablation citation with exact text from page 12. | review accepted | [event 40](trace.jsonl#L40) |
