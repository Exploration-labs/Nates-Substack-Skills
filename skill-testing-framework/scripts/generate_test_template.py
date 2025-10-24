#!/usr/bin/env python3
"""
Test Template Generator

Creates test case templates for skills based on the skill structure.

Usage:
    generate_test_template.py <skill-path> [--output <output-file>] [--format json|yaml]

Examples:
    generate_test_template.py /mnt/skills/public/pdf
    generate_test_template.py /mnt/skills/public/docx --output docx-tests.json
    generate_test_template.py ../my-skill --format yaml
"""

import sys
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any


def analyze_skill_structure(skill_path: Path) -> Dict[str, Any]:
    """Analyze a skill's structure to determine what tests to generate"""
    
    skill_md = skill_path / 'SKILL.md'
    scripts_dir = skill_path / 'scripts'
    
    structure = {
        'has_skill_md': skill_md.exists(),
        'has_scripts': scripts_dir.exists() and any(scripts_dir.iterdir()),
        'scripts': [],
        'skill_name': skill_path.name
    }
    
    # Find scripts
    if structure['has_scripts']:
        for script_file in scripts_dir.glob('*.py'):
            if script_file.name != '__pycache__':
                structure['scripts'].append(script_file.name)
    
    return structure


def generate_unit_tests(structure: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Generate unit test templates based on skill structure"""
    tests = []
    
    # Generate tests for each script
    for script in structure['scripts']:
        test = {
            "name": f"Test {script} executes successfully",
            "type": "script",
            "script": script,
            "args": [],
            "expected_exit_code": 0,
            "expected_output": None,
            "description": f"Verify that {script} runs without errors"
        }
        tests.append(test)
    
    return tests


def generate_integration_tests(structure: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Generate integration test templates"""
    skill_name = structure['skill_name']
    
    tests = [
        {
            "name": f"Test {skill_name} complete workflow",
            "type": "workflow",
            "description": f"End-to-end test of typical {skill_name} usage",
            "steps": [
                {
                    "action": "Setup test environment",
                    "details": "Create necessary test files and directories"
                },
                {
                    "action": "Execute workflow",
                    "details": "Run the main skill operation"
                },
                {
                    "action": "Validate output",
                    "details": "Check that output meets expectations"
                }
            ],
            "input": {
                "user_query": "Example user query that triggers this skill",
                "files": []
            },
            "expected_output": {
                "type": "Describe expected output type (file, text, etc.)",
                "validation": "Describe how to validate the output"
            }
        }
    ]
    
    return tests


def generate_regression_tests(structure: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Generate regression test templates"""
    skill_name = structure['skill_name']
    
    tests = [
        {
            "name": f"Regression: {skill_name} baseline behavior",
            "description": "Ensure skill behavior hasn't changed from established baseline",
            "input": {
                "user_query": "Example query with known expected behavior",
                "files": []
            },
            "baseline_file": f"baselines/{skill_name}_baseline_1.txt",
            "validation_method": "exact_match",  # or "contains", "pattern"
            "notes": "Update baseline_file path with actual baseline output location"
        }
    ]
    
    return tests


def generate_test_template(skill_path: Path, output_format: str = 'json') -> Dict[str, Any]:
    """Generate a complete test template for a skill"""
    
    structure = analyze_skill_structure(skill_path)
    
    template = {
        "skill_name": structure['skill_name'],
        "skill_path": str(skill_path),
        "test_version": "1.0",
        "description": f"Test cases for {structure['skill_name']} skill",
        
        "unit_tests": generate_unit_tests(structure),
        "integration_tests": generate_integration_tests(structure),
        "regression_tests": generate_regression_tests(structure),
        
        "_instructions": {
            "unit_tests": "Test individual components (scripts, functions) in isolation",
            "integration_tests": "Test complete workflows and interactions between components",
            "regression_tests": "Compare outputs against known baselines to catch regressions",
            "howto": "Fill in test details, then run with: run_tests.py <this-file>"
        }
    }
    
    return template


def save_template(template: Dict[str, Any], output_file: Path, output_format: str):
    """Save the template to a file"""
    
    with open(output_file, 'w') as f:
        if output_format == 'json':
            json.dump(template, f, indent=2)
        elif output_format == 'yaml':
            yaml.dump(template, f, default_flow_style=False, sort_keys=False)
    
    print(f"✅ Test template generated: {output_file}")
    print(f"\n📝 Next steps:")
    print(f"   1. Edit {output_file} to fill in test details")
    print(f"   2. Add expected outputs and validation criteria")
    print(f"   3. Create baseline files for regression tests if needed")
    print(f"   4. Run tests with: run_tests.py {output_file}")


def main():
    if len(sys.argv) < 2:
        print("Usage: generate_test_template.py <skill-path> [--output <output-file>] [--format json|yaml]")
        print("\nExamples:")
        print("  generate_test_template.py /mnt/skills/public/pdf")
        print("  generate_test_template.py /mnt/skills/public/docx --output docx-tests.json")
        print("  generate_test_template.py ../my-skill --format yaml")
        sys.exit(1)
    
    skill_path = Path(sys.argv[1])
    output_file = None
    output_format = 'json'
    
    # Parse arguments
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '--output' and i + 1 < len(sys.argv):
            output_file = Path(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == '--format' and i + 1 < len(sys.argv):
            output_format = sys.argv[i + 1].lower()
            if output_format not in ['json', 'yaml']:
                print(f"❌ Error: Invalid format '{output_format}'. Use 'json' or 'yaml'")
                sys.exit(1)
            i += 2
        else:
            print(f"Unknown argument: {sys.argv[i]}")
            sys.exit(1)
    
    if not skill_path.exists():
        print(f"❌ Error: Skill path not found: {skill_path}")
        sys.exit(1)
    
    if not output_file:
        # Generate default output filename
        skill_name = skill_path.name
        extension = 'json' if output_format == 'json' else 'yaml'
        output_file = Path(f"{skill_name}-tests.{extension}")
    
    print(f"🔍 Analyzing skill: {skill_path.name}")
    print(f"📄 Output format: {output_format}")
    print()
    
    template = generate_test_template(skill_path, output_format)
    save_template(template, output_file, output_format)


if __name__ == "__main__":
    main()
