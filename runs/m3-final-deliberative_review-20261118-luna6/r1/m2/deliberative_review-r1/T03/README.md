# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**deliberative_review · ok**

7 model calls · 3 reads · 36.11 s · $0.006452

7 decisions · 4 tool calls · 39367 input tokens (0 cached) · 3081 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.68

AutoGen presents a configurable framework for building LLM applications through conversations among agents backed by models, tools, and people. Its examples illustrate varied workflows and human/tool integration, while small math evaluations provide some comparative evidence. The contribution is useful as a framework and implementation report, but evidence for broad effectiveness is limited by narrow evaluations and many illustrative application examples.

- **strength**: The framework’s central design claim is that agents can combine different backends and involve people, with conversations organizing complex workflows.
  - Page 1 · citation: whitespace
  - Quote: "They can operate in various modes that employ combinations of LLMs, human inputs, and tools."

- **limitation**: The paper reports a concrete comparison on 12 level-5 math problems, but only one trial per problem; this is useful preliminary evidence, not a robust basis for general performance claims.
  - Page 11 · citation: exact
  - Quote: "With one trial, AutoGen scores 8/12 problems"

- **strength**: The multi-user problem-solving example illustrates how the framework can integrate a human expert into a workflow, though this example alone does not establish effectiveness at scale.
  - Page 12 · citation: whitespace
  - Quote: "The only development required is several lines of code for the ask for expert function"

- **limitation**: The authors flag potential risks when agents can act on external environments. The inspected excerpt raises the concern but does not establish the prevalence or severity of harms.
  - Page 24 · citation: exact
  - Quote: "could be risky."

Unresolved questions:

- How well do the framework’s benefits and failure modes generalize across other application domains and conversation patterns? I inspected selected pages only; several application sections are unobserved or represented by partial excerpts.
- How robust are the comparative results across more problems, trials, and model configurations? The available larger math comparison uses one trial on 12 problems.
- What safeguards and oversight are effective when agents execute generated code or change external environments? The available page 24 excerpt is partial.

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the paper’s later application examples and any evaluation results to determine whether AutoGen’s claimed usefulness is supported by concrete evidence, rather than examples alone.; Check the framework description and discussion for what is demonstrated about agent customization, conversation patterns, and human/tool integration, and for stated scope limits or failure cases.; Only page 1 is currently available; inspect the remaining pages before judging the evidence or treating any support as absent. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 7 matches on pages [3, 4, 7, 15, 20, 24] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | read pages [8, 9, 10] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [11, 12, 13] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: revise; Issues: The second and third observations substantially duplicate the same 12-problem result and quote. Consolidate them into one observation that acknowledges both the concrete evidence and its limited scope, then use the freed observation slot for another distinct, supported finding if useful.; Target: Revise the observations to avoid repeating the one-trial math result; retain the qualification that the remaining application pages and parts of the risk discussion were not inspected. | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | revise | Draft revised; Changes: Consolidated the duplicated math observations into one qualified finding and used the remaining observation for the distinct human-expert workflow example. The quotations and page numbers match observed excerpts. | [event 34](trace.jsonl#L34) · [event 37](trace.jsonl#L37) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "limitations"}` | Locate discussion of scope and limitations, then inspect application/evaluation evidence and counterevidence across the paper. | 7 matches on pages [3, 4, 7, 15, 20, 24] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect framework contribution, application evidence, and counterevidence to examples-only assessment. | read pages [8, 9, 10] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 11, "end": 13}` | Inspect application evaluation evidence and framework implementation details beyond the currently supplied excerpts. | read pages [11, 12, 13] | [event 22](trace.jsonl#L22) |
| 7 | submit_review `{"review": {"score": 0.68, "observations": 4}}` | Submit after the enforced critique and source validation. | review accepted | [event 39](trace.jsonl#L39) |
