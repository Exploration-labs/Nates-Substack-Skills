#!/usr/bin/env python3
"""
Validates skill consistency: frontmatter format, description quality, and terminology.
"""

import sys
from pathlib import Path
from typing import List, Dict
from analyze_skill import analyze_skill


class ValidationIssue:
    """Represents a validation issue."""
    
    SEVERITY_ERROR = 'ERROR'
    SEVERITY_WARNING = 'WARNING'
    SEVERITY_INFO = 'INFO'
    
    def __init__(self, severity: str, category: str, message: str):
        self.severity = severity
        self.category = category
        self.message = message
    
    def __str__(self):
        return f"[{self.severity}] {self.category}: {self.message}"


class SkillValidator:
    """Validates skill structure and content."""
    
    def __init__(self):
        self.issues: List[ValidationIssue] = []
    
    def validate(self, skill_path: str) -> List[ValidationIssue]:
        """Run all validation checks on a skill."""
        self.issues = []
        
        try:
            analysis = analyze_skill(skill_path)
        except Exception as e:
            self.issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_ERROR,
                'Parse Error',
                f"Failed to analyze skill: {e}"
            ))
            return self.issues
        
        self._validate_frontmatter(analysis)
        self._validate_description(analysis)
        self._validate_structure(analysis)
        self._validate_terminology(analysis)
        self._validate_resources(analysis)
        self._validate_examples(analysis)
        
        return self.issues
    
    def _validate_frontmatter(self, analysis: Dict):
        """Check required frontmatter fields and format."""
        metadata = analysis['metadata']
        
        # Required fields
        if 'name' not in metadata:
            self.issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_ERROR,
                'Frontmatter',
                "Missing required field: 'name'"
            ))
        elif not metadata['name']:
            self.issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_ERROR,
                'Frontmatter',
                "'name' field is empty"
            ))
        
        if 'description' not in metadata:
            self.issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_ERROR,
                'Frontmatter',
                "Missing required field: 'description'"
            ))
        elif not metadata['description']:
            self.issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_ERROR,
                'Frontmatter',
                "'description' field is empty"
            ))
        
        # Name format (should be lowercase with hyphens)
        if 'name' in metadata and metadata['name']:
            name = metadata['name']
            if not name.islower() or ' ' in name:
                self.issues.append(ValidationIssue(
                    ValidationIssue.SEVERITY_WARNING,
                    'Frontmatter',
                    f"Name '{name}' should be lowercase with hyphens (e.g., 'skill-name')"
                ))
    
    def _validate_description(self, analysis: Dict):
        """Check description quality and completeness."""
        description = analysis.get('description', '')
        
        if not description:
            return  # Already caught in frontmatter check
        
        # Length checks
        if len(description) < 50:
            self.issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_WARNING,
                'Description',
                f"Description is very short ({len(description)} chars). Should be comprehensive and specific."
            ))
        
        if len(description) > 500:
            self.issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_INFO,
                'Description',
                f"Description is quite long ({len(description)} chars). Consider if all content is essential for skill selection."
            ))
        
        # Content quality checks
        if not description[0].isupper():
            self.issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_WARNING,
                'Description',
                "Description should start with a capital letter"
            ))
        
        # Check for specificity
        vague_terms = ['various', 'multiple', 'different', 'some', 'general']
        for term in vague_terms:
            if term.lower() in description.lower():
                self.issues.append(ValidationIssue(
                    ValidationIssue.SEVERITY_INFO,
                    'Description',
                    f"Description contains vague term '{term}' - consider being more specific"
                ))
                break
        
        # Check for trigger phrases
        if 'when' not in description.lower() and 'use' not in description.lower():
            self.issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_INFO,
                'Description',
                "Consider adding trigger phrases ('when', 'use this when') to help with skill selection"
            ))
    
    def _validate_structure(self, analysis: Dict):
        """Check overall document structure."""
        sections = analysis.get('sections', {})
        body_length = analysis.get('body_length', 0)
        line_count = analysis.get('line_count', 0)
        
        # Check for empty body
        if body_length < 100:
            self.issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_WARNING,
                'Structure',
                f"SKILL.md body is very short ({body_length} chars)"
            ))
        
        # Check for excessive length (suggests need for references/)
        if line_count > 500:
            self.issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_WARNING,
                'Structure',
                f"SKILL.md is quite long ({line_count} lines). Consider moving detailed content to references/"
            ))
        
        # Check for common expected sections
        section_names = [s.lower() for s in sections.keys()]
        
        has_overview = any('overview' in s or 'about' in s for s in section_names)
        has_workflow = any('workflow' in s or 'usage' in s or 'how' in s for s in section_names)
        
        if not has_overview:
            self.issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_INFO,
                'Structure',
                "Consider adding an 'Overview' section to introduce the skill"
            ))
    
    def _validate_terminology(self, analysis: Dict):
        """Check for consistent terminology and style."""
        # Get all text content
        body = '\n'.join(analysis.get('sections', {}).values())
        
        # Check for inconsistent capitalization of common terms
        terms_to_check = {
            'claude': ['Claude', 'claude'],  # Should be 'Claude'
            'skill': ['Skill', 'skill'],  # Can vary by context
        }
        
        # Check for imperative/infinitive form (per guidelines)
        non_imperative_starts = [
            'you should', 'you can', 'you must', 'you will',
            'we should', 'we can', 'we must', 'we will'
        ]
        
        for phrase in non_imperative_starts:
            if phrase.lower() in body.lower():
                self.issues.append(ValidationIssue(
                    ValidationIssue.SEVERITY_INFO,
                    'Terminology',
                    f"Found '{phrase}' - consider using imperative form (e.g., 'Use' instead of 'You should use')"
                ))
                break
    
    def _validate_resources(self, analysis: Dict):
        """Check bundled resources are properly referenced."""
        resources = analysis.get('resources', {})
        sections = analysis.get('sections', {})
        body = '\n'.join(sections.values())
        
        # Check if scripts exist but aren't mentioned
        scripts = resources.get('scripts', [])
        if scripts:
            for script in scripts:
                script_name = Path(script).name
                if script_name not in body:
                    self.issues.append(ValidationIssue(
                        ValidationIssue.SEVERITY_WARNING,
                        'Resources',
                        f"Script '{script}' exists but isn't referenced in SKILL.md"
                    ))
        
        # Check if references exist but aren't mentioned
        references = resources.get('references', [])
        if references:
            for ref in references:
                ref_name = Path(ref).name
                if ref_name not in body:
                    self.issues.append(ValidationIssue(
                        ValidationIssue.SEVERITY_WARNING,
                        'Resources',
                        f"Reference file '{ref}' exists but isn't mentioned in SKILL.md"
                    ))
    
    def _validate_examples(self, analysis: Dict):
        """Check for presence and quality of code examples."""
        code_blocks = analysis.get('code_blocks', [])
        
        if not code_blocks:
            self.issues.append(ValidationIssue(
                ValidationIssue.SEVERITY_INFO,
                'Examples',
                "No code examples found. Consider adding examples if they would help clarify usage."
            ))
        
        # Check for language tags on code blocks
        for i, block in enumerate(code_blocks, 1):
            if block['language'] == 'text':
                self.issues.append(ValidationIssue(
                    ValidationIssue.SEVERITY_INFO,
                    'Examples',
                    f"Code block {i} has no language tag. Consider adding one for syntax highlighting."
                ))


def validate_skill(skill_path: str, verbose: bool = False) -> tuple[List[ValidationIssue], bool]:
    """
    Validate a skill and return issues.
    
    Returns:
        Tuple of (issues, has_errors)
    """
    validator = SkillValidator()
    issues = validator.validate(skill_path)
    
    has_errors = any(issue.severity == ValidationIssue.SEVERITY_ERROR for issue in issues)
    
    return issues, has_errors


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python validate_consistency.py <skill_directory> [--verbose]")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    verbose = '--verbose' in sys.argv
    
    issues, has_errors = validate_skill(skill_path, verbose)
    
    if not issues:
        print(f"✅ Skill validation passed with no issues!")
        sys.exit(0)
    
    # Group by severity
    errors = [i for i in issues if i.severity == ValidationIssue.SEVERITY_ERROR]
    warnings = [i for i in issues if i.severity == ValidationIssue.SEVERITY_WARNING]
    info = [i for i in issues if i.severity == ValidationIssue.SEVERITY_INFO]
    
    print(f"Validation Results for: {skill_path}")
    print("=" * 60)
    
    if errors:
        print(f"\n❌ ERRORS ({len(errors)}):")
        for issue in errors:
            print(f"  {issue}")
    
    if warnings:
        print(f"\n⚠️  WARNINGS ({len(warnings)}):")
        for issue in warnings:
            print(f"  {issue}")
    
    if info and verbose:
        print(f"\nℹ️  INFO ({len(info)}):")
        for issue in info:
            print(f"  {issue}")
    
    print(f"\nSummary: {len(errors)} errors, {len(warnings)} warnings, {len(info)} info")
    
    sys.exit(1 if has_errors else 0)
