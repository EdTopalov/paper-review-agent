# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**baseline · ok**

1 model calls · 0 reads · 6.95 s · $0.003270

1 decisions · 0 tool calls · 23863 input tokens (0 cached) · 575 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.75

SWE-agent presents an LM-oriented agent-computer interface for repository-level software engineering, combining targeted search, file viewing and editing, feedback, and context management. On SWE-bench, the authors report 12.47% resolved with GPT-4 Turbo and show on the 300-instance Lite subset that several interface choices outperform a shell-only configuration. The work offers a concrete system and useful evidence that interaction design can affect agent performance, while its results are bounded by the evaluated models, benchmark, and experimental setup.

- **strength**: The paper evaluates the system on the full benchmark and reports a substantial gap over the listed retrieval-augmented baselines.
  - Page 5 · citation: exact
  - Quote: "solving 12.47% (286/2,294) of the full SWE-bench test set"

- **strength**: The Lite-set ablations provide evidence that interface components, including editing and linting, can affect task resolution; the results are specific to this subset and setup.
  - Page 7 · citation: exact
  - Quote: "Without Linting, 15.0% ↓ 3.0"

- **limitation**: The authors report selecting the interface through qualitative analysis of a small hand-picked development set, so the extent to which this design process generalizes remains uncertain.
  - Page 5 · citation: not_found
  - Quote: "a small set of hand-picked easier examples from the development split of SWE-bench"

Unresolved questions:

- How robust are the reported interface gains across a broader range of language models, repositories, and software-engineering benchmarks?
- How much do the reported improvements depend on individual interface components versus their interaction with prompts, demonstrations, and context management?
- This assessment is based on the supplied 25-page preprint; I have not independently reproduced the experiments or inspected implementation details beyond what is reported in the paper.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
