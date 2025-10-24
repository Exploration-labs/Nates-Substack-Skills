#!/usr/bin/env python3
"""
Analyzes a SKILL.md file and extracts metadata, structure, and resources.
"""

import yaml
import re
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional


def parse_frontmatter(content: str) -> tuple[Dict, str]:
    """Extract YAML frontmatter and remaining content."""
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(frontmatter_pattern, content, re.DOTALL)
    
    if not match:
        return {}, content
    
    yaml_content = match.group(1)
    body = match.group(2)
    
    try:
        metadata = yaml.safe_load(yaml_content)
        return metadata or {}, body
    except yaml.YAMLError as e:
        print(f"Warning: Failed to parse YAML frontmatter: {e}", file=sys.stderr)
        return {}, content


def extract_sections(body: str) -> Dict[str, str]:
    """Extract major sections from markdown body."""
    sections = {}
    current_section = "introduction"
    current_content = []
    
    for line in body.split('\n'):
        if line.startswith('# '):
            if current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = line[2:].strip().lower().replace(' ', '_')
            current_content = []
        elif line.startswith('## '):
            if current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = line[3:].strip().lower().replace(' ', '_')
            current_content = []
        else:
            current_content.append(line)
    
    if current_content:
        sections[current_section] = '\n'.join(current_content).strip()
    
    return sections


def find_code_blocks(content: str) -> List[Dict[str, str]]:
    """Extract code blocks with their language tags."""
    code_blocks = []
    pattern = r'```(\w+)?\n(.*?)```'
    
    for match in re.finditer(pattern, content, re.DOTALL):
        language = match.group(1) or 'text'
        code = match.group(2).strip()
        code_blocks.append({
            'language': language,
            'code': code
        })
    
    return code_blocks


def find_references(body: str, skill_dir: Path) -> Dict[str, List[str]]:
    """Find references to bundled resources (scripts, references, assets)."""
    resources = {
        'scripts': [],
        'references': [],
        'assets': []
    }
    
    # Pattern for markdown links and file references
    link_pattern = r'\[(.*?)\]\((.*?)\)'
    
    for match in re.finditer(link_pattern, body):
        link_path = match.group(2)
        
        # Check if it's a relative path
        if not link_path.startswith('http'):
            for resource_type in resources.keys():
                if link_path.startswith(resource_type):
                    resources[resource_type].append(link_path)
    
    # Also check actual filesystem
    for resource_type in resources.keys():
        resource_dir = skill_dir / resource_type
        if resource_dir.exists():
            for file_path in resource_dir.rglob('*'):
                if file_path.is_file():
                    rel_path = file_path.relative_to(skill_dir)
                    path_str = str(rel_path)
                    if path_str not in resources[resource_type]:
                        resources[resource_type].append(path_str)
    
    return resources


def analyze_skill(skill_path: str) -> Dict:
    """
    Analyze a skill and return structured information.
    
    Args:
        skill_path: Path to skill directory or SKILL.md file
        
    Returns:
        Dictionary containing skill analysis
    """
    skill_path = Path(skill_path)
    
    # Handle both directory and file paths
    if skill_path.is_dir():
        skill_file = skill_path / 'SKILL.md'
        skill_dir = skill_path
    else:
        skill_file = skill_path
        skill_dir = skill_path.parent
    
    if not skill_file.exists():
        raise FileNotFoundError(f"SKILL.md not found at {skill_file}")
    
    content = skill_file.read_text(encoding='utf-8')
    metadata, body = parse_frontmatter(content)
    
    analysis = {
        'path': str(skill_dir),
        'metadata': metadata,
        'name': metadata.get('name', skill_dir.name),
        'description': metadata.get('description', ''),
        'sections': extract_sections(body),
        'code_blocks': find_code_blocks(body),
        'resources': find_references(body, skill_dir),
        'body_length': len(body),
        'line_count': len(body.split('\n'))
    }
    
    return analysis


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python analyze_skill.py <skill_directory_or_SKILL.md>")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    
    try:
        analysis = analyze_skill(skill_path)
        
        print(f"Skill Analysis: {analysis['name']}")
        print("=" * 60)
        print(f"Description: {analysis['description'][:100]}...")
        print(f"\nMetadata fields: {', '.join(analysis['metadata'].keys())}")
        print(f"Body length: {analysis['body_length']} chars, {analysis['line_count']} lines")
        print(f"\nSections found: {len(analysis['sections'])}")
        for section in analysis['sections'].keys():
            print(f"  - {section}")
        
        print(f"\nCode blocks: {len(analysis['code_blocks'])}")
        for i, block in enumerate(analysis['code_blocks'][:3], 1):
            print(f"  {i}. {block['language']} ({len(block['code'])} chars)")
        
        print("\nResources:")
        for resource_type, files in analysis['resources'].items():
            if files:
                print(f"  {resource_type}: {len(files)} file(s)")
                for f in files[:3]:
                    print(f"    - {f}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
