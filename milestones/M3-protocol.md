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

All methods use common task contracts; the three agents share evidence tools and
citation acceptance. PyAgent changes the harness and action encoding together.
The deliberative controller reserves decisions for planning and criticism.

The existing-method snapshot is based on `def61ec`; the deliberative controller
and hypothesis were committed in `10be7a3`, before their repeated test runs.
Each stage preserves evaluated source bytes in `source.zip` and records source/
input hashes and configuration. Subsequent fixes require a new comparison.

## Configuration and reproduction

The model is `gpt-6-luna`. The target is five repetitions per paper and method:
400 M2 attempts. Reading agents allow five reading actions and eight decisions.
All requests allow 4,000 output tokens, low reasoning, a 90-second timeout and one retry.
The saved launch blocks use six workers for existing methods and four for the
deliberative agent; actual completed repetitions are recorded in the results.

After [installation](../README.md#installation), install `requirements-m3.txt`
and configure `.env`. This command runs a fresh complete comparison with paid API calls:

```shell
paper-review verify
paper-review eval --variants agent pyagent_react deliberative_review baseline --model gpt-6-luna --repeats 5 --workers 6 --max-reads 5 --max-output-tokens 4000 --timeout 90 --retries 1 --reasoning-effort low --order-seed 20261118 --out runs/m3-luna6-r5
paper-review check runs/m3-luna6-r5
```

Expected output: `experiment.json`, `source.zip`, `progress.json`, `summary.json`,
a combined `README.md`, and 400 `<variant>-r<repeat>/<task>/trace.jsonl` files with
readable task reports. Every trace event identifies its variant.

The separate T17 diagnostic uses ten attempts and the same per-attempt limits:

```shell
paper-review eval --variants agent --task-ids T17 --model gpt-6-luna --repeats 10 --workers 4 --max-reads 5 --max-output-tokens 4000 --timeout 90 --retries 1 --reasoning-effort low --order-seed 20261118 --out runs/m3-t17-native-r10
paper-review check runs/m3-t17-native-r10
```

It writes ten traces under `agent-r<repeat>/T17/`. Report its failure count
separately from the main comparison; the [failure map](failure-map.md) interprets the traces.

## Measures

Completion is accepted reviews divided by all attempts. Verified success adds
verification of every citation. Per-repeat and per-paper results include decisions,
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
