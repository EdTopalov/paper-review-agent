# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**pyagent_react · ok**

6 model calls · 4 reads · 14.26 s · $0.001459

6 decisions · 5 tool calls · 28869 input tokens (21998 cached) · 762 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.65

CAMEL proposes role-playing prompts for two language-model agents to cooperate with reduced human guidance, and releases conversational datasets and tools intended to support study of multi-agent behavior. Its contribution is a practical framework and large-scale data-generation effort, with useful analysis of interaction failures and prompt variants. Evidence centers on GPT-3.5-turbo conversations and termination patterns; it does not establish broad task-completion capability.

- **strength**: The paper reports generating sizeable, explicitly described datasets from role, task, language, and domain combinations, making the framework concrete and potentially useful for studying agent interaction.
  - Page 9 · citation: whitespace
  - Quote: "yielding a total of 25,000 conversations"

- **strength**: The authors compare prompt variants and report a tradeoff: modifications improve end-of-task termination and reduce role reversals, but increase flake messages.
  - Page 12 · citation: normalized
  - Quote: "we observe a significant increase in the number of flake messages for Prompt V2 and Prompt V1 + Task Planner compared to original Prompt V1 as seen in Figure 9."

- **limitation**: The authors identify a central evidence gap: evaluating whether the generated conversations actually complete diverse tasks requires expert assessment, which they do not provide here.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **uncertainty**: Termination categories and prompt ablations provide evidence about interaction behavior, but the inspected evidence does not determine the correctness or usefulness of completed solutions.
  - Page 12 · citation: exact
  - Quote: "We provide an ablation study of the AI Society dataset."

Unresolved questions:

- How often do conversations produce correct, useful task outcomes, as judged by domain experts?
- Do the interaction patterns and prompt effects generalize beyond the two-agent GPT-3.5-turbo setting?
- How robust are the reported dataset characteristics to alternative models, prompts, or sampling procedures?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "experiments"}` | Locate the paper’s empirical evaluation and reported outcomes. | 7 matches on pages [4, 5, 7, 13, 19] | [event 6](trace.jsonl#L6) |
| 2 | no_tool_call invalid arguments: `` |  | no_tool_call | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 7, "end": 9}` | Inspect experiment design and evidence for agent cooperation. | read pages [7, 8, 9] | [event 15](trace.jsonl#L15) |
| 4 | read_pages `{"start": 12, "end": 14}` | Inspect stated scope boundaries and discussion of limitations. | read pages [12, 13, 14] | [event 20](trace.jsonl#L20) |
| 5 | read_pages `{"start": 10, "end": 11}` | Inspect dataset analysis and quantitative support for the proposed framework. | read pages [10, 11] | [event 25](trace.jsonl#L25) |
| 6 | submit_review `{"review": {"score": 0.65, "observations": 4}}` | Evidence covers the framework, generated datasets, prompt ablation, and stated evaluation limits. | review accepted | [event 30](trace.jsonl#L30) |
