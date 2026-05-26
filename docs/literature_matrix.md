# Literature Matrix

## Purpose

This matrix connects prior research to the constructs, measures, and design decisions in `ml-lab`. It should be used as a design instrument, not as a citation dump. Each source should justify a construct, measurement choice, experimental arm, interpretation boundary, or implementation decision.

Add sources only after verifying bibliographic details from the original publication or a reliable scholarly index.

## Evidence-quality categories

Use one category for each source.

| Category | Meaning | Recommended use |
| --- | --- | --- |
| Theory | Foundational or conceptual work. | Frame constructs and assumptions. |
| Empirical study | Original study with learner data. | Support measurement and expected effects. |
| Systematic review | Structured synthesis of prior studies. | Establish state of evidence and recurring limitations. |
| Methods paper | Design, measurement, or reproducibility guidance. | Support analysis and reporting choices. |
| Preprint | Unreviewed or not yet fully verified source. | Use cautiously and label clearly. |
| Policy/context | Institutional, practitioner, or policy source. | Motivate relevance, not core causal claims. |

## Source matrix

| Citation | Evidence category | Domain | Research design | Key construct | Measurement approach | Relevance to `ml-lab` | Code/design implication | Verification status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wood, Bruner, & Ross (1976) | Theory/empirical | Scaffolding | Tutor-child problem solving | Contingent support | Tutor intervention patterns | Establishes scaffolding as temporary support enabling performance beyond unaided ability. | Keep scaffold actions contingent on learner state. | Needs full APA/DOI verification. |
| Vygotsky (1978) | Theory | Learning theory | Conceptual synthesis | Zone of proximal development | Conceptual | Frames why timing and readiness matter. | Represent learner state before selecting scaffold action. | Needs edition verification. |
| Puntambekar & Hubscher (2005) | Theory/methods | Learning environments | Conceptual review | Scaffolding definition and fading | Conceptual criteria | Helps prevent overly broad use of “scaffolding.” | Require clear action names, intensities, and policy rules. | Needs full APA/DOI verification. |
| Azevedo/SRL literature | Empirical/theory | Self-regulated learning | TBD | Monitoring, regulation, calibration | Confidence, trace, and process measures | Supports metacognitive calibration as a primary outcome. | Preserve correctness, confidence, and calibration error. | Needs specific sources. |
| Adaptive scaffolding studies | Empirical | Intelligent tutoring / learning systems | TBD | Adaptive support | Task traces, prompts, performance | Supports comparison between adaptive and static support. | Compare `RuleBasedScaffoldPolicy` against `StaticScaffoldPolicy`. | Needs specific sources. |
| Cognitive-load literature | Theory/empirical | Learning sciences | TBD | Cognitive load | Self-report, task complexity, latency, performance | Supports balancing support against productive effort. | Add validated load proxy to `LearnerState`. | Needs specific sources. |
| Productive failure/productive struggle literature | Theory/empirical | Learning sciences | TBD | Productive struggle | Initial failure, later transfer | Supports avoiding premature over-assistance. | Add scaffold timing gates and fading rules. | Needs specific sources. |
| Learning transfer literature | Theory/empirical | Learning sciences | TBD | Transfer | Near/far transfer tasks | Supports transfer as a primary outcome. | Add task labels and transfer metrics. | Needs specific sources. |
| LLM-assisted learning studies | Empirical/review | AI education | TBD | AI help, overreliance, learning support | Prompt/use traces, performance, retention | Frames unguided LLM assistance as a comparison condition. | Refine `UnguidedLLMPolicy` and support logging. | Needs specific sources. |
| Human-AI reliance literature | Empirical/review | Human-AI interaction | TBD | Overreliance and trust calibration | Agreement with AI, verification behavior | Supports dependency and false-mastery concerns. | Distinguish help use from durable learning. | Needs specific sources. |

## Construct-to-code mapping

| Construct | Current code object | Current status | Future need |
| --- | --- | --- | --- |
| Learner state | `LearnerState` | Implemented with correctness, confidence, latency, hints, and metadata. | Add validated cognitive-load proxy. |
| Scaffold action | `ScaffoldAction` | Implemented with name, description, intensity, and metadata. | Add action taxonomy and fading tags. |
| Adaptive policy | `RuleBasedScaffoldPolicy` | Implemented as transparent adaptive baseline. | Add learned policy classes. |
| Static scaffold | `StaticScaffoldPolicy` | Implemented as non-adaptive comparison. | Add configurable static sequences. |
| Unguided LLM assistance | `UnguidedLLMPolicy` | Implemented as synthetic proxy. | Replace proxy with logged LLM-use traces in empirical work. |
| No-AI control | `ExperimentArm(policy=None)` | Implemented as unsupported baseline. | Preserve as clean comparison condition. |
| Calibration | `CalibrationMetric`; event-level `calibration_error` | Implemented. | Add learner-level aggregation and reliability checks. |
| Hint dependency | `HintDependencyMetric`; event-level `hint_count` | Implemented. | Distinguish hints, examples, explanations, and LLM help. |
| Arm comparison | `PairwiseComparison`; `compare_arms()` | Implemented with mean differences and Cohen's d. | Add confidence intervals and model-based estimates. |
| Durable learning | Not yet implemented. | Planned. | Add delayed post-test outcome. |
| Transfer | Not yet implemented. | Planned. | Add task labels and transfer metrics. |

## Claim-to-evidence map

| Claim | Evidence needed | Current status | Repository implication |
| --- | --- | --- | --- |
| Scaffolds should be contingent and temporary. | Foundational scaffolding theory and empirical adaptive-support studies. | Partially mapped. | Policy rules should depend on learner state and allow low/no support. |
| Adaptive support should be compared against static support. | Adaptive scaffolding studies and experimental design rationale. | Partially mapped. | Maintain separate adaptive and static arms. |
| Unguided AI assistance may support task completion without durable learning. | LLM learning studies, overreliance literature, retention/transfer studies. | Needs verified sources. | Treat LLM assistance as a comparison condition, not the default intervention. |
| Calibration is a core learning outcome. | Self-regulated learning and metacognition literature. | Needs specific sources. | Keep confidence and correctness in the event log. |
| Transfer and delayed outcomes matter more than immediate correctness alone. | Transfer and retention literature. | Needs specific sources. | Add delayed and transfer task types. |
| Synthetic results validate workflow, not human learning effects. | Simulation and reproducibility methods literature. | Needs methods sources. | Keep interpretation boundaries in docs and outputs. |

## Priority source retrieval checklist

- Verify full APA entry for Wood, Bruner, and Ross (1976).
- Verify full APA entry and edition details for Vygotsky (1978).
- Retrieve specific Puntambekar scaffolding sources and DOIs where available.
- Identify specific Azevedo/SRL sources for calibration and metacognitive scaffolding.
- Identify systematic reviews on AI/LLM tutoring and programming/STEM learning.
- Identify productive failure/productive struggle sources relevant to timing and over-assistance.
- Identify transfer-learning measurement sources for near/far transfer tasks.
- Identify human-AI reliance sources that distinguish trust, verification, and overreliance.

## Use rules

- Do not cite a source in manuscript text until its bibliographic details are verified.
- Prefer peer-reviewed empirical studies and systematic reviews for causal or effectiveness claims.
- Use theory papers to define constructs, not to claim effect sizes.
- Use policy/context sources only for motivation.
- Record how each source changes the code, study design, or interpretation plan.
