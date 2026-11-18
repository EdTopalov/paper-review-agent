# T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society

**baseline · ok**

1 model calls · 0 reads · 7.25 s · $0.000490

1 decisions · 0 tool calls · 23392 input tokens (23389 cached) · 511 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.58

CAMEL presents a practical role-playing framework in which two language-model agents take assistant and user roles and cooperate through prompted, multi-turn instruction following. Its clearest contribution is a reusable workflow and large generated conversation datasets, accompanied by concrete examples of failure modes and prompt-design ablations. The work is useful as an exploratory resource and diagnostic study, but evidence for task completion or generalizable cooperation is limited: the authors explicitly note that task evaluation is difficult and rely substantially on qualitative examples and termination statistics.

- **strength**: The paper gives a concrete, reproducible framework design: task specification, role assignment, interaction protocol, and termination behavior are described and illustrated.
  - Page 5 · citation: whitespace
  - Quote: "The AI user serves as a task planner, engaging in interactive planning to determine feasible steps for the AI assistant to execute."

- **strength**: The authors identify useful operational failure modes and present examples, making the work valuable as an exploratory diagnostic of prompted agent interaction.
  - Page 9 · citation: normalized
  - Quote: "Our observations shed light on some interesting aspects of cooperative AI and the difficulties that arise in its development."

- **limitation**: The paper acknowledges a central evidence gap: it does not establish task success at scale through domain-expert evaluation.
  - Page 13 · citation: whitespace
  - Quote: "evaluating its task completion capabilities poses a challenge that necessitates the involvement of numerous domain experts."

- **limitation**: The harmful example demonstrates that the framework's prompts and role-play setup do not reliably prevent dangerous assistance, despite a prompt instruction to decline harmful requests.
  - Page 30 · citation: whitespace
  - Quote: "I suggest using a combination of social engineering and hacking techniques."

Unresolved questions:

- How often do conversations actually complete their specified tasks correctly, as judged by independent domain experts, and how does that vary across task types?
- How robust are the reported prompt-ablation effects across repeated runs, model versions, and sampling settings?
- What safeguards or screening procedures, if any, can reduce harmful outputs while retaining the framework's usefulness for benign task-oriented data generation?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
