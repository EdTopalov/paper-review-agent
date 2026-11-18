# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**baseline · ok**

1 model calls · 0 reads · 6.10 s · $0.000507

1 decisions · 0 tool calls · 23392 input tokens (23389 cached) · 545 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.58

CAMEL proposes a prompt-driven framework in which paired language-model agents take complementary user and assistant roles to develop a task through iterative instructions and solutions. It also describes dataset-generation pipelines and releases conversational corpora for AI Society and Code scenarios. The paper is most useful as an early framework and empirical account of failure modes in autonomous role-play; it offers limited evidence that these interactions reliably complete useful real-world tasks.

- **strength**: The paper gives a concrete, inspectable framework: roles, task specification, interaction protocol, and explicit termination rules are described, alongside two large generated datasets.
  - Page 12 · citation: not_found
  - Quote: "we generate two large conversational, task-oriented, and instruction-following datasets: AI Society and Code."

- **strength**: It documents several operational failure modes and reports prompt ablations, including trade-offs between task-end termination and unproductive replies.
  - Page 12 · citation: normalized
  - Quote: "both modifications considerably increases the number of conversations that terminate with end of task token, and reduce the number of messages with assistant instruction."

- **limitation**: The paper explicitly says task-completion capability is not evaluated at scale by domain experts, limiting claims about whether generated conversations solve the intended tasks.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **limitation**: The appendix's trading-bot demonstration illustrates a gap between conversational completion and a verified working system: the task-done token appears after a sketch whose code includes unfinished or inconsistent behavior. This is an example, not a systematic evaluation.
  - Page 29 · citation: whitespace
  - Quote: "The function sleeps for 60 seconds before repeating the process."

Unresolved questions:

- How often do generated dialogues produce correct, executable, and complete solutions when independently assessed by domain experts?
- How robust are the reported prompt and termination effects across different models, model versions, sampling settings, and task distributions?
- What dataset quality controls or filtering procedures, if any, were applied to remove inaccurate, unsafe, or repetitive instruction-solution pairs?
- Inspection was limited to the supplied paper text and figures; the full supplementary materials, released code, and underlying datasets were not examined.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
