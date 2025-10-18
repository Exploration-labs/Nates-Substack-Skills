# Build vs Buy Decision Framework

Structured approach to deciding whether to build AI capability in-house or purchase vendor solution.

---

## Decision Framework

```
Decision Flow:

1. Does suitable vendor solution exist?
   NO → Must build
   YES → Continue to 2

2. Is this a core strategic capability?
   YES → Bias toward build
   NO → Continue to 3

3. Do you have available engineering talent?
   NO → Must buy
   YES → Continue to 4

4. Compare 3-year TCO: Build vs Buy
   Build significantly cheaper → Build
   Buy significantly cheaper → Buy
   Similar costs → Continue to 5

5. Time to value comparison
   Need fast (< 3 months) → Buy
   Can wait (3-12 months) → Either
   Long timeline acceptable → Build

6. Assess strategic factors (see below)
```

---

## Build Cost Estimation

### Initial Development (Months 0-6)
**Engineering**:
- 2-3 engineers × 6-12 months
- Loaded cost: $150K-300K per engineer-year
- Total: $150K-900K depending on complexity

**Infrastructure**:
- Cloud services: $5K-50K
- Development tools: $5K-20K
- Data/model costs: $10K-100K

**Other**:
- Product management: $25K-50K
- Design: $10K-30K
- Testing/QA: $20K-50K

**Year 1 Total**: $225K-1.2M

### Ongoing Costs (Years 2-3)
**Maintenance & Operations**:
- 1-2 engineers: $150K-600K/year
- Infrastructure: $20K-100K/year
- Model retraining: $10K-50K/year
- Improvements: $50K-200K/year

**Annual Ongoing**: $230K-950K

### 3-Year Build TCO
**Low complexity**: $700K-1.5M
**Medium complexity**: $1.5M-3M  
**High complexity**: $3M-6M+

---

## Buy Cost Estimation

### Year 1 Costs
**Licenses/Subscriptions**:
- Based on vendor pricing model
- Typical: $50K-500K

**Implementation**:
- Professional services: $25K-250K
- Internal time: $20K-100K
- Integration dev: $30K-150K

**Training**:
- User training: $10K-50K
- Admin training: $5K-20K

**Year 1 Total**: $140K-1.07M

### Years 2-3 Costs
**Annual Costs**:
- License renewals: 105-110% of Y1 (price increases)
- Usage growth: 10-30% annual increase
- Support: Usually included or $10K-50K
- Minor enhancements: $20K-100K

**Annual Ongoing**: $110K-660K

### 3-Year Buy TCO
**Low-end solution**: $360K-2.4M
**Mid-market solution**: $2.4M-4M
**Enterprise solution**: $4M-10M+

---

## Decision Matrix

| Factor | Weight | Build Score | Buy Score | Winner |
|--------|--------|-------------|-----------|--------|
| Total 3-year cost | 30% | [1-5] | [1-5] | |
| Time to value | 20% | [1-5] | [1-5] | |
| Strategic importance | 15% | [1-5] | [1-5] | |
| Team capability | 15% | [1-5] | [1-5] | |
| Flexibility/control | 10% | [1-5] | [1-5] | |
| Risk | 10% | [1-5] | [1-5] | |
| **Weighted Total** | | | | |

**Scoring**:
- 5 = Strongly favors this option
- 3 = Neutral
- 1 = Strongly against this option

**Decision**: Option with higher weighted total wins

---

## Build Advantages

✅ **Full control**: Own the roadmap and priorities  
✅ **Customization**: Exactly fits your needs  
✅ **No vendor lock-in**: Freedom to pivot  
✅ **Competitive advantage**: Proprietary capability  
✅ **Data privacy**: Data never leaves your infrastructure  
✅ **Cost at scale**: Cheaper if high volume usage  

---

## Build Disadvantages

❌ **High upfront cost**: Large initial investment  
❌ **Slow time to value**: 6-24 months typically  
❌ **Ongoing maintenance**: Permanent team needed  
❌ **Technical risk**: May not work as planned  
❌ **Opportunity cost**: Engineers not on other projects  
❌ **Expertise required**: Need specialized AI talent  

---

## Buy Advantages

✅ **Fast time to value**: Live in weeks/months  
✅ **Lower upfront cost**: Subscription model  
✅ **Vendor expertise**: Benefit from their R&D  
✅ **Reduced risk**: Solution already proven  
✅ **Predictable costs**: Monthly/annual fees  
✅ **No maintenance burden**: Vendor handles it  

---

## Buy Disadvantages

❌ **Vendor lock-in**: Switching costs are high  
❌ **Limited control**: On vendor's roadmap  
❌ **Customization limits**: May not fit perfectly  
❌ **Recurring costs**: Pay forever  
❌ **Cost at scale**: Expensive with high usage  
❌ **Data sharing**: Vendor access to your data  

---

## Build When...

✅ **Core strategic capability**: Key differentiator  
✅ **Unique requirements**: No vendor fits  
✅ **High volume usage**: Build economics work at scale  
✅ **Data sensitivity**: Cannot share with vendors  
✅ **Available talent**: Have engineers who can build  
✅ **Long-term horizon**: Can wait for ROI  
✅ **Competitive moat**: Want proprietary advantage  

**Example**: Recommendation engine for e-commerce - core to business, high volume, competitive advantage

---

## Buy When...

✅ **Commodity capability**: Not differentiating  
✅ **Speed critical**: Need solution now  
✅ **Lower cost**: Vendor cheaper than building  
✅ **Limited resources**: Can't spare engineering  
✅ **Proven solutions exist**: No need to reinvent  
✅ **Not core competency**: Focus elsewhere  
✅ **Risk averse**: Want proven solution  

**Example**: Email classification - commodity capability, vendors exist, not core business

---

## Hybrid Approach

**Sometimes best option**: Build some, buy some

**When hybrid makes sense**:
- Build core differentiating features
- Buy commodity features
- Use vendor for speed, transition to build later
- Buy for pilots, build if successful

**Example hybrid**:
- Buy: Text extraction from documents (commodity)
- Build: Custom classification for your domain (differentiation)

---

## Decision Case Studies

### Case Study 1: Customer Support Classification

**Situation**: E-commerce company, 10K tickets/month

**Build option**: $400K year 1, $200K/year ongoing = $800K 3-year TCO  
**Buy option**: $60K/year × 3 = $180K 3-year TCO

**Decision**: **Buy** - Not core to business, vendor solution works well, 4.4x cheaper

---

### Case Study 2: Product Recommendation Engine

**Situation**: Retailer, recommendations drive 30% of revenue

**Build option**: $800K year 1, $400K/year ongoing = $1.6M 3-year TCO  
**Buy option**: $200K/year × 3 = $600K 3-year TCO

**Decision**: **Build** - Core to business model, unique data, competitive advantage worth premium

---

### Case Study 3: Document Processing

**Situation**: Insurance company, 50K documents/month

**Build option**: $500K year 1, $250K/year ongoing = $1M 3-year TCO  
**Buy option**: $150K/year × 3 = $450K 3-year TCO

**Decision**: **Buy initially, build later** - Need fast solution for business, will build custom later as volume grows and costs justify

---

## Common Mistakes

❌ **Underestimating build costs**: Forgetting ongoing maintenance  
❌ **Overestimating build benefits**: Assuming perfect execution  
❌ **Ignoring opportunity cost**: Engineers could build revenue features  
❌ **Vendor lock-in fear paralyzing decision**: Some lock-in is acceptable for right solution  
❌ **Not actually comparing**: Building without checking if vendors exist  
❌ **Building because "we can"**: Engineering vanity projects  

---

## Final Decision Checklist

Before deciding, answer:

- [ ] Have we accurately estimated both build and buy costs?
- [ ] Have we factored in opportunity cost of building?
- [ ] Is this truly strategic or are we overestimating importance?
- [ ] Do we have the talent to build and maintain this?
- [ ] Have we evaluated at least 3 vendor options?
- [ ] Have we included all hidden costs (both options)?
- [ ] Does the timeline align with business needs?
- [ ] Have we considered hybrid approaches?

---

## Summary

**Build when**: Strategic capability, unique needs, high volume, available talent, long-term view

**Buy when**: Commodity capability, speed needed, limited resources, proven solutions exist

**Remember**: Build vs buy isn't permanent. Can buy now, build later (or vice versa). Choose based on current situation and strategic importance.