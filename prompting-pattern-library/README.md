# Prompting Pattern Library

A comprehensive, field-tested library of prompting patterns, failure modes, and model-specific guidance for effective LLM interactions.

**Version**: 1.0 (October 2025)  
**Tested with**: Claude 3.5/4, GPT-4/4o (October 2024), Gemini 1.5 Pro

---

## Quick Start

**New to prompting?** Start with [SKILL.md](SKILL.md) for an overview and quick reference.

**Debugging a prompt?** Jump to [Failure Modes](references/failure-modes.md) for diagnosis and fixes.

**Building cross-model systems?** Check [Model Quirks](references/model-quirks.md) for compatibility guidance.

**Need advanced patterns?** See [Orchestration Patterns](references/orchestration-patterns.md) for agentic workflows.

---

## Contents

### Core Documents

#### [SKILL.md](SKILL.md)
**Purpose**: Quick reference and navigation hub  
**Use when**: Starting a new prompting task, teaching prompting basics, or getting oriented  
**Key sections**:
- Common prompting patterns overview
- Core principles for effective prompting
- Model-specific considerations
- Quick reference to all bundled references

#### [references/prompt-patterns.md](references/prompt-patterns.md)
**Purpose**: Comprehensive catalog of 25+ proven prompting patterns  
**Use when**: Implementing specific prompting techniques, teaching prompting, or troubleshooting approach  
**Key sections**:
- Foundational patterns (zero-shot, few-shot, chain-of-thought)
- Structured output patterns (JSON, tables, delimiters)
- Role and persona patterns
- Advanced reasoning patterns (tree-of-thoughts, self-consistency)
- Quality control patterns (reflection, citation)
- Domain-specific patterns (code review, data analysis)
- Pattern combination strategies

**Cross-references**:
- For failures with these patterns → [Failure Modes](references/failure-modes.md)
- For model compatibility → [Model Quirks](references/model-quirks.md)
- For multi-step orchestration → [Orchestration Patterns](references/orchestration-patterns.md)

#### [references/failure-modes.md](references/failure-modes.md)
**Purpose**: Common prompting failures with diagnosis and fixes  
**Use when**: Debugging problematic prompts, preventing common mistakes, or understanding why a prompt failed  
**Key sections**:
- Ambiguity failures (unclear format, vague criteria, scope issues)
- Assumption failures (implicit context, missing constraints)
- Instruction conflict failures (contradictory requirements)
- Reasoning failures (logic errors, insufficient examples)
- Output quality failures (generic responses, inconsistency)
- Context window failures
- Edge case failures
- Model-specific failures

**Cross-references**:
- To fix with specific patterns → [Prompt Patterns](references/prompt-patterns.md)
- For model-specific workarounds → [Model Quirks](references/model-quirks.md)

#### [references/model-quirks.md](references/model-quirks.md)
**Purpose**: Model-specific guidance for Claude, GPT-4, GPT-4o, and Gemini  
**Use when**: Implementing cross-model systems, optimizing for specific models, or understanding model differences  
**Key sections**:
- Claude strengths and optimal patterns
- GPT-4 strengths and optimal patterns
- GPT-4o multimodal guidance
- Gemini strengths and optimal patterns
- Cross-model considerations
- Model selection decision tree
- Testing across models

**Cross-references**:
- For patterns mentioned → [Prompt Patterns](references/prompt-patterns.md)
- For model-specific failures → [Failure Modes](references/failure-modes.md)

#### [references/orchestration-patterns.md](references/orchestration-patterns.md)
**Purpose**: Advanced patterns for multi-step workflows, agentic systems, and prompt chains  
**Use when**: Building agent systems, orchestrating multi-step tasks, or implementing evaluation loops  
**Key sections**:
- Meta-prompting patterns
- Multi-agent orchestration
- Planner-executor patterns
- Evaluation and refinement loops
- Tool integration patterns
- Memory and state management

**Cross-references**:
- Uses foundational patterns from → [Prompt Patterns](references/prompt-patterns.md)
- For debugging orchestration → [Failure Modes](references/failure-modes.md)
- For model compatibility → [Model Quirks](references/model-quirks.md)

---

## Navigation by Use Case

### I want to...

**Learn prompting from scratch**
1. Read [SKILL.md](SKILL.md) overview
2. Study [Prompt Patterns](references/prompt-patterns.md) - start with Foundational Patterns
3. Review [Failure Modes](references/failure-modes.md) to avoid common mistakes

**Improve an existing prompt**
1. Identify issues in [Failure Modes](references/failure-modes.md)
2. Apply fixes from [Prompt Patterns](references/prompt-patterns.md)
3. Check [Model Quirks](references/model-quirks.md) if using specific model

**Build a multi-step AI workflow**
1. Review [Orchestration Patterns](references/orchestration-patterns.md)
2. Select appropriate patterns from [Prompt Patterns](references/prompt-patterns.md)
3. Test across models using [Model Quirks](references/model-quirks.md) guidance

**Teach prompting to others**
1. Use [SKILL.md](SKILL.md) as curriculum outline
2. Draw examples from [Prompt Patterns](references/prompt-patterns.md)
3. Use [Failure Modes](references/failure-modes.md) for "what not to do" lessons

**Debug a failing prompt**
1. Diagnose issue in [Failure Modes](references/failure-modes.md)
2. Apply recommended pattern from [Prompt Patterns](references/prompt-patterns.md)
3. Check model-specific considerations in [Model Quirks](references/model-quirks.md)

**Optimize for a specific model**
1. Read model section in [Model Quirks](references/model-quirks.md)
2. Adapt patterns from [Prompt Patterns](references/prompt-patterns.md)
3. Avoid model-specific anti-patterns from [Failure Modes](references/failure-modes.md)

---

## Pattern Complexity Levels

### Level 1: Foundational (Start Here)
- Zero-shot prompting
- Few-shot prompting
- Basic chain-of-thought
- Simple role assignment
- Format specification

**Documents**: [SKILL.md](SKILL.md), [Prompt Patterns](references/prompt-patterns.md) sections 1-2

### Level 2: Intermediate
- Structured output patterns
- Multi-step reasoning
- Self-consistency
- Reflection patterns
- Context management

**Documents**: [Prompt Patterns](references/prompt-patterns.md) sections 3-5, [Failure Modes](references/failure-modes.md)

### Level 3: Advanced
- Tree-of-thoughts
- Meta-prompting
- Multi-agent orchestration
- Evaluation loops
- Cross-model optimization

**Documents**: [Prompt Patterns](references/prompt-patterns.md) section 6-7, [Orchestration Patterns](references/orchestration-patterns.md), [Model Quirks](references/model-quirks.md)

---

## Model Version Notes

This library is tested with:
- **Claude 3.5 Sonnet** (June 2024) and **Claude 4 Sonnet** (October 2025)
- **GPT-4** and **GPT-4o** (October 2024 versions)
- **Gemini 1.5 Pro** (September 2024)

Pattern effectiveness may vary with newer model versions. When testing with updated models:
1. Start with foundational patterns (most stable across versions)
2. Test model-specific patterns from [Model Quirks](references/model-quirks.md)
3. Document any changes in behavior
4. Update orchestration patterns if agent capabilities shift

---

## Integration with Tools and Frameworks

This library's patterns integrate with:

**API Integrations**: Function calling patterns work with OpenAI function calls, Claude tool use, and Gemini function declarations

**Agent Frameworks**: Orchestration patterns compatible with LangChain, LlamaIndex, AutoGPT, and custom agent systems

**MCP Servers**: Tool integration patterns apply to Model Context Protocol implementations

**Evaluation Systems**: Reflection and self-consistency patterns support RLHF, evaluation loops, and quality scoring

See [Orchestration Patterns](references/orchestration-patterns.md) for specific integration guidance.

---

## Contributing and Feedback

This is a living document. As models evolve and new patterns emerge, this library should be updated to reflect current best practices.

**Versioning convention**:
- Major version (1.0, 2.0): Significant restructuring or major model changes
- Minor version (1.1, 1.2): New patterns, expanded sections
- Patch (1.1.1): Bug fixes, clarifications, small examples

---

## Quick Reference: Pattern → Use Case Mapping

| Pattern | Best For | Complexity | Document |
|---------|----------|------------|----------|
| Zero-shot | Simple, common tasks | Low | [Patterns](references/prompt-patterns.md#1-zero-shot-prompting) |
| Few-shot | Format specification | Low-Medium | [Patterns](references/prompt-patterns.md#2-few-shot-prompting) |
| Chain-of-thought | Reasoning tasks | Medium | [Patterns](references/prompt-patterns.md#3-chain-of-thought-cot) |
| JSON output | Structured data | Low | [Patterns](references/prompt-patterns.md#4-json-output-specification) |
| Role assignment | Domain expertise | Low | [Patterns](references/prompt-patterns.md#7-expert-role-assignment) |
| Tree-of-thoughts | Complex decisions | High | [Patterns](references/prompt-patterns.md#9-tree-of-thoughts) |
| Self-consistency | High-stakes answers | Medium-High | [Patterns](references/prompt-patterns.md#10-self-consistency) |
| Reflection | Quality assurance | Medium | [Patterns](references/prompt-patterns.md#12-reflection-and-self-critique) |
| Meta-prompting | Prompt optimization | High | [Orchestration](references/orchestration-patterns.md) |
| Planner-executor | Agent systems | High | [Orchestration](references/orchestration-patterns.md) |

---

## License

This prompting pattern library is designed for practical use in AI system development, education, and documentation.