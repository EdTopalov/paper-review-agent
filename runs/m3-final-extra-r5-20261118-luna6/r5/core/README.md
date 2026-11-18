# Evidence-assessment benchmark experiment

Model: `gpt-6-luna`. Split: `test`. 64 tasks per variant and 1 repetitions.

[Frozen plan](plan.json) · [Evaluated source](source.zip) · [Per-track quality scores](scores.json) · [Attempt records](records.jsonl)

Completion is a returned prediction, not a correctness score. Quality is reported separately for each track; evidence matching does not establish that the explanation is sound. Costs include failed attempts and retries.

| Variant | Completed / attempts | Calls / attempt | Input/output tokens / attempt | USD / attempt | Seconds / attempt |
|---|---:|---:|---:|---:|---:|
| agent | 53/64 | 4.08 | 10434.2/310.6 | 0.000558 | 6.87 |
| pyagent_react | 64/64 | 4.36 | 15401.2/1087.7 | 0.000983 | 14.39 |
| deliberative_review | 64/64 | 7.80 | 23062.8/1883.0 | 0.003670 | 23.93 |
| baseline | 64/64 | 1.00 | 6720.7/203.2 | 0.000186 | 3.36 |

## Content by track

Repeat values show run variation before pooling. Failures remain in every denominator. The JSON report includes evidence F1, category slices, group intervals, and per-attempt costs.

| Track | Variant | Primary measure | Each repeat | Pooled |
|---|---|---|---|---:|
| controlled | agent | Verdict accuracy | r1: 0.917 | 0.917 |
| controlled | pyagent_react | Verdict accuracy | r1: 0.833 | 0.833 |
| controlled | deliberative_review | Verdict accuracy | r1: 0.958 | 0.958 |
| controlled | baseline | Verdict accuracy | r1: 1.000 | 1.000 |
| qasper | agent | Answer F1 | r1: 0.339 | 0.339 |
| qasper | pyagent_react | Answer F1 | r1: 0.371 | 0.371 |
| qasper | deliberative_review | Answer F1 | r1: 0.359 | 0.359 |
| qasper | baseline | Answer F1 | r1: 0.418 | 0.418 |
| reviewcritique | agent | Binary macro-F1 | r1: 0.470 | 0.470 |
| reviewcritique | pyagent_react | Binary macro-F1 | r1: 0.688 | 0.688 |
| reviewcritique | deliberative_review | Binary macro-F1 | r1: 0.405 | 0.405 |
| reviewcritique | baseline | Binary macro-F1 | r1: 0.670 | 0.670 |

## Attempts

- [agent-r1/CB-12d6c0559e77](agent-r1/CB-12d6c0559e77/README.md): ok
- [agent-r1/CB-20fe26ed8a63](agent-r1/CB-20fe26ed8a63/README.md): ok
- [agent-r1/CB-25cf58af89f2](agent-r1/CB-25cf58af89f2/README.md): ok
- [agent-r1/CB-40388578e13d](agent-r1/CB-40388578e13d/README.md): ok
- [agent-r1/CB-449d322624b5](agent-r1/CB-449d322624b5/README.md): error
- [agent-r1/CB-527f16549e56](agent-r1/CB-527f16549e56/README.md): ok
- [agent-r1/CB-54f05a314634](agent-r1/CB-54f05a314634/README.md): ok
- [agent-r1/CB-5501cd8dd300](agent-r1/CB-5501cd8dd300/README.md): ok
- [agent-r1/CB-6d1256f826e3](agent-r1/CB-6d1256f826e3/README.md): ok
- [agent-r1/CB-72101445106e](agent-r1/CB-72101445106e/README.md): ok
- [agent-r1/CB-74e44d72cfb9](agent-r1/CB-74e44d72cfb9/README.md): ok
- [agent-r1/CB-7ad89dbcdedc](agent-r1/CB-7ad89dbcdedc/README.md): ok
- [agent-r1/CB-80bd654cbc97](agent-r1/CB-80bd654cbc97/README.md): ok
- [agent-r1/CB-8fe165c89164](agent-r1/CB-8fe165c89164/README.md): ok
- [agent-r1/CB-9445ca674aeb](agent-r1/CB-9445ca674aeb/README.md): ok
- [agent-r1/CB-b36c4ba21009](agent-r1/CB-b36c4ba21009/README.md): ok
- [agent-r1/CB-bc5465d35ac1](agent-r1/CB-bc5465d35ac1/README.md): ok
- [agent-r1/CB-bd50b5c34b5a](agent-r1/CB-bd50b5c34b5a/README.md): ok
- [agent-r1/CB-c1f1e166dec3](agent-r1/CB-c1f1e166dec3/README.md): ok
- [agent-r1/CB-cedf9028d20e](agent-r1/CB-cedf9028d20e/README.md): ok
- [agent-r1/CB-d08f00314b8d](agent-r1/CB-d08f00314b8d/README.md): ok
- [agent-r1/CB-d2c80b428f6e](agent-r1/CB-d2c80b428f6e/README.md): ok
- [agent-r1/CB-e758c8885528](agent-r1/CB-e758c8885528/README.md): ok
- [agent-r1/CB-fba8e76583d6](agent-r1/CB-fba8e76583d6/README.md): ok
- [agent-r1/QASPER-01209a3bead7](agent-r1/QASPER-01209a3bead7/README.md): ok
- [agent-r1/QASPER-0c234db3b380](agent-r1/QASPER-0c234db3b380/README.md): ok
- [agent-r1/QASPER-220d11a03897](agent-r1/QASPER-220d11a03897/README.md): ok
- [agent-r1/QASPER-25c1c4a91f5d](agent-r1/QASPER-25c1c4a91f5d/README.md): ok
- [agent-r1/QASPER-2e37e681942e](agent-r1/QASPER-2e37e681942e/README.md): ok
- [agent-r1/QASPER-4e748cb2b5e7](agent-r1/QASPER-4e748cb2b5e7/README.md): ok
- [agent-r1/QASPER-6c96e910bd98](agent-r1/QASPER-6c96e910bd98/README.md): error
- [agent-r1/QASPER-7bd6a6ec230e](agent-r1/QASPER-7bd6a6ec230e/README.md): ok
- [agent-r1/QASPER-893ec40b678a](agent-r1/QASPER-893ec40b678a/README.md): error
- [agent-r1/QASPER-8db6f8714bda](agent-r1/QASPER-8db6f8714bda/README.md): ok
- [agent-r1/QASPER-8dc707a0daf7](agent-r1/QASPER-8dc707a0daf7/README.md): ok
- [agent-r1/QASPER-8eefa116e3c3](agent-r1/QASPER-8eefa116e3c3/README.md): ok
- [agent-r1/QASPER-ababb79dd3c3](agent-r1/QASPER-ababb79dd3c3/README.md): ok
- [agent-r1/QASPER-b21bc0919369](agent-r1/QASPER-b21bc0919369/README.md): ok
- [agent-r1/QASPER-b591853e9389](agent-r1/QASPER-b591853e9389/README.md): ok
- [agent-r1/QASPER-b970f48d3077](agent-r1/QASPER-b970f48d3077/README.md): ok
- [agent-r1/QASPER-b9ea841b817b](agent-r1/QASPER-b9ea841b817b/README.md): ok
- [agent-r1/QASPER-ba539cab80d2](agent-r1/QASPER-ba539cab80d2/README.md): ok
- [agent-r1/QASPER-c59802881506](agent-r1/QASPER-c59802881506/README.md): ok
- [agent-r1/QASPER-dfca00be3284](agent-r1/QASPER-dfca00be3284/README.md): ok
- [agent-r1/RC-16a23f11844e](agent-r1/RC-16a23f11844e/README.md): ok
- [agent-r1/RC-17ae89b7e529](agent-r1/RC-17ae89b7e529/README.md): ok
- [agent-r1/RC-196c24d86b88](agent-r1/RC-196c24d86b88/README.md): ok
- [agent-r1/RC-19e4af168032](agent-r1/RC-19e4af168032/README.md): ok
- [agent-r1/RC-1d03f02eb4d7](agent-r1/RC-1d03f02eb4d7/README.md): ok
- [agent-r1/RC-2518e6de7eb6](agent-r1/RC-2518e6de7eb6/README.md): ok
- [agent-r1/RC-357185295521](agent-r1/RC-357185295521/README.md): ok
- [agent-r1/RC-39282147886f](agent-r1/RC-39282147886f/README.md): error
- [agent-r1/RC-59408ce4ca25](agent-r1/RC-59408ce4ca25/README.md): error
- [agent-r1/RC-599e8dc3a69c](agent-r1/RC-599e8dc3a69c/README.md): ok
- [agent-r1/RC-81274ac167fc](agent-r1/RC-81274ac167fc/README.md): error
- [agent-r1/RC-88f98dcc0dee](agent-r1/RC-88f98dcc0dee/README.md): error
- [agent-r1/RC-97b4064e1659](agent-r1/RC-97b4064e1659/README.md): ok
- [agent-r1/RC-9813f9c2cf5d](agent-r1/RC-9813f9c2cf5d/README.md): error
- [agent-r1/RC-ae631d292d42](agent-r1/RC-ae631d292d42/README.md): error
- [agent-r1/RC-cc398745c3c8](agent-r1/RC-cc398745c3c8/README.md): error
- [agent-r1/RC-d574e4d2099d](agent-r1/RC-d574e4d2099d/README.md): ok
- [agent-r1/RC-f0e2b1a1f91a](agent-r1/RC-f0e2b1a1f91a/README.md): error
- [agent-r1/RC-f5097b168055](agent-r1/RC-f5097b168055/README.md): ok
- [agent-r1/RC-f94db276afa4](agent-r1/RC-f94db276afa4/README.md): ok
- [baseline-r1/CB-12d6c0559e77](baseline-r1/CB-12d6c0559e77/README.md): ok
- [baseline-r1/CB-20fe26ed8a63](baseline-r1/CB-20fe26ed8a63/README.md): ok
- [baseline-r1/CB-25cf58af89f2](baseline-r1/CB-25cf58af89f2/README.md): ok
- [baseline-r1/CB-40388578e13d](baseline-r1/CB-40388578e13d/README.md): ok
- [baseline-r1/CB-449d322624b5](baseline-r1/CB-449d322624b5/README.md): ok
- [baseline-r1/CB-527f16549e56](baseline-r1/CB-527f16549e56/README.md): ok
- [baseline-r1/CB-54f05a314634](baseline-r1/CB-54f05a314634/README.md): ok
- [baseline-r1/CB-5501cd8dd300](baseline-r1/CB-5501cd8dd300/README.md): ok
- [baseline-r1/CB-6d1256f826e3](baseline-r1/CB-6d1256f826e3/README.md): ok
- [baseline-r1/CB-72101445106e](baseline-r1/CB-72101445106e/README.md): ok
- [baseline-r1/CB-74e44d72cfb9](baseline-r1/CB-74e44d72cfb9/README.md): ok
- [baseline-r1/CB-7ad89dbcdedc](baseline-r1/CB-7ad89dbcdedc/README.md): ok
- [baseline-r1/CB-80bd654cbc97](baseline-r1/CB-80bd654cbc97/README.md): ok
- [baseline-r1/CB-8fe165c89164](baseline-r1/CB-8fe165c89164/README.md): ok
- [baseline-r1/CB-9445ca674aeb](baseline-r1/CB-9445ca674aeb/README.md): ok
- [baseline-r1/CB-b36c4ba21009](baseline-r1/CB-b36c4ba21009/README.md): ok
- [baseline-r1/CB-bc5465d35ac1](baseline-r1/CB-bc5465d35ac1/README.md): ok
- [baseline-r1/CB-bd50b5c34b5a](baseline-r1/CB-bd50b5c34b5a/README.md): ok
- [baseline-r1/CB-c1f1e166dec3](baseline-r1/CB-c1f1e166dec3/README.md): ok
- [baseline-r1/CB-cedf9028d20e](baseline-r1/CB-cedf9028d20e/README.md): ok
- [baseline-r1/CB-d08f00314b8d](baseline-r1/CB-d08f00314b8d/README.md): ok
- [baseline-r1/CB-d2c80b428f6e](baseline-r1/CB-d2c80b428f6e/README.md): ok
- [baseline-r1/CB-e758c8885528](baseline-r1/CB-e758c8885528/README.md): ok
- [baseline-r1/CB-fba8e76583d6](baseline-r1/CB-fba8e76583d6/README.md): ok
- [baseline-r1/QASPER-01209a3bead7](baseline-r1/QASPER-01209a3bead7/README.md): ok
- [baseline-r1/QASPER-0c234db3b380](baseline-r1/QASPER-0c234db3b380/README.md): ok
- [baseline-r1/QASPER-220d11a03897](baseline-r1/QASPER-220d11a03897/README.md): ok
- [baseline-r1/QASPER-25c1c4a91f5d](baseline-r1/QASPER-25c1c4a91f5d/README.md): ok
- [baseline-r1/QASPER-2e37e681942e](baseline-r1/QASPER-2e37e681942e/README.md): ok
- [baseline-r1/QASPER-4e748cb2b5e7](baseline-r1/QASPER-4e748cb2b5e7/README.md): ok
- [baseline-r1/QASPER-6c96e910bd98](baseline-r1/QASPER-6c96e910bd98/README.md): ok
- [baseline-r1/QASPER-7bd6a6ec230e](baseline-r1/QASPER-7bd6a6ec230e/README.md): ok
- [baseline-r1/QASPER-893ec40b678a](baseline-r1/QASPER-893ec40b678a/README.md): ok
- [baseline-r1/QASPER-8db6f8714bda](baseline-r1/QASPER-8db6f8714bda/README.md): ok
- [baseline-r1/QASPER-8dc707a0daf7](baseline-r1/QASPER-8dc707a0daf7/README.md): ok
- [baseline-r1/QASPER-8eefa116e3c3](baseline-r1/QASPER-8eefa116e3c3/README.md): ok
- [baseline-r1/QASPER-ababb79dd3c3](baseline-r1/QASPER-ababb79dd3c3/README.md): ok
- [baseline-r1/QASPER-b21bc0919369](baseline-r1/QASPER-b21bc0919369/README.md): ok
- [baseline-r1/QASPER-b591853e9389](baseline-r1/QASPER-b591853e9389/README.md): ok
- [baseline-r1/QASPER-b970f48d3077](baseline-r1/QASPER-b970f48d3077/README.md): ok
- [baseline-r1/QASPER-b9ea841b817b](baseline-r1/QASPER-b9ea841b817b/README.md): ok
- [baseline-r1/QASPER-ba539cab80d2](baseline-r1/QASPER-ba539cab80d2/README.md): ok
- [baseline-r1/QASPER-c59802881506](baseline-r1/QASPER-c59802881506/README.md): ok
- [baseline-r1/QASPER-dfca00be3284](baseline-r1/QASPER-dfca00be3284/README.md): ok
- [baseline-r1/RC-16a23f11844e](baseline-r1/RC-16a23f11844e/README.md): ok
- [baseline-r1/RC-17ae89b7e529](baseline-r1/RC-17ae89b7e529/README.md): ok
- [baseline-r1/RC-196c24d86b88](baseline-r1/RC-196c24d86b88/README.md): ok
- [baseline-r1/RC-19e4af168032](baseline-r1/RC-19e4af168032/README.md): ok
- [baseline-r1/RC-1d03f02eb4d7](baseline-r1/RC-1d03f02eb4d7/README.md): ok
- [baseline-r1/RC-2518e6de7eb6](baseline-r1/RC-2518e6de7eb6/README.md): ok
- [baseline-r1/RC-357185295521](baseline-r1/RC-357185295521/README.md): ok
- [baseline-r1/RC-39282147886f](baseline-r1/RC-39282147886f/README.md): ok
- [baseline-r1/RC-59408ce4ca25](baseline-r1/RC-59408ce4ca25/README.md): ok
- [baseline-r1/RC-599e8dc3a69c](baseline-r1/RC-599e8dc3a69c/README.md): ok
- [baseline-r1/RC-81274ac167fc](baseline-r1/RC-81274ac167fc/README.md): ok
- [baseline-r1/RC-88f98dcc0dee](baseline-r1/RC-88f98dcc0dee/README.md): ok
- [baseline-r1/RC-97b4064e1659](baseline-r1/RC-97b4064e1659/README.md): ok
- [baseline-r1/RC-9813f9c2cf5d](baseline-r1/RC-9813f9c2cf5d/README.md): ok
- [baseline-r1/RC-ae631d292d42](baseline-r1/RC-ae631d292d42/README.md): ok
- [baseline-r1/RC-cc398745c3c8](baseline-r1/RC-cc398745c3c8/README.md): ok
- [baseline-r1/RC-d574e4d2099d](baseline-r1/RC-d574e4d2099d/README.md): ok
- [baseline-r1/RC-f0e2b1a1f91a](baseline-r1/RC-f0e2b1a1f91a/README.md): ok
- [baseline-r1/RC-f5097b168055](baseline-r1/RC-f5097b168055/README.md): ok
- [baseline-r1/RC-f94db276afa4](baseline-r1/RC-f94db276afa4/README.md): ok
- [deliberative_review-r1/CB-12d6c0559e77](deliberative_review-r1/CB-12d6c0559e77/README.md): ok
- [deliberative_review-r1/CB-20fe26ed8a63](deliberative_review-r1/CB-20fe26ed8a63/README.md): ok
- [deliberative_review-r1/CB-25cf58af89f2](deliberative_review-r1/CB-25cf58af89f2/README.md): ok
- [deliberative_review-r1/CB-40388578e13d](deliberative_review-r1/CB-40388578e13d/README.md): ok
- [deliberative_review-r1/CB-449d322624b5](deliberative_review-r1/CB-449d322624b5/README.md): ok
- [deliberative_review-r1/CB-527f16549e56](deliberative_review-r1/CB-527f16549e56/README.md): ok
- [deliberative_review-r1/CB-54f05a314634](deliberative_review-r1/CB-54f05a314634/README.md): ok
- [deliberative_review-r1/CB-5501cd8dd300](deliberative_review-r1/CB-5501cd8dd300/README.md): ok
- [deliberative_review-r1/CB-6d1256f826e3](deliberative_review-r1/CB-6d1256f826e3/README.md): ok
- [deliberative_review-r1/CB-72101445106e](deliberative_review-r1/CB-72101445106e/README.md): ok
- [deliberative_review-r1/CB-74e44d72cfb9](deliberative_review-r1/CB-74e44d72cfb9/README.md): ok
- [deliberative_review-r1/CB-7ad89dbcdedc](deliberative_review-r1/CB-7ad89dbcdedc/README.md): ok
- [deliberative_review-r1/CB-80bd654cbc97](deliberative_review-r1/CB-80bd654cbc97/README.md): ok
- [deliberative_review-r1/CB-8fe165c89164](deliberative_review-r1/CB-8fe165c89164/README.md): ok
- [deliberative_review-r1/CB-9445ca674aeb](deliberative_review-r1/CB-9445ca674aeb/README.md): ok
- [deliberative_review-r1/CB-b36c4ba21009](deliberative_review-r1/CB-b36c4ba21009/README.md): ok
- [deliberative_review-r1/CB-bc5465d35ac1](deliberative_review-r1/CB-bc5465d35ac1/README.md): ok
- [deliberative_review-r1/CB-bd50b5c34b5a](deliberative_review-r1/CB-bd50b5c34b5a/README.md): ok
- [deliberative_review-r1/CB-c1f1e166dec3](deliberative_review-r1/CB-c1f1e166dec3/README.md): ok
- [deliberative_review-r1/CB-cedf9028d20e](deliberative_review-r1/CB-cedf9028d20e/README.md): ok
- [deliberative_review-r1/CB-d08f00314b8d](deliberative_review-r1/CB-d08f00314b8d/README.md): ok
- [deliberative_review-r1/CB-d2c80b428f6e](deliberative_review-r1/CB-d2c80b428f6e/README.md): ok
- [deliberative_review-r1/CB-e758c8885528](deliberative_review-r1/CB-e758c8885528/README.md): ok
- [deliberative_review-r1/CB-fba8e76583d6](deliberative_review-r1/CB-fba8e76583d6/README.md): ok
- [deliberative_review-r1/QASPER-01209a3bead7](deliberative_review-r1/QASPER-01209a3bead7/README.md): ok
- [deliberative_review-r1/QASPER-0c234db3b380](deliberative_review-r1/QASPER-0c234db3b380/README.md): ok
- [deliberative_review-r1/QASPER-220d11a03897](deliberative_review-r1/QASPER-220d11a03897/README.md): ok
- [deliberative_review-r1/QASPER-25c1c4a91f5d](deliberative_review-r1/QASPER-25c1c4a91f5d/README.md): ok
- [deliberative_review-r1/QASPER-2e37e681942e](deliberative_review-r1/QASPER-2e37e681942e/README.md): ok
- [deliberative_review-r1/QASPER-4e748cb2b5e7](deliberative_review-r1/QASPER-4e748cb2b5e7/README.md): ok
- [deliberative_review-r1/QASPER-6c96e910bd98](deliberative_review-r1/QASPER-6c96e910bd98/README.md): ok
- [deliberative_review-r1/QASPER-7bd6a6ec230e](deliberative_review-r1/QASPER-7bd6a6ec230e/README.md): ok
- [deliberative_review-r1/QASPER-893ec40b678a](deliberative_review-r1/QASPER-893ec40b678a/README.md): ok
- [deliberative_review-r1/QASPER-8db6f8714bda](deliberative_review-r1/QASPER-8db6f8714bda/README.md): ok
- [deliberative_review-r1/QASPER-8dc707a0daf7](deliberative_review-r1/QASPER-8dc707a0daf7/README.md): ok
- [deliberative_review-r1/QASPER-8eefa116e3c3](deliberative_review-r1/QASPER-8eefa116e3c3/README.md): ok
- [deliberative_review-r1/QASPER-ababb79dd3c3](deliberative_review-r1/QASPER-ababb79dd3c3/README.md): ok
- [deliberative_review-r1/QASPER-b21bc0919369](deliberative_review-r1/QASPER-b21bc0919369/README.md): ok
- [deliberative_review-r1/QASPER-b591853e9389](deliberative_review-r1/QASPER-b591853e9389/README.md): ok
- [deliberative_review-r1/QASPER-b970f48d3077](deliberative_review-r1/QASPER-b970f48d3077/README.md): ok
- [deliberative_review-r1/QASPER-b9ea841b817b](deliberative_review-r1/QASPER-b9ea841b817b/README.md): ok
- [deliberative_review-r1/QASPER-ba539cab80d2](deliberative_review-r1/QASPER-ba539cab80d2/README.md): ok
- [deliberative_review-r1/QASPER-c59802881506](deliberative_review-r1/QASPER-c59802881506/README.md): ok
- [deliberative_review-r1/QASPER-dfca00be3284](deliberative_review-r1/QASPER-dfca00be3284/README.md): ok
- [deliberative_review-r1/RC-16a23f11844e](deliberative_review-r1/RC-16a23f11844e/README.md): ok
- [deliberative_review-r1/RC-17ae89b7e529](deliberative_review-r1/RC-17ae89b7e529/README.md): ok
- [deliberative_review-r1/RC-196c24d86b88](deliberative_review-r1/RC-196c24d86b88/README.md): ok
- [deliberative_review-r1/RC-19e4af168032](deliberative_review-r1/RC-19e4af168032/README.md): ok
- [deliberative_review-r1/RC-1d03f02eb4d7](deliberative_review-r1/RC-1d03f02eb4d7/README.md): ok
- [deliberative_review-r1/RC-2518e6de7eb6](deliberative_review-r1/RC-2518e6de7eb6/README.md): ok
- [deliberative_review-r1/RC-357185295521](deliberative_review-r1/RC-357185295521/README.md): ok
- [deliberative_review-r1/RC-39282147886f](deliberative_review-r1/RC-39282147886f/README.md): ok
- [deliberative_review-r1/RC-59408ce4ca25](deliberative_review-r1/RC-59408ce4ca25/README.md): ok
- [deliberative_review-r1/RC-599e8dc3a69c](deliberative_review-r1/RC-599e8dc3a69c/README.md): ok
- [deliberative_review-r1/RC-81274ac167fc](deliberative_review-r1/RC-81274ac167fc/README.md): ok
- [deliberative_review-r1/RC-88f98dcc0dee](deliberative_review-r1/RC-88f98dcc0dee/README.md): ok
- [deliberative_review-r1/RC-97b4064e1659](deliberative_review-r1/RC-97b4064e1659/README.md): ok
- [deliberative_review-r1/RC-9813f9c2cf5d](deliberative_review-r1/RC-9813f9c2cf5d/README.md): ok
- [deliberative_review-r1/RC-ae631d292d42](deliberative_review-r1/RC-ae631d292d42/README.md): ok
- [deliberative_review-r1/RC-cc398745c3c8](deliberative_review-r1/RC-cc398745c3c8/README.md): ok
- [deliberative_review-r1/RC-d574e4d2099d](deliberative_review-r1/RC-d574e4d2099d/README.md): ok
- [deliberative_review-r1/RC-f0e2b1a1f91a](deliberative_review-r1/RC-f0e2b1a1f91a/README.md): ok
- [deliberative_review-r1/RC-f5097b168055](deliberative_review-r1/RC-f5097b168055/README.md): ok
- [deliberative_review-r1/RC-f94db276afa4](deliberative_review-r1/RC-f94db276afa4/README.md): ok
- [pyagent_react-r1/CB-12d6c0559e77](pyagent_react-r1/CB-12d6c0559e77/README.md): ok
- [pyagent_react-r1/CB-20fe26ed8a63](pyagent_react-r1/CB-20fe26ed8a63/README.md): ok
- [pyagent_react-r1/CB-25cf58af89f2](pyagent_react-r1/CB-25cf58af89f2/README.md): ok
- [pyagent_react-r1/CB-40388578e13d](pyagent_react-r1/CB-40388578e13d/README.md): ok
- [pyagent_react-r1/CB-449d322624b5](pyagent_react-r1/CB-449d322624b5/README.md): ok
- [pyagent_react-r1/CB-527f16549e56](pyagent_react-r1/CB-527f16549e56/README.md): ok
- [pyagent_react-r1/CB-54f05a314634](pyagent_react-r1/CB-54f05a314634/README.md): ok
- [pyagent_react-r1/CB-5501cd8dd300](pyagent_react-r1/CB-5501cd8dd300/README.md): ok
- [pyagent_react-r1/CB-6d1256f826e3](pyagent_react-r1/CB-6d1256f826e3/README.md): ok
- [pyagent_react-r1/CB-72101445106e](pyagent_react-r1/CB-72101445106e/README.md): ok
- [pyagent_react-r1/CB-74e44d72cfb9](pyagent_react-r1/CB-74e44d72cfb9/README.md): ok
- [pyagent_react-r1/CB-7ad89dbcdedc](pyagent_react-r1/CB-7ad89dbcdedc/README.md): ok
- [pyagent_react-r1/CB-80bd654cbc97](pyagent_react-r1/CB-80bd654cbc97/README.md): ok
- [pyagent_react-r1/CB-8fe165c89164](pyagent_react-r1/CB-8fe165c89164/README.md): ok
- [pyagent_react-r1/CB-9445ca674aeb](pyagent_react-r1/CB-9445ca674aeb/README.md): ok
- [pyagent_react-r1/CB-b36c4ba21009](pyagent_react-r1/CB-b36c4ba21009/README.md): ok
- [pyagent_react-r1/CB-bc5465d35ac1](pyagent_react-r1/CB-bc5465d35ac1/README.md): ok
- [pyagent_react-r1/CB-bd50b5c34b5a](pyagent_react-r1/CB-bd50b5c34b5a/README.md): ok
- [pyagent_react-r1/CB-c1f1e166dec3](pyagent_react-r1/CB-c1f1e166dec3/README.md): ok
- [pyagent_react-r1/CB-cedf9028d20e](pyagent_react-r1/CB-cedf9028d20e/README.md): ok
- [pyagent_react-r1/CB-d08f00314b8d](pyagent_react-r1/CB-d08f00314b8d/README.md): ok
- [pyagent_react-r1/CB-d2c80b428f6e](pyagent_react-r1/CB-d2c80b428f6e/README.md): ok
- [pyagent_react-r1/CB-e758c8885528](pyagent_react-r1/CB-e758c8885528/README.md): ok
- [pyagent_react-r1/CB-fba8e76583d6](pyagent_react-r1/CB-fba8e76583d6/README.md): ok
- [pyagent_react-r1/QASPER-01209a3bead7](pyagent_react-r1/QASPER-01209a3bead7/README.md): ok
- [pyagent_react-r1/QASPER-0c234db3b380](pyagent_react-r1/QASPER-0c234db3b380/README.md): ok
- [pyagent_react-r1/QASPER-220d11a03897](pyagent_react-r1/QASPER-220d11a03897/README.md): ok
- [pyagent_react-r1/QASPER-25c1c4a91f5d](pyagent_react-r1/QASPER-25c1c4a91f5d/README.md): ok
- [pyagent_react-r1/QASPER-2e37e681942e](pyagent_react-r1/QASPER-2e37e681942e/README.md): ok
- [pyagent_react-r1/QASPER-4e748cb2b5e7](pyagent_react-r1/QASPER-4e748cb2b5e7/README.md): ok
- [pyagent_react-r1/QASPER-6c96e910bd98](pyagent_react-r1/QASPER-6c96e910bd98/README.md): ok
- [pyagent_react-r1/QASPER-7bd6a6ec230e](pyagent_react-r1/QASPER-7bd6a6ec230e/README.md): ok
- [pyagent_react-r1/QASPER-893ec40b678a](pyagent_react-r1/QASPER-893ec40b678a/README.md): ok
- [pyagent_react-r1/QASPER-8db6f8714bda](pyagent_react-r1/QASPER-8db6f8714bda/README.md): ok
- [pyagent_react-r1/QASPER-8dc707a0daf7](pyagent_react-r1/QASPER-8dc707a0daf7/README.md): ok
- [pyagent_react-r1/QASPER-8eefa116e3c3](pyagent_react-r1/QASPER-8eefa116e3c3/README.md): ok
- [pyagent_react-r1/QASPER-ababb79dd3c3](pyagent_react-r1/QASPER-ababb79dd3c3/README.md): ok
- [pyagent_react-r1/QASPER-b21bc0919369](pyagent_react-r1/QASPER-b21bc0919369/README.md): ok
- [pyagent_react-r1/QASPER-b591853e9389](pyagent_react-r1/QASPER-b591853e9389/README.md): ok
- [pyagent_react-r1/QASPER-b970f48d3077](pyagent_react-r1/QASPER-b970f48d3077/README.md): ok
- [pyagent_react-r1/QASPER-b9ea841b817b](pyagent_react-r1/QASPER-b9ea841b817b/README.md): ok
- [pyagent_react-r1/QASPER-ba539cab80d2](pyagent_react-r1/QASPER-ba539cab80d2/README.md): ok
- [pyagent_react-r1/QASPER-c59802881506](pyagent_react-r1/QASPER-c59802881506/README.md): ok
- [pyagent_react-r1/QASPER-dfca00be3284](pyagent_react-r1/QASPER-dfca00be3284/README.md): ok
- [pyagent_react-r1/RC-16a23f11844e](pyagent_react-r1/RC-16a23f11844e/README.md): ok
- [pyagent_react-r1/RC-17ae89b7e529](pyagent_react-r1/RC-17ae89b7e529/README.md): ok
- [pyagent_react-r1/RC-196c24d86b88](pyagent_react-r1/RC-196c24d86b88/README.md): ok
- [pyagent_react-r1/RC-19e4af168032](pyagent_react-r1/RC-19e4af168032/README.md): ok
- [pyagent_react-r1/RC-1d03f02eb4d7](pyagent_react-r1/RC-1d03f02eb4d7/README.md): ok
- [pyagent_react-r1/RC-2518e6de7eb6](pyagent_react-r1/RC-2518e6de7eb6/README.md): ok
- [pyagent_react-r1/RC-357185295521](pyagent_react-r1/RC-357185295521/README.md): ok
- [pyagent_react-r1/RC-39282147886f](pyagent_react-r1/RC-39282147886f/README.md): ok
- [pyagent_react-r1/RC-59408ce4ca25](pyagent_react-r1/RC-59408ce4ca25/README.md): ok
- [pyagent_react-r1/RC-599e8dc3a69c](pyagent_react-r1/RC-599e8dc3a69c/README.md): ok
- [pyagent_react-r1/RC-81274ac167fc](pyagent_react-r1/RC-81274ac167fc/README.md): ok
- [pyagent_react-r1/RC-88f98dcc0dee](pyagent_react-r1/RC-88f98dcc0dee/README.md): ok
- [pyagent_react-r1/RC-97b4064e1659](pyagent_react-r1/RC-97b4064e1659/README.md): ok
- [pyagent_react-r1/RC-9813f9c2cf5d](pyagent_react-r1/RC-9813f9c2cf5d/README.md): ok
- [pyagent_react-r1/RC-ae631d292d42](pyagent_react-r1/RC-ae631d292d42/README.md): ok
- [pyagent_react-r1/RC-cc398745c3c8](pyagent_react-r1/RC-cc398745c3c8/README.md): ok
- [pyagent_react-r1/RC-d574e4d2099d](pyagent_react-r1/RC-d574e4d2099d/README.md): ok
- [pyagent_react-r1/RC-f0e2b1a1f91a](pyagent_react-r1/RC-f0e2b1a1f91a/README.md): ok
- [pyagent_react-r1/RC-f5097b168055](pyagent_react-r1/RC-f5097b168055/README.md): ok
- [pyagent_react-r1/RC-f94db276afa4](pyagent_react-r1/RC-f94db276afa4/README.md): ok
