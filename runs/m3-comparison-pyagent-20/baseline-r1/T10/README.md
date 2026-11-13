# T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**baseline · ok**

1 model calls · 0 reads · 7.07 s · $0.003360

1 decisions · 0 tool calls · 23863 input tokens (0 cached) · 755 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.73

SWE-agent argues that language-model agents benefit from an agent-computer interface designed around their interaction needs, and tests this through repository-level software issue resolution. Its tailored search, file viewing, editing, feedback, and context-management tools achieve 12.47% resolution on the full SWE-bench test set with GPT-4 Turbo; ablations on SWE-bench Lite indicate that several interface choices contribute to performance. The paper offers a useful empirical case for interface design as a research variable, while results remain limited by modest resolution rates and the scale and scope of the ablations.

- **strength**: The full-test-set result provides evidence of practical value beyond the interface ablations, and the paper reports transfer to a second model. The comparison is not fully controlled against the cited RAG result, which uses a different setup.
  - Page 5 · citation: exact
  - Quote: "solving 12.47% (286/2,294) of the full SWE-bench test set"

- **strength**: The Lite-set ablations provide concrete evidence that interface design matters: summarized search, the 100-line viewer, and linting outperform the alternatives reported in the table.
  - Page 6 · citation: wrong_page
  - Quote: "SWE-agent solves 10.7 percentage points more issues than the baseline agent that uses just the default Linux shell."

- **limitation**: The authors say initial interface design relied partly on qualitative inspection of a small, selected set of development examples. This may limit how broadly the design process or resulting choices generalize; the paper also describes a later hyperparameter sweep.
  - Page 5 · citation: not_found
  - Quote: "a small set of hand-picked easier examples from the development split of SWE-bench."

- **uncertainty**: The reported behavior analysis identifies slow failure recovery, but it does not establish which changes would reliably improve recovery or whether larger budgets would help across other tasks. The supplied material does not resolve these questions.
  - Page 8 · citation: whitespace
  - Quote: "they rarely recognize dead ends or reset their problem solving approach."

Unresolved questions:

- How robust are the ACI gains across additional language models, software engineering benchmarks, and tasks beyond the Python repositories represented here?
- Would independent replications or broader development-set studies select similar interface components and hyperparameters?
- Which interventions can help agents detect and change unproductive strategies, and how would those interventions affect resolution and inference cost?
- Assessment is based on the supplied pages 1–25; the appendix begins but is not complete in the supplied material, limiting inspection of implementation details and any subsequent discussion.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
