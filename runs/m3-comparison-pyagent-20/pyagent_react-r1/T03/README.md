# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**pyagent_react · ok**

4 model calls · 2 reads · 12.50 s · $0.001696

4 decisions · 4 tool calls · 17136 input tokens (7137 cached) · 751 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.63

AutoGen presents a general framework for composing customizable conversational agents backed by LLMs, humans, and tools, and illustrates it across varied application workflows. The framework design and examples are useful contributions, but the inspected evidence is chiefly demonstrations and limited comparative evaluation, rather than broad evidence that multi-agent conversations improve task outcomes.

- **strength**: The paper clearly motivates a unified conversational interface for agents with different capabilities and flexible interaction patterns.
  - Page 2 · citation: whitespace
  - Quote: "every Autogen agent is made conversable – they can receive, react, and respond to messages."

- **strength**: The MiniWoB++ example includes a concrete comparison, reporting competitive results on selected clicking tasks.
  - Page 15 · citation: whitespace
  - Quote: "among the twelve clicking tasks, MiniWobChat achieves better results in four tasks and achieved parity in performance in three tasks."

- **limitation**: The reported MiniWoB++ comparison is scoped to selected clicking tasks and ten instances per task, so it does not establish performance across the full benchmark or other environments.
  - Page 16 · citation: exact
  - Quote: "For each clicking task, we reported the success rate for ten different instances."

- **uncertainty**: The OptiGuide productivity improvement is reported as a code-size reduction, but the inspected passage does not give a controlled or independently measured assessment of the claimed productivity benefit.
  - Page 14 · citation: whitespace
  - Quote: "The core workflow code for OptiGuide was reduced from over 430 lines to 100 lines using AutoGen, leading to significant productivity improvement."

Unresolved questions:

- How do AutoGen workflows compare with simpler or single-agent implementations under controlled, matched task and resource conditions?
- How robust are the examples to changes in LLM, prompt, cost, and task distribution?
- I inspected pages 1–4 and 14–16 only; important gaps remain about the paper’s other applications, implementation details, and any additional evaluation or limitations elsewhere in the document.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect the framework design and the paper’s concrete application examples. | read pages [2, 3, 4] | [event 6](trace.jsonl#L6) |
| 2 | read_pages invalid arguments: `{"start": 14, "end": 16, "reason": "Inspect reported evaluations and whether they quantify benefits or primarily illustrate use cases."})Action: read_pages({"start":14,"end":16,"re` |  | invalid_arguments | [event 11](trace.jsonl#L11) |
| 3 | read_pages `{"start": 14, "end": 16}` | Inspect reported evaluations and whether they quantify benefits or primarily illustrate use cases. | read pages [14, 15, 16] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.63, "observations": 4}}` | Submit an evidence-based assessment using the inspected framework overview and application evaluation pages. | review accepted | [event 21](trace.jsonl#L21) |
