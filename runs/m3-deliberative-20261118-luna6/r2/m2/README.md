# Experiment results

Open a task to read its review, decisions, tool outcomes, and optional evidence audit. [Settings](experiment.json) · [Evaluated source](source.zip)

Completion means the workflow returned an accepted review. The agent also blocks invalid citations; the one-call baseline does not. Verified citations match source text, not necessarily the meaning of a claim. Summary rates include failed attempts.

An evidence audit is a separate model judgment of claim support; supported counts are provisional verdicts. A first submission is the review proposed before citation repair.

| Method | Completed | All citations verified | Steps/task | Tools/task | Reads/task | Calls/task | Input tokens/task | Output tokens/task | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| deliberative_review | 14/20 | 14/20 | 7.30 | 4.25 | 3.35 | 7.30 | 40527.4 | 2873.7 | $0.006340 | 31.61 |

## Repetition variation

Verified success requires both a completed review and all quotations verified. It measures citation compliance, not assessment quality. Every planned attempt, including a failed attempt, stays in the denominator. Model IDs are not pooled.

| Method | Repeat | Completed | Verified success | Calls/task | Tokens/task (in/out) | USD/task | Seconds/task |
|---|---:|---:|---:|---:|---|---:|---:|
| deliberative_review | 1 | 14/20 | 14/20 | 7.30 | 40527.4/2873.7 | $0.006340 | 31.61 |

### Reliability across repetitions

pass^k estimates success on every one of k independent attempts: mean over papers of C(s,k)/C(n,k), where s is the number of verified successes and n the number of attempts for that paper. It is not success at least once. Independence is an assumption; few repetitions give limited precision.

| Method | Always / sometimes / never verified (papers) | pass^k | Mean absolute score difference within a paper | Score pairs |
|---|---|---|---:|---:|
| deliberative_review | 14 / 0 / 6 | k=1: 0.700 | unavailable | 0 |

### Paired differences between methods

Each paper contributes its mean over observed repetitions. Differences are left minus right. The 95% percentile bootstrap intervals resample papers 2,000 times, keeping each paper's repetitions together (seed 20261118). These exploratory intervals describe this convenience sample conditional on the observed repetitions; they do not capture future API model drift. A single paper has no interval. Scores use only completed reviews from papers completed by both methods and are not validated quality labels.

| Pair | Verified success difference (95% interval) | Score difference (95% interval) | Mean absolute task score difference | USD/task difference | Seconds/task difference |
|---|---|---|---:|---:|---:|

### Per-paper consistency

Score spread excludes failed attempts; completion counts retain them. Compare within-paper score variation above with between-method differences before interpreting small gaps.

| Method | Task | Completed / attempts | Verified / attempts | Mean score | Score sample SD | Score range |
|---|---|---:|---:|---:|---:|---|
| deliberative_review | T01 | 1/1 | 1/1 | 0.7600 | unavailable | [0.76, 0.76] |
| deliberative_review | T02 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| deliberative_review | T03 | 1/1 | 1/1 | 0.6200 | unavailable | [0.62, 0.62] |
| deliberative_review | T04 | 1/1 | 1/1 | 0.5200 | unavailable | [0.52, 0.52] |
| deliberative_review | T05 | 1/1 | 1/1 | 0.7000 | unavailable | [0.7, 0.7] |
| deliberative_review | T06 | 1/1 | 1/1 | 0.5800 | unavailable | [0.58, 0.58] |
| deliberative_review | T07 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| deliberative_review | T08 | 1/1 | 1/1 | 0.7300 | unavailable | [0.73, 0.73] |
| deliberative_review | T09 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |
| deliberative_review | T10 | 1/1 | 1/1 | 0.7800 | unavailable | [0.78, 0.78] |
| deliberative_review | T11 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| deliberative_review | T12 | 1/1 | 1/1 | 0.7300 | unavailable | [0.73, 0.73] |
| deliberative_review | T13 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| deliberative_review | T14 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| deliberative_review | T15 | 1/1 | 1/1 | 0.7200 | unavailable | [0.72, 0.72] |
| deliberative_review | T16 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| deliberative_review | T17 | 0/1 | 0/1 | unavailable | unavailable | unavailable |
| deliberative_review | T18 | 1/1 | 1/1 | 0.6600 | unavailable | [0.66, 0.66] |
| deliberative_review | T19 | 1/1 | 1/1 | 0.5800 | unavailable | [0.58, 0.58] |
| deliberative_review | T20 | 1/1 | 1/1 | 0.6800 | unavailable | [0.68, 0.68] |

## deliberative_review

Completed papers are ordered by absolute score, then task ID; errors follow.

| Task | Status | Score | Rejected submissions | First submission verified | Evidence audit | Calls | Tokens (in/out) | USD | Seconds |
|---|---|---:|---:|---|---|---:|---|---:|---:|
| [deliberative_review-r1/T10: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](deliberative_review-r1/T10/README.md) | ok | 0.78 | 0 | yes | not audited | 7 | 53554/3092 | $0.008080 | 33.74 |
| [deliberative_review-r1/T01: ReAct: Synergizing Reasoning and Acting in Language Models](deliberative_review-r1/T01/README.md) | ok | 0.76 | 0 | yes | not audited | 7 | 53201/3100 | $0.008032 | 33.03 |
| [deliberative_review-r1/T08: $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](deliberative_review-r1/T08/README.md) | ok | 0.73 | 0 | yes | not audited | 7 | 53889/3072 | $0.008113 | 32.41 |
| [deliberative_review-r1/T12: InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback](deliberative_review-r1/T12/README.md) | ok | 0.73 | 0 | yes | not audited | 6 | 38421/1848 | $0.005574 | 21.60 |
| [deliberative_review-r1/T14: RULER: What's the Real Context Size of Your Long-Context Language Models?](deliberative_review-r1/T14/README.md) | ok | 0.72 | 0 | yes | not audited | 7 | 48108/2770 | $0.007232 | 31.34 |
| [deliberative_review-r1/T15: Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering](deliberative_review-r1/T15/README.md) | ok | 0.72 | 1 | no | not audited | 8 | 59011/4145 | $0.009261 | 44.03 |
| [deliberative_review-r1/T05: WebArena: A Realistic Web Environment for Building Autonomous Agents](deliberative_review-r1/T05/README.md) | ok | 0.7 | 0 | yes | not audited | 7 | 30748/2790 | $0.005087 | 30.36 |
| [deliberative_review-r1/T09: Agentless: Demystifying LLM-based Software Engineering Agents](deliberative_review-r1/T09/README.md) | ok | 0.68 | 0 | yes | not audited | 6 | 30963/2006 | $0.004717 | 21.69 |
| [deliberative_review-r1/T20: RAFT: Adapting Language Model to Domain Specific RAG](deliberative_review-r1/T20/README.md) | ok | 0.68 | 0 | yes | not audited | 7 | 50002/3267 | $0.007692 | 35.02 |
| [deliberative_review-r1/T18: Gorilla: Large Language Model Connected with Massive APIs](deliberative_review-r1/T18/README.md) | ok | 0.66 | 0 | yes | not audited | 7 | 42068/2961 | $0.006580 | 32.04 |
| [deliberative_review-r1/T03: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](deliberative_review-r1/T03/README.md) | ok | 0.62 | 0 | yes | not audited | 8 | 30661/3237 | $0.005318 | 34.15 |
| [deliberative_review-r1/T06: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](deliberative_review-r1/T06/README.md) | ok | 0.58 | 0 | yes | not audited | 7 | 16018/2689 | $0.003173 | 30.46 |
| [deliberative_review-r1/T19: A Survey on Large Language Model based Autonomous Agents](deliberative_review-r1/T19/README.md) | ok | 0.58 | 0 | yes | not audited | 6 | 28641/1594 | $0.004231 | 19.24 |
| [deliberative_review-r1/T04: AgentBench: Evaluating LLMs as Agents](deliberative_review-r1/T04/README.md) | ok | 0.52 | 0 | yes | not audited | 8 | 21805/2872 | $0.004019 | 31.79 |
| [deliberative_review-r1/T02: Reflexion: an autonomous agent with dynamic memory and self-reflection](deliberative_review-r1/T02/README.md) | error | — | 0 | unavailable | not audited | 8 | 44130/3321 | $0.007021 | 36.02 |
| [deliberative_review-r1/T07: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](deliberative_review-r1/T07/README.md) | error | — | 1 | yes | not audited | 8 | 31127/3136 | $0.005292 | 34.38 |
| [deliberative_review-r1/T11: Executable Code Actions Elicit Better LLM Agents](deliberative_review-r1/T11/README.md) | error | — | 0 | unavailable | not audited | 8 | 73631/2612 | $0.010342 | 29.92 |
| [deliberative_review-r1/T13: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](deliberative_review-r1/T13/README.md) | error | — | 0 | unavailable | not audited | 8 | 33303/2664 | $0.005309 | 32.39 |
| [deliberative_review-r1/T16: CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society](deliberative_review-r1/T16/README.md) | error | — | 0 | unavailable | not audited | 8 | 44826/2921 | $0.006915 | 32.06 |
| [deliberative_review-r1/T17: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](deliberative_review-r1/T17/README.md) | error | — | 2 | no | not audited | 8 | 26442/3376 | $0.004803 | 36.59 |

Per-task cost/time includes unsuccessful attempts; audit cost is separate.
