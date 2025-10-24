# Writing Effective Tests for Skills

Best practices for creating comprehensive and maintainable skill tests.

## Test Design Principles

### 1. Test at Multiple Levels

**Unit Tests** - Test individual components in isolation
- Scripts should execute without errors
- Functions return expected types
- Edge cases are handled

**Integration Tests** - Test complete workflows
- End-to-end user scenarios
- Component interactions
- Real-world use cases

**Regression Tests** - Prevent breaking changes
- Compare against known baselines
- Track behavior changes over time
- Catch unintended side effects

### 2. Write Clear Test Names

Use descriptive names that explain what is being tested:

**Good:**
```json
"name": "Test PDF rotation preserves content and changes orientation"
```

**Bad:**
```json
"name": "Test 1"
```

### 3. Include Test Descriptions

Add context about what the test validates and why:

```json
{
  "name": "Test form field extraction",
  "description": "Verifies that all form fields are correctly identified and their properties (type, name, default value) are extracted accurately. This is critical for the form-filling workflow."
}
```

### 4. Use Appropriate Validation Methods

Choose validation methods based on what matters:

- **Exact match** - When output must be identical (data exports, calculations)
- **Contains** - When checking for specific content presence (error messages, required fields)
- **Pattern** - When format matters but content varies (timestamps, IDs)
- **Structural** - When structure matters but content is dynamic (documents, reports)

## Coverage Strategy

### Essential Test Coverage

Every skill should have tests for:

1. **Happy path** - Most common use case works correctly
2. **Error handling** - Graceful failure with clear error messages
3. **Edge cases** - Boundary conditions and unusual inputs
4. **Performance** - Operations complete in reasonable time

### Example Coverage Plan

```json
{
  "coverage_plan": {
    "happy_path": [
      "Standard user query with valid inputs",
      "Most common workflow sequence"
    ],
    "error_handling": [
      "Invalid input files",
      "Missing required parameters",
      "Malformed data"
    ],
    "edge_cases": [
      "Empty inputs",
      "Maximum size inputs",
      "Special characters in data",
      "Concurrent operations"
    ],
    "performance": [
      "Small file processing time < 1s",
      "Large file processing time < 30s",
      "Batch operations scale linearly"
    ]
  }
}
```

## Test Data Management

### Create Reusable Fixtures

Organize test data for reuse across multiple tests:

```
tests/
├── fixtures/
│   ├── pdfs/
│   │   ├── simple_form.pdf
│   │   ├── complex_document.pdf
│   │   └── edge_case_large.pdf
│   ├── inputs/
│   │   ├── valid_data.json
│   │   └── invalid_data.json
│   └── expected/
│       ├── extracted_text.txt
│       └── processed_output.json
├── baselines/
│   ├── pdf_baseline_v1.txt
│   └── docx_baseline_v1.json
└── test-suite.json
```

### Baseline Management

For regression tests, establish and maintain baselines:

**Creating a baseline:**
```bash
# Run skill and capture output
./scripts/process_document.py input.pdf > output.txt

# Create baseline from output
validate_test_results.py --create-baseline output.txt baselines/
```

**Updating baselines:**
- Review changes carefully before updating
- Document why baseline changed
- Consider if change is intentional or a regression
- Keep old baselines for comparison

## Writing Test Cases

### Unit Test Template

```json
{
  "name": "Descriptive test name",
  "type": "script",
  "script": "script_to_test.py",
  "args": ["arg1", "arg2"],
  "expected_exit_code": 0,
  "expected_output": {
    "pattern": "Success: .*"
  },
  "description": "What this test validates and why it matters"
}
```

### Integration Test Template

```json
{
  "name": "Descriptive workflow test name",
  "type": "workflow",
  "description": "Complete scenario being tested",
  "setup": {
    "actions": [
      "Create test directory",
      "Copy fixture files"
    ]
  },
  "steps": [
    {
      "action": "Step 1 description",
      "validation": "What to check"
    },
    {
      "action": "Step 2 description",
      "validation": "What to check"
    }
  ],
  "expected_output": {
    "type": "file",
    "validation": "How to validate the final output"
  },
  "cleanup": {
    "actions": [
      "Remove test directory",
      "Delete temporary files"
    ]
  }
}
```

### Regression Test Template

```json
{
  "name": "Regression: Specific behavior being tested",
  "description": "Why this baseline matters",
  "input": {
    "user_query": "Example query",
    "files": ["test_input.pdf"]
  },
  "baseline_file": "baselines/expected_output_v1.txt",
  "validation_method": "exact_match",
  "notes": "Important context about this test",
  "baseline_version": "1.0",
  "baseline_date": "2025-01-15"
}
```

## Test Maintenance

### When to Update Tests

**Update tests when:**
- Skill functionality intentionally changes
- New features are added
- Bugs are fixed (add regression test)
- Performance improvements are made

**Don't update tests when:**
- Tests fail due to actual bugs
- Output differs unexpectedly
- Behavior regresses

### Test Review Checklist

Before finalizing tests, verify:

- [ ] Test names are clear and descriptive
- [ ] Each test has a description explaining its purpose
- [ ] Validation methods are appropriate
- [ ] Test data is organized in fixtures
- [ ] Baselines are documented and versioned
- [ ] Edge cases are covered
- [ ] Error scenarios are tested
- [ ] Tests are independent (can run in any order)
- [ ] Tests clean up after themselves

## Common Patterns

### Testing Error Handling

```json
{
  "name": "Test error handling for missing input file",
  "type": "script",
  "script": "process_file.py",
  "args": ["nonexistent.pdf"],
  "expected_exit_code": 1,
  "expected_output": {
    "contains": "Error: File not found"
  },
  "description": "Verify graceful failure with clear error message"
}
```

### Testing with Multiple Inputs

```json
{
  "name": "Test processing multiple file types",
  "type": "parametrized",
  "test_cases": [
    {
      "input": "test.pdf",
      "expected_output": {"contains": "PDF processed"}
    },
    {
      "input": "test.docx",
      "expected_output": {"contains": "DOCX processed"}
    },
    {
      "input": "test.txt",
      "expected_output": {"contains": "TXT processed"}
    }
  ]
}
```

### Testing Performance

```json
{
  "name": "Test processing performance",
  "type": "performance",
  "script": "process_large_file.py",
  "args": ["large_file.pdf"],
  "max_execution_time": 30,
  "expected_exit_code": 0,
  "description": "Ensure large file processing completes within 30 seconds"
}
```

## Debugging Failed Tests

When a test fails:

1. **Check the failure message** - What specifically failed?
2. **Compare outputs** - Use validation tools to see differences
3. **Verify test data** - Are fixtures still valid?
4. **Check recent changes** - What changed in the skill?
5. **Run tests individually** - Isolate the failure
6. **Add logging** - Increase verbosity to see what's happening

### Using Validation Tools

```bash
# Compare actual vs expected output
validate_test_results.py actual.txt expected.txt --mode exact

# See detailed diff
validate_test_results.py actual.txt expected.txt --verbose

# Check pattern match
validate_test_results.py actual.txt expected.txt --mode pattern
```

## Best Practices Summary

1. **Test early, test often** - Add tests while developing the skill
2. **Start with happy path** - Ensure basic functionality works first
3. **Add edge cases** - Test boundary conditions and unusual inputs
4. **Document baselines** - Explain what each baseline represents
5. **Keep tests simple** - Each test should verify one thing
6. **Make tests independent** - Tests shouldn't depend on each other
7. **Use descriptive names** - Test names should explain what they test
8. **Version baselines** - Track baseline changes over time
9. **Review test failures** - Don't just update baselines blindly
10. **Maintain test data** - Keep fixtures organized and documented
