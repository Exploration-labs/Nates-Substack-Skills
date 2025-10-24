# Test Patterns for Different Skill Types

This reference provides test case examples for common skill patterns.

## Script-Based Skills

For skills that primarily use scripts to perform operations (e.g., PDF manipulation, image processing).

### Unit Test Example

```json
{
  "name": "Test PDF rotation script",
  "type": "script",
  "script": "rotate_pdf.py",
  "args": ["input.pdf", "output.pdf", "90"],
  "expected_exit_code": 0,
  "expected_output": null,
  "description": "Verify PDF rotation script executes without errors"
}
```

### Integration Test Example

```json
{
  "name": "Test complete PDF processing workflow",
  "type": "workflow",
  "description": "End-to-end test of PDF skill",
  "steps": [
    {
      "action": "Extract form fields",
      "script": "extract_form_field_info.py",
      "args": ["test_form.pdf"],
      "expected_output": {"pattern": "\\{.*fields.*\\}"}
    },
    {
      "action": "Fill form fields",
      "script": "fill_fillable_fields.py",
      "args": ["test_form.pdf", "filled_form.pdf", "data.json"],
      "expected_exit_code": 0
    }
  ],
  "expected_output": {
    "type": "file",
    "path": "filled_form.pdf",
    "validation": "File exists and is valid PDF"
  }
}
```

### Regression Test Example

```json
{
  "name": "Regression: PDF text extraction consistency",
  "description": "Ensure extracted text matches baseline",
  "input": {
    "script": "extract_text.py",
    "args": ["sample.pdf"]
  },
  "baseline_file": "baselines/sample_pdf_text.txt",
  "validation_method": "exact_match"
}
```

## Document Creation Skills

For skills that create or edit documents (e.g., DOCX, PPTX, XLSX).

### Integration Test Example

```json
{
  "name": "Test document creation with formatting",
  "type": "workflow",
  "description": "Create a formatted document and verify structure",
  "input": {
    "user_query": "Create a report with title, sections, and bullet points",
    "parameters": {
      "title": "Q4 Sales Report",
      "sections": ["Executive Summary", "Key Metrics", "Recommendations"]
    }
  },
  "expected_output": {
    "type": "docx",
    "validation": [
      "Contains title 'Q4 Sales Report'",
      "Has 3 main sections",
      "Includes bullet points in Recommendations section"
    ]
  }
}
```

### Regression Test Example

```json
{
  "name": "Regression: Presentation template consistency",
  "description": "Verify presentation maintains expected structure",
  "input": {
    "user_query": "Create a 5-slide pitch deck about AI startups",
    "template": "pitch_deck_template.pptx"
  },
  "baseline_file": "baselines/pitch_deck_structure.json",
  "validation_method": "structural_match",
  "notes": "Compare slide count, layout types, and key content areas"
}
```

## API Integration Skills

For skills that interact with external APIs or services.

### Unit Test Example

```json
{
  "name": "Test API authentication",
  "type": "function",
  "function": "authenticate_api",
  "input": {
    "credentials": "test_credentials.json"
  },
  "expected_output": {
    "contains": "access_token"
  },
  "description": "Verify successful API authentication"
}
```

### Integration Test Example

```json
{
  "name": "Test complete data fetch and processing",
  "type": "workflow",
  "description": "Fetch data from API and process it",
  "steps": [
    {
      "action": "Authenticate",
      "expected_result": "Success"
    },
    {
      "action": "Fetch data",
      "endpoint": "/api/v1/data",
      "expected_status": 200
    },
    {
      "action": "Process response",
      "expected_output": {"pattern": ".*processed.*"}
    }
  ]
}
```

## Workflow-Based Skills

For skills with multi-step sequential processes.

### Integration Test Example

```json
{
  "name": "Test multi-step form filling workflow",
  "type": "workflow",
  "description": "Complete form filling process from analysis to output",
  "steps": [
    {
      "step": 1,
      "action": "Analyze form structure",
      "validation": "Form fields identified"
    },
    {
      "step": 2,
      "action": "Create field mapping",
      "validation": "Mapping file created"
    },
    {
      "step": 3,
      "action": "Validate mapping",
      "validation": "No validation errors"
    },
    {
      "step": 4,
      "action": "Fill form",
      "validation": "Output file created"
    },
    {
      "step": 5,
      "action": "Verify output",
      "validation": "All fields filled correctly"
    }
  ]
}
```

## Reference Documentation Skills

For skills that primarily provide guidance and best practices.

### Integration Test Example

```json
{
  "name": "Test guideline application",
  "type": "workflow",
  "description": "Verify guidelines are correctly applied",
  "input": {
    "user_query": "Apply brand guidelines to create a presentation",
    "content": "Product launch announcement"
  },
  "expected_output": {
    "validation": [
      "Uses correct brand colors from guidelines",
      "Uses specified fonts",
      "Follows layout templates",
      "Includes required brand elements"
    ]
  }
}
```

### Regression Test Example

```json
{
  "name": "Regression: Style consistency check",
  "description": "Ensure styling remains consistent with guidelines",
  "input": {
    "user_query": "Create marketing materials using our brand guidelines",
    "test_case": "social_media_post"
  },
  "baseline_file": "baselines/brand_applied_example.json",
  "validation_method": "style_match",
  "notes": "Compare colors, fonts, spacing, and brand element usage"
}
```

## Test Data Management

### Creating Test Fixtures

```json
{
  "test_fixtures": {
    "pdf_samples": [
      {
        "name": "simple_form.pdf",
        "description": "Basic PDF form with text fields",
        "location": "fixtures/pdfs/simple_form.pdf"
      },
      {
        "name": "complex_document.pdf",
        "description": "Multi-page PDF with images and tables",
        "location": "fixtures/pdfs/complex_document.pdf"
      }
    ],
    "expected_outputs": [
      {
        "test": "pdf_text_extraction",
        "output_file": "fixtures/expected/extracted_text.txt"
      }
    ]
  }
}
```

## Validation Methods

### Available Validation Types

1. **exact_match** - Outputs must match exactly (whitespace normalized)
2. **contains** - Output must contain specified substring
3. **pattern** - Output must match regex pattern
4. **structural_match** - Document structure must match (for DOCX/PPTX/XLSX)
5. **functional_match** - Output achieves same functional result (for scripts)

### Example Validation Configurations

```json
{
  "validation_examples": [
    {
      "method": "exact_match",
      "use_case": "Text output that must be identical",
      "config": {
        "normalize_whitespace": true,
        "case_sensitive": true
      }
    },
    {
      "method": "pattern",
      "use_case": "Output with variable content but known format",
      "config": {
        "pattern": "Report generated: \\d{4}-\\d{2}-\\d{2}",
        "flags": ["MULTILINE"]
      }
    },
    {
      "method": "structural_match",
      "use_case": "Document with consistent structure but varying content",
      "config": {
        "check_elements": ["sections", "headings", "tables"],
        "ignore_content": true
      }
    }
  ]
}
```
