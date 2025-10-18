# AI Vendor Red Flags

Comprehensive catalog of warning signs indicating problematic AI vendors. Use this for initial screening to eliminate vendors before deep evaluation.

---

## How to Use This Guide

**Severity levels:**
- 🚩 **Red flag** - Serious concern, investigate deeply before proceeding
- 🔴 **Disqualifying** - Do not proceed without resolution
- ⚠️ **Yellow flag** - Notable concern, needs clarification

**Decision rule**: Multiple red flags in same category = disqualifying. Any single disqualifying flag = stop evaluation.

---

## Technical Red Flags

### 🔴 Vague About Core Technology
**Symptoms:**
- Won't explain how their AI actually works
- Claims "proprietary AI" but can't describe approach
- Defensive when asked technical questions
- No technical documentation available

**Why it matters**: If they can't explain their technology, either it doesn't exist or they're hiding something.

**What to do**: Press for technical details. If still vague, disqualify.

---

### 🔴 Impossible Claims
**Examples:**
- "100% accuracy on all tasks"
- "Our AI understands context perfectly"
- "Never makes mistakes"
- "Works on any use case without training"

**Why it matters**: AI is probabilistic. Anyone claiming perfection is lying or ignorant.

**What to do**: Ask for accuracy metrics with confidence intervals. If they can't provide or claims remain impossible, disqualify.

---

### 🚩 No Performance Metrics
**Symptoms:**
- Can't provide accuracy numbers
- Vague about performance ("very accurate")
- No benchmarks or evaluations
- Unwilling to test on your data

**Why it matters**: You can't manage what you don't measure. No metrics = no accountability.

**What to do**: Request performance evaluation on your data before commitment.

---

### 🚩 Black Box System
**Symptoms:**
- No visibility into how decisions are made
- Can't explain outputs
- No debugging or troubleshooting capabilities
- "Just trust the AI"

**Why it matters**: You need to debug issues and explain decisions to stakeholders.

**What to do**: Request explainability features or detailed logging.

---

### 🚩 Model Wrapper With High Markup
**Symptoms:**
- Thin UI layer over OpenAI/Anthropic API
- Charges 10x+ the underlying API cost
- No proprietary models or significant value-add
- Just access to commercially available models

**Why it matters**: You're paying huge markup for minimal value.

**What to do**: Calculate cost of building similar wrapper in-house. Often days, not months.

---

## Business Red Flags

### 🔴 No Verifiable Customers
**Symptoms:**
- Can't provide reference customers
- All customers are "under NDA" (convenient)
- References are all pilots, no production deployments
- Vague about customer count

**Why it matters**: No customers = unproven solution or failing business.

**What to do**: Demand verifiable references. No references = disqualify.

---

### 🔴 Financial Instability
**Symptoms:**
- Burning cash with no path to profitability
- Recently laid off significant staff
- Delayed or canceled product releases
- Desperate sales tactics (heavy discounting, aggressive terms)

**Why it matters**: Company may not exist in 12 months.

**What to do**: Assess financial stability through research. If concerning, require escrow for source code.

---

### 🚩 Heavy Customer Concentration
**Symptoms:**
- 50%+ of revenue from single customer
- Lose of major customer would threaten business
- Product heavily customized for specific customer

**Why it matters**: Their priorities are driven by their major customer, not broader market.

**What to do**: Assess whether roadmap aligns with your needs despite concentration.

---

### 🚩 Pivot or Identity Crisis
**Symptoms:**
- Recently pivoted from different market/product
- Unclear about core value proposition
- Trying to be everything to everyone
- Frequent strategy changes

**Why it matters**: Unstable direction indicates they haven't found product-market fit.

**What to do**: Assess whether current direction is sustainable.

---

## Pricing Red Flags

### 🔴 Hidden Fees
**Symptoms:**
- Base price doesn't include critical features
- Large implementation fees not mentioned upfront
- Expensive overage charges
- Support costs extra
- "Platform fees" on top of license

**Why it matters**: Actual cost is much higher than advertised.

**What to do**: Demand all-in pricing including implementation, support, and reasonable usage.

---

### 🚩 Complex, Unpredictable Pricing
**Symptoms:**
- Pricing calculator needed to estimate costs
- Different pricing for every customer
- Usage-based pricing with no caps
- Difficult to project annual spend

**Why it matters**: You can't budget for unpredictable costs.

**What to do**: Request simplified pricing or guaranteed caps.

---

### 🚩 "Enterprise Pricing" Opacity
**Symptoms:**
- Won't quote prices until late in sales process
- "Talk to sales" for pricing
- Prices vary wildly between customers
- No published pricing

**Why it matters**: Often means they'll charge whatever they think you'll pay.

**What to do**: Research what others paid. Demand justification for pricing.

---

### 🚩 Mandatory Professional Services
**Symptoms:**
- Software requires expensive implementation
- Professional services cost more than software
- Can't self-implement
- Recurring consulting fees required

**Why it matters**: You're buying consulting, not software.

**What to do**: Calculate true cost. Consider if this is sustainable model.

---

## Contract Red Flags

### 🔴 No Exit Clause
**Symptoms:**
- Multi-year lock-in with large termination penalties
- Can't terminate early under any circumstances
- Data deletion not guaranteed
- Difficult or expensive data export

**Why it matters**: You're trapped even if vendor fails to deliver.

**What to do**: Insist on reasonable termination clause (90-180 days notice). Non-negotiable.

---

### 🔴 Vendor Owns Your Data
**Symptoms:**
- Vendor claims rights to your input data
- Can use your data to train models
- Retains data indefinitely
- Unclear data ownership terms

**Why it matters**: Your proprietary data trains their models or competitors.

**What to do**: Must have explicit data ownership and deletion terms. Non-negotiable.

---

### 🚩 No Performance Guarantees
**Symptoms:**
- No SLAs
- "Best effort" language
- No remedies for poor performance
- Vague about uptime or accuracy

**Why it matters**: No accountability for failure.

**What to do**: Insist on SLAs with financial penalties for breach.

---

### 🚩 Unlimited Price Increases
**Symptoms:**
- Vendor can increase prices without limit
- Annual escalations not capped
- No price protection
- "Market rate" pricing adjustments

**Why it matters**: Costs can spiral without control.

**What to do**: Negotiate price caps or escalation limits.

---

## Behavioral Red Flags

### 🔴 Dishonest or Evasive
**Symptoms:**
- Caught in lies or exaggerations
- Won't answer direct questions
- Different team members give contradictory answers
- Blame others for their problems

**Why it matters**: If they lie during sales, what happens after you're a customer?

**What to do**: Disqualify immediately. Character matters.

---

### 🚩 Overpromising
**Symptoms:**
- "We can do anything"
- Agrees to every feature request
- Unrealistic timelines
- Vague about how they'll deliver

**Why it matters**: They'll underdeliver after you've committed.

**What to do**: Demand specifics and get commitments in writing.

---

### 🚩 Pressure Tactics
**Symptoms:**
- "Deal expires Friday" (arbitrary deadline)
- "Other customers about to sign" (artificial scarcity)
- Won't provide time for evaluation
- Dismisses your concerns

**Why it matters**: Good vendors don't need pressure. They have real demand.

**What to do**: Take your time. Good vendors will wait.

---

### 🚩 Bad-Mouthing Competitors
**Symptoms:**
- Spends time criticizing competitors
- Makes unverifiable claims about competitors
- Focuses on what competitors can't do vs what they can do
- Defensive about competitor comparisons

**Why it matters**: Indicates weak product. Good products sell themselves.

**What to do**: Independently verify claims about competitors.

---

## Demo Red Flags

### 🚩 Canned Demo Only
**Symptoms:**
- Won't demonstrate on your data
- Same demo for every prospect
- Can't deviate from script
- "Production system not available for demos"

**Why it matters**: Hiding limitations or system doesn't work on real data.

**What to do**: Insist on pilot with your actual data.

---

### 🚩 Demo Environment Issues
**Symptoms:**
- System is slow or unresponsive
- Frequent errors during demo
- "That's a known bug we're fixing"
- Demo only works with specific example

**Why it matters**: Production system likely has same issues.

**What to do**: Ask about production reliability and error rates.

---

### 🚩 No Live Demo Available
**Symptoms:**
- Only screenshots or videos
- "System is down for maintenance"
- Repeatedly rescheduling demo
- Need weeks of setup time

**Why it matters**: System may not actually work or doesn't exist yet.

**What to do**: Insist on live demonstration. No live demo = disqualify for production use.

---

## Reference Customer Red Flags

### 🔴 Won't Connect You With References
**Symptoms:**
- All references are "under NDA"
- References not available to speak
- Will only provide written testimonials
- References are all their employees' friends/family

**Why it matters**: No real customers or customers are unhappy.

**What to do**: Must speak with real customers. No references = disqualify.

---

### 🚩 References Are Only Pilots
**Symptoms:**
- All references are in pilot phase
- No production deployments
- References haven't renewed after pilot
- Pilots started months/years ago but never went to production

**Why it matters**: System doesn't work well enough for production use.

**What to do**: Find reference with production deployment.

---

### 🚩 References Have Different Use Case
**Symptoms:**
- References are in different industries
- References use product differently than you will
- References have much simpler use case
- No one doing what you want to do

**Why it matters**: Solution hasn't been proven for your use case.

**What to do**: Assess risk of being first with your use case.

---

## Partnership Red Flags

### 🚩 Heavy Reliance on Integrations
**Symptoms:**
- Core features require third-party integrations
- Multiple paid tools required
- "Works best with Partner X"
- Integration partners aren't committed

**Why it matters**: You're betting on multiple vendors, not one.

**What to do**: Map all dependencies and assess risk of any partner failing.

---

### 🚩 White Label of Another Product
**Symptoms:**
- Rebranded version of someone else's product
- No control over roadmap or features
- Core technology owned by others
- Middleman with no value add

**Why it matters**: Better to go directly to source or they may lose access.

**What to do**: Identify actual technology owner and assess relationship.

---

## Red Flag Scoring System

**Count red flags by category:**

| Category | Red Flags | Assessment |
|----------|-----------|------------|
| Technical | 0-1 | Acceptable |
| Technical | 2-3 | Concerning, investigate deeply |
| Technical | 4+ | Disqualify |
| Business | 0-1 | Acceptable |
| Business | 2-3 | High risk, require mitigation |
| Business | 4+ | Disqualify |
| Pricing | 0-2 | Manageable |
| Pricing | 3-4 | Negotiate or walk away |
| Pricing | 5+ | Disqualify |
| Contract | 0-1 | Typical |
| Contract | 2-3 | Require changes |
| Contract | 4+ | Disqualify |
| Behavioral | 1 | Note and monitor |
| Behavioral | 2-3 | Serious concern |
| Behavioral | 4+ | Disqualify |

**Any disqualifying (🔴) flag alone = stop evaluation**

**Multiple red flags in single category = disqualifying**

**Total red flags across all categories >10 = disqualify**

---

## Using This Guide

**During initial call/demo:**
- Note all red flags observed
- Ask direct questions about concerning areas
- Give vendor chance to address flags

**Before deep evaluation:**
- Review red flag count
- Disqualify vendors with multiple flags in single category
- Document remaining flags for due diligence

**During contract negotiation:**
- Use contract red flags as negotiation guide
- Get problematic terms changed or walk away

**Remember**: Your goal is to find good vendors, not save bad ones. Red flags exist to protect you from costly mistakes. When in doubt, walk away.