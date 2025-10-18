# Risk Assessment Framework

This reference provides a framework for identifying and categorizing technical risks when requirements are underspecified.

## Risk Categories

### Implementation Risk
Risks that impact the ability to build the feature correctly.

**High Risk Indicators:**
- Multiple valid interpretations of core functionality
- Unclear success criteria or acceptance criteria
- Missing business rules or edge case handling
- Ambiguous data model or entity relationships
- Undefined integration points with existing systems

**Assessment Questions:**
- Can engineers start implementation with current details?
- Are there multiple ways to interpret key requirements?
- What assumptions must be made to proceed?

**Example:**
"Document states 'users can share documents' but doesn't specify: sharing mechanism (link, email, in-app), permissions model, or what 'shared' means (view, edit, comment)."

### Performance Risk
Risks related to system performance, scale, and resource usage.

**High Risk Indicators:**
- No specified volume, load, or performance targets
- Potentially expensive operations (large data processing, complex queries)
- Real-time or latency-sensitive features without SLAs
- Missing caching or optimization strategy
- Unbounded data growth

**Assessment Questions:**
- What is the expected scale (users, data, requests)?
- Are there operations that could become bottlenecks?
- What performance is acceptable?

**Example:**
"Feature allows 'searching all historical transactions' but doesn't specify: expected transaction count per user, acceptable search latency, or result pagination."

### Security Risk
Risks related to data protection, access control, and vulnerabilities.

**High Risk Indicators:**
- Handling sensitive data (PII, financial, health) without protection requirements
- Missing authentication or authorization details
- User-generated content without validation/sanitization
- External integrations without security specifications
- Ambiguous data access controls

**Assessment Questions:**
- What data is sensitive and how should it be protected?
- Who can access what and when?
- What are the potential attack vectors?

**Example:**
"Users can upload files but no specification of: allowed file types, size limits, virus scanning, access controls, or where files are stored."

### Data Integrity Risk
Risks related to data consistency, accuracy, and reliability.

**High Risk Indicators:**
- Multiple systems updating the same data
- Missing conflict resolution strategy
- Unclear data lifecycle (creation, updates, deletion)
- No validation rules specified
- Eventual consistency without defined "eventual"
- Missing rollback or undo capabilities

**Assessment Questions:**
- How is data consistency maintained?
- What happens during concurrent updates?
- What validation prevents bad data?

**Example:**
"Inventory is updated from both POS and warehouse systems but no specification of: which system is source of truth, how conflicts are resolved, or update timing."

### Integration Risk
Risks related to dependencies on external systems or services.

**High Risk Indicators:**
- Dependencies on external APIs without failure handling
- Real-time dependencies on unreliable services
- Missing timeout or retry specifications
- Unclear data synchronization requirements
- No fallback strategy for service outages

**Assessment Questions:**
- What happens when external systems fail?
- How fresh must data be from external sources?
- What are the reliability expectations?

**Example:**
"Display real-time shipping rates from carrier APIs but no specification of: timeout handling, what to show during carrier outages, or caching strategy."

### Operational Risk
Risks related to deployment, monitoring, and maintenance.

**High Risk Indicators:**
- Complex data migration without strategy
- No rollback plan for problematic deployments
- Missing monitoring or alerting requirements
- Unclear deployment strategy (gradual, feature flags)
- Configuration needs not specified

**Assessment Questions:**
- How is this deployed and rolled back if needed?
- What visibility is needed into system health?
- What happens to existing data?

**Example:**
"Change user authentication system but no specification of: migration plan for existing users, rollback strategy, or how to handle users mid-session during deployment."

### User Experience Risk
Risks that impact user trust, satisfaction, or adoption.

**High Risk Indicators:**
- Missing error messages or error state UX
- No loading state specifications for slow operations
- Unclear feedback for user actions
- Missing accessibility considerations
- Ambiguous user expectations

**Assessment Questions:**
- What does the user see during errors, loading, empty states?
- How does the user know their action succeeded?
- What happens in unexpected scenarios?

**Example:**
"Submit form to external service but no specification of: loading indicator, success/error messaging, what happens if service is slow, or how user can retry."

### Compliance Risk
Risks related to regulatory, legal, or policy requirements.

**High Risk Indicators:**
- PII or sensitive data without retention policies
- International users without localization/regulatory consideration
- Financial transactions without audit trail
- User data without consent management
- Missing data residency requirements

**Assessment Questions:**
- What regulations apply (GDPR, HIPAA, PCI, etc.)?
- What audit or compliance reporting is needed?
- Are there data residency requirements?

**Example:**
"Store user health data but no specification of: HIPAA compliance requirements, data encryption, access logging, or retention policies."

## Risk Severity Levels

### Critical
**Impact:** Blocks implementation or risks significant production issues
**Characteristics:**
- Core functionality cannot be implemented without clarification
- Severe security or data integrity exposure
- Regulatory compliance violations likely
- Production-breaking failure scenarios unaddressed

**Action Required:** Must be resolved before implementation begins

### High  
**Impact:** Requires significant assumptions or introduces substantial technical debt
**Characteristics:**
- Multiple valid implementation paths with very different outcomes
- Moderate security or performance concerns
- Substantial rework likely needed after clarification
- Complex error scenarios undefined

**Action Required:** Should be resolved before starting implementation

### Medium
**Impact:** Creates uncertainty that may cause rework
**Characteristics:**
- Some implementation details can be reasonably assumed
- Edge cases undefined but unlikely to cause major issues
- Performance implications unclear but manageable
- Non-critical integration details missing

**Action Required:** Should be clarified during implementation

### Low
**Impact:** Minor uncertainty that can be resolved during implementation
**Characteristics:**
- Details can be reasonably inferred from context
- Standard patterns apply
- Edge cases are truly edge cases
- Can be iterated on after initial implementation

**Action Required:** Note for discussion but doesn't block progress

## Risk Assessment Template

```markdown
## Risk Assessment

### Critical Risks
1. **[Risk Name]**
   - Category: [Implementation/Security/Data/etc.]
   - Issue: [What is undefined or ambiguous]
   - Impact: [What could go wrong]
   - Questions: [What needs clarification]

### High Risks
[Same structure]

### Medium Risks
[Same structure]

### Low Risks
[Optional - only if worth noting]

## Recommended Actions
- [Prioritized list of what should be clarified before proceeding]
```

## Risk Identification Process

1. **Review each requirement** against the technical dimensions checklist
2. **Identify gaps** where critical details are missing
3. **Assess potential impact** of each gap
4. **Categorize risk** based on type and severity
5. **Formulate clarifying questions** to address each risk

## Common Risk Patterns

### Pattern: "Users can..."
**Risk:** Ambiguous access control
**Questions:** Who specifically? Under what conditions? What happens if unauthorized?

### Pattern: "System will process..."
**Risk:** Missing failure handling
**Questions:** What constitutes successful processing? What errors can occur? How are failures handled?

### Pattern: "Display data from..."
**Risk:** Missing data freshness and error states
**Questions:** How fresh must data be? What shows during loading? What if data unavailable?

### Pattern: "Integrate with..."
**Risk:** Undefined integration contract
**Questions:** What is the integration protocol? How are failures handled? What data is exchanged?

### Pattern: "Store/Save..."
**Risk:** Unclear data lifecycle and validation
**Questions:** What validation occurs? How long is data retained? Who can access stored data?

### Pattern: "Real-time..." or "Immediate..."
**Risk:** Undefined performance requirements
**Questions:** What exactly does real-time mean? What latency is acceptable? What happens if delayed?

## Communicating Risks

When presenting risks to stakeholders:

1. **Be specific:** Reference exact requirements and gaps
2. **Explain impact:** Describe real scenarios where issues could occur
3. **Avoid FUD:** Focus on genuine technical concerns, not hypotheticals
4. **Offer options:** When possible, suggest multiple approaches with tradeoffs
5. **Prioritize:** Help stakeholders understand what's critical vs nice-to-have

**Example:**
"The document mentions 'real-time notifications' (3 times) but doesn't specify:
- Acceptable notification delay (100ms? 1s? 5s?)
- What happens if delivery fails
- Expected notification volume

This is a HIGH RISK because we could build an expensive real-time system when a 5-second delay would be acceptable, or vice versa - build a queued system when instant delivery is required."
