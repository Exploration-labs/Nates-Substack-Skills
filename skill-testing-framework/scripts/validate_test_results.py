#!/usr/bin/env python3
"""
Test Results Validator

Validates test outputs against expected results and manages baseline files.

Usage:
    validate_test_results.py <actual-file> <expected-file> [--mode exact|contains|pattern]
    validate_test_results.py --create-baseline <output-file> <baseline-dir>

Examples:
    validate_test_results.py output.txt expected.txt
    validate_test_results.py result.json baseline.json --mode exact
    validate_test_results.py output.txt expected.txt --mode contains
    validate_test_results.py --create-baseline test_output.txt baselines/
"""

import sys
import json
import re
from pathlib import Path
from typing import Tuple, Optional
import difflib


class OutputValidator:
    """Validates test outputs against expectations"""
    
    def __init__(self, mode: str = 'exact'):
        self.mode = mode
        
    def validate(self, actual: str, expected: str) -> Tuple[bool, str]:
        """
        Validate actual output against expected output
        
        Returns: (passed, message)
        """
        if self.mode == 'exact':
            return self._validate_exact(actual, expected)
        elif self.mode == 'contains':
            return self._validate_contains(actual, expected)
        elif self.mode == 'pattern':
            return self._validate_pattern(actual, expected)
        else:
            return False, f"Unknown validation mode: {self.mode}"
    
    def _validate_exact(self, actual: str, expected: str) -> Tuple[bool, str]:
        """Exact string match"""
        actual_clean = actual.strip()
        expected_clean = expected.strip()
        
        if actual_clean == expected_clean:
            return True, "Exact match"
        else:
            # Generate diff for debugging
            diff = self._generate_diff(expected_clean, actual_clean)
            return False, f"Content mismatch:\n{diff}"
    
    def _validate_contains(self, actual: str, expected: str) -> Tuple[bool, str]:
        """Check if actual contains expected substring"""
        if expected in actual:
            return True, "Contains expected content"
        else:
            return False, f"Expected substring not found: '{expected}'"
    
    def _validate_pattern(self, actual: str, expected: str) -> Tuple[bool, str]:
        """Match against regex pattern"""
        try:
            if re.search(expected, actual, re.MULTILINE | re.DOTALL):
                return True, "Pattern matched"
            else:
                return False, f"Pattern not matched: {expected}"
        except re.error as e:
            return False, f"Invalid regex pattern: {e}"
    
    def _generate_diff(self, expected: str, actual: str) -> str:
        """Generate a unified diff between expected and actual"""
        expected_lines = expected.splitlines(keepends=True)
        actual_lines = actual.splitlines(keepends=True)
        
        diff = difflib.unified_diff(
            expected_lines,
            actual_lines,
            fromfile='expected',
            tofile='actual',
            lineterm=''
        )
        
        diff_text = ''.join(diff)
        if len(diff_text) > 500:
            diff_text = diff_text[:500] + "\n... (truncated)"
        
        return diff_text


def create_baseline(output_file: Path, baseline_dir: Path):
    """Create a baseline file from test output"""
    baseline_dir.mkdir(parents=True, exist_ok=True)
    
    baseline_file = baseline_dir / output_file.name
    
    if not output_file.exists():
        print(f"❌ Error: Output file not found: {output_file}")
        sys.exit(1)
    
    # Copy output to baseline
    import shutil
    shutil.copy2(output_file, baseline_file)
    
    print(f"✅ Baseline created: {baseline_file}")
    print(f"\n📝 This baseline can now be used in regression tests:")
    print(f'   "baseline_file": "{baseline_file}"')


def compare_files(actual_file: Path, expected_file: Path, mode: str = 'exact'):
    """Compare two files and report results"""
    
    if not actual_file.exists():
        print(f"❌ Error: Actual file not found: {actual_file}")
        sys.exit(1)
    
    if not expected_file.exists():
        print(f"❌ Error: Expected file not found: {expected_file}")
        sys.exit(1)
    
    # Read files
    with open(actual_file, 'r') as f:
        actual = f.read()
    
    with open(expected_file, 'r') as f:
        expected = f.read()
    
    # Validate
    validator = OutputValidator(mode)
    passed, message = validator.validate(actual, expected)
    
    # Print results
    print(f"\n📊 Validation Results")
    print(f"{'='*60}")
    print(f"Actual:   {actual_file}")
    print(f"Expected: {expected_file}")
    print(f"Mode:     {mode}")
    print(f"{'='*60}")
    
    if passed:
        print(f"✅ PASS: {message}")
        print()
        return 0
    else:
        print(f"❌ FAIL: {message}")
        print()
        return 1


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  validate_test_results.py <actual-file> <expected-file> [--mode exact|contains|pattern]")
        print("  validate_test_results.py --create-baseline <output-file> <baseline-dir>")
        print("\nExamples:")
        print("  validate_test_results.py output.txt expected.txt")
        print("  validate_test_results.py result.json baseline.json --mode exact")
        print("  validate_test_results.py output.txt expected.txt --mode contains")
        print("  validate_test_results.py --create-baseline test_output.txt baselines/")
        sys.exit(1)
    
    # Check for baseline creation mode
    if sys.argv[1] == '--create-baseline':
        if len(sys.argv) < 4:
            print("❌ Error: --create-baseline requires <output-file> <baseline-dir>")
            sys.exit(1)
        
        output_file = Path(sys.argv[2])
        baseline_dir = Path(sys.argv[3])
        create_baseline(output_file, baseline_dir)
        sys.exit(0)
    
    # Comparison mode
    actual_file = Path(sys.argv[1])
    expected_file = Path(sys.argv[2])
    mode = 'exact'
    
    # Parse additional arguments
    if len(sys.argv) >= 5 and sys.argv[3] == '--mode':
        mode = sys.argv[4]
        if mode not in ['exact', 'contains', 'pattern']:
            print(f"❌ Error: Invalid mode '{mode}'. Use 'exact', 'contains', or 'pattern'")
            sys.exit(1)
    
    exit_code = compare_files(actual_file, expected_file, mode)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
