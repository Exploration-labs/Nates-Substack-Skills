# Advanced Chunking Patterns Reference

This reference provides additional chunking strategies and decision frameworks for complex scenarios not covered in the main skill.

## Advanced Chunking Strategies

### 6. Layered Abstraction

**Best for:** Tasks requiring different levels of detail for different audiences

**Example scenario:** Creating both executive summary and detailed technical analysis

**Approach:**
- Session 1: High-level executive summary (research + draft)
- Session 2: Deep technical details (research + draft)
- Session 3: Supporting appendices and data tables

**Benefits:** Allows prioritization of most important layer first, can stop after any session if time-constrained

### 7. Hub-and-Spoke

**Best for:** Central theme with multiple independent supporting analyses

**Example scenario:** Company overview with deep dives into each business unit

**Approach:**
- Session 1: Core company profile (central hub)
- Session 2-N: Individual business unit analyses (spokes)
- Final session: Integration and cross-unit insights

**Benefits:** Hub provides context for all spokes; spokes can be tackled in any order

### 8. Dependency-Aware Sequencing

**Best for:** Multi-step processes where later steps depend on earlier decisions

**Example scenario:** Market entry strategy requiring market research → target selection → go-to-market plan

**Approach:**
- Explicitly map dependencies upfront
- Complete foundational analysis first
- Use findings to inform subsequent sessions
- Document decisions between sessions

**Benefits:** Ensures quality by building on validated foundations

### 9. Spiral Development

**Best for:** Complex creative projects benefiting from multiple refinement passes

**Example scenario:** Building a comprehensive training curriculum

**Approach:**
- Pass 1: Complete curriculum structure at high level (all modules outlined)
- Pass 2: Develop 50% of content in depth
- Pass 3: Develop remaining 50% in depth
- Pass 4: Quality pass and polish

**Benefits:** Maintains holistic view while making steady progress; can adjust scope mid-project

### 10. Resource Preloading

**Best for:** Tasks requiring heavy context that will be referenced throughout

**Example scenario:** Analyzing code changes across a large codebase

**Approach:**
- Session 0: Load and understand architecture/key files (no deliverable)
- Session 1-N: Actual analysis work with preloaded context
- Optimization: Summarize key context to carry forward efficiently

**Benefits:** Amortizes context loading cost across multiple work sessions

## Decision Framework for Strategy Selection

### Task Classification Matrix

| Task Characteristics | Recommended Strategy | Second Choice |
|---------------------|---------------------|---------------|
| Time-ordered data | Sequential Processing | Hub-and-Spoke |
| Multi-dimensional analysis | Dimensional Breakdown | Layered Abstraction |
| Large volume, pattern-finding | Subset Sampling | Sequential Processing |
| Independent parallel work | Parallel Track | Hub-and-Spoke |
| Requires iteration | Depth Progression | Spiral Development |
| Complex dependencies | Dependency-Aware | Sequential Processing |
| Mixed audience needs | Layered Abstraction | Depth Progression |
| Central + supporting topics | Hub-and-Spoke | Dimensional Breakdown |

### Hybrid Approaches

Real-world tasks often benefit from combining strategies:

**Example: Quarterly business review across 5 departments**

Hybrid approach:
1. Sequential (by quarter) + Parallel Track (by department)
2. Structure: Q1 Dept A-B, Q1 Dept C-E, Q2 Dept A-B, Q2 Dept C-E, etc.

**Example: Product comparison with deep research**

Hybrid approach:
1. Depth Progression (outline → content) + Parallel Track (by product)
2. Structure: Outline all products, develop Product A deep, develop Product B deep, synthesize

## Estimation Refinement Techniques

### Interactive Scoping

When task size is unclear, use a scoping conversation:

```
"Before I start, let me understand the scope to plan this well:
- Depth: Are you looking for [surface-level summary] or [detailed analysis with citations]?
- Breadth: Should I cover [subset] or [comprehensive coverage]?
- Output: Do you need [bullet points] or [formatted report/presentation]?

Your answers help me estimate whether we should chunk this task."
```

### Token Checkpoints

For borderline tasks, establish checkpoints:

```
"This might be achievable in one session, but it's close. I'll:
1. Complete the first major section
2. Check token usage at that point
3. Decide whether to continue or split remaining work

Sound good?"
```

### Progressive Disclosure with User

Don't present all options at once:

```
"This will exceed our token budget. I see two promising approaches:
A. Split by time period (quarters)
B. Split by analysis type (quantitative vs qualitative)

Which makes more sense for your needs?"
```

## Chunking Anti-Patterns

Avoid these common mistakes:

### ❌ Arbitrary Splits

**Bad:** "Let's do half now and half later"
**Why it fails:** No logical boundary, hard to resume coherently
**Better:** Identify natural boundaries (themes, time periods, categories)

### ❌ Unequal Chunks

**Bad:** Session 1 is 80% of work, Session 2 is 20%
**Why it fails:** Defeats purpose of chunking; Session 1 still exceeds budget
**Better:** Balance work across sessions to ~60-70% of budget each

### ❌ Chunk Interdependence

**Bad:** Session 2 requires re-analyzing everything from Session 1
**Why it fails:** Duplicates work, compounds token costs
**Better:** Design chunks to be relatively self-contained

### ❌ No Synthesis Plan

**Bad:** Create 5 independent analyses with no plan to integrate
**Why it fails:** User left to connect dots; misses overarching insights
**Better:** Always include final integration/synthesis session

### ❌ Over-Chunking

**Bad:** Split a 70% budget task into 4 mini-sessions
**Why it fails:** Overhead of context switching; destroys flow
**Better:** Only chunk when necessary (80%+ budget risk)

## Context Handoff Techniques

### Effective Session Summaries

At end of each chunk, provide:

1. **What was completed:** Specific deliverables and findings
2. **Key insights:** 3-5 critical points to carry forward
3. **Next session focus:** Clear starting point
4. **Open questions:** Unresolved items to address

**Example:**
```
Session 1 complete. We analyzed Q1-Q2 revenue data and found:
- 15% growth in Q2 driven by enterprise segment
- Consumer segment flat YoY
- Churn increased 3% in May (investigate further)

Next session: Analyze Q3-Q4 with focus on:
- Did enterprise growth continue?
- What happened with consumer rebound efforts?
- Did churn stabilize?
```

### User-Driven Handoffs

Coach users on what to say when resuming:

```
"When you're ready for Part 2, start a new conversation and say:
'Continue the Q3-Q4 analysis. In Part 1, we found [X, Y, Z]. Here are the Q3-Q4 files: [upload]'

This gives me the context I need to pick up smoothly."
```

## Special Considerations

### Working with External Tools

When chunking involves external tool research:

- **Front-load research**: Do heavy web searches early to inform all sessions
- **Document sources**: Save URLs/citations to reference across sessions
- **Cache findings**: Summarize research to avoid re-searching same topics

### Artifact-Heavy Tasks

When creating large artifacts (decks, documents):

- **Template first**: Establish structure/template in Session 1
- **Parallel development**: Can work on different sections independently
- **Final polish separate**: Reserve last session for formatting/refinement

### Real-Time Collaboration

If user wants to work synchronously through chunks:

- **Time-box sessions**: "Let's spend ~15 min on each section"
- **Quick transitions**: Minimize handoff overhead between chunks
- **Live pivots**: Be ready to adjust plan based on findings

## Measuring Success

Good chunking strategies should:

✅ Complete within token budget for each session
✅ Produce valuable interim deliverables (not just work-in-progress)
✅ Minimize redundant work across sessions
✅ Feel natural to resume (clear continuity)
✅ Allow flexibility to reprioritize between sessions

Poor chunking feels like:

❌ Constantly running out of tokens mid-session
❌ Extensive recap needed to resume work
❌ Deliverables only make sense when all chunks complete
❌ Frequent context re-loading of same information
