# README Template Reference

This document defines the standard structure for auto-generated skill READMEs.

## Structure

A well-formed README contains these sections in order:

### 1. Title and Description (Required)
```markdown
# {skill-name}

> {description from frontmatter}
```

### 2. Overview (Required)
Brief introduction to the skill's purpose and capabilities. Typically 1-3 paragraphs.

### 3. When to Use This Skill (Required)
Explicit trigger scenarios that help users understand when to invoke the skill. Should include:
- Common use cases
- Trigger phrases extracted from description
- Example queries

### 4. Skill Structure (Required)
Quick stats about the skill:
- Lines of documentation
- Number of sections
- Number of code examples
- Resource counts

### 5. Bundled Resources (If Present)
Organized by resource type:
- **Scripts** - Executable code
- **Reference Documentation** - Additional docs to load as needed
- **Assets** - Templates, images, fonts, etc.

Each resource listed with a link to the actual file.

### 6. Key Sections (Optional)
List of main documentation sections for quick navigation. Limit to top 5 most important sections.

### 7. Usage Examples (If Present)
Concrete code examples extracted from SKILL.md. Include:
- Language tag
- Actual working code
- Maximum 3 examples to keep README focused

### 8. Quality Validation (Optional)
Validation results showing:
- Pass/fail status
- Error count
- Warning count
- Collapsible details with specific issues

### 9. Footer (Required)
```markdown
---

_Documentation auto-generated from `SKILL.md`_
```

## Best Practices

### Conciseness
READMEs should be scannable. Keep descriptions brief and use formatting to highlight key information.

### Links
Always link to actual resources using relative paths. This makes the README actionable.

### Examples
Choose the most representative examples. Quality over quantity - 3 good examples beat 10 mediocre ones.

### Validation
Including validation results builds trust and helps maintain quality standards across skills.
