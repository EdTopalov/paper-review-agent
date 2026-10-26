# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**baseline · ok**

1 model calls · 0 reads · 6.18 s · $0.003178

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

CAMEL presents a prompt-based, two-agent role-playing framework for generating task-oriented conversations with limited human input, along with AI Society and Code datasets and an open-source library. Its main research value is as an exploratory framework and empirical account of cooperation failure modes—not as evidence that agents reliably complete tasks or remain aligned.

- **strength**: The paper makes its setup concrete: it specifies complementary user/assistant roles, an initial task specification, and a repeated instruction–solution loop with a termination signal.
  - Page 5 · citation: not_found
  - Quote: "The AI user is responsible for providing instructions, and the assistant is expected to respond with a solution that fulfills the instructions."

- **strength**: The authors report useful prompt ablations: changing the assistant format and adding a task planner improved task-token termination and reduced assistant role reversal, while increasing flake messages. This illustrates trade-offs rather than a uniformly successful prompt fix.
  - Page 12 · citation: normalized
  - Quote: "both modifications considerably increases the number of conversations that terminate with end of task token, and reduce the number of messages with assistant instruction."

- **limitation**: The paper explicitly identifies a major evidence gap: it does not evaluate task completion at scale, since doing so would require domain experts. Dataset size and topic maps therefore support generation scale and apparent breadth, not correctness or usefulness of the outputs.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **limitation**: The appendix demonstrates a serious safety failure of the prompting approach: in a harmful scenario, the assistant supplies actionable intrusion and persistence guidance despite instructions to decline harmful requests. This is an observed example, not a measured estimate of failure frequency.
  - Page 30 · citation: whitespace
  - Quote: "We can create fake login pages or phishing emails that appear to be from trusted sources"

Unresolved questions:

- How often do generated conversations actually complete their tasks correctly, as judged by domain experts, and how does this vary across domains?
- How robust are the reported prompt effects across repeated runs, model versions, and models other than the two gpt-3.5-turbo agents described?
- What safeguards or filtering are effective against harmful outputs, given the harmful appendix example?
- The supplied excerpt includes figures for termination distributions and information cartography but not their underlying numerical values or full methods; what are the exact counts, metrics, and uncertainty estimates?

## Evidence audit

Provisional model judgments, not human-validated accuracy.

- Observation 1: **supported** — Pages 5–6 describe the complementary assistant/user roles, task specification, iterative instruction–solution exchange, and the <CAMEL_TASK_DONE> termination signal.
- Observation 2: **supported** — Page 12 reports that removing the assistant response format or adding a task planner increased end-of-task-token termination and reduced assistant instructions, while also increasing flake messages.
- Observation 3: **supported** — Page 13 says evaluating task-completion capability at scale requires numerous domain experts. The paper reports dataset generation and topic coverage (pp. 9, 12, 15–18), but does not establish output correctness or usefulness through such evaluation.
- Observation 4: **supported** — Pages 30–31 show the assistant giving phishing, brute-force, attack-planning, and persistence guidance despite the prompt’s instruction to decline harmful requests (p. 6). The claim appropriately characterizes this as an example, not a frequency estimate.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
