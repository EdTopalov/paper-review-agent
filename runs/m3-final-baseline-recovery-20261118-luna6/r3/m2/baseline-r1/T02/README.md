# T02: Reflexion: an autonomous agent with dynamic memory and self-reflection

**baseline · ok**

1 model calls · 0 reads · 9.99 s · $0.000499

1 decisions · 0 tool calls · 14416 input tokens (14413 cached) · 710 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.65

ReflExion adds a natural-language reflection and memory loop to an LLM agent: after failure, the agent reviews its trajectory, stores advice, and tries again. The paper reports improved cumulative task success over repeated trials on AlfWorld and HotPotQA, with a less conclusive WebShop result. Its central value is a simple, broadly framed method for using feedback across trials; the evidence is promising but limited in scale and does not isolate the effects of reflection from other elements of the setup.

- **strength**: The paper presents a concrete, lightweight mechanism combining a failure-triggering heuristic, written reflection, memory, and retries, rather than requiring policy training.
  - Page 3 · citation: wrong_page
  - Quote: "Finally, we add the reflection to the agent’s memory, reset the environment, and start the next trial."

- **strength**: The AlfWorld evaluation reports a substantial improvement over the stated ReAct baseline across 134 environments, and the paper provides a trajectory illustrating how stored advice can change a later attempt.
  - Page 5 · citation: exact
  - Quote: "the agent used ReAct to solve 97% of the given environments in 12 trials"

- **limitation**: The HotPotQA results are reported inconsistently: the abstract gives 51%, while the results section gives 54% on the same 100-question dataset. This makes the precise headline result unclear.
  - Page 1 · citation: exact
  - Quote: "We observe success rates of 97% and 51%, respectively"

- **limitation**: The paper reports small benchmark evaluations and does not establish from the supplied evidence how robust the improvements are to different models, prompts, or task samples. The authors also report little improvement on WebShop, where tool quality may constrain performance.
  - Page 10 · citation: whitespace
  - Quote: "we observed a shortcoming in its ability to improve on its baseline performance in a third benchmark, WebShop"

Unresolved questions:

- Why do the abstract and HotPotQA results section report 51% and 54%, respectively, and which figure should be treated as the result?
- How much of the improvement comes specifically from reflection and memory, as opposed to repeated attempts, prompt examples, or other setup choices?
- Would the reported gains persist across additional task samples, language models, and prompt configurations?
- The supplied pages report aggregate outcomes and illustrative trajectories; what uncertainty estimates or more detailed per-task results support the reported gains?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
