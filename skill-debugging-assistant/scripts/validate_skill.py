#!/usr/bin/env python3
"""
Comprehensive skill validation script

Checks for common issues including:
- YAML frontmatter format and completeness
- Description quality and specificity
- File structure and naming conventions
- Token budget (SKILL.md line count)
- Absolute statements that might cause conflicts
- Reference file mentions in SKILL.md
"""

import sys
import os
import re
from pathlib import Path
from typing import List, Tuple

class SkillValidator:
    def __init__(self, skill_path: str):
        self.skill_path = Path(skill_path)
        self.errors = []
        self.warnings = []
        self.info = []
        
    def validate(self) -> bool:
        """Run all validation checks"""
        self.check_structure()
        self.check_frontmatter()
        self.check_description_quality()
        self.check_token_budget()
        self.check_absolute_statements()
        self.check_reference_mentions()
        self.check_extraneous_files()
        
        return len(self.errors) == 0
    
    def check_structure(self):
        """Check basic skill directory structure"""
        skill_md = self.skill_path / 'SKILL.md'
        if not skill_md.exists():
            self.errors.append("❌ SKILL.md not found")
            return
        
        self.info.append(f"✓ SKILL.md found")
        
        # Check for optional directories
        if (self.skill_path / 'scripts').exists():
            self.info.append(f"✓ scripts/ directory present")
        if (self.skill_path / 'references').exists():
            self.info.append(f"✓ references/ directory present")
        if (self.skill_path / 'assets').exists():
            self.info.append(f"✓ assets/ directory present")
    
    def check_frontmatter(self):
        """Validate YAML frontmatter"""
        skill_md = self.skill_path / 'SKILL.md'
        if not skill_md.exists():
            return
        
        content = skill_md.read_text()
        
        if not content.startswith('---'):
            self.errors.append("❌ No YAML frontmatter found (must start with ---)")
            return
        
        # Extract frontmatter
        match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not match:
            self.errors.append("❌ Invalid frontmatter format (must end with ---)")
            return
        
        frontmatter = match.group(1)
        
        # Check required fields
        if 'name:' not in frontmatter:
            self.errors.append("❌ Missing 'name' field in frontmatter")
        else:
            name_match = re.search(r'name:\s*(.+)', frontmatter)
            if name_match:
                name = name_match.group(1).strip()
                
                # Check naming convention (kebab-case)
                if not re.match(r'^[a-z0-9-]+$', name):
                    self.errors.append(f"❌ Name '{name}' must be kebab-case (lowercase, digits, hyphens only)")
                elif name.startswith('-') or name.endswith('-'):
                    self.errors.append(f"❌ Name '{name}' cannot start or end with hyphen")
                elif '--' in name:
                    self.errors.append(f"❌ Name '{name}' cannot contain consecutive hyphens")
                else:
                    self.info.append(f"✓ Name '{name}' follows conventions")
        
        if 'description:' not in frontmatter:
            self.errors.append("❌ Missing 'description' field in frontmatter")
        else:
            desc_match = re.search(r'description:\s*(.+)', frontmatter)
            if desc_match:
                description = desc_match.group(1).strip()
                
                # Check for angle brackets
                if '<' in description or '>' in description:
                    self.errors.append("❌ Description contains angle brackets (< or >)")
                
                # Check for placeholder text
                if 'TODO' in description or '[' in description:
                    self.errors.append("❌ Description contains TODO or placeholder text")
    
    def check_description_quality(self):
        """Check description quality and specificity"""
        skill_md = self.skill_path / 'SKILL.md'
        if not skill_md.exists():
            return
        
        content = skill_md.read_text()
        desc_match = re.search(r'description:\s*(.+)', content)
        
        if not desc_match:
            return
        
        description = desc_match.group(1).strip()
        
        # Check length
        if len(description) < 50:
            self.warnings.append(f"⚠️  Description is short ({len(description)} chars). Consider adding more detail.")
        elif len(description) > 500:
            self.warnings.append(f"⚠️  Description is long ({len(description)} chars). Consider being more concise.")
        else:
            self.info.append(f"✓ Description length appropriate ({len(description)} chars)")
        
        # Check for "when to use" indicators
        when_indicators = ['when', 'use for', 'use when', 'for queries', 'trigger', 'applies']
        has_when_indicator = any(indicator in description.lower() for indicator in when_indicators)
        
        if not has_when_indicator:
            self.warnings.append("⚠️  Description might lack 'when to use' indicators (when, use for, etc.)")
        
        # Check for overly generic terms
        generic_terms = ['helps with', 'assists', 'various', 'multiple', 'different']
        has_generic = any(term in description.lower() for term in generic_terms)
        
        if has_generic:
            self.warnings.append("⚠️  Description contains generic terms (helps with, assists, various). Be more specific.")
        
        # Check for specific triggers (file extensions, actions, etc.)
        has_specifics = bool(re.search(r'\.(docx|pdf|csv|xlsx|json|py|js|html)', description.lower()))
        has_specifics |= bool(re.search(r'\b(create|edit|analyze|debug|review|generate|extract|convert)\b', description.lower()))
        
        if not has_specifics:
            self.warnings.append("⚠️  Consider adding specific triggers (file types, action verbs, task types)")
    
    def check_token_budget(self):
        """Check SKILL.md size for token budget"""
        skill_md = self.skill_path / 'SKILL.md'
        if not skill_md.exists():
            return
        
        content = skill_md.read_text()
        lines = content.split('\n')
        line_count = len(lines)
        
        if line_count > 500:
            self.warnings.append(f"⚠️  SKILL.md has {line_count} lines (>500). Consider moving content to references/")
        elif line_count > 300:
            self.info.append(f"✓ SKILL.md has {line_count} lines (approaching limit, consider references)")
        else:
            self.info.append(f"✓ SKILL.md has {line_count} lines (well within budget)")
    
    def check_absolute_statements(self):
        """Check for absolute statements that might cause conflicts"""
        skill_md = self.skill_path / 'SKILL.md'
        if not skill_md.exists():
            return
        
        content = skill_md.read_text()
        
        # Pattern for absolute statements
        absolute_patterns = [
            (r'\bALWAYS\b', 'ALWAYS'),
            (r'\bNEVER\b', 'NEVER'),
            (r'\bMUST\b', 'MUST'),
            (r'\bREQUIRED\b', 'REQUIRED'),
            (r'\bCRITICAL\b', 'CRITICAL')
        ]
        
        found_absolutes = []
        for pattern, word in absolute_patterns:
            matches = re.findall(pattern, content)
            if matches:
                found_absolutes.append((word, len(matches)))
        
        if found_absolutes:
            warning_msg = "⚠️  Found absolute statements that might override user intent:"
            for word, count in found_absolutes:
                warning_msg += f"\n    - {word}: {count} occurrence(s)"
            warning_msg += "\n    Consider using: 'prefer', 'avoid', 'typically', 'by default' with conditional clauses"
            self.warnings.append(warning_msg)
    
    def check_reference_mentions(self):
        """Check if reference files are mentioned in SKILL.md"""
        skill_md = self.skill_path / 'SKILL.md'
        references_dir = self.skill_path / 'references'
        
        if not skill_md.exists() or not references_dir.exists():
            return
        
        skill_content = skill_md.read_text()
        
        # Find all reference files
        reference_files = [f.name for f in references_dir.glob('*.md')]
        
        if not reference_files:
            return
        
        # Check if each reference is mentioned in SKILL.md
        unmentioned = []
        for ref_file in reference_files:
            if ref_file not in skill_content:
                unmentioned.append(ref_file)
        
        if unmentioned:
            self.warnings.append(f"⚠️  Reference files not mentioned in SKILL.md: {', '.join(unmentioned)}")
            self.warnings.append("    Consider adding descriptions of when to load these files")
    
    def check_extraneous_files(self):
        """Check for unnecessary documentation files"""
        unwanted_files = ['README.md', 'CHANGELOG.md', 'INSTALLATION.md', 
                         'QUICK_REFERENCE.md', 'CONTRIBUTING.md']
        
        found_unwanted = []
        for filename in unwanted_files:
            if (self.skill_path / filename).exists():
                found_unwanted.append(filename)
        
        if found_unwanted:
            self.warnings.append(f"⚠️  Extraneous files found: {', '.join(found_unwanted)}")
            self.warnings.append("    Skills should only contain SKILL.md and bundled resources")
    
    def print_results(self):
        """Print validation results"""
        print(f"\n{'='*60}")
        print(f"Skill Validation: {self.skill_path.name}")
        print(f"{'='*60}\n")
        
        if self.errors:
            print("ERRORS:")
            for error in self.errors:
                print(f"  {error}")
            print()
        
        if self.warnings:
            print("WARNINGS:")
            for warning in self.warnings:
                print(f"  {warning}")
            print()
        
        if self.info:
            print("INFO:")
            for info in self.info:
                print(f"  {info}")
            print()
        
        print(f"{'='*60}")
        if self.errors:
            print("❌ VALIDATION FAILED - Fix errors before packaging")
        elif self.warnings:
            print("⚠️  VALIDATION PASSED WITH WARNINGS - Review warnings for improvements")
        else:
            print("✅ VALIDATION PASSED - Skill is ready to package")
        print(f"{'='*60}\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_skill.py <skill_directory>")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    
    if not os.path.isdir(skill_path):
        print(f"Error: '{skill_path}' is not a directory")
        sys.exit(1)
    
    validator = SkillValidator(skill_path)
    is_valid = validator.validate()
    validator.print_results()
    
    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()
