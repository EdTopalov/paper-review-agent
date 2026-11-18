# Evidence-assessment benchmark experiment

Model: `gpt-6-luna`. Split: `test`. 12 tasks per variant and 1 repetitions.

[Frozen plan](plan.json) · [Evaluated source](source.zip) · [Per-track quality scores](scores.json) · [Attempt records](records.jsonl)

Completion is a returned prediction, not a correctness score. Quality is reported separately for each track; evidence matching does not establish that the explanation is sound. Costs include failed attempts and retries.

| Variant | Completed / attempts | Calls / attempt | Input/output tokens / attempt | USD / attempt | Seconds / attempt |
|---|---:|---:|---:|---:|---:|
| agent | 11/12 | 15.00 | 66523.7/1069.8 | 0.002051 | 20.84 |
| pyagent_react | 12/12 | 15.25 | 77492.4/1808.3 | 0.002324 | 31.35 |
| deliberative_review | 12/12 | 22.83 | 88096.4/3595.7 | 0.012498 | 51.83 |
| baseline | 12/12 | 1.00 | 4018.7/523.1 | 0.000302 | 6.63 |

## Content by track

Repeat values show run variation before pooling. Failures remain in every denominator. The JSON report includes evidence F1, category slices, group intervals, and per-attempt costs.

| Track | Variant | Primary measure | Each repeat | Pooled |
|---|---|---|---|---:|
| selection | agent | Choice accuracy | r1: 0.750 | 0.750 |
| selection | pyagent_react | Choice accuracy | r1: 0.917 | 0.917 |
| selection | deliberative_review | Choice accuracy | r1: 0.250 | 0.250 |
| selection | baseline | Choice accuracy | r1: 0.917 | 0.917 |

## Attempts

- [agent-r1/SB-18f34443b4ea](agent-r1/SB-18f34443b4ea/README.md): error
- [agent-r1/SB-3f2caf640d8b](agent-r1/SB-3f2caf640d8b/README.md): ok
- [agent-r1/SB-4dd14ec2ecf0](agent-r1/SB-4dd14ec2ecf0/README.md): ok
- [agent-r1/SB-66e931b708c9](agent-r1/SB-66e931b708c9/README.md): ok
- [agent-r1/SB-7402e4ad7d74](agent-r1/SB-7402e4ad7d74/README.md): ok
- [agent-r1/SB-80e0d3dc1ce0](agent-r1/SB-80e0d3dc1ce0/README.md): ok
- [agent-r1/SB-86910a1a2a2b](agent-r1/SB-86910a1a2a2b/README.md): ok
- [agent-r1/SB-a60c27fb6809](agent-r1/SB-a60c27fb6809/README.md): ok
- [agent-r1/SB-e9e07484ab89](agent-r1/SB-e9e07484ab89/README.md): ok
- [agent-r1/SB-f094fd9a487e](agent-r1/SB-f094fd9a487e/README.md): ok
- [agent-r1/SB-f8e22c0984b8](agent-r1/SB-f8e22c0984b8/README.md): ok
- [agent-r1/SB-fbf196ced965](agent-r1/SB-fbf196ced965/README.md): ok
- [baseline-r1/SB-18f34443b4ea](baseline-r1/SB-18f34443b4ea/README.md): ok
- [baseline-r1/SB-3f2caf640d8b](baseline-r1/SB-3f2caf640d8b/README.md): ok
- [baseline-r1/SB-4dd14ec2ecf0](baseline-r1/SB-4dd14ec2ecf0/README.md): ok
- [baseline-r1/SB-66e931b708c9](baseline-r1/SB-66e931b708c9/README.md): ok
- [baseline-r1/SB-7402e4ad7d74](baseline-r1/SB-7402e4ad7d74/README.md): ok
- [baseline-r1/SB-80e0d3dc1ce0](baseline-r1/SB-80e0d3dc1ce0/README.md): ok
- [baseline-r1/SB-86910a1a2a2b](baseline-r1/SB-86910a1a2a2b/README.md): ok
- [baseline-r1/SB-a60c27fb6809](baseline-r1/SB-a60c27fb6809/README.md): ok
- [baseline-r1/SB-e9e07484ab89](baseline-r1/SB-e9e07484ab89/README.md): ok
- [baseline-r1/SB-f094fd9a487e](baseline-r1/SB-f094fd9a487e/README.md): ok
- [baseline-r1/SB-f8e22c0984b8](baseline-r1/SB-f8e22c0984b8/README.md): ok
- [baseline-r1/SB-fbf196ced965](baseline-r1/SB-fbf196ced965/README.md): ok
- [deliberative_review-r1/SB-18f34443b4ea](deliberative_review-r1/SB-18f34443b4ea/README.md): ok
- [deliberative_review-r1/SB-3f2caf640d8b](deliberative_review-r1/SB-3f2caf640d8b/README.md): ok
- [deliberative_review-r1/SB-4dd14ec2ecf0](deliberative_review-r1/SB-4dd14ec2ecf0/README.md): ok
- [deliberative_review-r1/SB-66e931b708c9](deliberative_review-r1/SB-66e931b708c9/README.md): ok
- [deliberative_review-r1/SB-7402e4ad7d74](deliberative_review-r1/SB-7402e4ad7d74/README.md): ok
- [deliberative_review-r1/SB-80e0d3dc1ce0](deliberative_review-r1/SB-80e0d3dc1ce0/README.md): ok
- [deliberative_review-r1/SB-86910a1a2a2b](deliberative_review-r1/SB-86910a1a2a2b/README.md): ok
- [deliberative_review-r1/SB-a60c27fb6809](deliberative_review-r1/SB-a60c27fb6809/README.md): ok
- [deliberative_review-r1/SB-e9e07484ab89](deliberative_review-r1/SB-e9e07484ab89/README.md): ok
- [deliberative_review-r1/SB-f094fd9a487e](deliberative_review-r1/SB-f094fd9a487e/README.md): ok
- [deliberative_review-r1/SB-f8e22c0984b8](deliberative_review-r1/SB-f8e22c0984b8/README.md): ok
- [deliberative_review-r1/SB-fbf196ced965](deliberative_review-r1/SB-fbf196ced965/README.md): ok
- [pyagent_react-r1/SB-18f34443b4ea](pyagent_react-r1/SB-18f34443b4ea/README.md): ok
- [pyagent_react-r1/SB-3f2caf640d8b](pyagent_react-r1/SB-3f2caf640d8b/README.md): ok
- [pyagent_react-r1/SB-4dd14ec2ecf0](pyagent_react-r1/SB-4dd14ec2ecf0/README.md): ok
- [pyagent_react-r1/SB-66e931b708c9](pyagent_react-r1/SB-66e931b708c9/README.md): ok
- [pyagent_react-r1/SB-7402e4ad7d74](pyagent_react-r1/SB-7402e4ad7d74/README.md): ok
- [pyagent_react-r1/SB-80e0d3dc1ce0](pyagent_react-r1/SB-80e0d3dc1ce0/README.md): ok
- [pyagent_react-r1/SB-86910a1a2a2b](pyagent_react-r1/SB-86910a1a2a2b/README.md): ok
- [pyagent_react-r1/SB-a60c27fb6809](pyagent_react-r1/SB-a60c27fb6809/README.md): ok
- [pyagent_react-r1/SB-e9e07484ab89](pyagent_react-r1/SB-e9e07484ab89/README.md): ok
- [pyagent_react-r1/SB-f094fd9a487e](pyagent_react-r1/SB-f094fd9a487e/README.md): ok
- [pyagent_react-r1/SB-f8e22c0984b8](pyagent_react-r1/SB-f8e22c0984b8/README.md): ok
- [pyagent_react-r1/SB-fbf196ced965](pyagent_react-r1/SB-fbf196ced965/README.md): ok
