# Paper Outline

## Working Title

**Best Practices for Adaptive Machine-Learning Scaffolding: Timing, Fading, Calibration, and Transfer in Human-AI Learning Systems**

## Abstract Argument

AI-supported learning systems can improve task completion, but task completion is not the same as learning. This paper argues that effective machine-learning scaffolding should be evaluated by whether it improves transfer, metacognitive calibration, and independent performance after support is removed. The project introduces a best-practices framework, an auditable scaffold-policy architecture, and a reproducible synthetic experiment for validating study design before human-subject pilot testing.

## 1. Introduction

### Problem

AI and machine-learning systems increasingly provide educational assistance, but unrestricted assistance can create learner dependence. Many systems optimize helpfulness, answer quality, or short-term task success rather than durable learning.

### Gap

The field needs practical, measurable best practices for when scaffolds should appear, how intense they should be, when they should fade, and how researchers should evaluate whether scaffolding improves independence rather than replacing learner cognition.

### Contribution

This paper contributes:

1. A best-practices framework for ML scaffolding
2. A scaffold-policy model based on learner-state evidence
3. Metrics for calibration and overreliance
4. A reproducible synthetic experiment comparing scaffold-design conditions
5. A protocol foundation for future human-subject evaluation

## 2. Background

### Educational Scaffolding

Scaffolding supports learners while they develop competence, but the support must eventually fade. The goal is independent performance.

### Human-AI Learning Systems

LLMs and adaptive ML systems can provide immediate support, but they can also reduce productive struggle if they intervene too early or too explicitly.

### Metacognition and Calibration

Learners need to understand not only the answer but also their confidence, uncertainty, and reasoning process. Calibration becomes a central outcome.

### Overreliance

Overreliance occurs when learners depend on scaffolds or AI-generated support in ways that weaken independent transfer.

## 3. Best-Practices Framework

The proposed framework includes:

- Preserve productive struggle
- Use learner-state evidence before intervention
- Prefer hint ladders over direct answers
- Fade support as competence increases
- Require metacognitive work
- Separate helpfulness from learning
- Penalize overreliance
- Make scaffold decisions auditable

## 4. System Design

### Learner State

The learner state model includes knowledge estimate, confidence, cognitive load, hint dependency, attempts, and elapsed time.

### Scaffold Types

The scaffold ladder includes orientation prompts, concept activation, diagnostic questions, strategy hints, micro-examples, partial solutions, and full explanations.

### Policy Logic

The timing-and-fading policy selects scaffolds based on overreliance risk, readiness for fading, initial attempts, and evidence of support need.

## 5. Synthetic Experiment

### Purpose

The synthetic experiment validates the experimental structure, metrics, and software pipeline before human-subject data collection.

### Conditions

- No-AI control
- Unrestricted AI assistance
- Static scaffolding
- Adaptive scaffold policy
- Adaptive timing-and-fading policy

### Outcomes

- Immediate accuracy
- Transfer accuracy
- Calibration error
- Overreliance score
- Premature help rate
- Unsupported drop rate

## 6. Expected Results Pattern

The theoretical expectation is that unrestricted AI assistance may improve immediate accuracy while producing higher overreliance and weaker transfer. Adaptive timing-and-fading should produce the strongest balance between supported performance and independent follow-up performance.

## 7. Discussion

The key design implication is that ML scaffolding should optimize appropriately timed independence rather than maximal assistance. The paper should discuss how this principle applies to intelligent tutoring systems, LLM assistants, coding education, and machine-learning education.

## 8. Limitations

Synthetic traces cannot establish causal learning effects in human learners. Human-subject pilot testing is required to validate the framework empirically.

## 9. Future Work

Future work should collect human learner traces, test the policy in real ML education tasks, estimate condition effects, and evaluate whether calibration and reduced overreliance mediate transfer gains.
