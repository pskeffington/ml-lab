# Manuscript Draft: Best-Practices Framework

## Best-Practices Framework for ML Scaffolding

The proposed framework treats scaffolding as a policy problem. A scaffold policy observes learner-state evidence, selects an appropriate form of support, determines the intensity of that support, and records the reason for intervention. This framing is useful because it separates educational assistance from unrestricted answer access. The goal is not to provide more help by default, but to provide the right support at the right time and to remove that support when the learner is ready.

The first principle is to preserve productive struggle. Learners should usually make an initial attempt before receiving high-intensity support. Early struggle gives the system evidence about misconceptions, uncertainty, and strategy use. It also helps prevent immediate reliance on generated explanations. Productive struggle should be bounded, however. If the learner shows repeated failure, excessive cognitive load, or inability to begin, the system should intervene with low- or moderate-intensity support.

The second principle is evidence-based intervention. A scaffold should not be selected solely because help is available. The policy should use observable learner evidence, including attempts, elapsed time, confidence, task difficulty, prior scaffold use, and recent correctness. These features allow the system to distinguish a learner who needs concept activation from a learner who needs a diagnostic question, a strategy hint, or scaffold fading.

The third principle is hint laddering. Rather than moving directly to a full explanation, support should progress from lighter to heavier forms. A useful sequence begins with orientation prompts and concept activation, then moves to diagnostic questions, strategy hints, worked micro-examples, partial solutions, and only later full explanations. This ladder preserves learner agency while still providing a path out of confusion.

The fourth principle is scaffold fading. Assistance should decrease as the learner demonstrates competence, confidence calibration, and reduced dependency. Fading is essential because the purpose of scaffolding is independent performance. Without fading, a system may improve supported task completion while weakening unsupported transfer.

The fifth principle is metacognitive engagement. Learners should often be asked to predict, explain, justify, or compare before receiving more explicit help. These prompts encourage the learner to monitor their own knowledge and uncertainty. In this framework, calibration is not a secondary outcome; it is a central indicator of whether scaffolding is improving self-regulated learning.

The sixth principle is overreliance measurement. A scaffold policy should not be judged only by immediate accuracy. It should also be evaluated for premature help-seeking, repeated high-intensity support, copy-forward behavior, unsupported performance drop-off, and confidence that exceeds correctness. These indicators help distinguish useful support from dependency-producing assistance.

The final principle is auditability. Each scaffold decision should record the learner state, selected scaffold, intensity, policy reason, and subsequent outcome. This makes the system interpretable for researchers and supports reproducible analysis. In educational AI, auditability is not only an engineering preference; it is necessary for evaluating whether a system is improving learning or simply making task completion easier.
