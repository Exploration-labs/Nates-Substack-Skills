# Use Case Fit Assessment

Framework for determining whether a vendor solution actually fits your specific use case.

---

## Assessment Framework

### 1. Define Your Use Case Clearly

**Core questions**:
- What problem are you solving?
- Who are the users?
- What's the success criteria?
- What are the constraints?
- What volume/scale is required?

**Be specific**: "Classify customer support tickets" not "AI for customer service"

---

### 2. Vendor Capability Match

**Assess**:
- Has vendor solved this exact problem before?
- Do they have customers with similar use cases?
- What's their track record in your domain?
- Can they provide relevant case studies?

**Scoring**:
- ✅ **Exact match**: Multiple customers, proven results
- ⚠️ **Close match**: Similar use cases, some adaptation needed
- ❌ **Poor match**: Different domain, unproven for your needs

---

### 3. Domain Expertise

**Questions for vendor**:
- How many customers in [your industry]?
- What industry-specific challenges have you solved?
- Do you understand [domain-specific terminology]?
- What domain expertise is on your team?

**Red flags**:
- No customers in your industry
- Generic solution claiming to work everywhere
- Doesn't understand domain nuances
- No domain experts on team

---

### 4. Data Requirements

**Assess compatibility**:
- What data do they need?
- Do you have that data available?
- What format/quality is required?
- How much data is needed?

**Common mismatches**:
- Vendor needs structured data, you have unstructured
- Requires large training set, you have small dataset
- Needs labeled data, you have unlabeled
- Different data format than you provide

---

### 5. Integration Requirements

**Evaluate**:
- Do they integrate with your existing systems?
- What APIs/webhooks do they support?
- Can they work with your tech stack?
- What's the integration complexity?

**Warning signs**:
- Requires replacing existing systems
- No integration with your tools
- Complex custom integration needed
- Incompatible tech stack

---

### 6. Scale and Performance

**Match your needs**:
- Can they handle your volume?
- What's their latency?
- How do they handle spikes?
- Can they grow with you?

**Mismatches to avoid**:
- Your volume exceeds their capacity
- Latency too slow for your use case
- Can't handle your traffic patterns
- Won't scale to future needs

---

## Fit Assessment Scorecard

| Dimension | Score (1-5) | Weight | Weighted |
|-----------|-------------|--------|----------|
| Use case match | | 30% | |
| Domain expertise | | 20% | |
| Data compatibility | | 20% | |
| Integration fit | | 15% | |
| Scale/performance | | 15% | |
| **Total** | | 100% | |

**Interpretation**:
- 4.0+: Excellent fit, proceed confidently
- 3.0-3.9: Reasonable fit, manageable gaps
- <3.0: Poor fit, high risk of failure

---

## Questions to Ask Yourself

**Before evaluation**:
1. Have I clearly defined the use case?
2. What are my success criteria?
3. What are my constraints?
4. What's my ideal solution?

**During evaluation**:
1. Have they solved this exact problem?
2. Can they show proof?
3. What gaps exist?
4. Are gaps addressable?

**Before decision**:
1. Am I confident they can deliver?
2. What's the risk of failure?
3. What's my backup plan?
4. Have I seen this working?

---

## Questions to Ask Vendor

**About experience**:
- "Show me 3 customers with similar use cases"
- "What results did they achieve?"
- "What challenges did they face?"
- "How is my use case different?"

**About capabilities**:
- "Walk me through how this would work for my specific use case"
- "What data do you need from me?"
- "What's the expected accuracy/performance?"
- "What are the limitations?"

**About proof**:
- "Can we do a pilot with my actual data?"
- "What's your success rate for similar use cases?"
- "Can I speak with similar customers?"
- "What happens if it doesn't work?"

---

## Common Use Case Mismatches

### Mismatch 1: Generic Solution for Specific Need
**Problem**: Vendor has generic tool, your need is highly specific  
**Example**: Generic text classifier vs industry-specific medical coding  
**Risk**: Won't work well, requires extensive customization

### Mismatch 2: Simple Solution for Complex Problem
**Problem**: Vendor built for simpler use case  
**Example**: Basic chatbot vs complex multi-turn dialogue  
**Risk**: Will hit limitations quickly

### Mismatch 3: Different Domain
**Problem**: Vendor from different industry  
**Example**: Retail vendor for healthcare use case  
**Risk**: Misses domain nuances, compliance issues

### Mismatch 4: Scale Mismatch
**Problem**: Built for different scale  
**Example**: SMB tool for enterprise deployment  
**Risk**: Performance issues, can't handle volume

### Mismatch 5: Data Type Mismatch
**Problem**: Optimized for different data  
**Example**: Text model for audio/video  
**Risk**: Poor accuracy, doesn't work as expected

---

## Red Flags for Poor Fit

🚩 "We can customize it for you" (expensive, risky)  
🚩 "No one's done exactly this before" (you're the guinea pig)  
🚩 "It should work for your use case" (not confident)  
🚩 "Just need to do some customization" (scope creep)  
🚩 "All our customers are different" (no proven pattern)  
🚩 Won't commit to specific outcomes  
🚩 Can't show similar customer success  

---

## Pilot Testing

**Before full commitment, pilot test**:

**Pilot structure**:
1. Define success criteria upfront
2. Test with real data (not cherry-picked examples)
3. Involve actual users
4. Set timeline (4-8 weeks typical)
5. Measure against criteria

**Pilot success criteria**:
- Accuracy/quality meets minimum threshold
- Performance acceptable
- Users can actually use it
- Integration works
- Costs align with expectations

**Pilot failure = Do not proceed**

---

## Decision Framework

```
Is use case match score ≥ 4.0?
├─ YES → Proceed to deep evaluation
└─ NO → Continue below

Is use case match score ≥ 3.0 AND gaps addressable?
├─ YES → Require pilot before commitment
└─ NO → Do not proceed

Are there alternative vendors with better fit?
├─ YES → Evaluate alternatives
└─ NO → Consider build vs buy
```

---

## Summary Checklist

Before selecting vendor, confirm:

- [ ] Vendor has solved this exact use case before
- [ ] Multiple customers with similar use case
- [ ] Vendor understands domain requirements
- [ ] Data compatibility confirmed
- [ ] Integration feasibility verified
- [ ] Scale/performance adequate
- [ ] Success criteria agreed upon
- [ ] Pilot completed successfully (if needed)

**If you can't check most boxes, fit is poor. Find better vendor or build.**