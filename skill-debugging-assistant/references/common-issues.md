# Common Skill Issues and Solutions

This reference provides detailed examples of common skill problems with before/after fixes. Use this when debugging complex or recurring issues.

## Trigger Failure Issues

### Issue 1: Description Too Generic

**Problem:** Skill doesn't trigger because description uses generic terms that don't match user queries.

**Example - Before:**
```yaml
name: data-analyzer
description: Analyzes data and provides insights
```

**Why it fails:**
- "Analyzes data" is too vague (what kind of data?)
- Missing trigger indicators (file types, specific tasks)
- No differentiation from other analysis skills
- Doesn't include terms users would actually say

**Example - After:**
```yaml
name: data-analyzer
description: Analyze CSV and Excel files to identify trends, outliers, and statistical patterns. Use when users request data analysis, statistical summaries, correlation analysis, or exploratory data analysis (EDA) on tabular data files.
```

**Why it works:**
- Specifies file types (.csv, .xlsx)
- Includes task types (trends, outliers, statistical patterns)
- Lists trigger phrases (data analysis, statistical summaries, correlation)
- Clarifies domain (tabular data)

### Issue 2: Missing Synonym Coverage

**Problem:** Skill triggers for some phrasings but not others.

**Example - Before:**
```yaml
name: resume-builder
description: Creates professional resumes in multiple formats
```

**Why it fails:**
- Only mentions "resumes" - misses CV, curriculum vitae
- Doesn't include action verbs users might use (write, make, build, design)
- Missing context about job applications

**Example - After:**
```yaml
name: resume-builder
description: Create, write, or update professional resumes and CVs for job applications. Use when users want to build, design, review, improve, or tailor resumes (or curriculum vitae) for specific positions. Supports multiple formats with ATS optimization.
```

**Why it works:**
- Includes synonyms: resume/CV/curriculum vitae
- Covers action verbs: create, write, update, build, design, review, improve, tailor
- Provides context: job applications, ATS optimization

### Issue 3: Overlapping Skill Descriptions

**Problem:** Two skills have similar descriptions, causing inconsistent triggering.

**Example - Before:**

Skill A:
```yaml
name: document-formatter
description: Formats documents and improves their appearance
```

Skill B:
```yaml
name: style-enhancer
description: Enhances document styling and formatting
```

**Why it fails:**
- Both mention "formatting" and "documents"
- No clear differentiation between the two skills
- User has no way to know which will trigger

**Example - After:**

Skill A:
```yaml
name: document-formatter
description: Apply structural formatting to documents including headings, tables of contents, page numbers, headers/footers, and layout adjustments. Use for structural document organization tasks in Word docs or PDFs.
```

Skill B:
```yaml
name: style-enhancer
description: Enhance visual styling of documents with custom fonts, colors, themes, and brand guidelines. Use for aesthetic improvements and brand consistency across presentations, documents, or marketing materials.
```

**Why it works:**
- Clear scope differentiation: structural vs. visual
- Different trigger terms: structural/layout vs. fonts/colors/themes
- Distinct use cases: organization vs. aesthetics

## False Positive Issues

### Issue 4: Over-Broad Description

**Problem:** Skill triggers for queries outside its intended scope.

**Example - Before:**
```yaml
name: code-helper
description: Helps with coding tasks and programming questions
```

**Why it fails:**
- "Helps with coding" triggers on ANY coding query
- No scope limitation (languages, types of tasks)
- Would trigger even for simple questions about syntax

**Example - After:**
```yaml
name: code-helper
description: Debug complex multi-file codebases and trace execution flow across modules. Use specifically for debugging hard-to-diagnose issues, not for simple syntax questions, code writing, or single-file problems. Focused on Python and JavaScript projects.
```

**Why it works:**
- Narrow scope: complex debugging, multi-file issues
- Explicit exclusions: "not for simple syntax questions"
- Language constraints: Python and JavaScript
- Specific trigger: hard-to-diagnose issues

### Issue 5: Absolute Statements Without Context

**Problem:** Skill applies instructions too broadly, overriding user intent.

**Example - Before:**
```markdown
## Writing Style

ALWAYS use formal academic language.
NEVER use contractions.
ALWAYS include citations for every claim.
```

**Why it fails:**
- No conditional logic or context awareness
- Would apply even when user requests casual tone
- "ALWAYS" overrides user preferences

**Example - After:**
```markdown
## Writing Style

When creating academic research documents:
- Prefer formal academic language
- Avoid contractions in formal sections
- Include citations for factual claims

Adapt the tone based on the document type and user's explicit preferences. For casual documents or when specifically requested, adjust formality accordingly.
```

**Why it works:**
- Conditional: "When creating academic research documents"
- Uses "prefer" and "avoid" instead of "always" and "never"
- Explicit adaptation clause for user preferences

## Instruction Conflict Issues

### Issue 6: Conflicting Instructions Within Skill

**Problem:** Different parts of SKILL.md give contradictory guidance.

**Example - Before:**
```markdown
## Report Structure

Always use the following structure:
1. Executive Summary
2. Methodology
3. Findings
4. Recommendations

## Custom Reports

For financial reports, use this structure:
1. Financial Overview
2. Revenue Analysis
3. Cost Breakdown
4. Projections
```

**Why it fails:**
- "Always use" conflicts with custom structure
- No precedence rules
- Unclear which applies for financial reports

**Example - After:**
```markdown
## Report Structure

### Default Structure

Use this structure unless a specialized format is needed:
1. Executive Summary
2. Methodology
3. Findings
4. Recommendations

### Specialized Formats

For domain-specific reports, adapt the structure. For example, financial reports should use:
1. Financial Overview
2. Revenue Analysis
3. Cost Breakdown
4. Projections

When in doubt, ask the user which format they prefer.
```

**Why it works:**
- Default with exception clause: "unless a specialized format is needed"
- Clear hierarchy: default → specialized
- Escape hatch: "ask the user"

### Issue 7: Critical Information in References

**Problem:** Essential workflow information buried in references that may not be loaded.

**Example - Before:**

SKILL.md:
```markdown
## Creating Reports

1. Gather data
2. Analyze trends
3. Generate report

For detailed analysis methods, see references/analysis-methods.md
```

references/analysis-methods.md:
```markdown
CRITICAL: Always validate data for outliers before analysis.
Never proceed without checking for null values.
```

**Why it fails:**
- Critical validation steps hidden in reference file
- May not be loaded during quick workflows
- User might skip validation unknowingly

**Example - After:**

SKILL.md:
```markdown
## Creating Reports

1. Gather data
2. **Validate data:**
   - Check for outliers
   - Verify no null values in critical fields
   - Confirm data types match expectations
3. Analyze trends (see references/analysis-methods.md for advanced techniques)
4. Generate report

Essential validation steps are above. For optional advanced analysis methods (regression, clustering, etc.), load references/analysis-methods.md.
```

**Why it works:**
- Critical steps in SKILL.md body
- Clear delineation: essential vs. optional
- References for advanced/optional details only

## Structural Issues

### Issue 8: SKILL.md Token Bloat

**Problem:** SKILL.md exceeds 500 lines, consuming too much context.

**Example - Before:**

SKILL.md contains:
- 50 lines of overview
- 200 lines of detailed API documentation
- 150 lines of examples
- 100 lines of edge case handling
- 50 lines of troubleshooting tips

**Why it fails:**
- Detailed API docs should be in references/
- Too many examples in main file
- Edge cases and troubleshooting are reference material

**Example - After:**

SKILL.md (150 lines total):
- 20 lines of overview
- 40 lines of core workflow
- 30 lines of essential examples
- 40 lines of quick reference
- 20 lines pointing to references

references/api-documentation.md:
- Detailed API documentation

references/examples.md:
- Comprehensive example collection

references/troubleshooting.md:
- Edge cases and troubleshooting

**Why it works:**
- SKILL.md contains only essential procedural knowledge
- Detailed information moved to purpose-specific references
- Clear indicators in SKILL.md about when to load each reference

### Issue 9: Missing Trigger Terms in Description

**Problem:** Description doesn't include domain-specific terminology users would naturally use.

**Example - Before:**
```yaml
name: legal-document-helper
description: Assists with legal documents
```

**Why it fails:**
- Doesn't mention specific document types (contracts, NDAs, agreements)
- Missing legal terminology (terms and conditions, clauses)
- No indication of what "assists" means

**Example - After:**
```yaml
name: legal-document-helper
description: Draft, review, and analyze legal contracts, NDAs, terms of service, privacy policies, and agreements. Use when users need help with legal document creation, contract review, clause analysis, or compliance checking. Identifies legal terminology, standard clauses, and potential issues.
```

**Why it works:**
- Lists specific document types: contracts, NDAs, ToS, privacy policies
- Includes legal terms: clauses, compliance, terminology
- Specifies actions: draft, review, analyze
- Clear use cases: creation, review, analysis

### Issue 10: Vague "When to Use" Indicators

**Problem:** Description doesn't clearly specify triggering scenarios.

**Example - Before:**
```yaml
name: image-processor
description: Processes images using various techniques and methods
```

**Why it fails:**
- "Various techniques" is not specific
- No indication of which image tasks trigger it
- Could be anything from basic cropping to ML-based analysis

**Example - After:**
```yaml
name: image-processor
description: Perform image transformations including resize, rotate, crop, format conversion, and basic filters. Use for image manipulation tasks, batch processing multiple images, or format conversions (PNG, JPEG, WebP). Not for AI-based image analysis or generation.
```

**Why it works:**
- Lists specific operations: resize, rotate, crop, format conversion
- Clarifies use cases: manipulation, batch processing, conversions
- Explicit exclusion: "Not for AI-based analysis or generation"
- Specifies supported formats

## Validation Error Issues

### Issue 11: Malformed YAML Frontmatter

**Problem:** YAML syntax errors prevent skill loading.

**Example - Before:**
```yaml
---
name: my-skill
description: This skill helps with analysis,
and provides insights
---
```

**Why it fails:**
- Multi-line description without proper YAML syntax
- Unquoted string with newline breaks YAML parsing

**Example - After:**
```yaml
---
name: my-skill
description: This skill helps with analysis and provides insights into data patterns
---
```

**Why it works:**
- Single-line description
- No unescaped special characters
- Valid YAML syntax

### Issue 12: Name Convention Violations

**Problem:** Skill name doesn't follow kebab-case convention.

**Examples of incorrect names:**
- `Skill_Debugger` (uses underscore)
- `skillDebugger` (uses camelCase)
- `Skill Debugger` (has space)
- `Skill-Debugger` (uses uppercase)

**Correct name:**
- `skill-debugger` (lowercase kebab-case)

## Progressive Disclosure Issues

### Issue 13: Not Leveraging References Effectively

**Problem:** All information crammed into SKILL.md when it could be split.

**Example - Before:**

Single SKILL.md with:
- Core workflow (necessary)
- Complete API reference (could be reference file)
- 20 detailed examples (could be reference file)
- Troubleshooting guide (could be reference file)
- Performance optimization tips (could be reference file)

**Example - After:**

SKILL.md:
```markdown
## Quick Start

[Essential workflow with 2-3 examples]

## Core Operations

[Most common operations with minimal examples]

## Resources

### references/api-reference.md
Complete API documentation. Load when you need detailed parameter information.

### references/examples.md
20+ detailed examples. Load when working on complex or unusual use cases.

### references/troubleshooting.md
Common errors and solutions. Load when debugging issues.

### references/optimization.md
Performance tuning guide. Load when optimizing for speed or resource usage.
```

**Why it works:**
- SKILL.md stays lean with essential information
- References clearly described with when-to-load guidance
- Information organized by purpose
- Progressive loading based on need

## Recommended Diagnostic Process

When encountering any issue:

1. **Start with description analysis** - 80% of trigger issues stem from poor descriptions
2. **Check for absolute statements** - Look for ALWAYS, NEVER, MUST without conditions
3. **Validate structure** - Run automated validation script
4. **Test with real queries** - Try 5+ variations of expected trigger queries
5. **Review similar skills** - Check for description overlap
6. **Analyze token budget** - Ensure SKILL.md is concise (<500 lines)
7. **Verify progressive disclosure** - Confirm proper use of references vs. SKILL.md body
