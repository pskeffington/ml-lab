# Manuscript Draft: Reproducibility and Protocol Validation

## Reproducibility and Protocol Validation

The repository is designed to make the scaffolding framework executable before empirical data collection. This is important because human-subject learning studies are costly, time-consuming, and sensitive to design ambiguity. A synthetic validation layer allows the research team to define the study conditions, outcome metrics, reporting workflow, and interpretation guardrails before recruiting learners.

The synthetic experiment compares five conditions: no-AI control, unrestricted AI assistance, static scaffolding, adaptive scaffold policy, and adaptive timing-and-fading policy. Each condition is represented through explicit configuration values that describe scaffold access, adaptivity, timing gates, fading, metacognitive prompting, and baseline hint dependency. This design makes the theoretical contrast between unrestricted help and disciplined scaffolding visible in code.

The primary synthetic outcomes are immediate accuracy, transfer accuracy, calibration error, overreliance score, premature help rate, and unsupported drop rate. These outcomes reflect the paper's central argument that immediate performance should not be treated as sufficient evidence of learning. The analysis workflow compares conditions against unrestricted AI assistance and ranks conditions using an independence score that rewards transfer while penalizing miscalibration and overreliance.

The reporting workflow generates markdown summaries for manuscript planning. These reports include condition-level results, deltas against unrestricted AI, an independence ranking, and an interpretation guardrail. The guardrail is necessary because synthetic traces cannot demonstrate real effects on human learners. Their value is methodological: they verify that the experimental design, code, and metrics are coherent before the framework is tested with real participants.

The project also includes automated tests for scaffold policies, experiment outputs, export utilities, statistical summaries, and reporting. This test suite helps ensure that future development remains aligned with the research design. By keeping conceptual claims, executable policy logic, metrics, and reporting artifacts in the same repository, the project supports a transparent path from theory to pilot study.
