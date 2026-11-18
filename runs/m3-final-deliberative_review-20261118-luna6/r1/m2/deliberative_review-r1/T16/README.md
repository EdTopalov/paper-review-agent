# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**deliberative_review · ok**

8 model calls · 4 reads · 29.42 s · $0.007096

8 decisions · 5 tool calls · 46472 input tokens (0 cached) · 2599 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.56

CAMEL proposes a two-agent role-playing framework: an AI user plans and issues instructions while an AI assistant responds, with the aim of developing tasks from initial ideas. It also presents the approach as a way to generate dialogue datasets for studying language-model behavior. The inspected pages make the interaction and prompting design concrete, but do not provide enough of the experimental results or dataset evaluation to judge how well the system completes tasks or how useful the datasets are.

- **strength**: The framework specifies distinct agent roles and an interaction loop, and its prompts define role, response, and termination behavior; this makes the proposed mechanism concrete, though not proof of successful task completion.
  - Page 6 · citation: whitespace
  - Quote: "Once the conversation phase commences, the AI assistant and AI user prompt each other automatically in a loop until termination."

- **limitation**: The paper acknowledges that rigorous task-completion evaluation is difficult and requires domain experts. This is an evaluation constraint, not evidence that the framework fails.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **uncertainty**: The paper describes a process for generating AI Society tasks, but the inspected pages do not establish dataset quality or usefulness. I did not inspect the reported results, dataset details, or comparisons, so these remain unassessed.
  - Page 8 · citation: whitespace
  - Quote: "we then use the task speciﬁer prompt passed to the LLM agent to make the task more speciﬁc."

Unresolved questions:

- What task-success results, baselines, or evaluation measures are reported in the uninspected portions of the paper?
- How are the AI Society and Code datasets filtered and validated, and what evidence supports their usefulness for research or training?
- How robust are the role-playing interactions across models and tasks beyond the examples and framework description inspected here?

## Deliberative phases

Plans and critic feedback are model judgments. Source evidence and full outputs remain in the linked trace events.

| Step | Role | Decision or outcome | Events |
|---|---|---|---|
| 1 | plan | Checks: Inspect the framework and prompting sections to identify exactly how the two agents are initialized and guided, and whether the proposed role-playing setup supports the claimed autonomous cooperation.; Inspect the evaluation, generated-dialogue examples, and any reported results or comparisons to determine what evidence supports task completion, scalability, and the claimed research value of generated data.; Inspect the discussion and limitations, and check the remaining paper for additional evidence or qualifications; only page 1 is currently observed, so support elsewhere is unknown. | [event 3](trace.jsonl#L3) · [event 6](trace.jsonl#L6) |
| 2 | investigate | 8 matches on pages [1, 2] | [event 7](trace.jsonl#L7) · [event 12](trace.jsonl#L12) |
| 3 | investigate | 4 matches on pages [1, 13, 21] | [event 13](trace.jsonl#L13) · [event 18](trace.jsonl#L18) |
| 4 | investigate | read pages [3, 4, 5] | [event 19](trace.jsonl#L19) · [event 24](trace.jsonl#L24) |
| 5 | draft | Draft prepared | [event 25](trace.jsonl#L25) · [event 28](trace.jsonl#L28) |
| 6 | critic | Recommendation: investigate; Issues: The draft appropriately acknowledges that key experimental evidence was not inspected, but that evidence is central to judging the paper’s contribution and supporting the 0.56 score. A targeted read of the evaluation and dataset-results sections could materially change the assessment.; Target: What evaluation results, baselines, and dataset-quality or usefulness evidence does the paper report for task completion, scalability, and the AI Society and Code datasets? | [event 30](trace.jsonl#L30) · [event 33](trace.jsonl#L33) |
| 7 | targeted_read | read pages [6, 7, 8] | [event 34](trace.jsonl#L34) · [event 39](trace.jsonl#L39) |
| 8 | revise | Draft revised; Changes: Updated C1 to incorporate the inspected prompting details and C2 to reflect that dataset-generation procedures are described, while retaining uncertainty about evaluation and dataset usefulness. The critic’s request for results cannot be resolved from the newly supplied pages, which cover prompting and the start of dataset construction, not reported evaluation outcomes. The score remains unchanged; the paper’s central empirical support remains substantially unassessed. | [event 40](trace.jsonl#L40) · [event 43](trace.jsonl#L43) |


## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 2 | search_paper `{"query": "role-playing"}` | Locate framework and evaluation passages to inspect evidence for the paper's central claims. | 8 matches on pages [1, 2] | [event 10](trace.jsonl#L10) |
| 3 | search_paper `{"query": "limitations"}` | Inspect discussion/limitations and seek counterevidence on scope and reported evidence before assessing. | 4 matches on pages [1, 13, 21] | [event 16](trace.jsonl#L16) |
| 4 | read_pages `{"start": 3, "end": 5}` | Inspect framework and prompting details for evidence on agent setup and autonomous cooperation. | read pages [3, 4, 5] | [event 22](trace.jsonl#L22) |
| 7 | read_pages `{"start": 6, "end": 8}` | Inspect experiment results and dataset evidence for task completion and scale. | read pages [6, 7, 8] | [event 37](trace.jsonl#L37) |
| 8 | submit_review `{"review": {"score": 0.56, "observations": 3}}` | Submit after the enforced critique and source validation. | review accepted | [event 45](trace.jsonl#L45) |
