#!/usr/bin/env python3
"""
Generates a README.md file for a skill based on its analysis.
"""

import sys
from pathlib import Path
from typing import Dict, List
from analyze_skill import analyze_skill
from validate_consistency import validate_skill


def format_resource_list(resources: List[str], base_path: str = '') -> str:
    """Format a list of resources as markdown list items."""
    if not resources:
        return "_None_"
    
    lines = []
    for resource in sorted(resources):
        resource_path = Path(resource)
        if base_path:
            link = f"[`{resource}`]({base_path}/{resource})"
        else:
            link = f"`{resource}`"
        lines.append(f"- {link}")
    
    return '\n'.join(lines)


def extract_key_examples(analysis: Dict) -> List[Dict]:
    """Extract representative code examples from the skill."""
    code_blocks = analysis.get('code_blocks', [])
    
    # Limit to first 3 most substantial examples
    examples = []
    for block in code_blocks[:3]:
        if len(block['code']) > 20:  # Skip trivial examples
            examples.append(block)
    
    return examples


def generate_usage_section(analysis: Dict) -> str:
    """Generate usage/trigger examples section."""
    name = analysis['name']
    description = analysis['description']
    
    # Try to extract trigger phrases from description
    triggers = []
    if 'when' in description.lower():
        # Extract phrases after "when"
        import re
        when_matches = re.finditer(r'when\s+([^.,;]+)', description, re.IGNORECASE)
        for match in when_matches:
            triggers.append(match.group(1).strip())
    
    usage = f"This skill is triggered when working with tasks related to {name}.\n\n"
    
    if triggers:
        usage += "**Common trigger scenarios:**\n"
        for trigger in triggers[:3]:
            usage += f"- {trigger}\n"
    else:
        usage += f"The skill activates based on: {description[:200]}...\n"
    
    return usage


def generate_readme(analysis: Dict, include_validation: bool = True) -> str:
    """
    Generate README.md content from skill analysis.
    
    Args:
        analysis: Skill analysis dictionary
        include_validation: Whether to include validation results
        
    Returns:
        README.md content as string
    """
    name = analysis['name']
    description = analysis['description']
    sections = analysis.get('sections', {})
    resources = analysis.get('resources', {})
    
    readme = []
    
    # Title and description
    readme.append(f"# {name}")
    readme.append("")
    readme.append(f"> {description}")
    readme.append("")
    
    # Overview (from first section or description)
    overview_section = sections.get('overview', sections.get('introduction', ''))
    if overview_section:
        readme.append("## Overview")
        readme.append("")
        # Take first few paragraphs
        paragraphs = overview_section.split('\n\n')[:2]
        readme.append('\n\n'.join(paragraphs))
        readme.append("")
    
    # When to use this skill
    readme.append("## When to Use This Skill")
    readme.append("")
    readme.append(generate_usage_section(analysis))
    readme.append("")
    
    # Structure
    readme.append("## Skill Structure")
    readme.append("")
    readme.append(f"- **Lines of documentation:** {analysis['line_count']}")
    readme.append(f"- **Sections:** {len(sections)}")
    readme.append(f"- **Code examples:** {len(analysis['code_blocks'])}")
    readme.append("")
    
    # Resources
    if any(resources.values()):
        readme.append("## Bundled Resources")
        readme.append("")
        
        if resources.get('scripts'):
            readme.append("### Scripts")
            readme.append("")
            readme.append(format_resource_list(resources['scripts'], 'scripts'))
            readme.append("")
        
        if resources.get('references'):
            readme.append("### Reference Documentation")
            readme.append("")
            readme.append(format_resource_list(resources['references'], 'references'))
            readme.append("")
        
        if resources.get('assets'):
            readme.append("### Assets")
            readme.append("")
            readme.append(format_resource_list(resources['assets'], 'assets'))
            readme.append("")
    
    # Key sections
    if len(sections) > 1:
        readme.append("## Key Sections")
        readme.append("")
        # List main sections (skip introduction/overview)
        main_sections = [s for s in sections.keys() 
                        if s not in ['introduction', 'overview', name.lower().replace('-', '_')]]
        
        for section in main_sections[:5]:  # Limit to top 5
            section_title = section.replace('_', ' ').title()
            readme.append(f"- **{section_title}**")
        readme.append("")
    
    # Usage examples
    examples = extract_key_examples(analysis)
    if examples:
        readme.append("## Usage Examples")
        readme.append("")
        for i, example in enumerate(examples, 1):
            readme.append(f"### Example {i}")
            readme.append("")
            readme.append(f"```{example['language']}")
            readme.append(example['code'][:300])  # Truncate long examples
            if len(example['code']) > 300:
                readme.append("...")
            readme.append("```")
            readme.append("")
    
    # Validation results (optional)
    if include_validation:
        try:
            issues, has_errors = validate_skill(analysis['path'])
            
            readme.append("## Quality Validation")
            readme.append("")
            
            if not issues:
                readme.append("✅ **All validation checks passed**")
            else:
                errors = [i for i in issues if i.severity == 'ERROR']
                warnings = [i for i in issues if i.severity == 'WARNING']
                
                if errors:
                    readme.append(f"❌ **{len(errors)} error(s) found**")
                if warnings:
                    readme.append(f"⚠️  **{len(warnings)} warning(s) found**")
                
                readme.append("")
                readme.append("<details>")
                readme.append("<summary>View validation details</summary>")
                readme.append("")
                for issue in issues[:10]:  # Limit output
                    readme.append(f"- `{issue.severity}` {issue.category}: {issue.message}")
                readme.append("")
                readme.append("</details>")
            
            readme.append("")
        except Exception as e:
            pass  # Skip validation section if it fails
    
    # Footer
    readme.append("---")
    readme.append("")
    readme.append(f"_Documentation auto-generated from `SKILL.md`_")
    
    return '\n'.join(readme)


def save_readme(skill_path: str, readme_content: str, output_path: str = None) -> str:
    """
    Save README to file.
    
    Args:
        skill_path: Path to skill directory
        readme_content: README content
        output_path: Optional custom output path
        
    Returns:
        Path where README was saved
    """
    skill_path = Path(skill_path)
    
    if skill_path.is_file():
        skill_path = skill_path.parent
    
    if output_path:
        readme_path = Path(output_path)
    else:
        readme_path = skill_path / 'README.md'
    
    readme_path.write_text(readme_content, encoding='utf-8')
    return str(readme_path)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python generate_readme.py <skill_directory> [output_path]")
        print("\nExamples:")
        print("  python generate_readme.py ./my-skill")
        print("  python generate_readme.py ./my-skill ./docs/MY_SKILL.md")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        print(f"Analyzing skill at: {skill_path}")
        analysis = analyze_skill(skill_path)
        
        print(f"Generating README for: {analysis['name']}")
        readme = generate_readme(analysis, include_validation=True)
        
        saved_path = save_readme(skill_path, readme, output_path)
        
        print(f"✅ README generated successfully: {saved_path}")
        print(f"   {len(readme.split(chr(10)))} lines, {len(readme)} characters")
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
