# AI Vendor Pricing Models

Guide to common AI vendor pricing structures, fair market rates, and how to evaluate pricing proposals.

---

## Common Pricing Models

### 1. Per-Seat / Per-User
**Structure**: Fixed monthly/annual fee per user

**Typical costs**: $50-500/user/month depending on features

**Advantages**:
- Predictable costs
- Easy to budget
- Scales with team size

**Disadvantages**:
- Doesn't reflect actual usage
- Can get expensive as team grows
- May pay for inactive users

**When it makes sense**: Tools used regularly by defined user set (e.g., content creation, analysis tools)

**Red flags**:
- Charging per-seat for API/backend services
- Must purchase minimum seats far exceeding needs
- No flexibility for occasional users

---

### 2. Usage-Based (API Calls, Tokens, Transactions)
**Structure**: Pay per API call, token processed, or transaction

**Typical costs**: Varies widely by use case
- Text processing: $0.001-0.10 per 1K tokens
- Image generation: $0.01-0.50 per image
- Predictions/classifications: $0.0001-0.01 per call

**Advantages**:
- Pay only for what you use
- Can start small and scale
- Aligned with value

**Disadvantages**:
- Unpredictable costs
- Can spike with increased usage
- Requires monitoring

**When it makes sense**: Variable usage patterns, APIs, batch processing

**Red flags**:
- No usage caps or alerts
- Charges 10x+ underlying API costs (for simple wrappers)
- Expensive overage rates
- Complex pricing tiers hard to predict

---

### 3. Platform / Base + Usage
**Structure**: Base platform fee + usage charges

**Typical costs**: $5K-50K/month base + usage fees

**Advantages**:
- Covers infrastructure costs
- Some predictability with base fee
- Can align usage with value

**Disadvantages**:
- High minimum commitment
- Dual pricing complexity
- Base fee may not cover reasonable usage

**When it makes sense**: Enterprise deployments with significant usage

**Red flags**:
- Base fee doesn't include any meaningful usage
- Both base and usage fees are high
- Unclear what base fee covers

---

### 4. Value-Based / Outcome-Based
**Structure**: Pricing tied to business outcomes

**Examples**:
- % of revenue enabled
- % of costs saved
- Per successful transaction/conversion

**Advantages**:
- Aligned with actual value
- Vendor shares risk
- Can justify high prices if ROI clear

**Disadvantages**:
- Complex to measure
- Requires data sharing
- May be expensive at scale

**When it makes sense**: Clear, measurable business outcomes

**Red flags**:
- Measurement methodology unclear
- Vendor controls measurement
- % fees grow without bounds

---

### 5. Professional Services Heavy
**Structure**: Software license + mandatory implementation/support

**Typical breakdown**: 30-50% software, 50-70% services

**Advantages**:
- Vendor-supported implementation
- Reduced internal resources needed

**Disadvantages**:
- High total cost
- Vendor lock-in for changes
- Recurring service fees

**When it makes sense**: Complex deployments requiring expertise

**Red flags**:
- Services cost more than software
- Mandatory ongoing services
- Can't self-implement/maintain

---

## Fair Market Rates (2025)

### Text/Language AI
- GPT-4 class models: $0.01-0.03 per 1K tokens
- Simple wrappers markup: 2-5x underlying cost acceptable
- Complex platforms: 5-10x markup for significant value-add
- Enterprise platforms: $10K-100K/month for substantial deployments

### Computer Vision
- Image classification: $0.001-0.01 per image
- Object detection: $0.01-0.05 per image
- Custom models: $25K-250K implementation + usage fees

### Speech/Audio
- Speech-to-text: $0.006-0.024 per minute
- Text-to-speech: $0.016-0.060 per 1M characters
- Custom voice models: $50K-500K + usage

### Predictive Analytics
- Simple models: $5K-50K/year for modest usage
- Complex ML platforms: $50K-500K/year enterprise licenses

---

## Total Cost of Ownership Calculation

### Direct Costs (Year 1)
1. Software licenses/subscriptions
2. Implementation fees
3. Training costs
4. Integration development
5. Data preparation

### Ongoing Costs (Year 2-3)
1. Annual license renewals
2. Usage/transaction fees
3. Maintenance and support
4. Updates and upgrades
5. Internal admin time

### Hidden Costs
1. Tool switching costs if it fails
2. Opportunity cost of delays
3. Security/compliance overhead
4. Performance optimization
5. Troubleshooting and debugging

**3-Year TCO Formula**:
```
TCO = (Y1 Direct Costs) + 
      (Y2 Ongoing Costs × 0.9) +  // Often decrease slightly
      (Y3 Ongoing Costs × 0.85) + // As usage optimizes
      (Hidden Costs × 3)           // Spread over 3 years
```

---

## Negotiation Strategies

### Before Negotiation
1. Understand your usage patterns
2. Know fair market rates
3. Get competing quotes
4. Identify your leverage points

### Key Negotiation Points

**Volume Discounts**:
- Request tiered pricing
- Negotiate breakpoints
- Get commitment to future discounts

**Caps and Protections**:
- Annual spending caps
- Price increase limits (5-10% max)
- Usage buffer before overages
- Commitment discounts

**Terms Improvements**:
- Shorter contract length
- Better termination clauses
- More flexible scaling
- Performance guarantees

**Value-Adds**:
- Included implementation
- Extended support hours
- Additional users/usage
- Training and enablement

### Leverage Points

**You have leverage when**:
- Multiple vendors compete
- You have alternatives (including build)
- Large contract size
- Quick decision timeline (if vendor is motivated)
- End of vendor's quarter/year

**Vendor has leverage when**:
- Unique capability
- You're deeply integrated
- Switching costs are high
- They're not desperate for the business

---

## Pricing Red Flags

### 🔴 Disqualifying
- Won't provide pricing until late in process
- Pricing requires NDA (hiding from competitors)
- Charges 20x+ underlying costs with minimal value-add
- No willingness to negotiate anything

### 🚩 Serious Concerns
- Complex pricing impossible to predict
- Hidden fees not disclosed upfront
- Expensive mandatory services
- Unlimited price escalations

### ⚠️ Noteworthy
- Higher than alternatives but justifiable
- Usage-based without caps
- Multi-year lock-in for discount

---

## Build vs Buy Cost Comparison

**Internal Build Estimate**:
```
Engineering cost: $150K-300K per engineer-year
2-3 engineers for 6-12 months = $150K-900K initial build
Ongoing maintenance: 1-2 engineers = $150K-600K/year
Infrastructure: $10K-100K/year
```

**When to build**:
- Vendor pricing exceeds build cost over 3 years
- Core strategic capability
- Have available engineering talent
- Requirements are unique

**When to buy**:
- Vendor cost significantly less than build
- Commodity capability
- Speed to market critical
- Limited engineering resources

---

## Questions to Ask About Pricing

1. **What's included in base price?**
2. **What costs extra?**
3. **What's a typical first-year total cost for a company our size?**
4. **How does pricing scale with usage?**
5. **Are there caps or overages?**
6. **What are implementation costs?**
7. **What's required for support?**
8. **How often do prices increase?**
9. **Can you provide customer references on pricing?**
10. **What happens if we exceed usage limits?**

---

## Case Study: Pricing Evaluation

**Vendor A**: $50K base + $0.01/transaction
- Expected usage: 2M transactions/year
- Year 1: $50K + $20K = $70K
- Year 2-3: Likely similar
- 3-year TCO: ~$210K

**Vendor B**: $100/user/month for 50 users
- Year 1: $60K
- Years 2-3: $60K each (likely grows with team)
- 3-year TCO: ~$180K-240K as team grows

**Build In-House**: 
- Year 1: $250K (2 engineers × 6 months + infrastructure)
- Years 2-3: $150K/year maintenance
- 3-year TCO: ~$550K

**Decision**: Vendor B likely best value for this scenario (lowest TCO, predictable, vendor-supported)

---

## Summary

**For straightforward assessment**:
1. Get all-in pricing including implementation
2. Calculate 3-year TCO
3. Compare to alternatives
4. Assess value delivered
5. Negotiate improvements

**Remember**: Cheapest option isn't always best. Consider total value, risk, and TCO over 3 years.