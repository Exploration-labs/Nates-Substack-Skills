# Decision Examples

This document provides concrete examples of when to offer skill capture vs. when to continue without offering.

## Context Window ROI Calculation

**Key insight**: A skill is worth capturing if:
- It will be reused 10+ times over multiple conversations
- Each reuse saves 500+ tokens of re-explanation
- The skill itself costs <5000 tokens to load

**ROI formula**: (Reuse_frequency × Tokens_saved) - Skill_token_cost > 0

## High-Confidence Capture Scenarios (OFFER)

### Example 1: Third Instance of Similar Task

**Context**: User has asked me to write internal comms docs three times, each with similar structure (context → update → action items → FAQ)

**Signal**: 
- Pattern has repeated 3 times ✓
- Structure is consistent ✓
- Likely to recur (ongoing company communications) ✓
- Each time requires re-explaining structure (~800 tokens) ✓

**Offer**: "I notice I've structured the last three internal comms documents in a similar way. Would it be helpful to capture this as a skill for future internal communications?"

**Expected ROI**: High - saves ~800 tokens per future use, likely 20+ uses

---

### Example 2: Complex Domain Knowledge Synthesis

**Context**: Through several conversations, user has explained their data pipeline architecture, table schemas, and common query patterns

**Signal**:
- Information spans multiple conversations ✓
- Requires significant context to re-explain (2000+ tokens) ✓
- User frequently asks data-related questions ✓
- Knowledge is stable (schemas don't change weekly) ✓

**Offer**: "I've built up understanding of your data architecture across our conversations. Would it be useful to formalize this as a skill so I can reference your schemas and patterns more efficiently in future conversations?"

**Expected ROI**: Very high - saves 2000+ tokens, dozens of potential uses

---

### Example 3: Novel Workflow with Clear Reusability

**Context**: User asked me to analyze a messy CSV with inconsistent formatting. I developed a multi-step validation → cleaning → analysis approach that worked well.

**Signal**:
- Workflow is novel and non-obvious ✓
- Problem type is clearly recurring (user mentions "I have lots of these CSVs") ✓
- Approach requires 1000+ tokens to explain each time ✓
- Generalizes beyond this specific file ✓

**Offer**: "The validation and cleaning approach I used here seems like it would work well for your other messy data files. Should I capture this as a skill for handling similar datasets?"

**Expected ROI**: High - user explicitly mentioned recurring need, saves 1000+ tokens per use

---

### Example 4: Workflow Optimization Pattern

**Context**: User asked me to generate a report from data. I developed an efficient pattern: fetch data → validate → analyze → format → generate visual summary. User seemed pleased with the comprehensive output.

**Signal**:
- Workflow chains multiple steps efficiently ✓
- User asked similar question before ✓
- Pattern produces notably better results than simpler approaches ✓
- Easy to apply to similar reporting tasks ✓

**Offer**: "I developed a multi-step reporting workflow here that seems to work well. Would you like me to formalize this for future data reporting tasks?"

**Expected ROI**: Medium-high - saves ~600 tokens, 10+ potential uses

## Low-Confidence Scenarios (DO NOT OFFER)

### Example 5: One-Off Creative Solution

**Context**: User asked me to generate a haiku about their cat Mr. Whiskers. I wrote a creative haiku.

**Signal**:
- ✗ Task is highly specific to this instance
- ✗ No pattern of repetition
- ✗ Solution doesn't generalize (writing haikus about cats generally? too broad)
- ✗ Low reuse probability

**Action**: Do NOT offer capture. This is creative work, not a reusable pattern.

---

### Example 6: Simple Task I Already Know

**Context**: User asked me to format some text as a bulleted list.

**Signal**:
- ✗ This is basic functionality I already have
- ✗ No novel approach involved
- ✗ No meaningful tokens to save

**Action**: Do NOT offer capture. No marginal value over existing capabilities.

---

### Example 7: Context-Specific Solution

**Context**: User asked me to fix a specific bug in their Python code related to a third-party library version conflict.

**Signal**:
- ✗ Highly context-specific to this codebase and library version
- ✗ Unlikely to recur in identical form
- ✗ Solution doesn't generalize to other contexts
- ✗ Low reusability

**Action**: Do NOT offer capture. Too specific to be reusable.

---

### Example 8: Ambiguous Reusability

**Context**: User asked me to draft an email to their manager about a project delay. I wrote a clear, professional email.

**Signal**:
- ✗ First time doing this type of task
- ? Might recur, but not clear (is this a pattern or one-off?)
- ✗ No strong signal of repetition yet

**Action**: Do NOT offer capture yet. Wait to see if they ask for similar emails 2+ times before offering.

---

### Example 9: Already Covered by Existing Skills

**Context**: User asked me to create a presentation with company branding. I used the brand-guidelines skill.

**Signal**:
- ✗ Existing skill already handles this
- ✗ No novel approach beyond what skill provides

**Action**: Do NOT offer capture. Would be redundant with existing skill.

## Recognition Patterns

### Strong Reusability Signals

✓ "I have lots of these [files/tasks/problems]"
✓ "We do this [weekly/monthly/regularly]"
✓ "Can you do the same thing you did for [previous task]?"
✓ Third or fourth instance of similar task
✓ User explicitly mentions this is an ongoing need
✓ Complex domain knowledge spanning multiple conversations

### Weak Reusability Signals

✗ First instance of a task
✗ Highly creative or one-off request
✗ Simple task using existing capabilities
✗ User says "just this once" or similar
✗ Context-specific solution that won't generalize

## Decision Threshold

**Offer skill capture when**:
- Confidence that it will save 10%+ of context window over 10+ uses: >95%
- AND one of:
  - Pattern has repeated 2+ times already
  - User explicitly indicates recurring need
  - Complex domain knowledge worth formalizing
  - Novel workflow with clear generalizability

**Do not offer when**:
- First instance of a pattern
- Highly context-specific
- Trivial or already well-covered by existing capabilities
- Creative/one-off work
- Ambiguous reusability
