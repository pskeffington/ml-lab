# Literature Matrix

## Purpose

This matrix organizes the literature needed for the paper on best practices in adaptive machine-learning scaffolding. The guiding claim is that effective scaffolding should improve learner independence, transfer, calibration, and unsupported recovery rather than simply increasing immediate assistance.

## Literature Clusters

### Cluster 1: Foundational Scaffolding Theory

| Source | Core Idea | Use in Paper | Relation to Project |
|---|---|---|---|
| Wood, Bruner, & Ross (1976), *The Role of Tutoring in Problem Solving* | Introduced scaffolding as tutor support that allows learners to complete tasks they could not complete alone. | Theoretical foundation for scaffolding as temporary, contingent support. | Supports the claim that scaffolds should be responsive to learner need and eventually withdrawn. |
| Vygotsky (1978), *Mind in Society* | Zone of proximal development frames learning as performance possible with support but not yet independently. | Background theory for why scaffold timing matters. | Supports learner-state evidence and productive-struggle thresholds. |
| Puntambekar & Kolodner (1998), distributed scaffolding | Learning environments can distribute support across tools, peers, representations, and activities. | Expands scaffolding beyond one tutor-one learner interaction. | Supports treating ML systems as one component in a broader scaffold ecology. |
| Puntambekar & Hubscher (2005), tools for scaffolding students | Warned that the term scaffolding is often used too broadly unless support is adaptive and temporary. | Helps justify a stricter best-practices framework. | Reinforces auditability, fading, and clear scaffold definitions. |

### Cluster 2: Adaptive Scaffolding and Self-Regulated Learning

| Source | Core Idea | Use in Paper | Relation to Project |
|---|---|---|---|
| Munshi et al. (2022), adaptive scaffolds in Betty's Brain | Adaptive scaffolds can support self-regulated learning behaviors, but effects vary by scaffold type and learner performance group. | Shows that scaffold design details matter; not all prompts are equally useful. | Supports condition-specific scaffold policies and learner-state evidence. |
| Azevedo and colleagues on metacognitive scaffolding and SRL | Learners benefit when systems support planning, monitoring, debugging, and reflection. | Background for calibration and metacognitive prompting. | Supports confidence-correctness calibration as a core outcome. |
| Just-in-time adaptive intervention framing | Scaffolds can be delivered at moments of likely need rather than continuously. | Supports timing gates and intervention thresholds. | Aligns with the TimingAndFadingPolicy implementation. |
| MetaCLASS (2026), metacognitive coaching with adaptive self-regulation support | LLMs may over-intervene when silence or minimal support is pedagogically preferable. | Strong recent support for the argument against maximal assistance. | Directly supports the project's emphasis on appropriately timed independence. |

### Cluster 3: LLM and AI Tutoring Systems

| Source | Core Idea | Use in Paper | Relation to Project |
|---|---|---|---|
| Liu et al. (2024), multimodal tutoring systems with pedagogical instructions | LLM-based tutoring can follow pedagogical scaffolding instructions and support self-paced learning. | Shows feasibility of LLM scaffolding when grounded in pedagogy. | Supports future integration of scaffold policies with LLM tutors. |
| Bewersdorff et al. (2024), multimodal LLMs in science education | Multimodal LLMs offer personalized support but require robust frameworks and responsible integration. | Supports responsible-design framing. | Reinforces the need for guardrails, auditability, and human learning outcomes. |
| Elnaffar et al. (2025), AI agents in programming education systematic review | AI tools in programming education show benefits but also setup barriers, overreliance, superficial learning, errors, and integrity concerns. | Helps justify the study's focus on overreliance and transfer. | Supports evaluating unrestricted AI against disciplined scaffolding. |
| AutoTutor literature | Conversational tutors can support deep reasoning through dialogue and adaptive feedback. | Historical precedent for dialogue-based intelligent tutoring. | Supports using metacognitive dialogue moves instead of direct answer delivery. |

### Cluster 4: Overreliance, Calibration, and False Mastery

| Source | Core Idea | Use in Paper | Relation to Project |
|---|---|---|---|
| Human-AI overreliance literature | Users may defer to AI outputs even when outputs are wrong or only plausibly correct. | Supports need for overreliance metrics. | Maps to premature help, high-intensity scaffold use, and unsupported drop-off. |
| AI trust paradox literature | Fluent AI outputs can appear trustworthy even when users lack the ability to verify them. | Supports calibration and confidence-correctness analysis. | Reinforces concern that immediate answer quality can mask poor learning. |
| OECD-style concerns about false mastery | Generative AI may create a shortcut that hides lack of durable understanding. | Use cautiously as policy/context framing, not primary empirical evidence. | Supports paper motivation around transfer and independent recovery. |
| Faculty survey literature on AI reliance | Faculty report concern that students may become overly reliant on AI tools. | Use as contextual motivation only. | Helps frame practical relevance but should not substitute for peer-reviewed evidence. |

### Cluster 5: Productive Struggle, Fading, and Transfer

| Source | Core Idea | Use in Paper | Relation to Project |
|---|---|---|---|
| Kapur on productive failure | Initial struggle before instruction can support deeper learning under appropriate conditions. | Supports productive-struggle threshold design. | Justifies not giving direct help before an initial attempt. |
| Cognitive-load and guidance literature | Guidance can reduce unnecessary load but excessive guidance may reduce generative processing. | Supports balanced scaffold intensity. | Maps to intensity values and cognitive-load learner-state fields. |
| Fading literature in scaffolding | Support should be gradually removed as learners gain competence. | Central to best-practices section. | Directly implemented in readiness-for-fading logic. |
| Transfer literature | Durable learning should be assessed using novel but related tasks. | Supports transfer as a primary outcome. | Maps to synthetic transfer accuracy and future pilot tasks. |

## Claim-to-Citation Map

| Manuscript Claim | Best Supporting Literature | Notes |
|---|---|---|
| Scaffolds should be temporary and contingent. | Wood, Bruner, & Ross; Vygotsky; Puntambekar & Hubscher | Use in introduction and framework. |
| AI assistance can improve task completion without guaranteeing learning. | LLM tutoring studies; programming education systematic reviews; overreliance literature | Use to motivate the gap. |
| Metacognitive prompts are central to durable learning. | Azevedo/SRL literature; MetaCLASS; Munshi et al. | Use in framework and outcome rationale. |
| Systems should avoid over-intervention. | MetaCLASS; productive failure literature; overreliance literature | Strong support for timing gates. |
| Transfer and calibration should outrank immediate accuracy. | SRL, transfer, and calibration literature | Use in methods and result interpretation. |
| Synthetic experiments validate workflow, not human learning effects. | Methodological/reproducibility literature | Needs additional methods citations later. |

## Priority Sources to Retrieve Next

1. Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving.
2. Puntambekar, S., & Hubscher, R. (2005). Tools for scaffolding students in a complex learning environment.
3. Munshi, A., Biswas, G., Baker, R., Ocumpaugh, J., Hutt, S., & Paquette, L. (2022). Analyzing adaptive scaffolds that help students develop self-regulated learning behaviors.
4. MetaCLASS (2026). Metacognitive coaching for learning with adaptive self-regulation support.
5. Systematic reviews on AI/LLM tutoring in programming or STEM education.
6. Productive failure/productive struggle literature, especially Kapur.
7. Calibration and self-regulated learning sources from Azevedo and related ITS research.

## Current Gap in the Matrix

The matrix still needs verified APA entries, DOIs where available, and a separate evidence-quality rating for each source. The next iteration should divide sources into peer-reviewed empirical studies, systematic reviews, theory papers, preprints, and policy/context sources.
