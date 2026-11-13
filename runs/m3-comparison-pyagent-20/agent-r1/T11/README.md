# T11: Executable Code Actions Elicit Better LLM Agents

**agent · ok**

4 model calls · 2 reads · 12.44 s · $0.001964

4 decisions · 4 tool calls · 20533 input tokens (9524 cached) · 1011 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.72

The paper proposes CodeAct: using executable Python as a flexible, composable agent action interface with iterative execution and feedback. It evaluates the approach across API-Bank and a newly curated benchmark, then contributes a 7,139-trajectory instruction dataset and fine-tuned open-source agents. The inspected results suggest sizeable gains on several agent tasks, but the pages reviewed do not establish robustness across deployment settings.

- **strength**: The method combines execution with feedback-driven revision in multi-turn interaction.
  - Page 1 · citation: whitespace
  - Quote: "Integrated with a Python interpreter, CodeAct can execute code actions and dynamically revise prior actions or emit new actions upon new obser- vations through multi-turn interactions."

- **strength**: The dataset spans several agent use cases and contains thousands of curated trajectories.
  - Page 8 · citation: exact
  - Quote: "Total 7,139 10 ,581,681 1482 .24"

- **strength**: The displayed table reports gains over base/instruct models on several agent tasks for the Mistral-based agent.
  - Page 8 · citation: exact
  - Quote: "CodeActAgent (Mistral) 7B57.4 32 .4 12 .2 46 .2 15.9"

- **limitation**: Training trajectory generation uses a limited set of proprietary model families, a reproducibility consideration for this data component.
  - Page 7 · citation: whitespace
  - Quote: "We run gpt-3.5-turbo-0613 from OpenAI, claude-1-instant and claude-2 from Anthropic on down-sampled data"

Unresolved questions:

- How do the full benchmark results, baselines, and statistical variability support the headline comparison across all 17 LLMs?
- How does unrestricted Python execution affect safety, reliability, and resource control in practical deployments?
- I inspected the abstract/first page and pages 6–8; the full evaluation methodology, benchmark construction, and stated limitations were not reviewed.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | search_paper `{"query": "20% higher"}` | Locate the paper's central quantitative comparison to assess evidence for its main performance claim. | 1 matches on pages [1] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 6, "end": 8}` | Inspect experimental setup and reported benchmark results for direct support and scope of the claims. | read pages [6, 7, 8] (text truncated by tool) | [event 10](trace.jsonl#L10) |
| 3 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | The inspected abstract, dataset description, and evaluation table establish the contribution and support; submit a calibrated review while noting uninspected portions. | citation_validation_failed; #1: hyphenation_ambiguous (pages [1]) | [event 16](trace.jsonl#L16) |
| 4 | submit_review `{"review": {"score": 0.72, "observations": 4}}` | Correct the first citation using an exact abstract quote observed on page 1, preserving validated evidence and scope caveats. | review accepted | [event 22](trace.jsonl#L22) |
