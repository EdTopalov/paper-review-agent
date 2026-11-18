# Repeated paper-review comparison protocol

The comparison keeps all 20 frozen papers in `data/eval/tasks.jsonl`, the
`m2-v1` review rubric, and the M2 citation checker. The separate
[evidence-assessment benchmark](benchmark-protocol.md) tests content judgments.

| Method | Mechanism and hypothesis | Source |
|---|---|---|
| `agent` | Native function-calling ReAct with full interaction history; reference condition. | [M2](M2.md), [ReAct](https://arxiv.org/abs/2210.03629). |
| `pyagent_react` | Imported ReAct harness with text actions; preserve verified completion without increasing mean cost. Inspect action errors and citation repair. | [PyAgent hypothesis and source](../variants/pyagent_react/README.md). |
| `deliberative_review` | Plan, investigate, draft, criticize in a fresh context, then revise; reduce missed counterevidence and scope errors. Inspect challenged claims and targeted reads. | [Hypothesis and sources](../variants/deliberative_review/README.md). |
| `baseline` | One full-paper structured-output call; reference for content accuracy and cost. | [M2](M2.md). |

Methods use common task contracts. Ordinary agent submissions require matching,
observed citations. At the decision cap, one final call requests a nullable public
answer without tools or retries: a valid non-null answer completes regardless of
citation checks, which remain separate diagnostics. Null, missing/invalid output,
and transport errors remain failures. Internal deliberative ledgers cannot block
this final public answer. Baseline uses its ordinary single full-paper call.

Hypotheses are preserved in `def61ec` (PyAgent) and `10be7a3` (deliberative).
The implementation is frozen before final collection. Each stage archives evaluated
source bytes in `source.zip` and records source/input hashes and configuration.

## Configuration and reproduction

The model is `gpt-6-luna`; three repetitions per paper and method plan 240 M2 attempts.
Reading agents allow five reading actions and 16 ordinary decisions, plus one
forced final call if needed (17 decisions maximum). Requests allow 4,000 output
tokens, low reasoning, a 90-second timeout and one transport retry; the final call
has no retry. Separate collection blocks use eight workers per agent and four for baseline.

After [installation](../README.md#installation) with `requirements-m3.txt` and
`.env`, this public-entry-point command runs a fresh paid M2 comparison:

```shell
paper-review verify
paper-review eval --variants agent pyagent_react deliberative_review baseline --model gpt-6-luna --repeats 3 --workers 8 --max-reads 5 --max-output-tokens 4000 --timeout 90 --retries 1 --reasoning-effort low --order-seed 20261118 --out runs/m3-m2-final-r3
paper-review check runs/m3-m2-final-r3
```

Expected output: `experiment.json`, `source.zip`, `progress.json`, `summary.json`,
a combined `README.md`, and 240 `<variant>-r<repeat>/<task>/trace.jsonl` files with
readable task reports. Every trace event identifies its variant. The benchmark
protocol gives the exact separate method-block commands used for combined collection.

A separate ten-attempt T17 diagnostic under this policy uses a fresh directory:

```shell
paper-review eval --variants agent --task-ids T17 --model gpt-6-luna --repeats 10 --workers 4 --max-reads 5 --max-output-tokens 4000 --timeout 90 --retries 1 --reasoning-effort low --order-seed 20261118 --out runs/m3-t17-final-r10
paper-review check runs/m3-t17-final-r10
```

It writes ten traces under `agent-r<repeat>/T17/`. Keep diagnostic frequencies
separately from the main comparison; the [failure map](failure-map.md) interprets the traces.

## Measures

Completion is non-null accepted reviews divided by all attempts. Verified success
additionally requires every citation verified. Per-repeat and per-paper results include decisions,
reading/tool/API calls, input/output tokens, estimated USD and latency per attempt.
Failures and retries retain their costs; missing paper scores remain missing.

For a paper with s verified successes in n repetitions, `pass^k` is
`C(s,k)/C(n,k)`, averaged over papers: success in every one of k independent attempts.
Report k=1..n, within-method score variation, and paired method differences with
95% bootstrap intervals over papers, keeping each paper's repetitions together.

The [M2 appendix](M3-results/M2.md) contains these measurements. Rational selection
uses M1's evidence-backed research and discussion value, repeatability and cost;
the [M3 report](M3.md) gives the choice using the new benchmark's content evidence.
The [human-label protocol](../data/quality/README.md) is optional for complete-review
quality. Any new evidence audit must retain the M2 judge and rubric and report label agreement.
