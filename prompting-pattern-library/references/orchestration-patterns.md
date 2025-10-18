# Orchestration Patterns for Multi-Step AI Workflows

Advanced patterns for building agent systems, prompt chains, and complex multi-step AI workflows.

**Prerequisites**: Familiarity with [foundational patterns](prompt-patterns.md), particularly chain-of-thought and structured output.

---

## Meta-Prompting Patterns

### 1. Prompt Generation
**When to use**: Dynamically creating prompts for downstream tasks based on context.

**Pattern**:
```
You are a prompt engineer. Generate an optimal prompt for [specific task].

Task requirements:
- [Requirement 1]
- [Requirement 2]

The generated prompt should:
1. Use appropriate prompting patterns
2. Include clear success criteria
3. Specify output format
4. Handle edge cases

Output the complete prompt text.
```

**Why it works**: Leverages the model's understanding of effective prompting to create task-specific instructions. Useful when task parameters vary but pattern remains consistent.

**Example application**: Customer support routing system generates category-specific analysis prompts based on ticket type.

**Cross-reference**: Uses [structured output](prompt-patterns.md#4-json-output-specification) and [role assignment](prompt-patterns.md#7-expert-role-assignment) patterns.

---

### 2. Prompt Optimization Loop
**When to use**: Iteratively improving prompts based on output quality.

**Pattern**:
```
Step 1: Execute current prompt
[Current prompt] → [Output 1]

Step 2: Evaluate output quality
Score the output on:
- Accuracy (1-5)
- Completeness (1-5)
- Format adherence (1-5)

Step 3: Identify improvement opportunities
What could make this output better?

Step 4: Revise prompt
Generate improved version incorporating identified improvements.

Step 5: Re-execute
[Improved prompt] → [Output 2]

Step 6: Compare
Is Output 2 meaningfully better? If not, try alternative approach.
```

**Why it works**: Systematic evaluation and refinement catches issues that single-pass prompting misses. The structured loop prevents iterating indefinitely.

**Implementation note**: Set maximum iterations (typically 3-5) to prevent endless refinement.

**Cross-reference**: Combines [reflection](prompt-patterns.md#12-reflection-and-self-critique) with iterative execution.

---

## Multi-Agent Orchestration

### 3. Planner-Executor Pattern
**When to use**: Complex tasks requiring strategic planning before execution.

**Pattern**:
```
# Planner Agent
You are a strategic planner. Given this task, create a detailed execution plan.

Task: [Complex task]

Generate a plan with:
1. High-level approach
2. Ordered sub-tasks
3. Dependencies
4. Success criteria per sub-task
5. Expected outputs

Output as JSON:
{
  "strategy": "overall approach",
  "subtasks": [
    {
      "id": 1,
      "description": "...",
      "dependencies": [],
      "success_criteria": "...",
      "expected_output": "..."
    }
  ]
}

---

# Executor Agent  
You are a task executor. Complete this sub-task from the plan.

Sub-task: [From planner output]
Context: [Relevant context from plan]
Success criteria: [From planner output]

Execute and provide result.
```

**Why it works**: Separation of planning and execution improves both phases. Planning without execution pressure produces better strategies. Execution with clear criteria produces more focused results.

**Scaling note**: For very complex tasks, use multiple specialized executors rather than one general executor.

**Real-world example**: Document analysis system where planner identifies key sections to analyze, then specialized executors handle financial analysis, legal review, and risk assessment in parallel.

**Cross-reference**: Planner uses [hierarchical breakdown](prompt-patterns.md#15-hierarchical-task-breakdown), executor uses domain-specific patterns.

---

### 4. Specialist Collaboration Pattern
**When to use**: Tasks requiring diverse expertise that no single prompt handles well.

**Pattern**:
```
# Coordinator
You are coordinating multiple specialists. Given this problem, determine which specialists to consult and in what order.

Problem: [Complex problem]

Available specialists:
- Technical: Code, architecture, security
- Business: Strategy, market analysis, financials
- Domain: [Specific domain expertise]

Generate consultation plan:
{
  "consultation_order": ["specialist1", "specialist2"],
  "questions_for_each": {...},
  "integration_strategy": "how to combine insights"
}

---

# Technical Specialist
You are a technical specialist. Address these specific questions:
[Questions from coordinator]

Context from other specialists:
[Relevant prior outputs]

---

# Business Specialist  
You are a business specialist. Address these questions:
[Questions from coordinator]

Technical insights:
[Relevant technical analysis]

---

# Synthesizer
Integrate insights from all specialists into coherent recommendation.

Technical perspective: [Summary]
Business perspective: [Summary]
Domain perspective: [Summary]

Generate unified recommendation resolving any conflicts and providing clear next steps.
```

**Why it works**: Different model instances can maintain different perspectives without contradiction. Explicit coordination prevents duplicate work and ensures insights connect.

**Latency consideration**: Serial consultation (one specialist after another) takes longer but produces more integrated results. Parallel consultation (all at once) is faster but may miss connections.

**Cross-reference**: Each specialist uses appropriate [role assignment](prompt-patterns.md#7-expert-role-assignment) and domain patterns.

---

## Evaluation and Refinement Loops

### 5. Generate-Critique-Revise Loop
**When to use**: High-quality outputs requiring multiple passes.

**Pattern**:
```
# Generator
Generate [output type] for [task].

Requirements:
[Specific requirements]

---

# Critic
Evaluate the generated output against these criteria:

Quality dimensions:
- [Dimension 1]: Score and justification
- [Dimension 2]: Score and justification
- [Dimension 3]: Score and justification

Specific improvements needed:
1. [Improvement 1]
2. [Improvement 2]

---

# Reviser
Given the critique, produce improved version addressing:
- [Improvement 1]
- [Improvement 2]

Original output:
[Generator output]

Critique:
[Critic output]

Generate revised version.

---

# Validator
Final check: Does revised version meet all requirements?
- [Requirement 1]: ✓/✗ + explanation
- [Requirement 2]: ✓/✗ + explanation

If any ✗, specify what still needs addressing.
```

**Why it works**: Separation of generation, critique, and revision allows each phase to focus on its task without conflicting objectives. Validation ensures the loop exits with quality output.

**Termination condition**: Maximum 3 revise cycles or validation passes. Prevents endless refinement.

**Cost optimization**: For less critical tasks, skip validator or combine critic and validator roles.

**Cross-reference**: Uses [reflection pattern](prompt-patterns.md#12-reflection-and-self-critique) but separates roles for stronger critique.

---

### 6. Ensemble Evaluation Pattern
**When to use**: High-stakes decisions requiring consensus.

**Pattern**:
```
# Generate multiple solutions
Instance 1: Solve [problem]
Instance 2: Solve [problem] (independent)
Instance 3: Solve [problem] (independent)

---

# Evaluator
Compare the three solutions:

Solution 1: [Summary]
Solution 2: [Summary]
Solution 3: [Summary]

Similarities:
- [Common element 1]
- [Common element 2]

Differences:
- [Divergence 1]
- [Divergence 2]

Confidence assessment:
- Where solutions agree: HIGH confidence
- Where solutions disagree: Investigate further or flag uncertainty

Recommended solution: [Selection with justification]
```

**Why it works**: Agreement across independent solutions indicates reliable answer. Disagreement flags areas needing human review or more investigation.

**Temperature consideration**: Use moderate temperature (0.7-0.8) for diverse perspectives without hallucination risk.

**When to skip**: For simple, well-defined tasks where single solution suffices.

**Cross-reference**: Similar to [self-consistency](prompt-patterns.md#10-self-consistency) but with explicit comparison logic.

---

## Tool Integration Patterns

### 7. Tool Selection and Execution
**When to use**: Agent has access to multiple tools and must choose appropriate ones.

**Pattern**:
```
# Tool Selector
Given this task, determine which tools to use and in what order.

Task: [User request]

Available tools:
- search(query): Web search
- calculator(expression): Math operations
- database_query(sql): Database access
- api_call(endpoint, params): External API

Generate execution plan:
{
  "steps": [
    {
      "tool": "tool_name",
      "params": {...},
      "rationale": "why this tool",
      "expected_output": "what we'll get"
    }
  ],
  "data_flow": "how outputs connect"
}

---

# Executor
Execute step [N] from plan:
Tool: [Tool name]
Parameters: [Parsed parameters]

[Execute tool call]

Result: [Tool output]

---

# Integrator
Given tool results, answer original user request.

Tool outputs:
- Step 1: [Result]
- Step 2: [Result]

User request: [Original request]

Generate natural language response incorporating tool results.
```

**Why it works**: Separating tool selection from execution prevents the model from making execution decisions while processing tool outputs. Clean separation of concerns.

**Error handling**: Include error recovery in executor - if tool fails, report to selector for alternative approach.

**Real-world note**: Most agent frameworks (LangChain, LlamaIndex) implement variants of this pattern. Understanding the pattern helps customize framework behavior.

**Cross-reference**: Tool selector uses [chain-of-thought](prompt-patterns.md#3-chain-of-thought-cot) for planning.

---

### 8. Function Call Orchestration
**When to use**: Coordinating multiple function calls with dependencies.

**Pattern**:
```
# Planner
Analyze the user request and determine function call sequence.

Request: [User request]

Available functions:
[Function schemas]

Generate call graph:
{
  "calls": [
    {
      "function": "function_name",
      "arguments": {...},
      "depends_on": ["call_id_1"],
      "provides": ["data_key_1"]
    }
  ],
  "execution_order": ["call_1", "call_2", "call_3"]
}

---

# Executor (for each call)
Execute function call [N]:
Function: [Function name]
Arguments: [Arguments, substituting results from dependencies]

---

# Response Builder
Given function results, construct user-facing response.

Function outputs:
[All function call results]

Original request:
[User request]

Build natural response that:
1. Directly answers the request
2. Incorporates relevant function outputs
3. Explains any limitations or caveats
```

**Why it works**: Explicit dependency management prevents calling functions with incomplete data. Separating response building from execution keeps function calls clean.

**Parallel execution**: Calls without dependencies can execute in parallel for speed.

**API integration note**: This pattern maps directly to OpenAI function calling, Claude tool use, and Gemini function declarations.

**Cross-reference**: Uses [structured output](prompt-patterns.md#4-json-output-specification) for call planning.

---

## Memory and State Management

### 9. Stateful Conversation Pattern
**When to use**: Multi-turn conversations requiring persistent context.

**Pattern**:
```
# State Manager
Maintain conversation state across turns.

Current state:
{
  "user_goal": "...",
  "gathered_information": {...},
  "pending_questions": [...],
  "conversation_phase": "discovery|analysis|recommendation"
}

User message: [Latest message]

Update state:
1. What new information did we learn?
2. What questions were answered?
3. What new questions arose?
4. Should we change phase?

Updated state:
[New state object]

---

# Response Generator
Given current state, generate next response.

State: [Current state from state manager]

Generate response that:
- Acknowledges new information
- Asks next logical question if needed
- Provides recommendation if sufficient information gathered
- Maintains conversation flow

---

# Turn Tracker
After each turn, persist:
{
  "turn_number": N,
  "state": [Current state],
  "user_message": [User input],
  "assistant_response": [Generated response]
}
```

**Why it works**: Explicit state tracking prevents context drift in long conversations. State updates are deterministic and inspectable.

**Storage**: Store state in database, cache, or session storage. Include timestamps for session timeout.

**Reset conditions**: Allow user to reset state explicitly. Automatically reset after timeout or goal completion.

**Real-world example**: Multi-step forms, diagnostic troubleshooting, requirements gathering.

**Cross-reference**: State manager uses [structured output](prompt-patterns.md#4-json-output-specification) for state representation.

---

### 10. Context Summarization Pattern
**When to use**: Conversations exceeding context window limits.

**Pattern**:
```
# Conversation History
[Turns 1-50]

---

# Summarizer
Summarize the conversation to date, preserving critical information.

Create rolling summary:
{
  "user_goal": "what user is trying to accomplish",
  "key_facts_gathered": [
    "fact 1",
    "fact 2"
  ],
  "decisions_made": [
    "decision 1 with rationale"
  ],
  "current_status": "where we are in the process",
  "next_steps": ["what should happen next"]
}

---

# Next Turn Handler
When user sends next message, use:
- Rolling summary (not full history)
- Last 5 turns (for immediate context)
- New user message

Generate response maintaining continuity.

---

# Update Trigger
After every 10 turns, or when adding turn would exceed context window, regenerate summary incorporating new information.
```

**Why it works**: Preserves semantic meaning while reducing token usage. Allows indefinite conversation length without context window errors.

**Compression ratio**: Typically 10:1 to 20:1 reduction in tokens while preserving key information.

**What to preserve**: User goals, explicit preferences, decisions made, key facts. What to discard: Chitchat, already-resolved questions, superseded information.

**Alternative approach**: Semantic chunking + vector search retrieval. More complex but retrieves relevant history dynamically.

---

## Evaluation Loop Patterns

### 11. Output Validation Chain
**When to use**: Outputs must meet strict criteria before being returned.

**Pattern**:
```
# Generator
Generate [output] per requirements.

---

# Format Validator
Check output format:
- Is it valid [JSON/markdown/etc]?
- Does it match schema?
- Are required fields present?

Pass: ✓ → Send to content validator
Fail: ✗ → Send to repair

---

# Content Validator  
Check output content:
- Does it answer the question?
- Is it factually consistent?
- Does it meet quality criteria?

Pass: ✓ → Send to user
Fail: ✗ → Send to repair with specific issues

---

# Repair Agent
Given validation failures, regenerate output.

Original output: [Failed output]
Issues: [Validation errors]

Regenerate addressing all issues.

→ Send back through validation chain (max 3 attempts)
```

**Why it works**: Explicit validation prevents low-quality outputs from reaching users. Repair loop fixes issues systematically.

**Short-circuit optimization**: If format validation fails, skip content validation. Fix format first.

**Max attempts**: 3 repair attempts is typical. After 3 failures, escalate to human or return error.

**Performance note**: Validation adds latency but dramatically improves reliability for production systems.

---

### 12. A/B Testing Pattern
**When to use**: Comparing prompt variants to optimize performance.

**Pattern**:
```
# Variant A
[Prompt version A]

# Variant B
[Prompt version B]

---

# Evaluator
For each test case, run both variants and compare:

Test case: [Input]

Variant A output: [Output A]
Variant B output: [Output B]

Evaluation criteria:
- Accuracy: A [score] vs B [score]
- Completeness: A [score] vs B [score]
- Format adherence: A [score] vs B [score]
- Latency: A [time] vs B [time]

Winner for this case: [A or B]

---

# Aggregator
Across all test cases:
- Variant A wins: [X%]
- Variant B wins: [Y%]
- Ties: [Z%]

Recommendation: [Deploy variant X because...]

Confidence: [HIGH if >70% wins, MEDIUM if 60-70%, LOW if <60%]
```

**Why it works**: Systematic comparison across diverse test cases reveals which variant performs better in practice, not just theory.

**Test set size**: 20-50 test cases for statistical significance. Include edge cases.

**Automated vs manual eval**: Automated evaluation for objective criteria (format, length). Human evaluation for subjective quality.

**Deployment strategy**: Canary rollout - start with 10% of traffic, monitor, scale up if metrics improve.

---

## Pattern Composition

### 13. Complex System Architecture
**When to use**: Building production AI systems with multiple components.

**Pattern**:
```
User Request
    ↓
[Intent Classifier]
    ↓
[Router: Which workflow?]
    ↓
┌─────────────┬──────────────┬──────────────┐
│  Workflow A │  Workflow B  │  Workflow C  │
└─────────────┴──────────────┴──────────────┘
    ↓
[Each workflow uses planner-executor pattern]
    ↓
[Validation chain ensures quality]
    ↓
[State manager updates conversation state]
    ↓
[Response builder creates user-facing output]
    ↓
[A/B testing evaluates performance]
    ↓
User Response
```

**Component selection guide**:
- **Intent classifier**: Route to appropriate workflow
- **Planner-executor**: Break complex tasks into steps
- **Validation chain**: Ensure output quality
- **State manager**: Track conversation across turns
- **Evaluation loop**: Continuous improvement

**Start simple**: Begin with single workflow, add routing when patterns emerge. Add validation when quality issues arise. Add state management when conversations grow complex.

**Cross-reference**: Combines multiple patterns from this document with foundational patterns from [prompt-patterns.md](prompt-patterns.md).

---

## Model-Specific Orchestration Notes

### Claude Orchestration
- Strong at maintaining state across orchestration steps
- XML structure works well for complex state representation
- Good at following multi-step workflows without drift
- Prefers explicit instructions over implicit handoffs

### GPT-4 Orchestration
- Function calling integrates well with tool patterns
- May need explicit reminders of orchestration position
- Works well with system message as persistent context
- Good at parallel specialist patterns

### Cross-Model Orchestration
- Use structured formats (JSON) for state that moves between models
- Different models for different roles (e.g., Claude for planning, GPT for execution)
- Test handoff points carefully - context may not transfer perfectly

---

## Orchestration Anti-Patterns

**Over-orchestration**: Not every task needs multiple agents. Use single-prompt patterns when sufficient.

**Tight coupling**: Orchestration components should communicate through well-defined interfaces, not implicit assumptions.

**Ignoring latency**: Each orchestration step adds latency. Minimize steps for time-sensitive applications.

**No escape hatch**: Orchestration loops need maximum iteration limits and failure paths.

**Over-complex state**: Track only information needed for decision-making. More state = more maintenance.

---

## Integration with MCP and Agent Frameworks

**MCP Server Implementation**: Tool integration patterns (#7-8) map directly to MCP tool definitions. State management (#9-10) maps to MCP resource concepts.

**LangChain Integration**: These patterns underlie LangChain's chains, agents, and memory abstractions. Understanding patterns helps customize framework behavior.

**Custom Implementations**: For non-framework systems, these patterns provide blueprints for building orchestration from scratch.

---

## Performance Optimization

**Parallel execution**: Run independent steps concurrently
**Caching**: Cache intermediate results for repeated sub-tasks  
**Early termination**: Exit evaluation loops as soon as quality threshold met
**Lazy loading**: Load context only when needed, not upfront
**Batching**: Group similar operations for efficiency

---

## Testing Orchestrated Systems

1. **Unit test**: Each component independently
2. **Integration test**: Component handoffs
3. **End-to-end test**: Full workflow with real inputs
4. **Failure test**: How system handles component failures
5. **Load test**: Performance under concurrent requests

**Test data**: Include happy path, edge cases, adversarial inputs, and failure scenarios.

---

## Version History

- **v1.0** (October 2025): Initial orchestration patterns for agent systems