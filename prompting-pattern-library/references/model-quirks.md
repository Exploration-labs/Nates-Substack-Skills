# Model-Specific Prompting Guidance

Different LLMs have unique characteristics that affect optimal prompting strategies. This reference covers model-specific patterns, anti-patterns, and considerations.

## Claude (Anthropic)

### Strengths
- Excellent at following complex, multi-part instructions
- Strong with structured output (JSON, XML, tables)
- Good at maintaining context over long conversations
- Handles nuanced, thoughtful tasks well
- Strong reasoning with explicit chain-of-thought
- Tends to be more cautious about uncertain information

### Optimal Patterns

**Conversational Tone**:
Claude responds well to polite, conversational prompts:
```
I need help analyzing this dataset. Could you:
1. Identify trends
2. Flag anomalies
3. Suggest next steps

Here's the data: [data]
```

**Structured Instructions**:
Claude excels with clearly structured, numbered instructions:
```
Analyze this contract for risk. Structure your analysis as:

## 1. Critical Risks
[List high-severity issues]

## 2. Moderate Concerns
[List medium-severity issues]

## 3. Recommendations
[Specific actions to mitigate risks]
```

**XML for Complex Structure**:
For very complex structured data, Claude works well with XML:
```
Extract information and format as:

<analysis>
  <summary>Brief overview</summary>
  <findings>
    <finding severity="high">Finding 1</finding>
    <finding severity="medium">Finding 2</finding>
  </findings>
  <recommendations>
    <recommendation priority="1">Action 1</recommendation>
  </recommendations>
</analysis>
```

### Anti-Patterns for Claude

**Over-assertiveness**: Claude may be overly cautious if pushed too hard:
```
❌ BAD: "You MUST give me an answer, even if you're not sure"
✅ GOOD: "If you're uncertain, please provide your best assessment and note the uncertainty"
```

**Excessive brevity requests**: Asking for extreme brevity may sacrifice quality:
```
❌ BAD: "Answer in 10 words exactly"
✅ GOOD: "Answer briefly, around 20-30 words"
```

### Claude-Specific Tips
- Use "Let's think step by step" for complex reasoning
- Prefers markdown formatting for readability
- Good at catching its own errors if asked to review
- Works well with iterative refinement prompts

---

## GPT-4 (OpenAI)

### Strengths
- Versatile across wide range of tasks
- Strong creative writing capabilities
- Good instruction following
- Handles diverse domains well
- Fast response time
- Good at code generation

### Optimal Patterns

**Direct Instructions**:
GPT-4 works well with direct, imperative instructions:
```
Generate 5 unique product names for an AI-powered scheduling tool.

Requirements:
- Under 10 characters
- Easy to pronounce
- Not generic words
- Available as .com domain (check)
```

**System Message + User Prompt**:
For tasks requiring consistent behavior, use system message:
```
System: You are a technical writing expert who specializes in API documentation.

User: Review this API endpoint documentation for clarity and completeness.
```

**Temperature Control Hints**:
When creativity matters, hint at it:
```
Brainstorm creative, unconventional solutions to [problem]. Think outside the box and don't limit yourself to obvious approaches.
```

### Anti-Patterns for GPT-4

**Overconfident errors**: GPT-4 may state incorrect info confidently:
```
❌ RISKY: "What is X?" (may confidently give wrong answer)
✅ SAFER: "What is X? Include confidence level and note if uncertain."
```

**Verbose without bounds**: Can be unnecessarily wordy:
```
❌ BAD: "Explain X"
✅ GOOD: "Explain X in under 150 words"
```

### GPT-4 Specific Tips
- Benefits from explicit word count limits
- Works well with "As a [role]" framing
- Good with role-play scenarios
- May need explicit instruction to avoid verbosity
- Benefits from examples of desired tone

---

## GPT-4o (OpenAI Multimodal)

### Strengths
- Excellent multimodal capabilities (vision + text)
- Strong at interpreting charts, diagrams, screenshots
- Good at code from images
- Fast response time

### Optimal Patterns for Vision Tasks

**Image Analysis**:
```
Analyze this diagram and:
1. Describe the overall structure
2. Identify key components
3. Explain relationships between components
4. Note any issues or inconsistencies
```

**Screenshot to Code**:
```
Convert this screenshot to HTML/CSS code.

Requirements:
- Responsive design
- Use Tailwind CSS
- Match colors as closely as possible
- Include hover states visible in the screenshot
```

**Chart Data Extraction**:
```
Extract data from this chart:
1. Identify chart type
2. Extract all data points as JSON
3. Note any trends or patterns
4. Flag data quality issues (missing labels, unclear scales)
```

### Vision-Specific Anti-Patterns

**Asking for precision beyond image quality**:
```
❌ BAD: "Extract exact hex codes from this low-res image"
✅ GOOD: "Identify approximate colors from this image (e.g., 'dark blue', 'light gray')"
```

---

## Gemini (Google)

### Strengths
- Strong analytical capabilities
- Good at structured tasks
- Excellent at following complex instructions
- Good at code generation and debugging
- Strong with factual, knowledge-based queries

### Optimal Patterns

**Structured Analytical Tasks**:
```
Analyze this dataset for:

Structure:
- Data types per column
- Missing value patterns
- Key statistics

Insights:
- Notable correlations
- Outliers
- Data quality issues

Recommendations:
- Cleaning steps needed
- Suggested analyses
```

**Step-by-Step Breakdowns**:
Gemini works well with explicit step structures:
```
Solve this problem using these steps:

Step 1: Understand the requirements
Step 2: Identify constraints
Step 3: Propose 3 solutions
Step 4: Compare tradeoffs
Step 5: Recommend best solution
```

### Anti-Patterns for Gemini

**Over-complex creative prompts**: May struggle with very abstract creative tasks:
```
❌ CHALLENGING: "Write a surrealist poem exploring quantum consciousness"
✅ BETTER: "Write a technical explanation of quantum computing in poetic form"
```

### Gemini-Specific Tips
- Excels at analytical and structured tasks
- Benefits from clear formatting requirements
- Good at factual question answering
- Works well with explicit reasoning requests

---

## Cross-Model Considerations

### When Model Choice Matters Most

**Creative Writing**: GPT-4 slight edge
**Code Generation**: Claude and GPT-4o both strong
**Long-Context Reasoning**: Claude edge
**Multimodal Tasks**: GPT-4o clear advantage
**Analytical Tasks**: All three strong, Gemini slight edge
**Following Complex Instructions**: Claude slight edge
**Speed**: GPT-4o and Gemini faster

### Universal Best Practices (All Models)

1. **Be Explicit**: State requirements clearly
2. **Provide Examples**: Show desired output for format-specific tasks
3. **Request Reasoning**: Ask for step-by-step thinking on complex tasks
4. **Specify Constraints**: State all requirements and limitations
5. **Iterate**: Start simple, refine based on results

### Format Specificity Across Models

**JSON Output** - Critical differences:

**Claude**:
```
Respond ONLY with valid JSON. Do not include explanations outside the JSON structure.

{"field": "value"}
```

**GPT-4**:
```
You must respond with valid JSON only. Do not include markdown code fences (```json) or any text outside the JSON object.
```

**Gemini**:
```
Output valid JSON only. Your entire response should be parseable JSON with no additional text.
```

### Temperature/Creativity Control

Models interpret creativity hints differently:

**High Creativity Needed**:
```
For Claude: "Think creatively and explore unconventional approaches"
For GPT-4: "Brainstorm innovative, outside-the-box solutions"
For Gemini: "Generate diverse solutions, including unconventional approaches"
```

**High Precision Needed**:
```
For Claude: "Prioritize accuracy and precision over creativity"
For GPT-4: "Provide factual, well-supported answers with citations"
For Gemini: "Focus on analytical rigor and evidence-based conclusions"
```

---

## Model Selection Decision Tree

```
Need multimodal (image + text)?
└─ YES → GPT-4o
└─ NO → Continue

Need very long context (100K+ tokens)?
└─ YES → Claude
└─ NO → Continue

Need fastest response?
└─ YES → GPT-4o or Gemini
└─ NO → Continue

Need complex instruction following?
└─ YES → Claude
└─ NO → Continue

Need creative writing?
└─ YES → GPT-4
└─ NO → Continue

Need structured analytical task?
└─ YES → All strong (Gemini slight edge)
└─ NO → Any model fine
```

---

## Testing Across Models

When implementing a prompt that must work across models:

1. **Test with simplest model first** (baseline)
2. **Identify model-specific failures**
3. **Adjust for most restrictive model** (narrowest capabilities)
4. **Verify all models handle result**

Example cross-model compatible prompt:
```
Analyze the following data.

Instructions:
1. Identify top 3 trends
2. Flag 2-3 anomalies
3. Provide 2 recommendations

Format your response as:

Trends:
1. [Trend]
2. [Trend]  
3. [Trend]

Anomalies:
- [Anomaly]
- [Anomaly]

Recommendations:
- [Recommendation]
- [Recommendation]

Data: [data]
```

This pattern works well across all models because:
- Clear structure
- Numbered steps
- Explicit format
- No model-specific quirks
- Bounded output

---

## Future-Proofing Prompts

As models improve, prompts should:
- Avoid assuming specific model limitations
- Focus on clear requirements rather than workarounds
- Use standard formats (JSON, Markdown) over proprietary
- Test across models periodically
- Document model-specific issues separately

**Pattern for maintainable prompts**:
```
# Core prompt (model-agnostic)
[Task description]
[Requirements]
[Format specification]

# Model-specific notes (comment in code)
# Claude: Works well as-is
# GPT-4: May need explicit brevity constraint
# Gemini: Strong performance on analytical aspects
```