# Knowledge Engineering Rationale

## 1. Psychological Grounding
- **Axis 1 (Locus):** Uses Rotter’s Locus of Control. We identify if the user is a 'Victim' of their day or a 'Victor' who took action.
- **Axis 2 (Orientation):** Based on Organ’s (1988) Organizational Citizenship Behavior. We track 'Contribution' (value-giving) vs 'Entitlement' (value-taking).
- **Axis 3 (Radius):** Inspired by Maslow’s Self-Transcendence. We measure the scope of the user's concern—from self-centric to altrocentric.

## 2. Design Trade-offs
I chose a **JSON-driven State Machine** to ensure deterministic integrity. 
- **Auditable Logic:** Every response can be traced back to a signal tally.
- **Trust:** Employees need to know that the system won't "hallucinate" different advice each night.
- **Interpolation:** Using the user's own language (e.g., "You said today was Tough") builds empathy without needing a generative LLM.

## 3. AI as a Power Tool
I used LLMs to iterate on the phrasing of the questions to ensure they felt like a "wise colleague" rather than a cold survey. The resulting tree is 100% code-based to meet the runtime constraints of DT-CultureTech.