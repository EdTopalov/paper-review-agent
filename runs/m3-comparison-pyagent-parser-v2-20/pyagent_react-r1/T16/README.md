# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**pyagent_react · ok**

4 model calls · 2 reads · 17.81 s · $0.001395

4 decisions · 4 tool calls · 12665 input tokens (6869 cached) · 1205 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.59

The paper presents role-playing prompts for two language-model agents to cooperate on tasks, along with a library and generated conversation datasets intended to support study of multi-agent behavior. It offers a useful framework and exploratory analyses, but its evidence is stronger for generating and characterizing conversations than for establishing task-solving capability.

- **strength**: The paper frames a practical approach to reducing the need for human prompting and presents role-playing as a framework for autonomous agent cooperation.
  - Page 1 · citation: whitespace
  - Quote: "Our approach involves using inception prompting to guide chat agents toward task completion while maintaining consistency with human intentions."

- **strength**: The dataset analysis includes prompt-design ablations and reports changes in conversation termination behavior, providing some empirical examination of design choices.
  - Page 12 · citation: exact
  - Quote: "We provide an ablation study of the AI Society dataset."

- **limitation**: The authors state that task completion is difficult to evaluate at the breadth they target; this is a significant scope boundary for claims about capability, not evidence that task completion fails.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **uncertainty**: The inspected evidence describes dataset topics and termination patterns, but does not establish whether generated conversations reliably solve tasks or how performance compares with alternatives.
  - Page 12 · citation: whitespace
  - Quote: "As seen in Figure 8, we notice that both modiﬁcations considerably increases the number of conversations that terminate with end of task token, and reduce the number of messages with assistant instruction."

Unresolved questions:

- How often do agents actually complete tasks correctly, under evaluation by domain experts, rather than merely terminate with an end-of-task token?
- How robust are the reported behaviors across models, task types, and settings beyond two communicating agents?
- I inspected the supplied first page and pages 12–14; the remaining paper, including its full methods and other experimental evidence, was not inspected.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "limitations"}` | Locate the paper’s stated scope boundaries and limitations. | 4 matches on pages [1, 13, 21] | [event 6](trace.jsonl#L6) |
| 2 | read_pages `{"start": 12, "end": 14}` | Inspect evaluation evidence, conclusions, and stated limitations. | read pages [12, 13, 14] | [event 11](trace.jsonl#L11) |
| 3 | submit_review `{"review": {"score": 0.59, "observations": 4}}` | Submit an evidence-based assessment using the observed introduction, dataset analysis, and limitations. | citation_validation_failed; #4: not_found | [event 17](trace.jsonl#L17) |
| 4 | submit_review `{"review": {"score": 0.59, "observations": 4}}` | Correct the unsupported paraphrase citation with an exact excerpt from page 12. | review accepted | [event 23](trace.jsonl#L23) |
