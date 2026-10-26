# Paper Review Agent

The M2 implementation, frozen 20-paper sample, measured comparison, and failure
analysis are documented in **[M2.md](M2.md)**. Source code is in
[`src/paper_review`](src/paper_review), with one entry point: `paper-review`.

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-m2.txt
.venv\Scripts\python.exe -m pip install --no-deps -e .
Copy-Item .env.example .env
# Fill OPENAI_API_KEY in .env locally. Never commit it.
.venv\Scripts\paper-review.exe verify
.venv\Scripts\paper-review.exe review data/eval/papers/T01.json --out runs/scratch/example --model gpt-6-luna
.venv\Scripts\paper-review.exe eval --out runs/my-comparison --model gpt-6-luna
```

The final integrated M2 experiment completed **19/20 agent tasks and 20/20
baseline tasks**. All citations were verified in 19/20 agent attempts and 7/20
baseline attempts; the agent uses a citation validation and repair loop. These
numbers measure completion and text fidelity, not research-review accuracy.
The bounded failure, costs, and provisional evidence audits are documented in the
[results](M2.md#integrated-results) and [failure analysis](M2.md#five-annotated-failed-decisions-retained-for-m3).
The API key is read from the local ignored `.env`, overriding inherited values.
`paper-review models` lists models accessible to that key's project.

The remainder of this README preserves the original **M1 design proposal**.
Implemented scope and deviations are stated in M2.md.

Paper Review Agent will help ML research teams, including JetBrains reading clubs, choose papers for discussion. Given several PDFs or paper URLs, it will return a ranking with an absolute score in `[0, 1]` for each paper and a short, evidence-backed assessment. Candidates can cover unrelated topics; a team profile or shared research question is optional future work.

This document describes the planned Python implementation.

## Task and scoring

Choosing a paper requires checking whether its contribution deserves attention and whether its evidence supports its claims. The agent will assess this research and discussion value using the supplied papers, including appendices and references.

The rubric will examine contribution, supporting evidence, scope and limitations, and intellectual depth. These dimensions will support an overall judgment against fixed anchors, without arbitrary numerical weights. Standards will match the paper type: experiments support empirical claims, arguments support theoretical claims, and reliable synthesis supports surveys. Negative results can also offer substantial value.

| Score anchor | Meaning |
|---|---|
| `0.00` | Essentially no substantive, supported research value. |
| `0.25` | Limited value or serious weaknesses in central claims. |
| `0.50` | Defensible work with useful insights. |
| `0.75` | Substantial contribution with convincing support. |
| `1.00` | Exceptional contribution and supporting evidence. |

These anchors are provisional and will be refined using existing reading-club comments. Intermediate scores are allowed. Scores will never be normalized within a batch: papers scoring `0.23`, `0.16`, and `0.09` still produce a ranking, while all remain weak candidates. An unreadable paper will receive a processing error rather than a low quality score.

## Architecture

Adaptive reading lets the agent investigate questions that emerge from a paper, such as whether an efficiency claim uses a fair cost comparison. A script can retrieve sections, while the model decides which checks a claim requires. A bounded [ReAct-style loop](https://arxiv.org/abs/2210.03629) will choose reading actions and update the assessment. Its benefit over a full-paper one-shot call will be tested.

1. Load each paper and extract text, sections, metadata, and page locations with PyMuPDF.
2. Assess papers independently in parallel. Tools such as `read_section`, `search_paper`, and `inspect_page` will expose relevant text, tables, and figures.
3. Review unresolved evidence and close leading scores when another read could affect the decision. Start with five reading actions per paper and one additional review round of at most two reads.
4. Validate scores and evidence locations, then sort deterministically and return the ranking.

Review may leave scores unchanged. Every revision must identify new evidence or a corrected interpretation; the controller will never require scores to separate.

We will try reasoning-capable models from different providers and select based on output quality, variance, and cost. Python will handle parsing, concurrency, retries, budgets, validation, sorting, and logging because these operations need predictable behavior.

Per-paper memory will retain inspected sections, evidence, unresolved questions, and remaining budget. Batch state will track review candidates. A persistent cache will store parsed papers, while experiment logs will record model settings, scores, actions, and costs. Document contents will be treated as data, including any embedded instructions.

## Failure map

These are anticipated risks identified through design analysis and literature; prototype results are still pending.

| Failure | Identification source | Response |
|---|---|---|
| Abstract hype hides weak support. | Task analysis: headline claims require checking methods and results. | Require evidence for central claims before scoring. |
| Parsing corrupts a table, formula, or result. | PDF layout analysis: extracted text can lose structure. | Inspect the source page or flag insufficient evidence. |
| The rubric favors a topic or paper type. | The requirement to compare unrelated empirical, theoretical, and survey papers. | Use type-appropriate support criteria and inspect disagreements during development. |
| Scores fluctuate or inflate in weak batches. | Fixed absolute anchors must survive repeated runs and changing candidates. | Score independently and measure repeated-run variance. |
| Close-score review forces changes or wastes reads. | Analysis of the proposed review trigger. | Permit unchanged scores and enforce the review budget. |
| A plausible assessment cites unsupported evidence. | Tool design: retrieving a passage does not establish that it supports a claim. | Preserve excerpts and locations so disagreements can be checked against the paper. |
| Reference scores reproduce model biases. | [Research on LLM judges](https://arxiv.org/abs/2306.05685) documents systematic evaluation biases. | Anchor references in existing comments, record uncertainty, and separate synthetic references. |

## Evaluation plan

### Build a small reference from existing feedback

Start with the 10–15 papers already discussed by the reading club. Reserve five papers before tuning the rubric or prompts; use recurring judgments from the remainder to refine the criteria and anchors.

For each paper, extract the comments' judgments about contributions, evidence, and limitations, then locate supporting passages in the paper. Keep original comments separate from model-added interpretations. A strong reference LLM will map this material to the score anchors, preserving disagreements and gaps. Repeat reference scoring three times, record its spread, and freeze the mean score before evaluating candidate models.

These references remain provisional because comments may be sparse or contradictory. Agreement with them provides limited evidence of usefulness.

Later, a SOTA LLM may generate comparable assessments and evidence for additional papers. Report results on those synthetic references separately from the reading-club set.

### Measure agreement, cost, and variance

The primary quality metric will be mean absolute error against frozen reference scores:

`MAE = mean(|agent_score - reference_score|)`

This checks absolute ratings, including cases where every candidate is weak. Ranking will follow the scores without a separate ranking metric.

Compare the adaptive agent with a full-paper one-shot baseline using the same model, rubric, document versions, and parser. Run each configuration five times on the same reserved papers, with reference comments and scores hidden from the evaluated model.

Report mean MAE and its standard deviation across runs, plus each paper's score variance. Also report mean API cost per paper and its standard deviation, including retries and review. Reference-score spread will show how much uncertainty comes from the targets themselves. Processing failures will be reported explicitly.

Select models and reading policies on development results, then freeze them for the reserved evaluation. Adaptive reading earns its place if it improves agreement or achieves comparable agreement at lower cost, with acceptable score variance.

## Extensions

Search can accept a topic or research request, retrieve candidates, and apply the same scorer. Poor candidates can trigger another search; missing evidence should trigger more reading. Query and cost budgets will bound this loop.

Automatic prompt optimization can later use a small Python loop or an adapter to a Koog optimizer. It will optimize development MAE and cost while keeping the rubric and reserved evaluation fixed.
