# Excel Formula Best Practices

## Core Principles

### 1. Formulas Should Scale
Build formulas that can be copied down or across without modification. Avoid hardcoded row references that break when copied.

❌ **Bad**: `=IF(A2="January", SUM(B2:B5), 0)` - breaks when copied down
✅ **Good**: `=SUMIF($A:$A, "January", $B:$B)` - works everywhere

### 2. Formulas Should Be Auditable
Others (or future you) should be able to understand the formula logic without extensive investigation.

❌ **Bad**: `=IF(A2>0,IF(B2>10,IF(C2<5,D2*0.1,D2*0.15),IF(C2<5,D2*0.2,D2*0.25)),0)`
✅ **Good**: Use helper columns or lookup tables to break complex logic into steps

### 3. Avoid Fragile Dependencies
Formulas should not break when columns/rows are inserted or deleted.

❌ **Bad**: `=SUM(B2:B100)` - breaks if rows inserted above or below
✅ **Good**: `=SUM(B:B)` or use structured table references `=SUM(Table1[Revenue])`

## Modern Formula Functions (Use These)

### Conditional Logic

**SWITCH** (not nested IFs)
```excel
=SWITCH(A2, "Small", 100, "Medium", 200, "Large", 300, "Unknown")
```
Use when mapping values to results. Much cleaner than IF chains.

**IFS** (not nested IFs)
```excel
=IFS(A2<10, "Small", A2<50, "Medium", A2>=50, "Large", TRUE, "Unknown")
```
Use when you have multiple condition checks. Evaluates in order, returns first TRUE.

**Lookup Tables** (not nested IFs)
Instead of `=IF(A2="Q1", 100, IF(A2="Q2", 200, ...))`, create a lookup table:
```excel
Quarter | Budget
Q1      | 100
Q2      | 200
Q3      | 150
Q4      | 300

=XLOOKUP(A2, LookupTable[Quarter], LookupTable[Budget], "Not Found")
```

### Lookups

**XLOOKUP** (not VLOOKUP/HLOOKUP/INDEX-MATCH)
```excel
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```
Benefits:
- Can look left or right (VLOOKUP can only look right)
- Returns array (for multiple columns)
- Built-in error handling with 4th argument
- Faster than INDEX-MATCH

Example:
```excel
=XLOOKUP(A2, Customers[ID], Customers[Name], "Customer Not Found")
```

If XLOOKUP not available (Excel 2019 or earlier):
```excel
=INDEX(Customers[Name], MATCH(A2, Customers[ID], 0))
```

### Aggregation

**SUMIFS/COUNTIFS/AVERAGEIFS** (not array formulas or SUMIF with multiple criteria)
```excel
=SUMIFS(sum_range, criteria_range1, criterion1, [criteria_range2, criterion2], ...)
```

Example - sum sales for specific region and product:
```excel
=SUMIFS(Sales[Amount], Sales[Region], "West", Sales[Product], "Widget")
```

**FILTER** (Excel 365+ for dynamic arrays)
```excel
=FILTER(array, include, [if_empty])
```
Returns subset of data matching criteria. Results are dynamic.

Example - all West region sales:
```excel
=FILTER(Sales, Sales[Region]="West", "No sales found")
```

### Text Manipulation

**TEXTJOIN** (not concatenating with &)
```excel
=TEXTJOIN(delimiter, ignore_empty, text1, [text2], ...)
```

Example - combine first and last name with space:
```excel
=TEXTJOIN(" ", TRUE, A2, B2)
```

**CONCAT** (not CONCATENATE or &)
```excel
=CONCAT(text1, [text2], ...)
```
Simpler syntax than CONCATENATE, can handle ranges.

### Date/Time

**EOMONTH** for month-end dates:
```excel
=EOMONTH(A2, 0)  // Last day of month in A2
=EOMONTH(A2, 1)  // Last day of next month
```

**EDATE** for date arithmetic:
```excel
=EDATE(A2, 3)  // Date 3 months after A2
```

**DATEDIF** for date differences:
```excel
=DATEDIF(start_date, end_date, "M")  // Months between dates
=DATEDIF(start_date, end_date, "Y")  // Years between dates
```

## Formula Anti-Patterns to Avoid

### Anti-Pattern 1: Deeply Nested IFs

❌ **Bad**:
```excel
=IF(A2="Small", 100, IF(A2="Medium", 200, IF(A2="Large", 300, IF(A2="XL", 400, 0))))
```

✅ **Good** (use SWITCH or lookup table):
```excel
=SWITCH(A2, "Small", 100, "Medium", 200, "Large", 300, "XL", 400, 0)
```

Or better yet, use a lookup table for maintainability.

### Anti-Pattern 2: Hardcoded Constants in Formulas

❌ **Bad**:
```excel
=B2 * 1.15  // What is 1.15? Magic number!
```

✅ **Good** (reference assumption cell):
```excel
=B2 * (1 + $Assumptions.$B$5)  // Where B5 contains labeled growth rate
```

### Anti-Pattern 3: Fragile Cell References

❌ **Bad**:
```excel
=VLOOKUP(A2, B:F, 3, FALSE)  // Column 3 breaks if columns inserted
```

✅ **Good** (use structured references):
```excel
=XLOOKUP([@Customer], Customers[ID], Customers[Name])
```

### Anti-Pattern 4: Array Formulas Where Simpler Options Exist

❌ **Bad**:
```excel
=SUM(IF(A2:A100="West", B2:B100, 0))  // Requires Ctrl+Shift+Enter
```

✅ **Good**:
```excel
=SUMIF(A:A, "West", B:B)  // Simple, clear, fast
```

### Anti-Pattern 5: VLOOKUP

VLOOKUP has limitations:
- Can't look to the left
- Column index breaks when columns inserted
- Slower than XLOOKUP

✅ **Use XLOOKUP instead**:
```excel
=XLOOKUP(lookup, lookup_range, return_range)
```

### Anti-Pattern 6: Calculating in Excel Instead of Formula

❌ **Bad** (Python-calculated and hardcoded):
```python
total = sum([100, 200, 300])
sheet['B10'] = 600  # Hardcoded result
```

✅ **Good** (Excel formula):
```python
sheet['B10'] = '=SUM(B2:B9)'  # Dynamic, recalculates
```

## Working with Tables (Structured References)

Convert ranges to Tables (Ctrl+T) to use structured references:

**Benefits**:
- Formulas auto-expand when rows added
- Column names instead of cell references
- Easier to read: `[@Revenue]` vs `B2`

**Syntax**:
```excel
=[@ColumnName]              // Current row value
=[ColumnName]               // Entire column (outside table)
=Table1[ColumnName]         // Entire column (from elsewhere)
=Table1[[#Headers],[Column]]  // Just headers
=Table1[[#Totals],[Column]]   // Just totals row
```

**Example - calculate margin %**:
```excel
=[@Revenue] - [@COGS]) / [@Revenue]
```
Much clearer than `=(B2-C2)/B2`

## Error Handling

**IFERROR** for graceful failures:
```excel
=IFERROR(XLOOKUP(A2, Customers[ID], Customers[Name]), "Not Found")
```

**IFNA** specifically for #N/A errors:
```excel
=IFNA(VLOOKUP(...), "No Match")
```

**Never** leave formulas that result in #DIV/0!, #REF!, #VALUE!, etc. in production files. Always wrap in error handlers.

## Performance Optimization

### Use Whole Column References Carefully
✅ **Good** for SUMIF, COUNTIF, etc.: `=SUMIF(A:A, "West", B:B)`
❌ **Bad** for volatile functions: `=SUM(A:A)` calculates millions of cells

### Avoid Volatile Functions When Possible
These recalculate on every change, even if their inputs didn't change:
- NOW(), TODAY()
- RAND(), RANDBETWEEN()
- OFFSET(), INDIRECT()
- INFO()

Use when necessary, but minimize usage in large workbooks.

### Use Calculation Operators Instead of Functions
✅ **Faster**: `=A2*B2`
❌ **Slower**: `=PRODUCT(A2:B2)`

## Formula Documentation

**Add comments to complex formulas**:
1. Right-click cell → Insert Comment/Note
2. Explain logic, assumptions, or special cases
3. Document data sources for hardcoded values

**Name ranges/cells meaningfully**:
Instead of `=B2*$G$5`, use `=[@Price]*GrowthRate` where GrowthRate is a named cell.

## Common Financial Model Formulas

### Revenue Growth
```excel
=PreviousPeriodRevenue * (1 + GrowthRate)
```

### Cumulative Sum (Running Total)
```excel
=SUM($B$2:B2)  // Copy down, $ locks start row
```

### Year-over-Year Growth
```excel
=(CurrentYear - PriorYear) / PriorYear
```

### Compound Annual Growth Rate (CAGR)
```excel
=(EndingValue / BeginningValue) ^ (1 / NumberOfYears) - 1
```

### Month-over-Month Change
```excel
=(CurrentMonth - PreviousMonth) / PreviousMonth
```

### Percentage of Total
```excel
=PartValue / $TotalValue$  // Lock total reference
```

## Debugging Formulas

### Evaluate Formula (F9)
1. Select part of formula in formula bar
2. Press F9 to see calculated result
3. Press Esc to return to formula

### Trace Precedents/Dependents
- Formulas tab → Trace Precedents: Shows cells formula depends on
- Formulas tab → Trace Dependents: Shows cells that depend on this cell

### Show Formulas (Ctrl+`)
Toggle between seeing values and seeing formulas in all cells

### Error Checking
1. Formulas tab → Error Checking
2. Identifies common issues like:
   - Numbers stored as text
   - Formulas inconsistent with surrounding formulas
   - Empty cell references

## Version Compatibility

**Excel 365/2021 Dynamic Arrays**:
- FILTER, SORT, UNIQUE, SEQUENCE, XLOOKUP, LET

**Excel 2019**:
- IFS, SWITCH, CONCAT, TEXTJOIN, MAXIFS, MINIFS

**Excel 2016 and earlier**:
- Must use INDEX-MATCH instead of XLOOKUP
- Use nested IFs instead of IFS/SWITCH
- Use & instead of TEXTJOIN

**Check version before using** dynamic arrays or newer functions. When building for broad compatibility, use Excel 2016-compatible formulas.
