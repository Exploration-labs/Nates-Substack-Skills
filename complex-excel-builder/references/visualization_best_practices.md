# Excel Visualization Best Practices

## Core Principles

### 1. Choose the Right Chart for the Data Story

**Time Series Data** → Line or Column Charts
**Comparisons** → Bar Charts (horizontal) or Column Charts (vertical)
**Part-to-Whole** → Stacked Bar Charts or Treemaps (NOT pie charts)
**Distribution** → Histogram or Box Plot
**Correlation** → Scatter Plot
**Composition Over Time** → Stacked Area or Stacked Column

### 2. Minimize Chart Junk
Remove elements that don't convey information:
- Unnecessary gridlines
- 3D effects (distort perception)
- Heavy borders
- Decorative backgrounds
- Redundant legends when labels suffice

### 3. Maximize Data-Ink Ratio
Maximize the proportion of ink devoted to displaying data vs decoration.

## Chart Type Selection Guide

### Bar Charts (Horizontal) - PREFERRED for Comparisons

✅ **Use when**:
- Comparing categories (revenue by region, customers by segment)
- Long category names (easier to read horizontally)
- Showing rankings or ordered data

✅ **Benefits**:
- Easy to compare lengths
- Natural reading direction for category labels
- Works well with many categories

**Example use cases**:
- Revenue by product line
- Customer count by region
- Feature usage frequency
- Survey response distributions

### Column Charts (Vertical) - PREFERRED for Time Series

✅ **Use when**:
- Showing time series data (months, quarters, years)
- Comparing values across categories with short labels
- Displaying discrete time periods

**Example use cases**:
- Monthly revenue
- Quarterly customer growth
- Weekly active users

### Line Charts - PREFERRED for Trends

✅ **Use when**:
- Showing continuous data over time
- Comparing 2-4 trends simultaneously
- Emphasizing rate of change

❌ **Avoid**:
- More than 4-5 lines (becomes crowded and hard to read)
- Discrete categories (use bar/column instead)
- When exact values matter more than trends

**Best practices**:
- Limit to 3-4 lines maximum
- Use distinct colors (not shades of the same color)
- Label lines directly (not just in legend)
- Start Y-axis at zero unless showing small variations in large numbers

**Example use cases**:
- ARR growth over time
- CAC trends across quarters
- User engagement metrics month-over-month

### Stacked Bar/Column - For Part-to-Whole Over Time

✅ **Use when**:
- Showing composition AND total simultaneously
- Comparing proportions across periods
- Components are additive

❌ **Avoid**:
- When comparing individual components (use grouped instead)
- More than 5-6 categories (becomes hard to read)

**Example use cases**:
- Revenue composition by product line
- Customer distribution by plan type
- Cost breakdown by category

### Area Charts - For Cumulative Totals

✅ **Use when**:
- Showing volume or magnitude over time
- Emphasizing cumulative totals
- Part-to-whole relationships evolving over time

❌ **Avoid**:
- When exact values are important (overlap obscures values)
- More than 3-4 areas (too cluttered)

### Scatter Plots - For Correlations

✅ **Use when**:
- Exploring relationship between two variables
- Identifying clusters or outliers
- Showing distribution of data points

**Example use cases**:
- CAC vs. LTV by customer segment
- Revenue vs. marketing spend
- Churn rate vs. engagement score

### Waterfall Charts - For Sequential Changes

✅ **Use when**:
- Showing how initial value changes through additions/subtractions
- Breaking down variance or change components

**Example use cases**:
- Revenue bridge (start → +new → -churn → end)
- Budget vs. actual variance analysis
- Cohort movement (retained vs. churned vs. new)

## What NOT to Use

### ❌ Pie Charts - AVOID

**Why pie charts are problematic**:
1. Humans are bad at comparing angles and areas
2. Hard to compare multiple pies
3. Small slices become illegible
4. Don't scale well beyond 3-4 categories

✅ **Use instead**: Bar chart (horizontal)

**Example - Revenue by Region**:
❌ Pie chart with 6 colored slices
✅ Horizontal bar chart, sorted by value

### ❌ 3D Charts - AVOID

**Why 3D charts are problematic**:
1. Perspective distorts values (front appears larger)
2. Harder to read exact values
3. Added visual complexity without information gain
4. Looks dated and unprofessional

✅ **Use instead**: 2D version of the same chart type

### ❌ Donut Charts - AVOID (Same as Pie)

Same problems as pie charts, but with center removed (less data-ink!).

### ❌ Radar/Spider Charts - RARELY APPROPRIATE

**Problems**:
- Hard to compare areas
- Axis order affects perception
- Not suitable for most business data

**Only use** for truly multidimensional profiles (personality assessments, etc.)

### ❌ Multiple Y-Axes - USE SPARINGLY

**Problems**:
- Can be manipulated to exaggerate/hide relationships
- Hard to read and interpret
- Often misleading

✅ **Better alternatives**:
- Use two separate charts stacked vertically
- Normalize to index or percentage
- Use secondary axis only when scales are very different and relationship is important

## Chart Design Best Practices

### Colors

**Do**:
- Use color to highlight key data points
- Maintain consistent color scheme across workbook
- Use colorblind-friendly palettes
- Use contrasting colors for different series
- Gray out non-essential data to emphasize key points

**Don't**:
- Use red/green only (colorblind issues)
- Use more than 5-6 distinct colors in one chart
- Use rainbow color schemes (no semantic meaning)
- Use similar shades for different categories

**Recommended palette** (colorblind-safe):
- Primary: Blue (#4472C4)
- Secondary: Orange (#ED7D31)
- Tertiary: Gray (#A5A5A5)
- Positive: Dark Green (#70AD47)
- Negative: Dark Red (#C65911)

### Axes

**Y-Axis**:
- Start at zero for bar/column charts (unless showing small variations)
- Use appropriate increments (1s, 5s, 10s, 100s, not 7s or 13s)
- Label with units (%, $M, K, etc.)
- Remove gridlines if not needed for precision

**X-Axis**:
- Order meaningfully (time, alphabet, value)
- Angle labels only if necessary (45° max)
- Consider using top labels for better readability

### Titles and Labels

**Chart Title**:
- Descriptive, not generic ("Q4 2024 Revenue by Region" not "Revenue")
- Action-oriented if showing insight ("West Region Drives 40% of Revenue")

**Axis Labels**:
- Include units in axis title ("Revenue ($M)")
- Don't repeat units on every tick mark

**Data Labels**:
- Use when exact values are important
- Format consistently (decimals, thousands separator)
- Don't use when trends matter more than exact values
- Position outside bar end for readability

**Legend**:
- Place where it doesn't obscure data (usually right or bottom)
- Consider direct labeling instead of legend when possible
- Remove legend if only one series

### Gridlines

**Horizontal gridlines**: Use for bar/column charts to aid value reading
**Vertical gridlines**: Rarely needed (usually omit)
**Both**: Almost never

**Formatting**:
- Light gray, not black
- Thin lines, not thick
- Major gridlines only (not minor)

### Size and Spacing

- Chart should be large enough to read comfortably
- Don't cram multiple complex charts on one sheet
- Leave white space around charts
- Maintain consistent chart sizes across workbook

## Dashboard Design Principles

### Layout

**F-Pattern** (readers scan top-left to right, then down):
- Most important metric/chart: Top-left
- Supporting details: Right and below
- Least critical: Bottom-right

**Z-Pattern** (for smaller content):
- Top-left to top-right
- Diagonal to bottom-left
- Bottom-left to bottom-right

### Hierarchy

1. **KPI Numbers** (largest, top)
   - Large font (24-36pt)
   - Current value + change from prior period
   - Green/red indicator for positive/negative

2. **Primary Charts** (main insights)
   - 2-3 key visualizations
   - Medium size, prominent placement

3. **Supporting Charts** (context and detail)
   - Smaller, below or to right
   - Provide breakdowns and details

### Information Density

**Don't overcrowd**:
- Maximum 6-8 visualizations per dashboard
- Each chart should tell ONE story
- Use filters/slicers for interactivity rather than cramming all views

### Consistency

- Same colors mean same things throughout
- Same chart types for same data types
- Same formatting for similar metrics
- Aligned elements (charts, titles, labels)

## Excel-Specific Chart Creation Best Practices

### 1. Use Tables as Data Sources

```python
# Convert range to table first
sheet['A1'] = 'Month'
sheet['B1'] = 'Revenue'
# ... add data ...

# Then reference table in chart, not cell ranges
# Charts auto-update when table rows added
```

### 2. Named Ranges for Chart Data

Makes formulas readable and charts easier to manage:
```python
wb.create_named_range('MonthlyRevenue', sheet, '$B$2:$B$13')
# Use 'MonthlyRevenue' in chart series
```

### 3. Dynamic Chart Titles

Link chart title to a cell with a formula:
```excel
="Revenue Growth: " & TEXT(B10, "0.0%")
```
Chart title updates automatically when data changes.

### 4. Conditional Formatting in Tables

Use conditional formatting for data bars, color scales, icon sets in tables:
- Data bars: Good for showing relative magnitude
- Color scales: Good for heatmaps
- Icon sets: Good for status indicators

**Don't mix** conditional formatting AND charts showing same data (redundant).

## Common Visualization Mistakes

### Mistake 1: Starting Y-Axis Above Zero to Exaggerate Differences

❌ Revenue chart starting at $900K shows dramatic 50% visual drop for 10% decline
✅ Start at zero to show true proportional change

**Exception**: When showing small variations in large numbers (stock prices, temperature), non-zero start is acceptable BUT clearly label.

### Mistake 2: Using Line Charts for Categorical Data

❌ Line chart connecting product categories (shoes → shirts → hats)
✅ Bar chart for categories (no inherent order or continuity)

### Mistake 3: Too Many Data Series

❌ Line chart with 12 lines (impossible to distinguish)
✅ Show top 3-4 lines + "Other" aggregate OR use small multiples (separate charts)

### Mistake 4: Inappropriate Aspect Ratio

❌ Tall, narrow chart exaggerates vertical change
❌ Short, wide chart minimizes change
✅ Roughly 1.5:1 to 2:1 width:height ratio (golden ratio ~1.6:1)

### Mistake 5: Unclear Purpose

❌ Generic "Revenue Over Time" with no insight
✅ "Q4 Revenue Increased 23% YoY Driven by Enterprise Segment"

### Mistake 6: Unlabeled or Ambiguous Axes

❌ Y-axis labeled "Amount" (what units? millions? percentage?)
✅ "Revenue ($M)" or "Revenue ($000s)"

## Chart Type Decision Tree

```
Start: What are you showing?

├─ Change over time?
│  ├─ Continuous trend? → Line Chart (≤4 series)
│  └─ Discrete periods? → Column Chart
│
├─ Comparison between categories?
│  ├─ Simple comparison? → Bar Chart (horizontal)
│  ├─ Composition over time? → Stacked Column
│  └─ Part-to-whole at one point? → Stacked Bar (NOT pie)
│
├─ Relationship between variables?
│  └─ Correlation? → Scatter Plot
│
├─ Distribution?
│  └─ Frequency distribution? → Histogram
│
└─ Sequential change breakdown?
   └─ Additions/subtractions? → Waterfall Chart
```

## Accessibility

- Use patterns/textures in addition to colors (for colorblind users)
- Ensure sufficient contrast (text readable)
- Alt text for charts (describe what chart shows)
- Don't rely solely on color to convey information

## Testing Your Visualization

Ask yourself:
1. Can I understand the key message in 5 seconds?
2. Can I remove any elements without losing information?
3. Are all axes clearly labeled with units?
4. Can this be understood without explanation?
5. Is the chart type optimal for this data?
6. Would this work in black and white? (print test)
7. Does it avoid misleading visual tricks?

If you answer "no" to any question, revise the chart.
