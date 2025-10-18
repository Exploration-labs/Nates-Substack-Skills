# AI Vendor Evaluation Criteria

Comprehensive framework for systematically evaluating AI vendors across all critical dimensions.

---

## How to Use This Framework

**Scoring system**: Rate each criterion on a 1-5 scale
- **5 = Excellent**: Exceeds expectations, clear competitive advantage
- **4 = Good**: Meets expectations, no concerns
- **3 = Acceptable**: Adequate, minor concerns
- **2 = Concerning**: Significant gaps or risks
- **1 = Unacceptable**: Dis

qualifying issues

**Weighting**: Adjust weights based on your priorities (default weights provided)

**Threshold**: Generally, vendors scoring below 3.5 overall warrant serious concern

---

## 1. Technical Capability (Weight: 25%)

### 1.1 Core Technology Assessment
**What to evaluate**: Underlying AI models, architecture, technical approach

**Questions to ask:**
- What models do you use (proprietary vs third-party)?
- How do you handle model updates and deprecations?
- What's your approach to accuracy and reliability?
- How do you measure and improve model performance?

**Good answers include:**
- Specific model names and versions
- Clear testing and evaluation methodology
- Concrete accuracy metrics with confidence intervals
- Regular model evaluation and improvement process

**Red flags:**
- Vague about technical details
- Claims of "proprietary AI" without substance
- No clear performance metrics
- Overpromising accuracy ("99.9% accurate on all tasks")

**Score 5**: Proprietary models with proven performance, clear testing methodology, transparent about limitations  
**Score 3**: Solid implementation of third-party models, reasonable performance claims  
**Score 1**: Vague technical claims, no performance data, unrealistic promises

---

### 1.2 Integration Complexity
**What to evaluate**: How difficult will implementation be?

**Questions to ask:**
- What's your typical implementation timeline?
- What integrations do you support (APIs, webhooks, etc.)?
- What technical resources are required from our team?
- Can you provide implementation case studies?

**Good answers include:**
- Realistic timeline (measured in weeks/months, not days)
- Standard integration patterns (REST APIs, webhooks)
- Clear documentation and SDKs
- Reference customers with similar technical stacks

**Red flags:**
- "It's plug-and-play" (nothing is)
- Requires proprietary infrastructure
- Vague about integration requirements
- No documentation or examples

**Score 5**: Standard APIs, excellent documentation, proven integrations, realistic timelines  
**Score 3**: Reasonable integration approach, adequate documentation  
**Score 1**: Custom integration required, poor documentation, unrealistic timelines

---

### 1.3 Scalability and Performance
**What to evaluate**: Can this solution handle your growth?

**Questions to ask:**
- What are your current scale limits (requests/sec, data volume)?
- How do you handle traffic spikes?
- What's your typical latency?
- Do you have SLAs for performance?

**Good answers include:**
- Specific capacity numbers
- Auto-scaling capabilities
- Latency guarantees (p50, p95, p99)
- Formal SLAs with penalties

**Red flags:**
- Vague about capacity
- No SLAs or guarantees
- Unclear about handling scale
- "We've never hit limits" (not credible)

**Score 5**: Proven at scale, clear SLAs, excellent performance metrics  
**Score 3**: Adequate for current needs, reasonable performance  
**Score 1**: Unclear about scale, no SLAs, performance concerns

---

### 1.4 Security and Compliance
**What to evaluate**: Data protection, regulatory compliance, security practices

**Questions to ask:**
- What certifications do you have (SOC 2, ISO 27001, etc.)?
- How is customer data handled and protected?
- Do you support data residency requirements?
- What's your security incident history?

**Good answers include:**
- Current security certifications
- Clear data handling practices
- Compliance with relevant regulations (GDPR, CCPA, HIPAA if applicable)
- Transparent security practices

**Red flags:**
- No security certifications
- Vague about data handling
- "We've never been hacked" (everyone's been tested)
- Unwilling to discuss security

**Score 5**: Multiple certifications, excellent security practices, transparent  
**Score 3**: Basic security measures, working toward certifications  
**Score 1**: No certifications, unclear security practices

---

## 2. Business Viability (Weight: 20%)

### 2.1 Company Stability
**What to evaluate**: Will this vendor exist in 2-3 years?

**Questions to ask:**
- How long have you been in business?
- What's your funding situation?
- How many customers do you have?
- What's your revenue trajectory?

**Good indicators:**
- 2+ years in business
- Profitable or recently raised funding
- 20+ paying customers
- Growing revenue

**Red flags:**
- Brand new company (<1 year)
- Burning cash with no clear path to profitability
- Few customers or declining revenue
- Heavy dependence on single customer

**Score 5**: Profitable, growing revenue, strong customer base  
**Score 3**: Funded, reasonable burn rate, growing customer base  
**Score 1**: Financial concerns, very early stage, unstable

---

### 2.2 Customer Base and References
**What to evaluate**: Track record with similar customers

**Questions to ask:**
- Who are your reference customers?
- Can I speak with customers in similar industries?
- What's your customer retention rate?
- How many customers have similar use cases to ours?

**Good answers include:**
- Multiple verifiable reference customers
- High retention rate (>90%)
- Customers willing to speak with you
- Similar use cases to yours

**Red flags:**
- Can't provide references
- All references are pilots, no production deployments
- High churn rate
- No customers similar to your use case

**Score 5**: Excellent references, high retention, proven in your domain  
**Score 3**: Some references, reasonable retention  
**Score 1**: No verifiable references, high churn, no domain experience

---

### 2.3 Product Roadmap
**What to evaluate**: Alignment of vendor's direction with your needs

**Questions to ask:**
- What's on your product roadmap for next 12 months?
- How do you prioritize features?
- What's your release cadence?
- Do you have a customer advisory board?

**Good answers include:**
- Clear roadmap aligned with your needs
- Regular releases (monthly/quarterly)
- Customer-driven prioritization
- Transparent about priorities

**Red flags:**
- Vague roadmap or "everything is on the roadmap"
- Roadmap doesn't align with your needs
- Infrequent releases
- Sales-driven feature promises

**Score 5**: Clear roadmap, aligned with your needs, customer-driven  
**Score 3**: Reasonable roadmap, some alignment  
**Score 1**: Vague or misaligned roadmap

---

## 3. Pricing and Value (Weight: 20%)

### 3.1 Pricing Model Fairness
**What to evaluate**: Is the pricing structure reasonable and transparent?

**Questions to ask:**
- What's included in base pricing?
- What are additional costs (implementation, support, overage)?
- How do prices scale with usage?
- Are there volume discounts?

**Good pricing characteristics:**
- Transparent pricing structure
- Predictable costs
- Reasonable scaling
- Aligned with value delivered

**Red flags:**
- Hidden fees or surprise charges
- Complex pricing that's hard to predict
- High implementation fees
- Expensive overages

**Score 5**: Transparent, fair, predictable, aligned with value  
**Score 3**: Reasonable pricing with some complexity  
**Score 1**: Opaque pricing, high fees, poor value

See [pricing-models.md](pricing-models.md) for detailed pricing analysis.

---

### 3.2 Total Cost of Ownership
**What to evaluate**: Full 3-year cost including hidden costs

**Components to consider:**
- Software license/subscription fees
- Implementation costs
- Training and change management
- Ongoing maintenance and support
- Integration development and maintenance
- Internal resource costs

**Analysis approach:**
1. Calculate direct costs (licenses, fees)
2. Add implementation costs (professional services, internal time)
3. Add ongoing costs (support, maintenance, updates)
4. Compare to alternative solutions (including build in-house)

**Score 5**: TCO significantly lower than alternatives, clear value  
**Score 3**: TCO competitive with alternatives  
**Score 1**: TCO significantly higher than alternatives

See [build-vs-buy.md](build-vs-buy.md) for TCO analysis framework.

---

### 3.3 Value Delivered
**What to evaluate**: Does the solution deliver sufficient ROI?

**Questions to ask:**
- What measurable outcomes can we expect?
- What's the typical payback period?
- Can you provide ROI case studies?
- How do you measure success?

**Good answers include:**
- Specific, measurable outcomes
- Realistic payback periods (12-24 months typical)
- Verifiable case studies
- Clear success metrics

**Red flags:**
- Vague about outcomes
- Unrealistic ROI claims
- No case studies or metrics
- Can't define success

**Score 5**: Clear, measurable ROI with case studies, realistic payback  
**Score 3**: Reasonable value proposition, some evidence  
**Score 1**: Unclear value, no supporting evidence

---

## 4. Implementation Risk (Weight: 20%)

### 4.1 Implementation Complexity
**What to evaluate**: How difficult will deployment be?

**Factors to assess:**
- Technical integration complexity
- Data preparation required
- Change management needs
- Training requirements

**Questions to ask:**
- What's your average time to first value?
- What percentage of implementations succeed?
- What are common implementation challenges?
- What support do you provide during implementation?

**Good answers include:**
- Time to value measured in weeks, not months
- High success rate (>80%)
- Honest about challenges
- Dedicated implementation support

**Red flags:**
- Very long implementation timelines
- High failure rate or vague about success
- Downplaying implementation difficulty
- Limited implementation support

**Score 5**: Straightforward implementation, high success rate, excellent support  
**Score 3**: Manageable complexity, reasonable support  
**Score 1**: High complexity, low success rate, poor support

---

### 4.2 Vendor Support Quality
**What to evaluate**: Will you get help when you need it?

**Questions to ask:**
- What support tiers do you offer?
- What's your average response time for critical issues?
- Do you have a dedicated customer success team?
- What's your support availability (24/7, business hours)?

**Good answers include:**
- Tiered support with SLAs
- Fast response for critical issues (<1 hour)
- Dedicated support team
- Support hours matching your needs

**Red flags:**
- Email-only support
- Slow response times
- No dedicated support
- Support costs extra

**Score 5**: Excellent support with fast response, dedicated team, strong SLAs  
**Score 3**: Adequate support, reasonable response times  
**Score 1**: Poor support, slow response, no SLAs

---

### 4.3 Change Management Requirements
**What to evaluate**: How much organizational change is required?

**Factors to consider:**
- Process changes required
- User adoption challenges
- Stakeholder management needs
- Training requirements

**Assessment:**
- Low risk: Minimal process change, easy adoption
- Medium risk: Some process change, moderate training needed
- High risk: Significant process redesign, extensive training required

**Score 5**: Minimal change required, easy adoption  
**Score 3**: Moderate change, manageable with planning  
**Score 1**: Massive change, high adoption risk

---

## 5. Contract Terms (Weight: 15%)

### 5.1 Contract Flexibility
**What to evaluate**: How locked in will you be?

**Key terms to assess:**
- Contract length and renewal terms
- Termination clauses and notice periods
- Data portability and export
- Pricing escalation protections

**Good terms:**
- Annual contracts with option to renew
- Reasonable termination clauses (90 days notice)
- Full data export capabilities
- Price protection or caps

**Red flags:**
- Multi-year lock-in with penalties
- Difficult or expensive to exit
- No data portability
- Unlimited price increases

**Score 5**: Flexible terms, easy exit, strong protections  
**Score 3**: Reasonable terms with some lock-in  
**Score 1**: Heavy lock-in, difficult exit, poor protections

See [contract-checklist.md](contract-checklist.md) for detailed contract guidance.

---

### 5.2 Performance Guarantees
**What to evaluate**: Are vendors accountable for performance?

**Key elements:**
- Uptime SLAs (99.9% typical for production systems)
- Performance guarantees (latency, throughput)
- Accuracy or quality metrics
- Remedies for SLA breaches

**Good guarantees:**
- Clear, measurable SLAs
- Financial penalties for breaches
- Transparent reporting on SLA compliance

**Red flags:**
- No SLAs or vague guarantees
- No remedies for breaches
- "Best effort" language

**Score 5**: Strong SLAs with financial penalties, transparent reporting  
**Score 3**: Basic SLAs, some accountability  
**Score 1**: No SLAs or weak guarantees

---

### 5.3 Data Rights and IP Protection
**What to evaluate**: Who owns what?

**Key questions:**
- Who owns the data we input?
- Can you use our data to train models?
- Who owns the outputs/results?
- What happens to our data if we terminate?

**Good terms:**
- Customer owns all input data
- Vendor cannot use customer data without permission
- Customer owns or has full rights to outputs
- Data deletion upon termination

**Red flags:**
- Vendor claims rights to customer data
- Vendor can use data to train models
- Unclear ownership of outputs
- Data retained indefinitely

**Score 5**: Customer owns all data and outputs, clear deletion terms  
**Score 3**: Reasonable data terms with some usage rights  
**Score 1**: Vendor retains significant data rights

---

## Evaluation Score Calculation

### Overall Score Formula
```
Overall Score = (Technical × 0.25) + (Business × 0.20) + (Pricing × 0.20) + 
                (Implementation × 0.20) + (Contract × 0.15)
```

### Interpretation
- **4.5-5.0**: Excellent vendor, strong recommendation
- **4.0-4.4**: Good vendor, proceed with confidence
- **3.5-3.9**: Acceptable vendor, manageable risks
- **3.0-3.4**: Concerning, significant risks to address
- **<3.0**: Not recommended, too many red flags

### Decision Matrix

| Overall Score | Individual Category Score <2 | Recommendation |
|---------------|------------------------------|----------------|
| ≥4.0 | No | Proceed |
| ≥4.0 | Yes | Proceed with mitigation plan for weak area |
| 3.5-3.9 | No | Proceed cautiously, detailed risk assessment |
| 3.5-3.9 | Yes | Do not proceed without significant improvements |
| <3.5 | Any | Do not proceed |

---

## Customizing Weights for Your Situation

**Adjust weights based on priorities:**

**Early-stage company / High risk tolerance:**
- Increase Technical (30%), decrease Business (15%)
- Willing to bet on unproven vendors for technical advantage

**Enterprise / Risk-averse:**
- Increase Business (25%), Contract (20%)
- Prioritize stability and favorable terms

**Pilot project / Low commitment:**
- Increase Technical (30%), decrease Contract (10%)
- Can afford to try and switch vendors

**Mission-critical system:**
- Increase Implementation (25%), Business (25%)
- Cannot afford deployment failure or vendor going away

---

## Special Considerations

### For AI-Native Companies
Additional questions to ask:
- What's your approach to model drift?
- How do you handle adversarial inputs?
- What's your process for continuous improvement?
- How do you measure model fairness and bias?

### For Regulated Industries
Additional factors to assess:
- Specific compliance certifications (HIPAA, PCI-DSS, etc.)
- Audit trail capabilities
- Data sovereignty options
- Regulatory reporting features

### For High-Volume Use Cases
Additional focus areas:
- Per-unit economics at scale
- Batch processing capabilities
- Caching and optimization options
- Volume discount structures

---

## Using This Framework

**Step 1**: Review evaluation criteria and adjust weights for your situation  
**Step 2**: Conduct vendor interviews and demos focused on evaluation criteria  
**Step 3**: Score each vendor using the scorecard template  
**Step 4**: Review scores and identify any disqualifying issues (any category <2)  
**Step 5**: Compare vendor scores and make selection based on overall fit

**Remember**: Scores are a framework for structured decision-making, not a replacement for judgment. Use scores to identify risks and inform discussion, not as the sole decision factor.