# Effective Prompting Patterns for Vibe Coding

This reference provides proven prompt templates and patterns for effective vibe coding across different scenarios.

## Core Prompting Principles

1. **Be specific, not vague** - "Build a login system with email validation" > "Make auth"
2. **Explain intent first** - Help AI understand the "why" before the "what"
3. **Include context** - Tech stack, constraints, environment
4. **Request confirmation** - Ask AI to confirm approach before generating
5. **Ask for explanations** - Request edge cases and implementation details
6. **Iterate gradually** - Build complexity layer by layer

## Prompt Structure Template

```
[CONTEXT]
I'm building [project description] using [tech stack].

[INTENT]
I need to [what you're trying to accomplish] because [why].

[SPECIFIC REQUEST]
Create [specific component/feature] that [specific requirements].

[CONSTRAINTS]
- Requirement 1
- Requirement 2
- Requirement 3

[VALIDATION REQUEST]
Please confirm this approach before generating code, and explain any edge cases I should consider.
```

## Category-Specific Prompt Patterns

### 1. Initial Project Setup

**Pattern: Comprehensive Setup**
```
I want to build a [type of app] that [primary purpose].

Tech stack I want to use:
- Frontend: [framework]
- Backend: [framework/service]
- Database: [database]
- Deployment: [platform]

Please:
1. Confirm this stack is appropriate for my use case
2. Set up the project structure with proper folder organization
3. Initialize with version control
4. Set up environment variable handling
5. Create a README with setup instructions

Primary features (MVP only):
- [Feature 1]
- [Feature 2]
- [Feature 3]
```

**Example:**
```
I want to build a task management app that helps individuals track daily todos.

Tech stack:
- Frontend: React with Vite
- Backend: Supabase
- Deployment: Vercel

Please:
1. Confirm this stack is appropriate
2. Set up the project structure
3. Initialize Git and create .gitignore
4. Set up environment variables for Supabase
5. Create README with setup instructions

MVP features only:
- Add tasks
- Mark tasks complete
- View task list
```

### 2. Feature Implementation

**Pattern: Secure Feature Addition**
```
Context: I'm working on [project type] using [tech stack].

I need to add [feature name] that allows users to [action].

Requirements:
- [Functional requirement 1]
- [Functional requirement 2]
- Security: Input validation, sanitization, [specific security needs]
- Error handling: [expected error scenarios]

Please:
1. Confirm the approach before implementing
2. Implement with security best practices
3. Include error handling
4. Write with modular, maintainable code
5. Add comments for complex logic
6. Suggest any edge cases I should test
```

**Example:**
```
Context: I'm working on a todo app using React and Supabase.

I need to add task editing that allows users to modify existing tasks.

Requirements:
- Inline editing on click
- Save on Enter or blur
- Cancel on Escape
- Security: Validate task ownership, sanitize input
- Error handling: Handle network failures, show user-friendly messages

Please:
1. Confirm this UX approach is good
2. Implement with proper input validation
3. Include optimistic updates with rollback
4. Add loading states
5. Handle errors gracefully
6. Identify edge cases to test
```

### 3. Debugging and Error Resolution

**Pattern: Contextual Debugging**
```
I'm trying to [what you're attempting] in my [project type].

Expected behavior:
[What should happen]

Actual behavior:
[What's actually happening]

Error message:
```
[Full error with stack trace]
```

Relevant code:
```[language]
[Code snippet]
```

Environment:
- [Framework and version]
- [Other relevant dependencies]

Please debug this step-by-step and explain:
1. What's causing the error
2. Why my current approach doesn't work
3. How to fix it properly
4. Any related issues I should watch for
```

**Example:**
```
I'm trying to authenticate users in my React + Supabase app.

Expected behavior:
User submits login form, gets authenticated, redirected to dashboard.

Actual behavior:
Form submits but nothing happens. No error in console.

Error message:
(none visible)

Relevant code:
```javascript
const handleLogin = async (email, password) => {
  const { data, error } = await supabase.auth.signIn({
    email,
    password
  });
  navigate('/dashboard');
};
```

Environment:
- React 18.2
- Supabase 2.38.0

Please debug this step-by-step and explain what's wrong.
```

### 4. Architecture Decisions

**Pattern: Trade-off Analysis**
```
I'm building [project] and need to decide between [Option A] and [Option B] for [specific need].

Option A: [Description]
Pros I see: [Your understanding]
Cons I see: [Your concerns]

Option B: [Description]
Pros I see: [Your understanding]
Cons I see: [Your concerns]

Context:
- User count estimate: [number]
- Budget constraints: [details]
- Timeline: [deadline]
- Technical skill level: [your level]
- Scalability needs: [requirements]

Please:
1. Explain the key trade-offs
2. Recommend the simpler option unless complexity is justified
3. Identify any hidden costs or complications
4. Suggest if there's a third option I haven't considered
```

**Example:**
```
I'm building a social app and need to decide between REST API vs GraphQL.

REST:
Pros: Simpler, I understand it, easier to debug
Cons: Multiple endpoints, over-fetching

GraphQL:
Pros: Flexible queries, single endpoint
Cons: More complex setup, harder to debug

Context:
- User count: 100-500 expected in first year
- Budget: Minimal, using free tiers
- Timeline: 2 weeks to MVP
- Skill level: Intermediate, never used GraphQL
- Scalability: Eventually will need it, but not now

Please recommend the best option for MVP with justification.
```

### 5. Code Review and Refactoring

**Pattern: Code Quality Improvement**
```
Please review this [component/function/file] for:
1. Security vulnerabilities
2. Performance issues
3. Code maintainability
4. Edge cases not handled
5. Best practice violations

Code:
```[language]
[Your code]
```

Specifically concerned about:
- [Concern 1]
- [Concern 2]

Please provide:
1. List of issues found (prioritized by severity)
2. Refactored version with improvements
3. Explanation of changes made
4. Suggestions for testing
```

**Example:**
```
Please review this user registration function for security and quality:

```javascript
app.post('/register', async (req, res) => {
  const { email, password, name } = req.body;
  const user = await db.createUser(email, password, name);
  res.json({ success: true, user });
});
```

Specifically concerned about:
- Input validation
- Password security
- Error handling

Please provide prioritized issues, refactored code, and explanation.
```

### 6. Testing

**Pattern: Comprehensive Test Generation**
```
Please generate tests for this [component/function]:

Code to test:
```[language]
[Your code]
```

Test requirements:
- Framework: [testing framework]
- Test types needed: [unit/integration/e2e]
- Coverage areas:
  - Happy path
  - Edge cases
  - Error scenarios
  - [Specific scenarios]

Please provide:
1. Complete test file with all scenarios
2. Explanation of what each test validates
3. Any additional edge cases I should consider
4. Setup/teardown if needed
```

**Example:**
```
Please generate tests for this task creation function:

```javascript
async function createTask(userId, title, description) {
  if (!title || title.length > 200) {
    throw new Error('Invalid title');
  }
  return await db.tasks.create({
    userId,
    title,
    description,
    createdAt: new Date()
  });
}
```

Test requirements:
- Framework: Jest
- Cover happy path, validation errors, database errors
- Test with various input lengths
- Test with special characters

Please provide complete test file with explanations.
```

### 7. Documentation

**Pattern: Auto-Documentation**
```
Please create comprehensive documentation for this [component/API/project]:

[Code or project description]

Documentation needed:
- README with setup instructions
- API endpoint documentation (if applicable)
- Component usage examples (if applicable)
- Environment variables required
- Deployment instructions
- Known limitations
- Troubleshooting guide

Target audience: [Developers/non-technical users/both]

Please format in clear markdown with code examples.
```

## Anti-Patterns (What NOT to Do)

### ❌ Too Vague
"Build a social media app"
- No tech stack specified
- No feature definition
- No constraints
- AI will make many assumptions

### ❌ Too Ambitious in Single Prompt
"Build a complete e-commerce platform with user authentication, product catalog, shopping cart, payment processing, admin dashboard, and email notifications"
- Too much at once
- Likely to produce broken code
- Better to build incrementally

### ❌ No Context
"Add a database"
- What kind of database?
- For what purpose?
- What data needs storing?
- AI will guess (probably wrong)

### ❌ No Validation Request
"Create a login system" (and accepting code without review)
- May have security holes
- Might not match your needs
- No explanation of implementation
- Always ask for confirmation and explanation

### ❌ Copy-Paste Errors Without Context
```
Error: Cannot read property 'map' of undefined
Fix this
```
- No code provided
- No explanation of what you're trying to do
- AI can't help effectively

## Advanced Prompt Patterns

### Chain-of-Thought Prompting
```
I need to implement [feature].

Let's think through this step-by-step:
1. What data structures do we need?
2. What are the user interaction flows?
3. What edge cases exist?
4. What security considerations apply?
5. How should errors be handled?

Please answer these questions first, then implement based on the analysis.
```

### Constraint-Based Prompting
```
Create [feature] with these strict constraints:
- MUST use [technology]
- MUST NOT exceed [size/time limit]
- MUST handle [specific edge case]
- MUST follow [specific pattern]

If any constraint cannot be met, explain why before proceeding.
```

### Iterative Refinement Pattern
```
[First prompt] Create a basic [feature]

[After receiving code]
Good start. Now enhance it to:
- Add [specific improvement]
- Handle [edge case]
- Improve [aspect]

[After second iteration]
Almost there. Final refinements:
- Optimize [specific area]
- Add [polish]
```

### Security-First Pattern
```
Create [feature] following security best practices:

Required security measures:
- Input validation: [specific requirements]
- Output encoding: [requirements]
- Authentication: [requirements]
- Authorization: [requirements]
- Rate limiting: [requirements]
- Error handling: [requirements]

Please confirm security approach before implementation, then generate code with security comments explaining each measure.
```

## Prompt Optimization Tips

### 1. Length vs. Specificity Balance
- Short prompts → Fast but generic results
- Long prompts → Slower but tailored results
- Sweet spot: 3-7 sentences + clear requirements list

### 2. Use Examples When Helpful
```
Create a filter component like this:
[Example or mockup]

With functionality similar to [reference app]
```

### 3. Reference Previous Work
```
Using the same pattern as our UserList component, create a ProductList component that...
```

### 4. Specify What NOT to Include
```
Create this feature but:
- Don't add animation (keeping it simple)
- Don't use external libraries
- Don't implement feature X yet (future iteration)
```

### 5. Request Explanatory Comments
```
...and include comments explaining:
- Why you chose this approach
- What each complex section does
- Any gotchas I should know about
```

## Tool-Specific Prompt Adjustments

### For Lovable/Bolt (Visual Focus)
```
Create a [component] with:
- Clean, modern UI design
- Mobile-responsive layout
- Accessibility features (ARIA labels, keyboard navigation)
- Smooth transitions
- Following [design system if applicable]
```

### For Cursor (Code Focus)
```
Implement [feature] with:
- TypeScript for type safety
- Comprehensive error handling
- Unit tests included
- Documentation comments
- Following existing project patterns in [file/folder]
```

### For Replit (Learning Focus)
```
Build [feature] and explain:
- Why each decision was made
- What each code block does
- Common mistakes to avoid
- How to extend this later
```

## Common Scenarios Library

### Authentication System
```
Create a secure authentication system using [auth service]:
- Email/password login
- User registration with email verification
- Password reset functionality
- Session management
- Protected routes
- Logout functionality

Security requirements:
- Password hashing (if not using auth service)
- Input validation
- Rate limiting on auth endpoints
- Secure session storage

Please confirm approach, then implement step-by-step.
```

### CRUD Operations
```
Create full CRUD operations for [resource]:
- Create: Form with validation
- Read: List view and detail view
- Update: Inline or modal editing
- Delete: With confirmation dialog

Requirements:
- Input validation on all forms
- Loading states during operations
- Error handling with user feedback
- Optimistic updates where appropriate
- Authorization checks (users own their data)

Use [tech stack] and implement with proper security.
```

### API Integration
```
Integrate [API name] to [purpose]:

API documentation: [link or key details]

Features needed:
- [Feature 1]
- [Feature 2]

Requirements:
- API key stored in environment variables
- Error handling for API failures
- Rate limiting awareness
- Caching if appropriate
- Loading states
- User-friendly error messages

Please review the API docs, confirm approach, then implement.
```

## Measuring Prompt Effectiveness

A good prompt results in code that:
- ✅ Runs without immediate errors
- ✅ Handles expected edge cases
- ✅ Includes basic security measures
- ✅ Is reasonably maintainable
- ✅ Includes helpful comments
- ✅ Matches your tech stack and patterns

If you're not getting these results, refine your prompts using patterns from this guide.

## Quick Reference

**Every prompt should answer:**
1. What are you building?
2. What tech stack?
3. What specific requirements?
4. What constraints or edge cases?
5. What security considerations?

**Every prompt should request:**
1. Confirmation before generation
2. Explanation of approach
3. Edge cases to test
4. Security considerations

**Every prompt should avoid:**
1. Vague language
2. Assuming AI knows your context
3. Kitchen-sink feature requests
4. Accepting first output without review
