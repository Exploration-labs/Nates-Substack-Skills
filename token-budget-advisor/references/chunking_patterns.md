# Chunking Patterns Reference

This document provides detailed strategies for chunking complex tasks to manage token budgets effectively.

## Sequential Processing

**Best for:** Time-series data, chronological analysis, ordered datasets

**Pattern:**
1. Divide by natural time boundaries (quarters, years, months)
2. Process each segment independently
3. Synthesize findings at the end

**Example:**
- "Let's analyze Q1-Q2 first, then Q3-Q4"
- "I'll review January-June, then July-December"
- "Starting with 2023 data, then moving to 2024"

**Communication template:**
> "This analysis spans [timeframe]. I recommend splitting into [N] parts: [list parts]. Should I start with [first part]?"

## Dimensional Breakdown

**Best for:** Multi-faceted analysis, complex comparisons, thematic reviews

**Pattern:**
1. Identify key dimensions (themes, categories, metrics)
2. Analyze each dimension separately
3. Cross-reference and synthesize

**Example:**
- "Let's examine financial health first, then operational efficiency, then market position"
- "I'll analyze technical feasibility, then cost implications, then timeline"
- "First pass: data quality. Second pass: insights extraction"

**Communication template:**
> "This requires analyzing [N] dimensions: [list]. I'll tackle [dimension 1] first, which covers [scope]. Continue with that?"

## Iterative Refinement

**Best for:** Long documents, comprehensive reports, creative content

**Pattern:**
1. Create outline or structure
2. Draft core sections
3. Refine and add detail in subsequent passes

**Example:**
- "First: outline with headers and key points"
- "Second: draft main sections"
- "Third: add supporting detail and polish"

**Communication template:**
> "For a comprehensive [output type], I'll use an iterative approach: [outline steps]. This ensures quality while managing token usage. Start with the outline?"

## Divide and Conquer

**Best for:** Multiple independent files, parallel analyses, comparative studies

**Pattern:**
1. Process subset A independently
2. Process subset B independently
3. Compare/synthesize results

**Example:**
- "Analyze competitor A's docs, then competitor B's docs, then compare"
- "Review technical docs first, business docs second"
- "Process first half of files, then second half"

**Communication template:**
> "I'll analyze [subset A] first ([N] files), then [subset B] ([M] files). This gives us focused insights before the comparison. Ready to start with [subset A]?"

## Focused Deep Dive

**Best for:** Single complex file requiring thorough analysis, detailed code review

**Pattern:**
1. Initial scan for structure and overview
2. Deep analysis of critical sections
3. Comprehensive pass on remaining sections

**Example:**
- "First: scan the document structure and executive summary"
- "Second: deep dive on the methodology section"
- "Third: analyze findings and recommendations"

**Communication template:**
> "This [document/codebase] needs careful attention. I'll start with [high-level overview], then focus on [critical sections], then [comprehensive pass]. This approach ensures I catch important details. Begin?"

## Incremental Artifact Building

**Best for:** Large spreadsheets, complex presentations, multi-page documents

**Pattern:**
1. Build core structure/template
2. Populate main sections iteratively
3. Add polish and supporting elements

**Example:**
- "Create workbook structure with tabs and headers"
- "Populate financial data sections"
- "Add visualizations and formatting"

**Communication template:**
> "I'll build this [artifact type] in stages: [stage 1: structure], [stage 2: core content], [stage 3: refinement]. This ensures we can review and adjust between stages. Start with the structure?"

## Hybrid Approaches

Most complex tasks benefit from combining patterns:

**Research + Synthesis:**
1. Gather information (sequential searches)
2. Organize by theme (dimensional)
3. Draft report (iterative refinement)

**Multi-File Analysis + Report:**
1. Process files in batches (divide and conquer)
2. Extract key themes (dimensional)
3. Build comprehensive report (iterative)

## Estimation Guidelines

Use these heuristics to gauge when chunking is needed:

**High risk (almost certainly chunk):**
- 5+ large files uploaded AND request for comprehensive analysis
- Request for "complete," "thorough," "detailed" report
- 10+ tool calls likely needed
- Output artifact expected to be >1000 lines
- Multiple passes needed (analysis → synthesis → formatting)

**Medium risk (consider chunking):**
- 3-4 files uploaded with analysis request
- 5-8 tool calls likely needed
- Output artifact 500-1000 lines
- Complex multi-step workflow

**Low risk (probably fine):**
- 1-2 files with focused question
- <5 tool calls needed
- Output under 500 lines
- Single-focus task

## Selection Decision Tree

```
Is the task complex with multiple aspects?
├─ YES → Use Dimensional Breakdown or Divide and Conquer
└─ NO → Continue

Does the task involve time-series or ordered data?
├─ YES → Use Sequential Processing
└─ NO → Continue

Is the output a long document/artifact?
├─ YES → Use Iterative Refinement or Incremental Building
└─ NO → Continue

Does the task require deep analysis of a single complex item?
├─ YES → Use Focused Deep Dive
└─ NO → Task may not need chunking
```
