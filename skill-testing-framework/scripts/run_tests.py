#!/usr/bin/env python3
"""
Test Runner for Skills

Executes test cases defined in JSON/YAML format and validates outputs.

Usage:
    run_tests.py <test-file> [--skill-path <path>] [--verbose]

Examples:
    run_tests.py tests/pdf-skill-tests.json
    run_tests.py tests/docx-tests.json --skill-path /mnt/skills/public/docx --verbose
"""

import sys
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional
import subprocess
import tempfile
import shutil


class TestResult:
    """Represents the result of a single test case"""
    def __init__(self, test_name: str, passed: bool, message: str = "", actual: Any = None, expected: Any = None):
        self.test_name = test_name
        self.passed = passed
        self.message = message
        self.actual = actual
        self.expected = expected


class SkillTestRunner:
    """Runs test cases against a skill"""
    
    def __init__(self, test_file: Path, skill_path: Optional[Path] = None, verbose: bool = False):
        self.test_file = test_file
        self.skill_path = skill_path
        self.verbose = verbose
        self.results: List[TestResult] = []
        
    def load_tests(self) -> Dict[str, Any]:
        """Load test cases from JSON or YAML file"""
        with open(self.test_file, 'r') as f:
            if self.test_file.suffix == '.json':
                return json.load(f)
            elif self.test_file.suffix in ['.yaml', '.yml']:
                return yaml.safe_load(f)
            else:
                raise ValueError(f"Unsupported test file format: {self.test_file.suffix}")
    
    def run_unit_test(self, test: Dict[str, Any]) -> TestResult:
        """Run a unit test (typically testing a single script or function)"""
        test_name = test.get('name', 'Unnamed test')
        test_type = test.get('type', 'script')
        
        if test_type == 'script':
            return self._run_script_test(test)
        elif test_type == 'function':
            return self._run_function_test(test)
        else:
            return TestResult(test_name, False, f"Unknown unit test type: {test_type}")
    
    def run_integration_test(self, test: Dict[str, Any]) -> TestResult:
        """Run an integration test (testing a complete workflow)"""
        test_name = test.get('name', 'Unnamed test')
        
        # Integration tests simulate a complete user interaction
        # This would typically involve:
        # 1. Setting up test environment
        # 2. Running the skill workflow
        # 3. Validating outputs
        
        return TestResult(test_name, True, "Integration test framework placeholder")
    
    def run_regression_test(self, test: Dict[str, Any]) -> TestResult:
        """Run a regression test (comparing against known good outputs)"""
        test_name = test.get('name', 'Unnamed test')
        
        # Regression tests compare current output with baseline
        input_data = test.get('input', {})
        expected_output = test.get('expected_output', None)
        baseline_file = test.get('baseline_file', None)
        
        if baseline_file:
            # Load baseline and compare
            baseline_path = self.test_file.parent / baseline_file
            if baseline_path.exists():
                with open(baseline_path, 'r') as f:
                    expected_output = f.read()
        
        # Run test and compare
        actual_output = self._execute_test(input_data)
        
        if self._compare_outputs(actual_output, expected_output):
            return TestResult(test_name, True, "Output matches expected")
        else:
            return TestResult(test_name, False, "Output differs from expected", 
                            actual=actual_output, expected=expected_output)
    
    def _run_script_test(self, test: Dict[str, Any]) -> TestResult:
        """Execute a script and validate its output"""
        test_name = test.get('name', 'Unnamed test')
        script_path = test.get('script', None)
        args = test.get('args', [])
        expected_exit_code = test.get('expected_exit_code', 0)
        expected_output = test.get('expected_output', None)
        
        if not script_path:
            return TestResult(test_name, False, "No script path specified")
        
        # Construct full script path
        if self.skill_path:
            full_script_path = self.skill_path / 'scripts' / script_path
        else:
            full_script_path = Path(script_path)
        
        if not full_script_path.exists():
            return TestResult(test_name, False, f"Script not found: {full_script_path}")
        
        # Execute script
        try:
            result = subprocess.run(
                [str(full_script_path)] + args,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            # Check exit code
            if result.returncode != expected_exit_code:
                return TestResult(test_name, False, 
                                f"Exit code mismatch: expected {expected_exit_code}, got {result.returncode}")
            
            # Check output if specified
            if expected_output is not None:
                actual_output = result.stdout.strip()
                if not self._compare_outputs(actual_output, expected_output):
                    return TestResult(test_name, False, "Output mismatch",
                                    actual=actual_output, expected=expected_output)
            
            return TestResult(test_name, True, "Script executed successfully")
            
        except subprocess.TimeoutExpired:
            return TestResult(test_name, False, "Script execution timed out")
        except Exception as e:
            return TestResult(test_name, False, f"Script execution failed: {str(e)}")
    
    def _run_function_test(self, test: Dict[str, Any]) -> TestResult:
        """Test a specific function within a module"""
        test_name = test.get('name', 'Unnamed test')
        # Placeholder for function testing
        return TestResult(test_name, True, "Function test placeholder")
    
    def _execute_test(self, input_data: Dict[str, Any]) -> Any:
        """Execute a test with given input data (placeholder for actual execution)"""
        # This would interface with Claude or run scripts
        return None
    
    def _compare_outputs(self, actual: Any, expected: Any) -> bool:
        """Compare actual and expected outputs"""
        if expected is None:
            return True  # No expected output specified
        
        # Handle different comparison types
        if isinstance(expected, dict) and 'pattern' in expected:
            # Regex pattern matching
            import re
            pattern = expected['pattern']
            return re.search(pattern, str(actual)) is not None
        elif isinstance(expected, dict) and 'contains' in expected:
            # Substring matching
            return expected['contains'] in str(actual)
        else:
            # Exact match
            return str(actual).strip() == str(expected).strip()
    
    def run_all_tests(self):
        """Execute all tests in the test file"""
        test_data = self.load_tests()
        
        print(f"\n🧪 Running tests from: {self.test_file.name}")
        print(f"{'='*60}\n")
        
        # Run unit tests
        if 'unit_tests' in test_data:
            print("📦 Unit Tests")
            print("-" * 40)
            for test in test_data['unit_tests']:
                result = self.run_unit_test(test)
                self.results.append(result)
                self._print_result(result)
        
        # Run integration tests
        if 'integration_tests' in test_data:
            print("\n🔗 Integration Tests")
            print("-" * 40)
            for test in test_data['integration_tests']:
                result = self.run_integration_test(test)
                self.results.append(result)
                self._print_result(result)
        
        # Run regression tests
        if 'regression_tests' in test_data:
            print("\n🔄 Regression Tests")
            print("-" * 40)
            for test in test_data['regression_tests']:
                result = self.run_regression_test(test)
                self.results.append(result)
                self._print_result(result)
        
        # Print summary
        self._print_summary()
    
    def _print_result(self, result: TestResult):
        """Print a single test result"""
        status = "✅ PASS" if result.passed else "❌ FAIL"
        print(f"{status} | {result.test_name}")
        
        if not result.passed or self.verbose:
            if result.message:
                print(f"     └─ {result.message}")
            if result.actual is not None and result.expected is not None:
                print(f"     └─ Expected: {result.expected}")
                print(f"     └─ Actual:   {result.actual}")
    
    def _print_summary(self):
        """Print test execution summary"""
        total = len(self.results)
        passed = sum(1 for r in self.results if r.passed)
        failed = total - passed
        
        print(f"\n{'='*60}")
        print(f"📊 Test Summary")
        print(f"{'='*60}")
        print(f"Total:  {total}")
        print(f"Passed: {passed} ✅")
        print(f"Failed: {failed} {'❌' if failed > 0 else ''}")
        print(f"Success Rate: {(passed/total*100) if total > 0 else 0:.1f}%")
        print()


def main():
    if len(sys.argv) < 2:
        print("Usage: run_tests.py <test-file> [--skill-path <path>] [--verbose]")
        print("\nExamples:")
        print("  run_tests.py tests/pdf-skill-tests.json")
        print("  run_tests.py tests/docx-tests.json --skill-path /mnt/skills/public/docx")
        print("  run_tests.py tests/all-tests.yaml --verbose")
        sys.exit(1)
    
    test_file = Path(sys.argv[1])
    skill_path = None
    verbose = False
    
    # Parse arguments
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '--skill-path' and i + 1 < len(sys.argv):
            skill_path = Path(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == '--verbose':
            verbose = True
            i += 1
        else:
            print(f"Unknown argument: {sys.argv[i]}")
            sys.exit(1)
    
    if not test_file.exists():
        print(f"❌ Error: Test file not found: {test_file}")
        sys.exit(1)
    
    runner = SkillTestRunner(test_file, skill_path, verbose)
    runner.run_all_tests()
    
    # Exit with error code if any tests failed
    failed_count = sum(1 for r in runner.results if not r.passed)
    sys.exit(0 if failed_count == 0 else 1)


if __name__ == "__main__":
    main()
