# Question Templates & Examples

This reference provides templates for structuring clarifying questions and examples demonstrating effective requirements elicitation.

## Question Structuring Principles

### Effective Questions:
- Are specific and actionable
- Reference concrete scenarios from the document
- Avoid making assumptions
- Identify ambiguity rather than inventing detail
- Are organized by audience (PM vs Engineering team)
- Include context about why the question matters

### Question Template Format:
```
**[Dimension]:** [Brief context from document]
- [Specific question]?
- [Follow-up question if needed]?

*Why this matters:* [Brief explanation of technical impact]
```

## Question Categories by Audience

### Questions for Product Manager

These questions clarify product intent, user expectations, and business rules:

#### User Behavior & Intent
- "When [specific user action], what should the user see/experience?"
- "What should happen if [edge case scenario]?"
- "Who is the primary user for [feature]? Are there secondary user types?"
- "What should the user be able to do with [thing mentioned]?"
- "What happens when [conflicting actions occur]?"

#### Business Rules & Logic
- "The document mentions [business concept] - what are the specific rules governing this?"
- "What defines [business term] in this context?"
- "Are there exceptions to [rule mentioned]?"
- "What validation should occur before [action]?"
- "What happens if [business condition] is not met?"

#### Scope & Boundaries
- "The document mentions [feature aspect] - is this in scope for this phase?"
- "What is explicitly out of scope?"
- "What existing functionality should be preserved/changed/removed?"
- "Are there must-have vs nice-to-have elements?"

#### Success & Measurement
- "How will we know [feature] is working correctly from a user perspective?"
- "What metrics define success?"
- "What user feedback or data validates this works?"

### Questions for Engineering Team

These questions elicit technical decisions and architectural considerations:

#### Architecture & Design
- "What systems/components need to be involved?"
- "Where should [functionality] be implemented (client, server, service)?"
- "How should [feature] integrate with [existing system]?"
- "What is the appropriate integration pattern for [requirement]?"
- "Are there existing components we should reuse or extend?"

#### Data & State
- "How should [data mentioned] be structured and stored?"
- "What is the relationship between [entity A] and [entity B]?"
- "Where should [state] live and how should it be managed?"
- "What is the data lifecycle for [entity]?"
- "How should we handle data consistency for [scenario]?"

#### Performance & Scale
- "What is the expected volume of [requests/data/users]?"
- "What are acceptable latency targets for [operation]?"
- "How should [feature] scale as usage grows?"
- "Are there caching opportunities for [data]?"
- "What operations can be asynchronous vs synchronous?"

#### Security & Access
- "What authentication/authorization is required?"
- "Who should have access to [functionality/data]?"
- "What sensitive data needs protection?"
- "Are there compliance requirements (GDPR, etc.)?"
- "What audit logging is needed?"

#### Error Handling & Reliability
- "What should happen when [external dependency] fails?"
- "How should the system behave during [failure scenario]?"
- "What retry/fallback strategy is appropriate?"
- "What errors need to surface to users vs be logged?"
- "What is the rollback plan if [issue occurs]?"

#### Operations & Deployment
- "How should [feature] be deployed (gradual rollout, feature flag, etc.)?"
- "What configuration will be needed?"
- "What monitoring/alerting is needed?"
- "How can this be rolled back if needed?"
- "What migration is required for existing data?"

## Examples: Good vs Bad Requirements Analysis

### Example 1: User Authentication

**Product Document Says:**
"Users should be able to log in with social providers."

**❌ Bad Response (Making Assumptions):**
"This requires implementing OAuth 2.0 with Google, Facebook, and Apple Sign-In. We'll store JWT tokens in localStorage and refresh them every 30 minutes. The user table needs a social_provider_id column with a unique constraint."

**✅ Good Response (Eliciting Details):**

**Questions for PM:**
- **User Experience:** What social providers should be supported (Google, Facebook, Apple, others)?
- **Account Linking:** Can a user link multiple social accounts to one profile? What happens if they try to log in with a different provider using the same email?
- **Account Creation:** Should logging in with social automatically create an account, or require additional steps?
- **User Data:** What information do we need from the social provider (name, email, profile picture, etc.)?

**Questions for Engineering:**
- **Authentication Flow:** Where should OAuth tokens be stored and managed?
- **Session Management:** What is the appropriate session duration and refresh strategy?
- **Existing Systems:** How does this integrate with our current authentication system?
- **Data Model:** How should social provider associations be stored relative to user accounts?

**Identified Gaps:**
- No specification of which social providers
- Unclear account linking/creation flow
- No session management requirements
- No error handling for failed social auth

### Example 2: Notifications

**Product Document Says:**
"Send notifications when orders are updated."

**❌ Bad Response (Making Assumptions):**
"We'll use Firebase Cloud Messaging for push notifications and SendGrid for emails. Users get notified immediately when order status changes to 'shipped', 'delivered', or 'cancelled'. Notifications include order number, status, and tracking link."

**✅ Good Response (Eliciting Details):**

**Questions for PM:**
- **User Control:** What order updates warrant notification (all status changes, or specific ones)?
- **Notification Channels:** Should notifications be push, email, SMS, or user-configurable?
- **Frequency:** Should users receive one notification per change, or can updates be batched?
- **Content:** What information should the notification contain?
- **User Preferences:** Can users opt out or customize notification preferences?

**Questions for Engineering:**
- **Trigger Logic:** What exactly triggers a notification (database update, service event, external webhook)?
- **Delivery Mechanism:** What notification infrastructure exists or needs to be implemented?
- **Reliability:** How do we handle notification delivery failures?
- **Scale:** What is the expected notification volume?
- **Timing:** Should notifications be real-time or can they be queued?

**Identified Gaps:**
- Which order status changes warrant notification
- Notification channel (push, email, SMS)
- User notification preferences
- Timing and batching requirements

### Example 3: Search Functionality

**Product Document Says:**
"Add search to help users find their past transactions."

**❌ Bad Response (Making Assumptions):**
"Implement Elasticsearch for full-text search with fuzzy matching. Index transaction_id, amount, date, merchant_name with a 2-hour sync delay. Support advanced queries with date ranges and amount filters. Return results sorted by relevance score with pagination at 25 per page."

**✅ Good Response (Eliciting Details):**

**Questions for PM:**
- **Search Scope:** What fields should be searchable (amount, merchant, date, description, category, etc.)?
- **Search Behavior:** Should search be exact match, partial match, or fuzzy?
- **Result Display:** How should results be displayed? What information needs to be shown?
- **Filters:** Are filters needed (date range, amount range, merchant, category)?
- **Empty Results:** What happens if no transactions match?

**Questions for Engineering:**
- **Search Technology:** What search capabilities exist in our current stack?
- **Data Volume:** How many transactions per user are we searching through?
- **Performance:** What response time is acceptable for search queries?
- **Data Freshness:** How fresh should search results be (real-time, 1-minute delay, etc.)?
- **Ranking:** How should results be sorted (relevance, date, amount)?

**Identified Gaps:**
- Searchable fields not specified
- Search matching behavior unclear
- No performance/latency requirements
- Result ranking criteria undefined

## Common Requirement Anti-Patterns

### Vague Quantifiers
❌ "Handle many users"
❌ "Fast response time"
❌ "Store data efficiently"

✅ Ask: "What is the expected user count?" "What latency is acceptable?" "What is the expected data volume?"

### Missing Error States
❌ "Display user profile"

✅ Ask: "What if the profile doesn't exist?" "What if the profile is loading?" "What if there's a network error?"

### Ambiguous Actions
❌ "Process the order"

✅ Ask: "What specific steps constitute processing?" "What happens at each step?" "What can fail?"

### Undefined Terms
❌ "Implement the workflow"

✅ Ask: "What are the specific steps in the workflow?" "Who is involved at each step?" "What are the decision points?"

### Implicit Assumptions
❌ "Users can edit their posts"

✅ Ask: "Can users edit posts indefinitely or within a time window?" "What happens to comments/likes after edit?" "Is edit history tracked?"

## Structuring the Output

Organize clarifying questions into a clear document structure:

```markdown
# Requirements Clarification: [Feature Name]

## Summary
[1-2 sentence overview of the feature and key areas needing clarification]

## Critical Gaps
[List the most important missing details that block implementation]

## Questions for Product Manager
### [Category 1]
- Question 1
- Question 2

### [Category 2]
- Question 3
- Question 4

## Questions for Engineering Team  
### [Category 1]
- Question 1
- Question 2

### [Category 2]
- Question 3
- Question 4

## Risk Assessment
[Risks identified based on current gaps]

## Assumptions to Validate
[Any assumptions implied by the document that should be explicitly confirmed]
```
