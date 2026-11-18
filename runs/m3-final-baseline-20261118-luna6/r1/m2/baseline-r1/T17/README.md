# T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

**baseline · ok**

1 model calls · 0 reads · 8.18 s · $0.000517

1 decisions · 0 tool calls · 18064 input tokens (18061 cached) · 673 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.69

The paper introduces Plan-and-Solve prompting, a zero-shot approach that asks an LLM to plan a problem’s subtasks before solving them, with PS+ adding instructions to extract variables and calculate intermediate results. On ten reasoning datasets using GPT-3, the authors report gains over Zero-shot-CoT and competitive results against several few-shot and program-based baselines. The contribution is a simple, practical prompting method supported by broad task coverage, though the evidence is limited to one model family and does not establish how broadly the results generalize.

- **strength**: The evaluation spans arithmetic, commonsense, and symbolic reasoning, and reports accuracy comparisons with multiple prompting baselines. This breadth supports the method’s practical value across several task types.
  - Page 2 · citation: whitespace
  - Quote: "We evaluate our proposed prompting on six math reasoning datasets"

- **strength**: The main results show consistent gains over Zero-shot-CoT on the six arithmetic datasets; PS+ also exceeds Zero-shot-CoT on both commonsense and both symbolic datasets, though it does not outperform every few-shot baseline.
  - Page 6 · citation: not_found
  - Quote: "Zero-shot-PS+ prompting 71.9 65.4"

- **limitation**: The evidence is confined to GPT-3, specifically text-davinci-003 in the main experiments. The paper therefore does not establish whether the gains transfer to other model families or sizes.
  - Page 5 · citation: whitespace
  - Quote: "we use the public GPT-3 (Brown et al., 2020) (175B) as the backbone language model"

- **uncertainty**: The error analysis examines 100 GSM8K examples, but the inspected description does not specify an annotation procedure or inter-annotator agreement. The reliability of the error-category comparisons is therefore unclear.
  - Page 7 · citation: hyphenation_ambiguous
  - Quote: "Subsequently, we analyze and determine the error types of all these problems"

Unresolved questions:

- Do PS and PS+ retain their gains on other model families, model sizes, and current language models?
- How sensitive are the results to prompt wording and prompt selection, beyond the variants evaluated in the appendix?
- How reproducible are the reported error-category findings under a specified annotation protocol or independent raters?
- The assessment covers the supplied 24 pages, including the appendix examples and prompt tables; it does not include any material beyond those pages.

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
