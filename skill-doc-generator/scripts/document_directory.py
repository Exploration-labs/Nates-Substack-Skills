#!/usr/bin/env python3
"""
Generates documentation for all skills in a directory.
"""

import sys
import traceback
from pathlib import Path
from typing import List, Dict
from analyze_skill import analyze_skill
from generate_readme import generate_readme, save_readme
from validate_consistency import validate_skill


def find_skills(directory: str, recursive: bool = True) -> List[Path]:
    """
    Find all SKILL.md files in directory.
    
    Args:
        directory: Root directory to search
        recursive: Whether to search subdirectories
        
    Returns:
        List of paths to SKILL.md files
    """
    directory = Path(directory)
    
    if not directory.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    skill_files = []
    
    if recursive:
        skill_files = list(directory.rglob('SKILL.md'))
    else:
        skill_files = list(directory.glob('*/SKILL.md'))
    
    return sorted(skill_files)


def create_index_file(skills: List[Dict], output_path: Path):
    """Generate an index/catalog of all skills."""
    lines = []
    
    lines.append("# Skills Documentation Index")
    lines.append("")
    lines.append(f"Documentation for {len(skills)} skills.")
    lines.append("")
    
    # Group by category if possible (based on path structure)
    categorized = {}
    uncategorized = []
    
    for skill in skills:
        path = Path(skill['path'])
        # Try to extract category from path
        parts = path.parts
        if len(parts) > 1 and parts[-2] not in ['skill-doc-generator', '.']:
            category = parts[-2]
        else:
            category = 'Other'
        
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(skill)
    
    # Output by category
    for category in sorted(categorized.keys()):
        lines.append(f"## {category.title()}")
        lines.append("")
        
        for skill in sorted(categorized[category], key=lambda x: x['name']):
            name = skill['name']
            desc = skill['description'][:100] + "..." if len(skill['description']) > 100 else skill['description']
            
            # Link to README if it exists
            skill_path = Path(skill['path'])
            readme_path = skill_path / 'README.md'
            
            if readme_path.exists():
                try:
                    rel_path = readme_path.relative_to(output_path.parent)
                    lines.append(f"### [{name}]({rel_path})")
                except (ValueError, AttributeError):
                    lines.append(f"### [{name}](./README.md)")
            else:
                lines.append(f"### {name}")
            
            lines.append("")
            lines.append(f"{desc}")
            lines.append("")
            
            # Add quick stats
            lines.append(f"- **Lines:** {skill['line_count']}")
            lines.append(f"- **Resources:** {sum(len(v) for v in skill['resources'].values())} files")
            lines.append("")
    
    content = '\n'.join(lines)
    output_path.write_text(content, encoding='utf-8')
    return str(output_path)


def document_directory(
    directory: str,
    output_dir: str = None,
    recursive: bool = True,
    generate_index_file: bool = True,
    validate: bool = True
) -> Dict:
    """
    Document all skills in a directory.
    
    Args:
        directory: Directory containing skills
        output_dir: Optional output directory for documentation
        recursive: Whether to search subdirectories
        generate_index_file: Whether to create an index file
        validate: Whether to run validation
        
    Returns:
        Statistics dictionary
    """
    directory = Path(directory)
    
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Searching for skills in: {directory}")
    skill_files = find_skills(directory, recursive)
    
    if not skill_files:
        print("⚠️  No SKILL.md files found")
        return {'total': 0, 'successful': 0, 'failed': 0}
    
    print(f"Found {len(skill_files)} skill(s)")
    print("")
    
    stats = {
        'total': len(skill_files),
        'successful': 0,
        'failed': 0,
        'errors': 0,
        'warnings': 0
    }
    
    analyzed_skills = []
    
    for skill_file in skill_files:
        skill_dir = skill_file.parent
        skill_name = skill_dir.name
        
        try:
            print(f"Processing: {skill_name}...")
            
            # Analyze
            analysis = analyze_skill(skill_dir)
            analyzed_skills.append(analysis)
            
            # Validate if requested
            if validate:
                issues, has_errors = validate_skill(skill_dir)
                errors = [i for i in issues if i.severity == 'ERROR']
                warnings = [i for i in issues if i.severity == 'WARNING']
                
                stats['errors'] += len(errors)
                stats['warnings'] += len(warnings)
                
                if errors:
                    print(f"  ❌ {len(errors)} error(s)")
                elif warnings:
                    print(f"  ⚠️  {len(warnings)} warning(s)")
                else:
                    print(f"  ✅ Validated")
            
            # Generate README
            readme_content = generate_readme(analysis, include_validation=validate)
            
            # Save README
            if output_dir:
                # Save to output directory
                skill_output_dir = output_dir / skill_name
                skill_output_dir.mkdir(exist_ok=True)
                readme_path = skill_output_dir / 'README.md'
            else:
                # Save alongside SKILL.md
                readme_path = skill_dir / 'README.md'
            
            readme_path.write_text(readme_content, encoding='utf-8')
            print(f"  📄 README: {readme_path}")
            
            stats['successful'] += 1
            
        except Exception as e:
            print(f"  ❌ Failed: {e}")
            stats['failed'] += 1
        
        print("")
    
    # Generate index if requested
    if generate_index_file and analyzed_skills:
        index_path = output_dir / 'INDEX.md' if output_dir else directory / 'INDEX.md'
        create_index_file(analyzed_skills, index_path)
        print(f"📚 Index generated: {index_path}")
        print("")
    
    # Summary
    print("=" * 60)
    print("Summary:")
    print(f"  Total skills: {stats['total']}")
    print(f"  Successful: {stats['successful']}")
    print(f"  Failed: {stats['failed']}")
    if validate:
        print(f"  Total errors: {stats['errors']}")
        print(f"  Total warnings: {stats['warnings']}")
    
    return stats


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python document_directory.py <directory> [options]")
        print("\nOptions:")
        print("  --output <dir>     Output directory for documentation")
        print("  --no-recursive     Don't search subdirectories")
        print("  --no-index         Don't generate index file")
        print("  --no-validate      Skip validation checks")
        print("\nExamples:")
        print("  python document_directory.py /mnt/skills/user")
        print("  python document_directory.py ./skills --output ./docs")
        sys.exit(1)
    
    directory = sys.argv[1]
    
    # Parse options
    args = sys.argv[2:]
    output_dir = None
    recursive = '--no-recursive' not in args
    generate_index = '--no-index' not in args
    validate = '--no-validate' not in args
    
    if '--output' in args:
        idx = args.index('--output')
        if idx + 1 < len(args):
            output_dir = args[idx + 1]
    
    try:
        stats = document_directory(
            directory,
            output_dir=output_dir,
            recursive=recursive,
            generate_index_file=generate_index,
            validate=validate
        )
        
        sys.exit(0 if stats['failed'] == 0 else 1)
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)
