# T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering

**baseline · ok**

1 model calls · 0 reads · 7.73 s · $0.000336

1 decisions · 0 tool calls · 8838 input tokens (8835 cached) · 495 output tokens

[Structured trace](trace.jsonl) contains full arguments, model outputs, and observations. This page shows the review once and summarizes each decision.

## Review · score 0.62

AlphaCodium presents a practical, test-driven multi-stage inference flow for code generation: reflect on the problem, reason about public tests, generate additional tests, and iteratively run and repair candidate code. On CodeContests, the authors report substantial pass@5 improvements over a direct prompt across GPT-3.5, GPT-4, and DeepSeek, and compare favorably with selected prior results. The contribution is a useful engineering method supported by benchmark results, though the paper leaves important questions about which components drive the gains and how robust the comparisons are.

- **strength**: The main reported comparison shows sizable gains over a direct prompt across models and both validation and test sets, including GPT-4 validation pass@5 rising from 19% to 44%.
  - Page 7 · citation: whitespace
  - Quote: "AlphaCodium flow consistently and significantly improves the performance of LLMs on CodeContests problems"

- **strength**: The paper gives a concrete account of the method, including public-test iteration, AI-generated tests, and test anchors that preserve previously passed cases during repairs.
  - Page 6 · citation: whitespace
  - Quote: "the test anchors will protect us against an incorrectly fixed code."

- **limitation**: Comparisons to prior work are not fully controlled or reproducible from the paper’s account: the authors note evaluation subtleties and rely on reported numbers, while the methods differ in model and sampling setup.
  - Page 7 · citation: hyphenation_ambiguous
  - Quote: "We compare to the numbers reported in the papers"

- **uncertainty**: The results do not isolate the effects of individual flow stages or design choices; the paper describes the full flow’s gains but does not establish which components are necessary or sufficient.
  - Page 5 · citation: hyphenation_ambiguous
  - Quote: "some steps can be combined into a single LLM call"

Unresolved questions:

- How much of the improvement comes from problem reflection, generated tests, iterative repair, test anchors, or their combination?
- How sensitive are the reported gains to model version, prompt details, inference settings, and the budget allocated to each problem?
- How often are AI-generated tests incorrect, and how reliably do test anchors prevent harmful repairs or preserve genuinely correct behavior?
- I inspected the supplied pages, including the results and appendices, but not the implementation or external evaluation artifacts; how closely would an independent run reproduce the reported figures?

## Decisions

| Step | Action and key arguments | Purpose | Outcome | Event |
|---|---|---|---|---|
| 1 | final_answer  |  | final response recorded | [event 5](trace.jsonl#L5) |
