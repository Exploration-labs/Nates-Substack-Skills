# Technical Dimensions Checklist

This reference provides a comprehensive framework for identifying missing technical details in product documents. Use this to systematically analyze requirements across all critical dimensions.

## Data & State Management

### Data Models
- What entities/objects are involved?
- What are the attributes and their types?
- What are the relationships between entities?
- What is the cardinality (one-to-one, one-to-many, many-to-many)?
- Are there constraints (uniqueness, nullability, validation rules)?
- What is the data lifecycle (creation, updates, deletion, archival)?

### State Management
- What state needs to be tracked?
- Where does state live (client, server, database, cache)?
- How does state change over time?
- What triggers state transitions?
- Are there state conflicts to resolve?
- What happens during partial failures?

### Data Sources & Sinks
- Where does data originate?
- Where does data need to flow to?
- Are there external data dependencies?
- What data needs to be synchronized across systems?
- What are the data retention requirements?

## Interfaces & Integration

### APIs & Endpoints
- What are the API operations (read, write, delete)?
- What are the request/response formats?
- What are the authentication/authorization requirements?
- What are the rate limits or quotas?
- Are there pagination requirements?
- What error responses should be returned?

### System Integration
- What systems need to integrate?
- What is the integration pattern (sync, async, event-driven)?
- What happens when external systems are unavailable?
- Are there data transformation requirements?
- What is the retry/fallback strategy?

### User Interfaces
- What are the user interaction flows?
- What inputs are required from users?
- What validation happens on input?
- What feedback is provided to users?
- What are the accessibility requirements?
- What device types/form factors are supported?

## Performance & Scale

### Volume & Load
- What is the expected data volume?
- What is the expected number of users/requests?
- What is the expected growth rate?
- Are there usage spikes or patterns?
- What is the acceptable latency for operations?

### Performance Requirements
- What are the response time targets?
- What are the throughput requirements?
- Are there batch processing needs?
- What operations must be real-time vs eventual consistency?
- What are the resource constraints (memory, CPU, storage)?

### Scalability
- How should the system scale (horizontal, vertical)?
- What are the scaling triggers?
- Are there autoscaling requirements?
- What is the expected lifespan of the feature?

## Security & Privacy

### Authentication & Authorization
- Who can access this feature?
- What are the permission levels?
- How are users authenticated?
- What authorization checks are needed?
- Are there role-based access controls?
- What audit logging is required?

### Data Protection
- What data is sensitive or PII?
- What encryption is required (at rest, in transit)?
- Are there data residency requirements?
- What data can be cached and for how long?
- Are there data anonymization needs?
- What are the GDPR/compliance requirements?

### Security Threats
- What are the potential attack vectors?
- What input validation is needed?
- Are there rate limiting requirements?
- What security monitoring is needed?

## Reliability & Operations

### Error Handling
- What can go wrong?
- How should errors be handled?
- What error messages should users see?
- What should be logged for debugging?
- Are there cascading failure scenarios?

### Availability & Durability
- What is the uptime requirement (SLA)?
- What happens during planned maintenance?
- How is data backed up?
- What is the disaster recovery plan?
- Are there geographic redundancy requirements?

### Monitoring & Observability
- What metrics should be tracked?
- What alerts should be configured?
- What debugging information is needed?
- How will success be measured?
- What dashboards are needed?

### Operational Concerns
- How is the feature deployed?
- What is the rollout strategy (gradual, feature flags)?
- How can the feature be rolled back?
- What configuration is needed?
- Are there maintenance procedures?

## Business Logic & Rules

### Business Rules
- What are the business rules and constraints?
- Are there exceptions to the rules?
- How should edge cases be handled?
- What validations are required?
- Are there workflow approvals needed?

### Calculations & Algorithms
- What calculations are performed?
- What formulas or algorithms are used?
- What is the precision/rounding behavior?
- Are there regulatory requirements for calculations?

### Workflows & Processes
- What is the step-by-step process?
- What are the decision points?
- What happens at each step?
- Who is notified and when?
- What are the timeout/expiration rules?

## Dependencies & Constraints

### Technical Dependencies
- What libraries/frameworks are required?
- What external services are needed?
- What infrastructure is required?
- Are there version compatibility requirements?
- What are the licensing constraints?

### Ordering & Timing
- What is the sequence of operations?
- Are there dependencies between steps?
- What is time-sensitive?
- Are there deadlines or timeouts?
- What happens if timing is violated?

### Backwards Compatibility
- What existing functionality is affected?
- How do we handle existing data?
- What migration is needed?
- What is the deprecation strategy?
- Are there API versioning needs?

## User Experience & Behavior

### User Expectations
- What does the user expect to happen?
- What should happen when nothing matches?
- What defaults should be set?
- What options are configurable?
- What help/documentation is needed?

### Edge Cases & Boundaries
- What happens with empty data?
- What happens with maximum data?
- What happens with invalid input?
- What happens with concurrent operations?
- What happens with stale data?

### Localization & Internationalization
- What content needs translation?
- Are there locale-specific formats (dates, numbers)?
- What timezones are involved?
- Are there regional regulations?

## Testing & Validation

### Test Scenarios
- What are the happy path scenarios?
- What are the failure scenarios?
- What edge cases need testing?
- What performance tests are needed?
- What security tests are needed?

### Acceptance Criteria
- How do we know it works correctly?
- What defines "done"?
- What are the success metrics?
- What data validates the feature?
