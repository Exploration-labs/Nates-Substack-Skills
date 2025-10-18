# AI Vendor Contract Checklist

Essential terms for AI vendor agreements and negotiation guidance.

---

## Critical Contract Terms

### 1. Data Ownership and Rights

**Must have**:
- ✅ Customer owns all input data
- ✅ Customer owns all outputs/results  
- ✅ Vendor cannot use customer data without explicit permission
- ✅ Data deleted within 30 days of termination

**Negotiate**:
- Vendor rights to anonymized, aggregated data
- Model training on customer data (should be opt-in only)

**Red flags**:
- Vendor claims ownership of customer data
- Vendor can use data without restriction
- Data retained indefinitely
- Unclear ownership terms

---

### 2. Performance Guarantees (SLAs)

**Must have**:
- ✅ Uptime SLA (99.9% for production systems)
- ✅ Performance metrics (latency, throughput)
- ✅ Financial penalties for SLA breaches
- ✅ Transparent SLA reporting

**Typical SLAs**:
- Uptime: 99.9% (8.76 hours downtime/year)
- Response time: <1 second p95
- Support response: <1 hour for critical issues

**Penalties for breach**:
- 5-10% monthly fee credit per percentage point below SLA
- Right to terminate if sustained breaches

**Red flags**:
- No SLAs or "best effort" only
- No remedies for breaches
- Vague metrics

---

### 3. Termination and Exit

**Must have**:
- ✅ Can terminate with 90-180 days notice
- ✅ No penalty for termination (or reasonable penalty)
- ✅ Full data export in standard format
- ✅ Continued access during transition period

**Negotiate**:
- Termination for convenience
- Termination for cause (vendor breach)
- Reduced notice period
- Transition assistance

**Red flags**:
- Multi-year lock-in with large penalties
- Difficult or expensive data export
- No termination for cause option
- Vendor can hold data hostage

---

### 4. Pricing and Payment Terms

**Must have**:
- ✅ Clear pricing structure
- ✅ Annual price increase caps (5-10% max)
- ✅ Reasonable payment terms (Net 30)
- ✅ No surprise fees

**Negotiate**:
- Volume discounts
- Multi-year discount
- Usage caps or buffers
- Payment terms (Net 45/60)

**Red flags**:
- Unlimited price increases
- Hidden fees
- Prepayment required
- Short payment terms

---

### 5. Intellectual Property

**Must have**:
- ✅ Customer retains all IP in their data
- ✅ Vendor retains IP in their platform
- ✅ Clear ownership of deliverables
- ✅ Customer can use outputs freely

**Watch for**:
- Vendor claims rights to customer IP
- Restrictions on output usage
- Requirements to credit vendor

---

### 6. Security and Compliance

**Must have**:
- ✅ Security certifications (SOC 2, ISO 27001)
- ✅ Compliance with relevant regulations
- ✅ Data encryption at rest and in transit
- ✅ Breach notification requirements (24-48 hours)

**Negotiate**:
- Specific compliance certifications needed
- Data residency requirements
- Audit rights
- Security assessments

---

### 7. Liability and Indemnification

**Must have**:
- ✅ Vendor liable for breaches
- ✅ Indemnification for IP claims
- ✅ Reasonable liability caps
- ✅ No broad customer indemnification

**Typical caps**:
- Liability: 12 months of fees paid
- Exceptions: Breaches, IP infringement, gross negligence

**Red flags**:
- No liability or very low caps
- Customer indemnifies vendor broadly
- Vendor not liable for anything

---

### 8. Support and Maintenance

**Must have**:
- ✅ Defined support hours
- ✅ Response time commitments
- ✅ Regular updates included
- ✅ Dedicated support contact

**Typical support**:
- Business hours: 9am-5pm local time
- Critical issues: <1 hour response
- Standard issues: <24 hour response

**Negotiate**:
- 24/7 support if needed
- Faster response times
- Dedicated success manager
- Training included

---

## Negotiation Guide

### Before Negotiation

**Prepare**:
1. Understand your priorities
2. Know your walk-away points
3. Get competing proposals
4. Identify leverage points

**Prioritize your asks**:
- Must-haves (deal breakers)
- Important (will fight for)
- Nice-to-haves (will accept trade-offs)

---

### Negotiation Tactics

**For better pricing**:
- Request multi-year discount
- Commit to higher volume
- Pay annually vs monthly
- Reduce included features

**For better terms**:
- Shorter contract length
- Better termination clause
- Stronger SLAs with penalties
- Data ownership clarity

**What to trade**:
- Longer commitment for discount
- Reference/case study for concessions
- Public announcement for better terms
- Higher volume for better rates

**When you have leverage**:
- Multiple vendors competing
- Large contract size
- End of vendor's quarter/year
- You can build in-house

---

### Red Lines (Non-Negotiable)

**Never accept**:
1. Vendor owns your data
2. No ability to terminate
3. Unlimited price increases
4. No SLAs or accountability

**Push back hard on**:
1. Multi-year lock-in
2. Vague performance terms
3. Broad indemnification
4. Limited liability

---

## Contract Review Checklist

### Before Signing

**Data Terms** (Review pages: ___)
- [ ] Customer owns input data
- [ ] Customer owns outputs
- [ ] No vendor rights to use data
- [ ] Data deletion upon termination

**SLAs** (Review pages: ___)
- [ ] Uptime guarantees defined
- [ ] Performance metrics specified
- [ ] Financial penalties for breaches
- [ ] Reporting and measurement clear

**Termination** (Review pages: ___)
- [ ] Reasonable termination clause
- [ ] Data export guaranteed
- [ ] No excessive penalties
- [ ] Transition support included

**Pricing** (Review pages: ___)
- [ ] All costs disclosed
- [ ] Price increase caps
- [ ] Usage limits clear
- [ ] No hidden fees

**Liability** (Review pages: ___)
- [ ] Vendor liability defined
- [ ] Reasonable caps
- [ ] Indemnification mutual
- [ ] Breach consequences clear

**Security** (Review pages: ___)
- [ ] Certifications listed
- [ ] Compliance requirements met
- [ ] Breach notification terms
- [ ] Audit rights included

---

## Special Situations

### For Startups
**Additional protections needed**:
- Flexible scaling (up or down)
- Shorter contracts (annual vs multi-year)
- Lower minimum commitments
- Freedom to change use cases

### For Enterprises
**Additional requirements**:
- Stronger SLAs
- 24/7 support
- Security audits
- Compliance certifications
- Dedicated resources

### For Regulated Industries
**Must include**:
- Specific compliance certifications
- Data residency guarantees
- Audit trail capabilities
- Breach notification procedures
- Business Associate Agreement (if HIPAA)

---

## Common Vendor Pushback (and Responses)

**Vendor**: "Our standard contract doesn't allow changes"
**Response**: "We need these changes for legal/risk reasons. What's your approval process?"

**Vendor**: "We can't provide those SLAs"
**Response**: "What SLAs can you commit to? How do you handle breaches?"

**Vendor**: "Pricing is firm"
**Response**: "We have competing proposals at lower prices. Can you match?"

**Vendor**: "We need data rights for model improvement"
**Response**: "We'll consider opt-in anonymized data sharing. Not blanket rights."

**Vendor**: "Multi-year required for this price"
**Response**: "Annual contract at 10% higher price works, or multi-year with opt-out after year 1."

---

## Final Review Questions

Before signing, ask yourself:

1. Can we exit this contract reasonably if needed?
2. Do we own our data completely?
3. Is the vendor accountable for performance?
4. Are costs predictable and capped?
5. Are our key risks addressed?
6. Have we negotiated fairly?
7. Can legal and procurement approve?
8. Are we comfortable with vendor's liability limits?

**If any answer is "no", renegotiate or walk away.**

---

## Summary

**Essential terms**:
1. Data ownership (customer)
2. SLAs with penalties
3. Reasonable termination
4. Price protections
5. Liability and indemnification

**Remember**: Everything in a contract is negotiable. Vendors have "standard contracts" but will modify for the right deal. Don't accept unfavorable terms without trying to negotiate.