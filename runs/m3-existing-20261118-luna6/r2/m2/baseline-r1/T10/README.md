# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**baseline · ok**

1 model calls · 0 reads · 7.68 s · $0.000559

1 decisions · 0 tool calls · 23863 input tokens (23860 cached) · 641 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.76

SWE-agent argues that language-model agents perform better on repository-level software engineering when they use an interface designed for their needs, rather than a conventional shell. It introduces tailored search, file-viewing, editing, feedback, and context-management tools, and reports 12.47% resolved on the full SWE-bench test set with GPT-4 Turbo. Ablations on SWE-bench Lite support the claim that several interface choices contribute to performance, though the evidence is bounded by the tested models, benchmark, and experimental setup.

- **strength**: The paper provides direct benchmark evidence for the system’s practical contribution and tests transfer to a second model.
  - Page 5 · citation: whitespace
  - Quote: "SWE-agent with GPT-4 Turbo yields the best performance, solving 12.47% (286/2,294) of the full SWE-bench test set and 18.00% (54/300) of the Lite split."

- **strength**: Interface ablations offer useful evidence that the design is not merely a packaging change: tested alternatives to editing, search, viewer size, and context management generally perform worse on Lite.
  - Page 6 · citation: whitespace
  - Quote: "We consider different approaches to searching and editing (see Figures 4 and 5 respectively) and study how information should be presented to the language model"

- **limitation**: The interface design process includes qualitative selection on a small, hand-picked development set, which limits how confidently the reported ablation results establish broadly general design principles.
  - Page 5 · citation: whitespace
  - Quote: "we arrived at the final ACI design through qualitative analysis of system behavior on small set of hand-picked easier examples from the development split of SWE-bench."

Unresolved questions:

- How much of the reported improvement would persist with other base models, newer model versions, or software-engineering benchmarks beyond SWE-bench?
- Which interface elements provide the most reliable gains across task types and repositories, beyond the Lite-subset ablations?
- The supplied material covers pages 1–25, ending during the appendix; conclusions here are limited to the methods and results visible in those pages.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
