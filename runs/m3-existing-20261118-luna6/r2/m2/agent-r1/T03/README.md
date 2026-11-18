# T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**agent · ok**

4 model calls · 3 reads · 8.62 s · $0.001040

4 decisions · 4 tool calls · 14551 input tokens (9033 cached) · 545 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.66

AutoGen presents a flexible, conversational multi-agent framework integrating LLMs, tools, and human input, with configurable interaction patterns and diverse application examples. Its concrete demonstrations make the framework useful and its small math comparison provides initial evidence, but the support is primarily illustrative and the quantitative evaluation is narrow.

- **strength**: The central design contribution is a unified conversational abstraction for agents with configurable capabilities and interaction patterns.
  - Page 2 · citation: exact
  - Quote: "F2 Conversable agents with unified conversation interface."

- **strength**: The paper reports a direct comparative evaluation, including a larger sample than the initial qualitative trials; AutoGen is competitive but not uniformly better.
  - Page 11 · citation: whitespace
  - Quote: "With one trial, AutoGen scores 8/12 problems, and both ChatGPT+Plugin and ChatGPT+Code Interpreter score 7/12 problems."

- **limitation**: The detailed autonomous comparison described here is based on very few problems and repetitions, limiting generalization from the result.
  - Page 10 · citation: whitespace
  - Quote: "We use two level-5 problems from the MATH dataset for the qualitative evaluation and test on each problem for 3 times."

- **uncertainty**: The inspected pages do not establish systematic performance or cost across the framework’s many demonstrated application domains; examples are broad, but the quantitative evidence inspected is math-focused.
  - Page 9 · citation: exact
  - Quote: "We present six examples of diverse applications built using AutoGen."

Unresolved questions:

- How does AutoGen perform across larger, independently sampled benchmarks and repeated trials in application domains beyond math?
- How sensitive are outcomes to model choice, conversation configuration, and tool or human-input costs?
- I inspected the framework overview and math-evaluation pages, not the full implementation details, all application sections, or discussion of limitations; conclusions about those areas remain uncertain.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "evaluation"}` | Locate the paper’s evaluation evidence to assess how well its framework claims are supported. | 8 matches on pages [9, 10, 11, 12] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 2, "end": 3}` | Inspect design and stated contribution to evaluate framework novelty and intended scope. | read pages [2, 3] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 9, "end": 11}` | Inspect evaluation setup and reported outcomes to judge the strength and limits of empirical support. | read pages [9, 10, 11] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.66, "observations": 4}}` | Evidence covers the framework design and a bounded math evaluation; submit an assessment that states the empirical scope limits. | review accepted | [event 20](trace.jsonl#L20) |
