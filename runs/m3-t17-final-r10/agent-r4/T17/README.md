# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**agent · ok**

8 model calls · 4 reads · 21.95 s · $0.003566

8 decisions · 8 tool calls · 85398 input tokens (70254 cached) · 1992 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

The paper introduces Plan-and-Solve prompting, a zero-shot instruction template that asks an LLM to plan subtasks before solving, plus PS+ instructions emphasizing variable extraction and intermediate calculations. GPT-3 evaluations across ten math, commonsense, and symbolic datasets show improvements over zero-shot CoT, with competitive arithmetic results against selected few-shot baselines. The approach is simple and useful, though evidence is concentrated on one model family and one prompt design, and semantic misunderstanding remains unresolved.

- **strength**: The method is a clear extension of zero-shot CoT: explicitly ask for a plan and then execution.
  - Page 3 · citation: whitespace
  - Quote: "Our Zero-shot PS prompting method instead includes the instructions “ devise a plan ” and “ carry out the plan ”"

- **strength**: PS+ reports better arithmetic accuracy than zero-shot CoT and approaches few-shot CoT performance in the displayed results.
  - Page 6 · citation: exact
  - Quote: "PS+ (ours) 91.8 59.3 92.2 46.0 94.7 75.7 76.7"

- **limitation**: The main experiments use a single stated model setup; transfer beyond it is an open question.
  - Page 5 · citation: whitespace
  - Quote: "Following Auto-CoT (Zhang et al., 2022), we use the public GPT-3 (Brown et al., 2020) (175B) as the backbone language model"

- **limitation**: The authors note prompt sensitivity and continued semantic errors as limitations.
  - Page 9 · citation: whitespace
  - Quote: "The GPT-3 models are sensitive to the expressions in prompts, thus we need to carefully design the prompts."

Unresolved questions:

- How well does the method transfer to other model families or sizes?
- How robust are findings to prompt wording and repeated runs?
- I inspected the method, main results, and limitations, but not the appendices; further experimental detail there could affect assessment of robustness.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | read_pages `{"start": 2, "end": 4}` | Inspect method definitions and early experimental setup/results. | read pages [2, 3, 4] | [event 5](trace.jsonl#L5) |
| 2 | read_pages `{"start": 5, "end": 7}` | Review benchmark results, comparisons, and experimental protocol. | read pages [5, 6, 7] | [event 10](trace.jsonl#L10) |
| 3 | read_pages `{"start": 8, "end": 10}` | Inspect remaining analyses, stated limitations, and conclusion for scope and caveats. | read pages [8, 9, 10] | [event 15](trace.jsonl#L15) |
| 4 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Evidence covers the proposed prompting method, comparative results, and author-stated limitations; submit a calibrated assessment. | citation_validation_failed; #3: not_found; #4: hyphenation_ambiguous (pages [9]) | [event 20](trace.jsonl#L20) |
| 5 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Correct ambiguous citations by quoting exact observed wording from pages 5 and 9, then submit the assessment. | citation_validation_failed; #3: not_found; #4: hyphenation_ambiguous (pages [9]) | [event 25](trace.jsonl#L25) |
| 6 | read_pages `{"start": 9, "end": 9}` | Retrieve exact author limitations wording and citation text for final review. | read pages [9] | [event 30](trace.jsonl#L30) |
| 7 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Submit final evidence-based review with exact limitation quote copied from page 9. | citation_validation_failed; #3: not_found; #4: not_found | [event 35](trace.jsonl#L35) |
| 8 | submit_review `{"review": {"score": 0.69, "observations": 4}}` | Use a verbatim continuous passage on page 9 to resolve quote matching and complete the review. | review accepted | [event 40](trace.jsonl#L40) |
