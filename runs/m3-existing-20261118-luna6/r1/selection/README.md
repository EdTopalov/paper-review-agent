# Evidence-assessment benchmark experiment

Model: `gpt-6-luna`. Split: `test`. 12 tasks per variant and 1 repetitions.

[Frozen plan](plan.json) · [Evaluated source](source.zip) · [Per-track quality scores](scores.json) · [Attempt records](records.jsonl)

Completion is a returned prediction, not a correctness score. Quality is reported separately for each track; evidence matching does not establish that the explanation is sound. Costs include failed attempts and retries.

| Variant | Completed / attempts | Calls / attempt | Input/output tokens / attempt | USD / attempt | Seconds / attempt |
|---|---:|---:|---:|---:|---:|
| agent | 12/12 | 16.08 | 73201.2/1126.2 | 0.002585 | 23.23 |
| pyagent_react | 12/12 | 16.08 | 81223.1/1703.0 | 0.002523 | 29.21 |
| baseline | 11/12 | 1.00 | 4018.7/574.5 | 0.000790 | 6.64 |

## Content by track

Repeat values show run variation before pooling. Failures remain in every denominator. The JSON report includes evidence F1, category slices, group intervals, and per-attempt costs.

| Track | Variant | Primary measure | Each repeat | Pooled |
|---|---|---|---|---:|
| selection | agent | Choice accuracy | r1: 0.750 | 0.750 |
| selection | pyagent_react | Choice accuracy | r1: 0.917 | 0.917 |
| selection | baseline | Choice accuracy | r1: 0.917 | 0.917 |

## Attempts

- [agent-r1/SB-18f34443b4ea](agent-r1/SB-18f34443b4ea/README.md): ok
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
- [baseline-r1/SB-4dd14ec2ecf0](baseline-r1/SB-4dd14ec2ecf0/README.md): error
- [baseline-r1/SB-66e931b708c9](baseline-r1/SB-66e931b708c9/README.md): ok
- [baseline-r1/SB-7402e4ad7d74](baseline-r1/SB-7402e4ad7d74/README.md): ok
- [baseline-r1/SB-80e0d3dc1ce0](baseline-r1/SB-80e0d3dc1ce0/README.md): ok
- [baseline-r1/SB-86910a1a2a2b](baseline-r1/SB-86910a1a2a2b/README.md): ok
- [baseline-r1/SB-a60c27fb6809](baseline-r1/SB-a60c27fb6809/README.md): ok
- [baseline-r1/SB-e9e07484ab89](baseline-r1/SB-e9e07484ab89/README.md): ok
- [baseline-r1/SB-f094fd9a487e](baseline-r1/SB-f094fd9a487e/README.md): ok
- [baseline-r1/SB-f8e22c0984b8](baseline-r1/SB-f8e22c0984b8/README.md): ok
- [baseline-r1/SB-fbf196ced965](baseline-r1/SB-fbf196ced965/README.md): ok
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
