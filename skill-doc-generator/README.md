# skill-doc-generator

> Auto-generates standardized README documentation from SKILL.md files, validates consistency (frontmatter, descriptions, terminology), and creates usage examples. Use when documenting individual skills, generating docs for multiple skills in a directory, or validating skill quality standards.

## Overview

This skill automates the creation of standardized README files for skills by analyzing SKILL.md files, extracting structure and examples, validating quality standards, and generating comprehensive documentation. It ensures consistency across skill documentation while providing actionable validation feedback.

## When to Use This Skill

This skill is triggered when working with tasks related to skill-doc-generator.

**Common trigger scenarios:**
- documenting individual skills


## Skill Structure

- **Lines of documentation:** 208
- **Sections:** 16
- **Code examples:** 8

## Bundled Resources

### Scripts

- [`scripts/__pycache__/analyze_skill.cpython-312.pyc`](scripts/scripts/__pycache__/analyze_skill.cpython-312.pyc)
- [`scripts/__pycache__/validate_consistency.cpython-312.pyc`](scripts/scripts/__pycache__/validate_consistency.cpython-312.pyc)
- [`scripts/analyze_skill.py`](scripts/scripts/analyze_skill.py)
- [`scripts/document_directory.py`](scripts/scripts/document_directory.py)
- [`scripts/generate_readme.py`](scripts/scripts/generate_readme.py)
- [`scripts/validate_consistency.py`](scripts/scripts/validate_consistency.py)

### Reference Documentation

- [`references/consistency-rules.md`](references/references/consistency-rules.md)
- [`references/readme-template.md`](references/references/readme-template.md)
- [`references/terminology-standards.md`](references/references/terminology-standards.md)

## Key Sections

- **Skill Documentation Generator**
- **Workflow**
- **Document All User Skills With Validation**
- **Quick Pass Without Validation**
- **Script Reference**

## Usage Examples

### Example 1

```bash
python scripts/analyze_skill.py <skill_directory>
```

### Example 2

```bash
python scripts/validate_consistency.py <skill_directory> --verbose
```

### Example 3

```bash
python scripts/generate_readme.py <skill_directory> [output_path]
```

## Quality Validation

⚠️  **2 warning(s) found**

<details>
<summary>View validation details</summary>

- `INFO` Description: Description contains vague term 'multiple' - consider being more specific
- `INFO` Terminology: Found 'you should' - consider using imperative form (e.g., 'Use' instead of 'You should use')
- `WARNING` Resources: Script 'scripts/__pycache__/analyze_skill.cpython-312.pyc' exists but isn't referenced in SKILL.md
- `WARNING` Resources: Script 'scripts/__pycache__/validate_consistency.cpython-312.pyc' exists but isn't referenced in SKILL.md

</details>

---

_Documentation auto-generated from `SKILL.md`_