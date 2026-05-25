# Result Interpretation Guide

## Purpose

This guide defines how synthetic and future empirical results should be interpreted in the scaffolding study.

## Central Interpretation Rule

A condition should not be considered superior merely because it improves immediate task accuracy. The strongest condition is the one that improves transfer, calibration, and independent follow-up performance while keeping overreliance low.

## Metric Priorities

### Highest Priority

Transfer accuracy and unsupported follow-up performance are the strongest indicators of durable learning.

### High Priority

Calibration error indicates whether learners understand the limits of their own knowledge. Lower calibration error is preferred.

### High Priority

Overreliance score indicates whether scaffolds are replacing learner cognition. Lower overreliance is preferred.

### Secondary Priority

Immediate accuracy is useful, but it can be inflated by high-intensity help. It should be interpreted alongside transfer and dependency metrics.

## Expected Directional Pattern

The theoretical expectation is that unrestricted AI assistance may produce strong immediate accuracy but weaker transfer and higher overreliance. Static scaffolding should reduce some risk but may still fail to adapt to learner state. Adaptive scaffolding should improve targeting, while timing-and-fading should produce the strongest balance of transfer and independence.

## Warning Against Overclaiming

Synthetic data cannot demonstrate real learning effects. It can only validate the structure of the experiment, the behavior of the metrics, and the reproducibility of the analysis pipeline.

## Manuscript Language

Preferred wording:

> The synthetic experiment served as a reproducibility and protocol-validation step. It was used to verify that the experimental conditions, scaffold-policy assumptions, and outcome metrics were operationalized before human-subject pilot testing.

Avoid wording that implies synthetic outcomes are empirical evidence about human learners.
