# Common Prompting Failure Modes and Fixes

This reference catalogs frequent prompting failures, their symptoms, root causes, and solutions.

## Ambiguity Failures

### Failure: Unclear Output Format
**Symptoms**: Model produces correct content in wrong format (paragraph instead of list, JSON instead of table, etc.)

**Root Cause**: Output format not explicitly specified.

**Bad Prompt**:
```
Summarize these customer complaints.
```

**Good Prompt**:
```
Summarize these customer complaints as a markdown table with columns: Issue Category, Frequency, Severity (1-5), Recommended Action.
```

**Fix Pattern**: Always specify exact output format using examples or explicit schemas.

---

### Failure: Vague Success Criteria
**Symptoms**: Model produces output but user unsure if it's "good enough."

**Root Cause**: Success criteria not defined.

**Bad Prompt**:
```
Make this email more professional.
```

**Good Prompt**:
```
Make this email more professional by:
1. Removing casual language ("hey", "gonna")
2. Using formal greetings/closings
3. Restructuring to: context → request → next steps
4. Keeping under 150 words
```

**Fix Pattern**: Define specific, measurable success criteria.

---

### Failure: Ambiguous Scope
**Symptoms**: Model either over-delivers (too much detail) or under-delivers (too brief).

**Root Cause**: Desired depth/breadth not specified.

**Bad Prompt**:
```
Explain machine learning.
```

**Good Prompt**:
```
Explain machine learning in 200 words for a C-level executive with no technical background. Focus on business value, not algorithms. Include 1-2 concrete use cases relevant to financial services.
```

**Fix Pattern**: Specify audience, length, depth, and focus areas.

---

## Assumption Failures

### Failure: Implicit Context
**Symptoms**: Model produces generic response when specific context needed.

**Root Cause**: Assuming model knows context you haven't provided.

**Bad Prompt**:
```
How should we price this feature?
```

**Good Prompt**:
```
How should we price our new real-time analytics feature?

Context:
- B2B SaaS, enterprise customers
- Current pricing: $500-5000/month per company
- Competition charges $1-5 per query
- We offer unlimited queries
- Our cost: $0.10 per 1000 queries
- Target margin: 70%
```

**Fix Pattern**: Include all relevant context explicitly, even if it seems obvious.

---

### Failure: Undefined Technical Level
**Symptoms**: Response either too technical or not technical enough.

**Root Cause**: Audience expertise level not specified.

**Bad Prompt**:
```
Explain how DNS works.
```

**Good Prompt**:
```
Explain how DNS works for a junior software engineer who:
- Understands HTTP and basic networking
- Doesn't know the details of DNS resolution
- Needs to debug a DNS propagation issue
```

**Fix Pattern**: Explicitly define audience expertise level and knowledge gaps.

---

### Failure: Missing Constraints
**Symptoms**: Model produces otherwise good output that violates unstated requirements.

**Root Cause**: Constraints not specified.

**Bad Prompt**:
```
Write a regex to validate email addresses.
```

**Good Prompt**:
```
Write a regex to validate email addresses.

Requirements:
- Python 3 syntax
- Must validate: standard emails, plus-addressing (user+tag@domain.com), subdomains
- Must reject: spaces, missing @, invalid TLDs
- Must work without external libraries
- Include 5 test cases (3 valid, 2 invalid)
```

**Fix Pattern**: State all constraints and requirements explicitly.

---

## Instruction Conflict Failures

### Failure: Contradictory Requirements
**Symptoms**: Unpredictable output, model picks one requirement and ignores conflicting one.

**Root Cause**: Instructions that cannot be satisfied simultaneously.

**Bad Prompt**:
```
Write a comprehensive yet concise analysis of this 50-page document.
```

**Resolution Options**:

Option 1 (Prioritize):
```
Write a concise analysis (300 words maximum) of this 50-page document, focusing only on the three most critical findings.
```

Option 2 (Staged):
```
First, write a comprehensive analysis (1500 words).
Then, condense it to a 300-word executive summary.
```

**Fix Pattern**: Resolve contradictions by prioritizing or staging requirements.

---

### Failure: Format vs. Content Conflict
**Symptoms**: Model compromises either format or content quality.

**Root Cause**: Format requirements too restrictive for content needs.

**Bad Prompt**:
```
Explain quantum entanglement in exactly 50 words, including mathematical formulas.
```

**Good Prompt**:
```
Explain quantum entanglement in approximately 50-75 words. If mathematical formulas are necessary, count them as 10 words each.
```

**Fix Pattern**: Build flexibility into format requirements or adjust content expectations.

---

## Reasoning Failures

### Failure: Lack of Step-by-Step Reasoning
**Symptoms**: Model jumps to conclusions, makes calculation errors, shows faulty logic.

**Root Cause**: Not explicitly requesting reasoning process.

**Bad Prompt**:
```
If I invest $10,000 at 7% annual return, compounded quarterly, for 15 years, how much will I have?
```

**Good Prompt**:
```
If I invest $10,000 at 7% annual return, compounded quarterly, for 15 years, how much will I have?

Show your work step-by-step:
1. State the compound interest formula
2. Define each variable
3. Substitute values
4. Show calculation
5. State final answer
```

**Fix Pattern**: Explicitly request step-by-step reasoning for any calculation or logical task.

---

### Failure: Insufficient Example Diversity
**Symptoms**: Model handles shown examples well but fails on variations.

**Root Cause**: Few-shot examples too similar.

**Bad Few-Shot** (all similar):
```
Example 1: "Great product!" → Positive
Example 2: "Excellent service!" → Positive
Example 3: "Love it!" → Positive
```

**Good Few-Shot** (diverse):
```
Example 1: "Great product!" → Positive
Example 2: "Terrible, broke after one use." → Negative
Example 3: "It's okay, nothing special." → Neutral
Example 4: "Fast shipping but the item was damaged." → Mixed
```

**Fix Pattern**: Include diverse examples covering edge cases, not just typical cases.

---

## Output Quality Failures

### Failure: Overly Generic Output
**Symptoms**: Response is correct but not useful; could apply to anything.

**Root Cause**: Prompt too general or examples too generic.

**Bad Prompt**:
```
Give me tips for improving our product.
```

**Good Prompt**:
```
Give me tips for improving user onboarding in our B2B analytics dashboard.

Current issues:
- 40% of users abandon during first session
- Time-to-first-value averages 45 minutes (target: 15 minutes)
- Support tickets peak on day 1-2 of trial

Our product allows users to connect data sources, build visualizations, and share dashboards. Main complexity: SQL query builder.
```

**Fix Pattern**: Provide specific context and constraints to get specific advice.

---

### Failure: Repetitive Output
**Symptoms**: Model repeats same information or phrasing.

**Root Cause**: Insufficient structure or explicit variety requirements.

**Bad Prompt**:
```
Write 10 email subject lines for our product launch.
```

**Good Prompt**:
```
Write 10 email subject lines for our product launch.

Requirements:
- 3 focused on problem/pain point
- 3 focused on solution/benefit
- 2 focused on social proof
- 2 focused on urgency/scarcity
- All under 50 characters
- Vary tone: some direct, some curiosity-driven, some fear-driven
```

**Fix Pattern**: Request explicit variety in approach, tone, or angle.

---

### Failure: Inconsistent Tone
**Symptoms**: Tone shifts within response (formal to casual, technical to non-technical).

**Root Cause**: Tone not explicitly specified or reinforced.

**Bad Prompt**:
```
Write an announcement about our security incident.
```

**Good Prompt**:
```
Write an announcement about our security incident.

Tone requirements:
- Serious and professional throughout
- Transparent about the incident
- Reassuring about protective measures
- No minimizing language ("small", "minor", "just")
- Maintain consistent formality (no casual phrases)
```

**Fix Pattern**: Specify tone explicitly and provide examples of what to avoid.

---

## Context Window Failures

### Failure: Lost Context in Long Conversations
**Symptoms**: Model forgets earlier instructions or context in long conversations.

**Root Cause**: Important information beyond context window or too far back.

**Fix Pattern**: Restate critical context periodically:
```
Continuing our analysis (reminder: we're focusing on B2B SaaS companies with $1-10M ARR)...
```

---

### Failure: Overloaded Context
**Symptoms**: Model struggles with many simultaneous constraints.

**Root Cause**: Too much information in single prompt.

**Bad Prompt**:
```
Write an email that:
[15 different requirements]
```

**Good Prompt** (staged):
```
Step 1: Draft an email covering [core requirements 1-3]

[Get output]

Step 2: Revise the draft to add [requirements 4-6]

[Get output]

Step 3: Polish for [final requirements 7-8]
```

**Fix Pattern**: Break complex tasks into sequential steps.

---

## Edge Case Failures

### Failure: No Handling of Edge Cases
**Symptoms**: Model produces code/logic that fails on edge cases.

**Root Cause**: Edge cases not mentioned in prompt.

**Bad Prompt**:
```
Write a function to calculate age from birthdate.
```

**Good Prompt**:
```
Write a function to calculate age from birthdate.

Handle these edge cases:
- Birthdate is today (age = 0)
- Birthdate is in the future (return error)
- Birthdate is Feb 29 (leap year)
- Invalid dates (return error)
- Missing input (return error)

Include test cases for each edge case.
```

**Fix Pattern**: Explicitly enumerate edge cases to handle.

---

## Model-Specific Failures

### Failure: Format Not Preserved
**Symptoms**: JSON broken, markdown malformed, structure lost.

**Model-Specific Solutions**:

**For Claude**:
```
Output ONLY valid JSON. Your entire response must be parseable JSON with no additional text before or after.

{
  "field": "value"
}

Do not include markdown code blocks or explanations outside the JSON.
```

**For GPT-4**:
```
You must respond with valid JSON only. Do not include ```json``` tags or any text outside the JSON structure.
```

**Fix Pattern**: Use model-specific format enforcement language.

---

### Failure: Overconfident Errors
**Symptoms**: Model states incorrect information confidently.

**Model-Specific Mitigations**:

**For all models**:
```
Important: If you're not certain about any fact, explicitly state your uncertainty rather than guessing. Say "I'm not sure about X" rather than providing potentially incorrect information.

For any claims you make, indicate confidence level: [High], [Medium], or [Low]
```

**Fix Pattern**: Explicitly request uncertainty acknowledgment.

---

## Debugging Prompts

### Diagnostic Pattern for Failures
When a prompt fails, debug systematically:

```
1. Check for ambiguity
   - Is output format clear?
   - Are success criteria defined?
   - Is scope specified?

2. Check for assumptions
   - Is all context provided?
   - Is expertise level specified?
   - Are constraints stated?

3. Check for conflicts
   - Do requirements contradict?
   - Are format and content compatible?

4. Check reasoning requirements
   - Should I request step-by-step thinking?
   - Do I need few-shot examples?

5. Check specificity
   - Is this too generic?
   - Do I need concrete examples?
   - Are edge cases covered?
```

---

## Quick Failure Diagnosis Checklist

**Output in wrong format?** → Add explicit format specification
**Output too generic?** → Add specific context and constraints
**Output too brief/detailed?** → Specify desired length and depth
**Incorrect reasoning?** → Add "show your work" or chain-of-thought
**Inconsistent quality?** → Add few-shot examples showing desired quality
**Model seems confused?** → Check for contradictory instructions
**Edge cases failing?** → Explicitly enumerate edge cases to handle
**Losing context?** → Restate critical information
**Too many requirements?** → Break into sequential steps

---

## Prevention Checklist

Before sending a prompt, verify:
- [ ] Output format explicitly specified
- [ ] All relevant context provided
- [ ] Audience/expertise level stated
- [ ] Success criteria defined
- [ ] No contradicting requirements
- [ ] Constraints listed
- [ ] Edge cases mentioned (if applicable)
- [ ] Examples included (for format-specific tasks)
- [ ] Reasoning method specified (for complex tasks)