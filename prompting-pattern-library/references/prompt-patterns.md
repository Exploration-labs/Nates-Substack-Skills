# Comprehensive Prompting Pattern Library

This reference contains proven prompting patterns organized by category, with examples and guidance for each.

## Foundational Patterns

### 1. Zero-Shot Prompting
**When to use**: Simple, well-defined tasks where the model has sufficient training data.

**Pattern**:
```
[Clear task description]
[Any necessary context]
[Output specifications]
```

**Example**:
```
Summarize the following article in 3 sentences, focusing on the main argument and key supporting evidence:

[Article text]
```

**Why this works**:
- **Explicit constraints** ("3 sentences") prevent overlong summaries
- **Focused direction** ("main argument and key supporting evidence") guides what to extract
- **Single instruction** keeps cognitive load low for straightforward tasks
- Model training includes millions of summarization examples, so pattern recognition activates immediately

**Strengths**: Simple, token-efficient, works well for common tasks.
**Limitations**: May struggle with novel or highly specific tasks.

**When it fails**: See [Ambiguity Failures](../references/failure-modes.md#ambiguity-failures) if output format unclear, or [Assumption Failures](../references/failure-modes.md#assumption-failures) if context insufficient.

**Model notes**: All major models (Claude, GPT-4, Gemini) handle zero-shot well for common tasks. See [Model Quirks](../references/model-quirks.md) for model-specific optimization.

---

### 2. Few-Shot Prompting
**When to use**: Tasks requiring specific format, style, or approach that's easier to show than describe.

**Pattern**:
```
[Task description]

Example 1:
Input: [Example input 1]
Output: [Example output 1]

Example 2:
Input: [Example input 2]
Output: [Example output 2]

Now complete:
Input: [Actual input]
Output:
```

**Example**:
```
Extract key entities from customer feedback and categorize sentiment.

Example 1:
Input: "The new interface is confusing but the customer service team helped me figure it out."
Output: {"interface": "negative", "customer_service": "positive"}

Example 2:
Input: "Fast shipping and great product quality!"
Output: {"shipping": "positive", "product_quality": "positive"}

Now complete:
Input: "Disappointed with the battery life, though the screen is beautiful."
Output:
```

**Why this works**:
- **Pattern demonstration**: Examples teach the model the exact format and style, not through description but through demonstration
- **Edge case handling**: Example 1 shows mixed sentiment (negative + positive in same input), which is harder to specify in instructions
- **Format precision**: JSON structure is immediately clear from examples, no need for schema description
- **Implicit rules**: Model infers rules like "extract multiple entities" and "per-entity sentiment" from examples alone

**Strengths**: Highly effective for format specification, style matching, edge case handling.
**Limitations**: Uses more tokens, requires good examples.

**Best practices**:
- Use 2-5 examples (more rarely helps)
- Include edge cases in examples
- Ensure examples are high quality
- Make examples diverse

**When it fails**: See [Reasoning Failures](../references/failure-modes.md#reasoning-failures) section on "Insufficient Example Diversity" if model struggles with variations not shown in examples.

**Model comparison**: 
- **Claude**: Excellent at inferring patterns from 2-3 examples
- **GPT-4**: May benefit from one extra example for complex formats
- **Gemini**: Works well with 3-4 examples for structured tasks
See [Model Quirks](../references/model-quirks.md) for detailed guidance.

---

### 3. Chain-of-Thought (CoT)
**When to use**: Complex reasoning tasks, math problems, multi-step logic.

**Pattern**:
```
[Problem description]

Think through this step-by-step:
1. [First reasoning step]
2. [Second reasoning step]
...
Therefore, [conclusion]
```

**Example**:
```
A store sells apples for $0.50 each or $5 for a dozen. If I need 30 apples, what's the cheapest way to buy them?

Think through this step-by-step:
```

**Why this works**:
- **Forced decomposition**: "Step-by-step" requirement prevents jumping to conclusions
- **Intermediate verification**: Each step can be checked for logical consistency
- **Error reduction**: Multi-step problems solved as sequence of smaller problems have dramatically lower error rates
- **Transparency**: Reasoning is visible and debuggable, unlike direct answers

**Research basis**: Chain-of-thought prompting improves accuracy on reasoning tasks by 40-60% compared to direct answering (Wei et al., 2022). The improvement comes from forcing the model to "show its work" rather than pattern-matching to an answer.

**Strengths**: Dramatically improves reasoning accuracy, makes logic transparent.
**Limitations**: Uses more tokens, slower.

**Variations**:
- "Let's think step by step" - proven effective phrase
- "Show your work" - educational framing
- "Explain your reasoning" - professional framing
- "Walk me through your logic" - conversational framing

**When it fails**: If reasoning goes off track, see [Reasoning Failures](../references/failure-modes.md#reasoning-failures). For multi-step tasks requiring orchestration, see [Planner-Executor Pattern](../references/orchestration-patterns.md#3-planner-executor-pattern).

**Model performance**:
- **Claude**: Excellent at maintaining coherent reasoning over many steps
- **GPT-4**: Strong reasoning, may occasionally skip steps if not explicitly required
- **Gemini**: Good analytical reasoning, benefits from explicit step numbering
For detailed model guidance, see [Model Quirks](../references/model-quirks.md).

---

## Structured Output Patterns

### 4. JSON Output Specification
**When to use**: Need structured, machine-parseable output.

**Pattern**:
```
[Task description]

Respond ONLY with valid JSON in this exact format:
{
  "field1": "description",
  "field2": "description",
  "nested": {
    "field3": "description"
  }
}
```

**Example**:
```
Analyze this product review for sentiment and key topics.

Respond ONLY with valid JSON in this exact format:
{
  "overall_sentiment": "positive|negative|neutral",
  "sentiment_score": 0-100,
  "key_topics": ["topic1", "topic2"],
  "purchase_intent": "high|medium|low|none"
}

Review: "Great product but shipping took forever."
```

**Strengths**: Reliable structured output, easy to parse programmatically.
**Best practices**:
- Use all caps for "ONLY" to emphasize format constraints
- Provide exact schema
- Include type hints
- Specify valid values for enum fields

---

### 5. Markdown Table Output
**When to use**: Comparative data, lists with multiple attributes.

**Pattern**:
```
[Task description]

Output as a markdown table with these columns:
| Column1 | Column2 | Column3 |
```

**Example**:
```
Compare these three frameworks on the following criteria.

Output as a markdown table with these columns:
| Framework | Learning Curve | Performance | Community Size |
```

**Strengths**: Human-readable, structured, good for comparisons.

---

### 6. Delimited Sections
**When to use**: Multi-part responses, clear separation of content types.

**Pattern**:
```
[Task description]

Structure your response as:

## Section 1 Name
[Section 1 content]

## Section 2 Name
[Section 2 content]
```

**Example**:
```
Analyze this startup pitch deck.

Structure your response as:

## Strengths
[List 3-5 strengths]

## Weaknesses
[List 3-5 weaknesses]

## Key Questions
[List 3 critical questions for founders]
```

---

## Role and Persona Patterns

### 7. Expert Role Assignment
**When to use**: Domain-specific tasks requiring specialized knowledge or perspective.

**Pattern**:
```
You are a [specific role] with [relevant expertise].

[Task description from that role's perspective]
```

**Example**:
```
You are a senior security architect with 15 years of experience in financial services infrastructure.

Review this API design for security vulnerabilities and compliance concerns with PCI-DSS standards.
```

**Strengths**: Frames response appropriately, activates relevant knowledge.
**Limitations**: Can introduce unnecessary jargon if role not well-chosen.

---

### 8. Audience-Specific Framing
**When to use**: Content that must be appropriate for specific audience level.

**Pattern**:
```
Explain [topic] as if speaking to [specific audience with defined characteristics].

Key audience characteristics:
- [Characteristic 1]
- [Characteristic 2]
- [Characteristic 3]
```

**Example**:
```
Explain how neural networks work as if speaking to:
- A C-level executive with no technical background
- Who needs to make budget decisions about ML initiatives
- Who has 10 minutes to understand the basics
```

---

## Advanced Reasoning Patterns

### 9. Tree of Thoughts
**When to use**: Complex problems with multiple valid approaches.

**Pattern**:
```
[Problem description]

Generate 3 different approaches to solve this:

Approach 1: [First approach]
Pros: [Advantages]
Cons: [Disadvantages]

Approach 2: [Second approach]
Pros: [Advantages]
Cons: [Disadvantages]

Approach 3: [Third approach]
Pros: [Advantages]
Cons: [Disadvantages]

Based on this analysis, the best approach is [selection] because [reasoning].
```

**Strengths**: Explores solution space, reveals tradeoffs.
**Limitations**: Token-heavy, may be overkill for simple problems.

---

### 10. Self-Consistency
**When to use**: High-stakes decisions, need confidence in answer.

**Pattern**:
```
[Problem description]

Generate 3 independent solutions to this problem, then compare them:

Solution 1:
[First solution with reasoning]

Solution 2:
[Second solution with reasoning]

Solution 3:
[Third solution with reasoning]

Comparing these solutions, the most reliable answer is [final answer] because [reasoning about consistency].
```

---

### 11. Analogical Reasoning
**When to use**: Explaining complex concepts, finding creative solutions.

**Pattern**:
```
[Task description]

Approach this by:
1. Finding an analogy from [familiar domain]
2. Mapping key elements
3. Using the analogy to [solve problem / explain concept]
```

**Example**:
```
Explain how Kubernetes works.

Approach this by finding an analogy from shipping logistics, mapping key concepts (pods, nodes, scheduler), then explaining Kubernetes through that lens.
```

---

## Quality Control Patterns

### 12. Reflection and Self-Critique
**When to use**: High-quality outputs, catching errors.

**Pattern**:
```
[Task description]

First, provide your initial response:
[Response]

Now critique your own response:
- What assumptions did I make?
- What could go wrong?
- What did I miss?
- How could this be improved?

Revised response incorporating self-critique:
[Improved response]
```

---

### 13. Citation Requirements
**When to use**: Fact-based content requiring verification.

**Pattern**:
```
[Task description]

Requirements:
- Cite specific sources for each claim
- Distinguish between facts and interpretations
- Flag uncertain information
- Provide source reliability assessment
```

**Example**:
```
Summarize the current state of quantum computing commercialization.

Requirements:
- Cite specific sources for each claim (company announcements, research papers, industry reports)
- Distinguish between announced capabilities and demonstrated capabilities
- Flag claims that are contested or uncertain
- Note source bias (e.g., company PR vs. independent analysis)
```

---

### 14. Uncertainty Acknowledgment
**When to use**: Prevent confident errors, understand knowledge boundaries.

**Pattern**:
```
[Task description]

In your response:
- Clearly state when you're uncertain
- Provide confidence levels for claims
- Suggest verification methods
- Acknowledge limitations
```

---

## Decomposition Patterns

### 15. Hierarchical Task Breakdown
**When to use**: Complex, multi-step projects.

**Pattern**:
```
[Complex task]

Break this down into:
1. High-level phases
2. Sub-tasks per phase
3. Dependencies and ordering
4. Success criteria for each sub-task
```

**Example**:
```
Plan a migration from monolithic architecture to microservices.

Break this down into:
1. High-level phases (assessment, planning, pilot, migration, optimization)
2. Specific sub-tasks per phase
3. Dependencies (what must happen before what)
4. Success criteria for each sub-task
```

---

### 16. Iterative Refinement
**When to use**: Outputs requiring multiple passes to perfect.

**Pattern**:
```
[Initial task]

Draft 1: [Quick initial version]

Improvement areas: [What to fix]

Draft 2: [Improved version]

Final polish: [Polished version]
```

---

## Context Management Patterns

### 17. Explicit Context Framing
**When to use**: Ambiguous tasks, shared context assumptions.

**Pattern**:
```
Context:
- [Relevant background information]
- [Constraints or requirements]
- [Assumed knowledge]

Given this context: [Task]
```

**Example**:
```
Context:
- We're a B2B SaaS company selling to enterprises
- Average deal size is $100K
- Sales cycle is 6-9 months
- We use challenger sales methodology

Given this context: Review this cold email template and suggest improvements.
```

---

### 18. Constraint Specification
**When to use**: Tasks with important limitations.

**Pattern**:
```
[Task description]

Constraints:
- Must: [Required elements]
- Must not: [Prohibited elements]
- Should: [Preferred elements]
- Should not: [Discouraged elements]
```

---

## Meta-Prompting Patterns

### 19. Prompt Improvement Request
**When to use**: Iterating on prompts themselves.

**Pattern**:
```
I want to accomplish: [Goal]

My current prompt is:
"[Current prompt]"

Improve this prompt by:
1. Identifying weaknesses
2. Suggesting specific improvements
3. Providing the rewritten prompt
```

---

### 20. Task Clarification
**When to use**: Uncertain about task specifics.

**Pattern**:
```
[Initial task description]

Before proceeding, ask me:
- Clarifying questions about requirements
- Questions about constraints
- Questions about desired output format
- Questions about success criteria
```

---

## Domain-Specific Patterns

### 21. Code Review Pattern
**When to use**: Reviewing or improving code.

**Pattern**:
```
Review this code for:

Correctness:
- Does it work as intended?
- Edge cases?

Quality:
- Readability
- Maintainability
- Performance

Best Practices:
- Language idioms
- Security concerns
- Testing needs

Code:
[Code to review]
```

---

### 22. Writing Improvement Pattern
**When to use**: Editing or improving written content.

**Pattern**:
```
Improve this text for:

Clarity:
- Simplify complex sentences
- Remove ambiguity

Concision:
- Remove unnecessary words
- Tighten phrasing

Engagement:
- Improve opening
- Strengthen transitions
- Compelling close

Original text:
[Text]
```

---

### 23. Data Analysis Pattern
**When to use**: Analyzing data or trends.

**Pattern**:
```
Analyze this data for:

Descriptive Statistics:
- Central tendencies
- Distributions
- Outliers

Patterns:
- Trends over time
- Correlations
- Anomalies

Insights:
- What does this mean?
- What's surprising?
- What questions does this raise?

Data:
[Data]
```

---

## Combination Patterns

### 24. Few-Shot + Chain-of-Thought
**When to use**: Complex reasoning tasks with specific format requirements.

**Pattern**:
```
[Task description]

Example:
Input: [Example input]
Reasoning: [Step-by-step reasoning]
Output: [Example output]

Now apply the same reasoning process:
Input: [Actual input]
Reasoning:
```

---

### 25. Role + Reflection
**When to use**: Expert-level outputs requiring quality assurance.

**Pattern**:
```
As a [expert role], [complete task].

Then, as a [critic/reviewer role], critique the work and suggest improvements.

Finally, integrate the critique into an improved version.
```

---

## Pattern Selection Guide

**Simple factual tasks**: Zero-shot prompting
**Format-specific tasks**: Few-shot prompting
**Reasoning tasks**: Chain-of-thought
**High-stakes decisions**: Self-consistency + Reflection
**Complex projects**: Hierarchical breakdown + Iterative refinement
**Domain expertise**: Role assignment + Context framing
**Multi-part responses**: Delimited sections + Structured output

**Combine patterns** when dealing with complex requirements. Most effective prompts use 2-3 patterns together.

## Anti-Patterns to Avoid

**Vague instructions**: "Make it better" → Specify what "better" means
**Over-complexity**: 10 requirements → Focus on 2-3 critical requirements
**Conflicting constraints**: "Be brief but comprehensive" → Choose one
**Implicit assumptions**: Model can't read your mind → State everything explicitly
**Over-politeness**: "If you don't mind, could you possibly..." → Be direct and clear