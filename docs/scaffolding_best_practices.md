# Scaffolding Best Practices for Machine-Learning Learning Systems

## Purpose

This document defines the working best-practices framework for the ml-lab research project. The framework is designed for publishable evaluation of machine-learning scaffolding in human-AI learning systems.

## Guiding Principle

Effective scaffolding should increase learner independence over time. A scaffold is successful when the learner performs better after support is removed, not merely when the learner completes a supported task.

## Best-Practice Framework

### 1. Preserve Productive Struggle

The system should avoid immediate answer-giving. Learners should make an initial attempt before high-intensity support is provided unless the task is clearly inaccessible.

Implementation rule:

- No direct explanation before an initial attempt.
- Low-intensity orientation prompts are allowed early.
- High-intensity scaffolds require evidence of need.

### 2. Use Evidence Before Intervention

Scaffolds should be selected from observable learner evidence rather than generic assumptions.

Relevant evidence includes:

- Number of attempts
- Error pattern
- Confidence level
- Time on task
- Prior scaffold use
- Concept history
- Current difficulty estimate

### 3. Prefer Hint Ladders Over Direct Answers

Support should move gradually from general prompts to explicit guidance.

Recommended ladder:

1. Orientation prompt
2. Concept activation
3. Diagnostic question
4. Strategy hint
5. Worked micro-example
6. Partial solution
7. Full explanation after learner attempt

### 4. Fade Support as Competence Increases

Scaffolding should decrease as learner performance improves. Fading should be explicit in the policy rather than left to instructor intuition.

Fading indicators:

- Increased correctness
- Improved confidence calibration
- Reduced time to correct solution
- Reduced need for repeated hints
- Successful transfer to new task variants

### 5. Require Metacognitive Work

Scaffolds should frequently ask learners to predict, explain, compare, or justify before receiving more explicit help.

Useful metacognitive prompts:

- What do you think the next step is?
- Which concept applies here and why?
- How confident are you in this answer?
- What would change if the data distribution shifted?
- What evidence supports your choice?

### 6. Separate Helpfulness From Learning

Immediate helpfulness is not sufficient evidence of learning. The project should distinguish supported task completion from durable learning.

Evaluation should include:

- Delayed post-test
- Transfer task
- Unsupported independent task
- Calibration score
- Hint dependency score

### 7. Penalize Overreliance

The system should measure whether learners become dependent on scaffolds.

Overreliance signals:

- Requesting help before attempting
- Repeated use of high-intensity scaffolds
- Copying scaffold text into answers
- Performance collapse after scaffold removal
- High confidence in scaffolded but incorrect answers

### 8. Make Scaffold Decisions Auditable

Every scaffold decision should be logged with the learner state, task state, selected scaffold, and reason for selection. This supports reproducibility and paper-ready analysis.

Minimum decision log fields:

- learner_id
- task_id
- timestamp
- learner_state
- scaffold_type
- scaffold_intensity
- policy_reason
- outcome_after_scaffold

## Paper Contribution

The paper should present this framework as a practical design and evaluation standard for adaptive ML scaffolding. The key distinction is that the framework treats scaffolding as a policy problem: when to intervene, how much to help, when to fade, and how to know whether independence improved.
