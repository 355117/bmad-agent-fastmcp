# {{Project Name}} Product Requirements Document (PRD)

[[LLM: The default path and filename unless specified is docs/prd.md]]

[[LLM: If available, review any provided document or ask if any are optionally available: Project Brief]]

## Goals and Background Context

[[LLM: Populate the 2 child sections based on what we have received from user description or the provided brief. Allow user to review the 2 sections and offer changes before proceeding]]

### Goals

[[LLM: Bullet list of 1 line desired outcomes the PRD will deliver if successful - user and project desires]]

### Background Context

[[LLM: 1-2 short paragraphs summarizing the background context, such as what we learned in the brief without being redundant with the goals, what and why this solves a problem, what the current landscape or need is etc...]]

### Change Log

[[LLM: Track document versions and changes]]

| Date | Version | Description | Author |
| :--- | :------ | :---------- | :----- |

## Requirements

[[LLM: Draft the list of functional and non functional requirements under the two child sections, and immediately execute tasks#advanced-elicitation display]]

### Functional

[[LLM: Each Requirement will be a bullet markdown and an identifier sequence starting with FR`.]]
@{example: - FR6: The Todo List uses AI to detect and warn against adding potentially duplicate todo items that are worded differently.}

### Non Functional

[[LLM: Each Requirement will be a bullet markdown and an identifier sequence starting with NFR`.]]
@{example: - NFR1: AWS service usage **must** aim to stay within free-tier limits where feasible.}

^^CONDITION: has_ui^^

## User Interface Design Goals

[[LLM: Capture high-level UI/UX vision to guide Design Architect and to inform story creation. Steps:

1. Pre-fill all subsections with educated guesses based on project context
2. Present the complete rendered section to user
3. Clearly let the user know where assumptions were made
4. Ask targeted questions for unclear/missing elements or areas needing more specification
5. This is NOT detailed UI spec - focus on product vision and user goals
6. Defer detailed UI design to UX Expert agent]]

### Target Users

[[LLM: Who will use this application? Include user personas, skill levels, and primary use cases]]

### User Experience Goals

[[LLM: What should users feel when using this application? Include emotional goals, efficiency targets, and success metrics]]

### Design Principles

[[LLM: Core design principles that should guide all UI decisions. Examples: simplicity, accessibility, mobile-first, etc.]]

### Key User Flows

[[LLM: High-level description of the most important user journeys through the application]]

^^END_CONDITION^^

## User Stories

[[LLM: Create user stories based on requirements. Each story should follow the format: "As a [user type], I want [goal] so that [benefit]". Group related stories under epic headings.]]

### Epic: [Epic Name]

[[LLM: Group related user stories under epic headings]]

- **Story ID**: [Unique identifier]
- **As a** [user type], **I want** [goal] **so that** [benefit]
- **Acceptance Criteria**:
  - [ ] [Specific, testable criteria]
  - [ ] [Additional criteria]

## Technical Considerations

[[LLM: High-level technical requirements and constraints that will inform architecture decisions]]

### Platform Requirements

[[LLM: Target platforms, browsers, devices, etc.]]

### Performance Requirements

[[LLM: Response times, throughput, scalability needs]]

### Security Requirements

[[LLM: Authentication, authorization, data protection needs]]

### Integration Requirements

[[LLM: External systems, APIs, third-party services]]

## Success Metrics

[[LLM: How will we measure if this product is successful?]]

### Key Performance Indicators (KPIs)

[[LLM: Quantifiable metrics that indicate success]]

### User Satisfaction Metrics

[[LLM: How will we measure user satisfaction and engagement?]]

## Timeline and Milestones

[[LLM: High-level project timeline with major milestones]]

### Phase 1: MVP

[[LLM: Core features for minimum viable product]]

### Phase 2: Enhancement

[[LLM: Additional features and improvements]]

### Phase 3: Scale

[[LLM: Features for scaling and optimization]]

## Assumptions and Dependencies

[[LLM: Document key assumptions and external dependencies]]

### Assumptions

[[LLM: What are we assuming to be true?]]

### Dependencies

[[LLM: What external factors could impact this project?]]

## Risks and Mitigation

[[LLM: Identify potential risks and mitigation strategies]]

### Technical Risks

[[LLM: Technology-related risks and how to address them]]

### Business Risks

[[LLM: Market, user adoption, or business model risks]]

## Appendix

[[LLM: Additional supporting information, research, or references]]

### Research and References

[[LLM: Links to market research, competitor analysis, user research, etc.]]

### Glossary

[[LLM: Define any technical terms or domain-specific language used in this document]]