# Security Checklist for Vibe Coding

AI-generated code frequently contains security vulnerabilities. This comprehensive checklist helps identify and prevent common security issues in vibe-coded applications.

## Critical Statistics

- **40% of AI-generated database queries** are vulnerable to SQL injection
- **Security gaps** are the #1 reason vibe-coded apps fail in production
- **AI tools lack security context** and often implement outdated or insecure patterns
- **Most breaches** in AI-generated code come from input validation failures

## Quick Security Prompt Templates

Use these when prompting AI to generate code:

**General Security:**
"Implement this feature following security best practices: input validation, output encoding, parameterized queries, HTTPS only, and environment variables for secrets."

**Authentication:**
"Use [library name] for authentication. Include password hashing, session management, account lockout, and secure password reset functionality."

**Database Operations:**
"Write this query using parameterized statements to prevent SQL injection. Validate all inputs before database operations."

**API Endpoints:**
"Create this API endpoint with input validation, rate limiting, authentication checks, and authorization for the specific resource."

## Pre-Development Security Setup

### Environment Configuration Checklist
- [ ] Create `.env` file for local secrets
- [ ] Add `.env` to `.gitignore` immediately
- [ ] Document required environment variables in README
- [ ] Never commit API keys, database credentials, or tokens
- [ ] Use proper environment variable services (Vercel, Railway, etc.)

### Dependency Management Checklist
- [ ] Use latest stable versions of dependencies
- [ ] Run `npm audit` or `pip-audit` weekly
- [ ] Update dependencies monthly
- [ ] Remove unused dependencies
- [ ] Check dependency age and maintenance status

## Input Validation (Priority 1)

### Every Input Must Be Validated
- [ ] Frontend validation (UX + first defense)
- [ ] Backend validation (true security boundary)
- [ ] Length limits enforced
- [ ] Type validation (string, number, email, etc.)
- [ ] Format validation (regex where appropriate)
- [ ] Sanitization for special characters
- [ ] Rate limiting on submission endpoints

### SQL Injection Prevention (Critical)
- [ ] Use parameterized queries or prepared statements
- [ ] Never concatenate user input into SQL
- [ ] Use ORM query builders (they parameterize automatically)
- [ ] Validate inputs before database operations
- [ ] Use least-privilege database users
- [ ] Never return raw database errors to users

### XSS Prevention
- [ ] Never use `innerHTML` with user content
- [ ] Use `textContent` or framework escaping
- [ ] Sanitize HTML if rich text required (use DOMPurify)
- [ ] Set Content-Security-Policy headers
- [ ] Validate and escape all user-generated content

### CSRF Protection
- [ ] CSRF tokens for POST, PUT, DELETE operations
- [ ] Tokens validated on backend
- [ ] SameSite cookie attribute set
- [ ] Tokens regenerated after authentication

## Authentication & Authorization

### Authentication Checklist
- [ ] Use established auth library (Supabase, Firebase, Auth0, NextAuth)
- [ ] Passwords hashed with bcrypt/argon2 (never MD5/SHA1)
- [ ] Minimum password requirements enforced
- [ ] Account lockout after failed login attempts
- [ ] Secure session management
- [ ] Password reset functionality secure
- [ ] Email verification for new accounts
- [ ] HTTPS enforced for all auth endpoints

### Authorization Checklist
- [ ] Every protected route checks authentication
- [ ] Every data operation checks ownership/permissions
- [ ] Users can only modify their own data
- [ ] Admin functions have role checks
- [ ] API endpoints validate permissions
- [ ] Don't trust client-side permissions

### Session Management Checklist
- [ ] Secure cookie flags (httpOnly, secure, sameSite)
- [ ] Session expiration implemented (1-24 hours)
- [ ] Sessions invalidated on logout
- [ ] Session regeneration after authentication
- [ ] Strong session secret from environment variable

## API Security

### Rate Limiting Checklist
- [ ] Rate limiting on all public APIs
- [ ] Stricter limits for auth endpoints (3-5 attempts per 15 min)
- [ ] Different limits for authenticated vs unauthenticated users
- [ ] Appropriate HTTP headers returned

### CORS Configuration Checklist
- [ ] CORS configured with specific allowed origins
- [ ] No wildcard (*) in production
- [ ] Credentials handled properly
- [ ] Different configs for development and production

### Error Handling Checklist
- [ ] Generic error messages to users
- [ ] Detailed logging internally only
- [ ] No stack traces in production
- [ ] No database error details exposed
- [ ] No file paths or system info exposed
- [ ] Custom error pages configured

## Data Protection

### Encryption Checklist
**In Transit:**
- [ ] HTTPS everywhere (enforce with HSTS)
- [ ] Valid SSL certificate
- [ ] TLS 1.2 or higher
- [ ] No mixed content warnings

**At Rest:**
- [ ] Sensitive fields encrypted in database
- [ ] Encryption keys stored in environment variables
- [ ] Consider field-level encryption for PII

### Password Handling
- [ ] Passwords hashed with bcrypt (salt rounds 12+)
- [ ] Password requirements enforced
- [ ] Common passwords blocked
- [ ] Password strength indicator provided

### Privacy Compliance
- [ ] Privacy policy in place
- [ ] Clear consent for data collection
- [ ] Data export functionality
- [ ] Data deletion functionality
- [ ] Minimal data collection principle

## File Upload Security

### File Upload Checklist
- [ ] Validate file types (whitelist approach)
- [ ] Limit file sizes (specify maximum)
- [ ] Sanitize filenames
- [ ] Store outside webroot
- [ ] Don't trust file extensions (check content)
- [ ] Generate unique filenames
- [ ] Consider virus scanning for user uploads

## Common AI-Generated Vulnerabilities

### Patterns to Watch For

**1. Hardcoded Secrets**
```javascript
// BAD - AI often does this
const API_KEY = "sk-1234567890abcdef";

// GOOD - Always use environment variables
const API_KEY = process.env.API_KEY;
```

**2. String Concatenation in SQL**
```python
# BAD - SQL injection vulnerable
query = f"SELECT * FROM users WHERE id = {user_id}"

# GOOD - Parameterized query
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_id,))
```

**3. Weak Input Validation**
```javascript
// BAD - No validation
app.post('/user', (req, res) => {
  db.createUser(req.body);
});

// GOOD - Comprehensive validation
app.post('/user', (req, res) => {
  const { email, name } = req.body;
  if (!email || !isValidEmail(email)) {
    return res.status(400).json({ error: 'Invalid email' });
  }
  if (!name || name.length > 100) {
    return res.status(400).json({ error: 'Invalid name' });
  }
  db.createUser({ email, name });
});
```

**4. Missing Authorization Checks**
```javascript
// BAD - Only checks authentication
app.delete('/post/:id', requireAuth, async (req, res) => {
  await Post.delete(req.params.id);
});

// GOOD - Checks authorization
app.delete('/post/:id', requireAuth, async (req, res) => {
  const post = await Post.findById(req.params.id);
  if (post.userId !== req.user.id) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  await Post.delete(req.params.id);
});
```

## Security Testing

### Manual Testing Checklist
- [ ] Test with malicious inputs (SQL, XSS payloads)
- [ ] Test with extremely long inputs
- [ ] Test with special characters
- [ ] Test authorization boundaries
- [ ] Test rate limiting
- [ ] Test file upload restrictions

### Automated Testing Tools
- [ ] OWASP ZAP for vulnerability scanning
- [ ] Snyk for dependency vulnerabilities
- [ ] npm audit / pip-audit for package security
- [ ] ESLint security plugins

### Pre-Deployment Checklist
- [ ] All secrets in environment variables
- [ ] HTTPS enforced
- [ ] Security headers configured
- [ ] Rate limiting active
- [ ] Error messages sanitized
- [ ] Logging configured (but no sensitive data logged)
- [ ] Security scan completed
- [ ] Code review focusing on security

## When to Get Professional Help

Seek security professional review when:
- Handling payment information
- Storing sensitive personal data
- Building healthcare or financial applications
- User count exceeds 1,000
- Dealing with authentication systems
- Operating in regulated industries

## Security Prompt Library

**For each feature you build, use appropriate security prompts:**

**User Registration:**
"Create user registration with secure password hashing (bcrypt, 12 salt rounds), email validation, input sanitization, and rate limiting (5 attempts per 15 minutes)."

**Login System:**
"Implement login with account lockout after 5 failed attempts, secure session management (httpOnly, secure, sameSite cookies), and proper error messages that don't reveal user existence."

**Data Updates:**
"Create this update endpoint with authentication check, authorization verification (user owns the resource), input validation, and parameterized database queries."

**File Upload:**
"Implement file upload with type whitelist (only images), 5MB size limit, filename sanitization, storage outside webroot, and unique filename generation."

**API Endpoint:**
"Create this API endpoint with rate limiting (100 requests per 15 minutes), input validation, authentication required, and proper error handling."

## Emergency Response Plan

If you discover a security vulnerability:

1. **Immediate Actions:**
   - Take affected systems offline if actively exploited
   - Preserve logs for investigation
   - Document the vulnerability

2. **Assessment:**
   - Determine scope of exposure
   - Identify affected users/data
   - Check logs for exploitation attempts

3. **Remediation:**
   - Fix the vulnerability immediately
   - Deploy patch to production
   - Force password resets if needed
   - Notify affected users if data was compromised

4. **Prevention:**
   - Add automated tests for the vulnerability
   - Update security checklist
   - Review similar code patterns
   - Improve security prompts

## Resources

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP Cheat Sheets: https://cheatsheetseries.owasp.org/
- CWE Top 25: https://cwe.mitre.org/top25/
- Security Headers: https://securityheaders.com/
