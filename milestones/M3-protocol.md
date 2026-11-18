# Repeated paper-review comparison protocol

The [benchmark-design proposal](benchmark-design.md) adds an externally labelled
quality track that assumes no new human annotation. It supplements this frozen
M2 comparison and should be validated before launching a large experiment matrix.
The human assessment section below remains an optional, stronger evaluation path.

Status: registered experiment plan. Full comparative runs and human annotation
have not been performed for the evidence-memory variant. Development smoke tests
verify execution and are excluded from benchmark results. Commit this protocol
and implementations before collecting new benchmark outcomes. Historical M2 and
PyAgent outcomes informed the hypotheses; this is not an unseen-dataset study.

## Mechanisms and predictions

Three agent variants and one baseline share the frozen `m2-v1` assessment rubric,
text snapshots, citation checker, model settings, and execution limits.

| Method | Mechanism | Prediction and trace evidence | Source |
|---|---|---|---|
| `agent` | M2 native function-calling ReAct with complete interaction history. | Reference condition; repeated T17 outcomes test whether its citation-repair failure is recurrent. | [M2](M2.md), [ReAct](https://arxiv.org/abs/2210.03629). |
| `pyagent_react` | Imported ReAct harness plus a text-action protocol. | Preserve verified completion without increasing mean cost; malformed actions may instead consume decisions. Inspect protocol errors and repair trajectories. | [Registered PyAgent hypothesis](../variants/pyagent_react/README.md), MIT dependency. |
| `evidence_memory` | Native loop recites exact observed evidence, page provenance, compact action outcomes, and latest citation diagnostics; discards old drafts. | Reduce input tokens on multi-step repairs, particularly T17, without reducing verified completion. Inspect `context_memory` events and successive request inputs. Quality improvement is not presumed. | [Mechanism and hypothesis](../variants/evidence_memory/README.md). |
| `baseline` | Full frozen paper in one structured-output call. | Fast reference for assessment quality and cost. It accepts reviews even when quotations fail verification. | [M2 baseline](M2.md). |

PyAgent changes harness and action encoding together; results cannot isolate the
framework from the protocol. Evidence memory changes context construction, not
the rubric, tool schema, reading budget, or acceptance rule. A model change is a
crossed experiment factor, not an additional agent architecture.

## Frozen design

- Inputs: all 20 tasks in `data/eval/tasks.jsonl`, unchanged. Run `paper-review verify`.
- Primary model: `gpt-6-luna`. Secondary block: `gpt-5.6-luna`. Both are available
  through the configured provider and have documented token rates. Aliases can
  drift; retain request/response model IDs, timestamps, source archive, and hashes.
- Five independent attempts per task, method, and model: 400 reviews per model,
  800 total. These are planned runs, not an instruction to start them automatically.
- Five reading actions; eight decisions; 4,000 output tokens per request; low
  reasoning; 90-second timeout; one retry; three workers. Defaults match M2.
- Each model uses a separate output directory. Seeded job shuffling mixes methods,
  tasks, and repetitions within a model block to reduce fixed-order confounding.
  Model sampling remains stochastic; the scheduling seed does not seed the API.
- Keep failures and their incurred costs. Preserve incomplete experiments; do not
  delete failed outcomes or rerun only unsuccessful cells to improve scores.
- Freeze the implementation before benchmark collection. A correctness fix after
  inspecting outcomes requires a new revision and fresh complete comparison.

Run the following only when starting the full experiment, with the installed
`requirements-m3.txt` environment and a configured `.env`:

```shell
paper-review verify
paper-review eval --variants agent pyagent_react evidence_memory baseline --model gpt-6-luna --repeats 5 --workers 3 --max-reads 5 --max-output-tokens 4000 --timeout 90 --retries 1 --reasoning-effort low --order-seed 20261118 --out runs/m3-luna6-r5
paper-review eval --variants agent pyagent_react evidence_memory baseline --model gpt-5.6-luna --repeats 5 --workers 3 --max-reads 5 --max-output-tokens 4000 --timeout 90 --retries 1 --reasoning-effort low --order-seed 20261119 --out runs/m3-luna56-r5
paper-review check runs/m3-luna6-r5
paper-review check runs/m3-luna56-r5
```

Expected outputs: one `experiment.json`, `source.zip`, combined `README.md`, and
400 `<method>-r<repeat>/<task>/trace.jsonl` files per model. Every event identifies
its variant. The report contains per-attempt links and per-repeat statistics.
Printed completion counts are measurements, not prescribed expected values.

T17's F05 diagnostic adds ten native-agent repetitions on the primary model:

```shell
paper-review eval --variants agent --task-ids T17 --model gpt-6-luna --repeats 10 --workers 3 --out runs/m3-t17-native-r10
paper-review check runs/m3-t17-native-r10
```

Report failures out of ten for this diagnostic separately from the five T17
attempts in the main comparison. Classify each failure by actual trace events:
repeated citation rejection, API error, malformed action, or another cause. The
archived repair loop is evidence of a symptom; PDF hyphen handling remains a
possible contributor, not an established general root cause.

## Measures and comparisons

**Completion**: accepted reviews / all attempts. **Verified success**: completed
reviews with every quotation verified / all attempts. This is the common M2
mechanical measure, not assessment quality; agents enforce it at acceptance.
Quote-level matching uses all returned observations as its denominator.

Report each repeat before pooling: completion and verified-success rates; mean
decisions, reading actions, tool calls, API calls, input/output/cached tokens,
estimated USD, and elapsed seconds per attempt. Costs include failed attempts
and retries; human annotation and optional evidence-audit costs are separate.
Token rates estimate provider charges and are not an invoice.

Per task, report successes out of five and score sample standard deviation on
completed reviews, with the number of available scores. Never impute a missing
paper score as zero. For task i with s_i successes in n attempts, estimate
`pass^k = mean_i(C(s_i,k) / C(n,k))` for k=1..n: success in **every** one of k
independent attempts. This differs from pass@k (at least one success). It assumes
stationary, independent attempts; a shared API backend may violate that assumption.

Compare methods using paired task means, with 95% bootstrap intervals that
resample papers while retaining their repeated attempts. These intervals describe
variation over this convenience sample; they do not capture all provider drift
or sampling bias. Compare between-method mean-score differences to repeated
within-method score differences. A score shift is not evidence of better reviews.
Do not treat 100 attempts as 100 independent papers or pool the two model blocks.

## Assessment quality and rational selection

Use the [human-label protocol](../data/quality/README.md): support, central evidence
coverage, calibration, and reading-club usefulness, plus critical factual errors
and observation-level judgments. Two independent readers label the same blinded
reviews against the source. Initial balanced subset: T01, T03, T08, T13, T17,
repetitions 1 and 2, all four methods, separately within each model (40 attempts
per model). These cases include known diagnostic material; findings are a targeted
audit, not a population-wide quality estimate. Expand to the full sample before
making broad quality claims if the targeted audit is inconclusive.

If the M2 evidence judge is rerun, retain exactly its `gpt-6-luna` model and
`AUDIT_PROMPT` rubric in `audit.py`, and report agreement with human claim labels
only where label definitions match. Do not silently introduce a new judge and
call its scores directly comparable to M2. Empty human templates are not labels.

M1's performance measure is defensible research and discussion value, supported
by paper evidence, at acceptable cost and repeatability. Its planned MAE against
human reference scores remains unavailable. Select by substantive human evidence
first: compare critical errors and all-attempt adequate-review rates (all four
dimensions at least 1, no critical error). If quality differences remain unresolved,
report a Pareto set of quality, reliability, cost, and latency. Prefer the cheaper
method only when evidence supports comparable quality and reliability; a
non-significant difference alone does not demonstrate equivalence. Give pass^k
for the eventual winner and state whether differences exceed within-method
variation. No winner is established by the current smoke tests.
