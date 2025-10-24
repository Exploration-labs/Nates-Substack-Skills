# Known Skill Patterns and Effective Combinations

This reference documents empirically-validated skill combinations and workflow patterns.

## Common Workflow Patterns

### Document Creation Pipeline
**Pattern**: Research → Write → Format → Review

**Typical Skills**:
- Research phase: Skills with `web_search`, `google_drive_search`
- Writing phase: Skills with `docx`, `markdown` formats
- Formatting phase: Skills with document styling capabilities
- Review phase: Skills with text analysis features

**Token Efficiency**: Use research skills first, then clear context before document creation

### Data Analysis Pipeline
**Pattern**: Extract → Transform → Analyze → Visualize → Report

**Typical Skills**:
- Extract: Skills handling `xlsx`, `csv`, `pdf` extraction
- Transform: Skills with data processing scripts
- Analyze: Skills with calculation/formula capabilities
- Visualize: Skills creating charts/graphs
- Report: Skills generating formatted outputs

**Optimization**: Batch data extraction before analysis to minimize tool switching

### Presentation Development Pipeline
**Pattern**: Content → Structure → Design → Polish

**Typical Skills**:
- Content: Research and content generation skills
- Structure: Outlining and organization skills
- Design: `pptx` skills with template/theme support
- Polish: Editing and formatting skills

**Best Practice**: Finalize content before design to avoid rework cycles

## Anti-Patterns to Avoid

### Redundant Format Conversions
**Problem**: Multiple skills converting between same format pairs
**Impact**: Increased tool calls, inconsistent results
**Solution**: Standardize on single conversion approach per format pair

### Circular Dependencies
**Problem**: Skill A requires output from Skill B, which requires output from Skill A
**Impact**: Workflow deadlock
**Solution**: Identify and break circular chains; use intermediate formats

### Premature Optimization
**Problem**: Loading multiple heavy skills "just in case"
**Impact**: Token budget exhaustion
**Solution**: Load skills progressively as needed

## High-Synergy Combinations

### Document + Research
Skills handling document formats paired with web/drive search create efficient research reports.

### Spreadsheet + PDF
Skills reading PDFs and populating spreadsheets enable data extraction workflows.

### Code + Web
Development skills paired with web tools enable reference-driven coding.

### Presentation + Data
Presentation skills with data visualization create data-driven decks.

## Token Budget Management Strategies

### Progressive Loading
1. Load only core workflow skill initially
2. Add supporting skills as needed
3. Unload completed workflow skills

### Skill Chunking
For complex workflows, break into phases:
- Phase 1: Research (load research skills)
- Phase 2: Creation (unload research, load creation skills)
- Phase 3: Finalization (load only formatting skills)

### Reference File Usage
Skills with large SKILL.md files should:
- Keep core workflow in SKILL.md (<500 lines)
- Move examples to reference files
- Load references only when specific patterns needed

## Performance Optimization Patterns

### Batch Operations
When multiple items need same skill:
- Process all items in single activation
- Avoid repeated skill loading/unloading

### Tool Call Minimization
- Combine related operations in single tool call
- Cache intermediate results when possible
- Use scripts for repetitive operations

### Format Standardization
Within workflow, standardize on minimal format set:
- Reduces skill activation overhead
- Simplifies tool chain
- Improves reliability
