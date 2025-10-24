# Consistency Rules Reference

Detailed validation rules for ensuring skill quality and consistency.

## Frontmatter Validation

### Required Fields
- **name**: Must be present and non-empty
  - Format: lowercase with hyphens (e.g., `skill-name`)
  - No spaces or underscores
  - Example: `pdf-editor` ✅, `PDF Editor` ❌, `pdf_editor` ❌

- **description**: Must be present and non-empty
  - Minimum length: 50 characters (warning if shorter)
  - Maximum length: 500 characters (info if longer)
  - Must start with capital letter
  - Should include trigger phrases (`when`, `use`)

### Optional But Recommended
- **license**: Legal terms reference
- **version**: Semantic versioning

## Description Quality

### Content Requirements
1. **Specificity**: Avoid vague terms
   - ❌ "various tasks"
   - ✅ "spreadsheet formulas and data visualization"

2. **Trigger Clarity**: Include when/how to use
   - ❌ "Helps with documents"
   - ✅ "When Claude needs to create, edit, or review .docx files"

3. **Completeness**: Cover key capabilities
   - What does it do?
   - When should it be used?
   - What are the main features?

### Length Guidelines
- **Too short** (<50 chars): Missing essential details
- **Ideal** (50-200 chars): Concise and complete
- **Good** (200-500 chars): Comprehensive
- **Too long** (>500 chars): May need editing for clarity

## Structure Validation

### Body Length
- **Minimum**: 100 characters (warning if less)
- **Maximum**: 500 lines (warning if more - suggests need for references/)

### Expected Sections
While not strictly required, skills typically benefit from:
- **Overview/About**: Introduction to the skill
- **Workflow/Usage**: How to use it
- **Examples**: Concrete demonstrations

### Resource Organization
- Scripts in `scripts/`
- Documentation in `references/`
- Templates/assets in `assets/`
- All resources should be referenced in SKILL.md

## Terminology Standards

### Writing Style
- Use imperative/infinitive form
  - ✅ "Use this script to rotate PDFs"
  - ❌ "You should use this script to rotate PDFs"

- Be direct and action-oriented
  - ✅ "Run analyze.py to extract metadata"
  - ❌ "You can run analyze.py if you want to extract metadata"

### Consistency
- **Claude**: Always capitalize (it's a proper noun)
- **SKILL.md**: All caps for the filename
- **skill**: Lowercase when referring to the concept

### Avoid Second Person
- ❌ "You should", "You can", "You must"
- ✅ "Use", "Run", "Create", "Execute"

## Resource Validation

### Referenced Resources
All bundled resources should be mentioned in SKILL.md:
- Scripts should be referenced by name or path
- Reference files should be linked in context
- Assets should be mentioned where applicable

### Unreferenced Resources (Warning)
If a resource exists but isn't mentioned, it may be:
- Dead code/docs that should be removed
- Important but forgotten in documentation

## Code Examples

### Best Practices
- Always include language tags: ` ```python` not ` ``` `
- Keep examples concise and focused
- Ensure examples are complete and runnable
- Provide context for what the example demonstrates

### Quantity
- No examples: INFO (consider adding if helpful)
- 1-5 examples: Ideal range
- 5+ examples: Consider moving to references/

## Error Severity Levels

### ERROR
Violations that prevent skill from working correctly:
- Missing required frontmatter fields
- Empty required fields
- Critical structural issues

### WARNING
Issues that affect quality but don't break functionality:
- Naming convention violations
- Short descriptions
- Unreferenced resources
- Excessive length (>500 lines)

### INFO
Suggestions for improvement:
- Stylistic recommendations
- Missing optional sections
- Terminology suggestions
- Code example language tags

## Validation Checklist

When validating a skill, check:

- [ ] Frontmatter has required fields
- [ ] Name follows naming conventions
- [ ] Description is comprehensive and clear
- [ ] Body has reasonable length
- [ ] Key sections are present
- [ ] Resources are properly referenced
- [ ] Code examples have language tags
- [ ] Terminology is consistent
- [ ] Style is imperative/infinitive
