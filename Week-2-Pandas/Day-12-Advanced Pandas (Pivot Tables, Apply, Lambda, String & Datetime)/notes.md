# 📘 Day 12 – Advanced Pandas (AI/ML Revision)

> Goal: Learn the most important Pandas features used in Data Analysis, Machine Learning, and AI preprocessing.

---

# 📌 Topics Covered

- Pivot Tables
- apply()
- lambda
- String Methods (.str)
- Datetime (.dt)
- Feature Engineering
- Exporting Data

---

# 1. Pivot Tables

## What is a Pivot Table?

A Pivot Table summarizes large datasets by grouping rows and performing aggregations.

Think of it as the Pandas equivalent of **Excel Pivot Tables**.

---

## Syntax

```python
pd.pivot_table(
    data,
    values="column",
    index="group",
    columns="optional",
    aggfunc="mean"
)
```

---

## Parameters

| Parameter | Purpose |
|------------|------------------------------|
| data | DataFrame |
| values | Column to calculate |
| index | Row grouping |
| columns | Column grouping |
| aggfunc | mean, sum, count, max... |
| fill_value | Replace NaN |
| margins | Add totals |

---

## Common Aggregations

```python
mean
sum
count
max
min
median
std
```

---

## Example

```python
students.pivot_table(
    values="Marks",
    index="Class",
    aggfunc="mean"
)
```

---

## Multiple Groups

```python
students.pivot_table(
    values="Marks",
    index=["Class","Gender"],
    aggfunc="mean"
)
```

---

## Column Groups

```python
students.pivot_table(
    values="Marks",
    index="Class",
    columns="Subject",
    aggfunc="mean"
)
```

---

## Missing Values

```python
fill_value=0
```

---

## Totals

```python
margins=True
```

---

## pivot() vs pivot_table()

| pivot() | pivot_table() |
|----------|---------------|
| Reshape | Summarize |
| No duplicates | Handles duplicates |
| No aggregation | Aggregation |

---

# 2. apply()

## What is apply()?

Applies a function to every value or every row.

---

## Syntax

```python
df["column"].apply(function)
```

or

```python
df["column"].apply(lambda x: ...)
```

---

## Example

```python
students["Pass"] = students["Marks"].apply(
    lambda x: x >= 40
)
```

---

## Custom Function

```python
def grade(mark):

    if mark >= 90:
        return "A"

    elif mark >= 75:
        return "B"

    elif mark >= 60:
        return "C"

    return "D"

students["Grade"] = students["Marks"].apply(grade)
```

---

## Row-wise apply

```python
students.apply(
    function,
    axis=1
)
```

Remember

```
axis=0 → Columns

axis=1 → Rows
```

---

# 3. Lambda Functions

## What is Lambda?

An anonymous one-line function.

---

## Syntax

```python
lambda arguments: expression
```

---

## Example

```python
lambda x: x * 2
```

---

## Used With

- apply()
- map()
- assign()

---

## Examples

```python
students["Double"] = students["Marks"].apply(
    lambda x: x * 2
)
```

---

```python
students["Result"] = students["Marks"].apply(
    lambda x:
    "Pass"
    if x >= 40
    else "Fail"
)
```

---

# 4. String Methods

Used to clean text columns.

Access using

```python
.str
```

---

## Most Important Methods

```python
.lower()

.upper()

.title()

.strip()

.replace()

.contains()

.split()

.len()

.startswith()

.endswith()
```

---

## Examples

Convert lowercase

```python
df["Email"] = df["Email"].str.lower()
```

---

Remove spaces

```python
df["Name"] = df["Name"].str.strip()
```

---

Title Case

```python
df["Name"] = df["Name"].str.title()
```

---

Contains

```python
df["Email"].str.contains("gmail")
```

---

Split

```python
df["Email"].str.split("@")
```

---

Length

```python
df["Name"].str.len()
```

---

# 5. Datetime

Most datasets store dates as strings.

Convert first.

```python
pd.to_datetime()
```

---

## Example

```python
df["Date"] = pd.to_datetime(df["Date"])
```

---

## Common Features

```python
.dt.year

.dt.month

.dt.day

.dt.day_name()

.dt.month_name()

.dt.weekday

.dt.quarter

.dt.hour
```

---

## Example

```python
df["Year"] = df["Date"].dt.year
```

---

# 6. Feature Engineering

Creating new useful columns.

Example

```python
df["Revenue"] = df["Quantity"] * df["Price"]
```

---

Categorization

```python
df["Sales_Level"] = df["Revenue"].apply(

    lambda x:

    "High"

    if x >= 10000

    else "Low"
)
```

---

# 7. AI/ML Workflow

```
Read CSV
      │
Inspect Data
      │
Handle Missing Values
      │
Clean Strings
      │
Convert Datetime
      │
Feature Engineering
      │
GroupBy
      │
Pivot Tables
      │
Export Clean Dataset
```

---

# Most Used Functions

```python
read_csv()

head()

info()

describe()

shape

loc

iloc

fillna()

dropna()

drop_duplicates()

rename()

sort_values()

groupby()

pivot_table()

apply()

lambda

str.lower()

str.strip()

str.contains()

pd.to_datetime()

dt.year

dt.month

to_csv()
```

---

# Interview Questions

### Difference between apply() and lambda?

- apply() → Pandas method
- lambda → Python anonymous function

---

### Difference between pivot() and pivot_table()?

pivot()

- Reshapes data

pivot_table()

- Summarizes data
- Supports aggregation

---

### Why convert dates?

To extract

- Year
- Month
- Weekday
- Quarter

for analysis and machine learning.

---

# AI/ML Takeaways

✅ Clean data before training.

✅ Handle missing values.

✅ Create new features.

✅ Use Pivot Tables for EDA.

✅ Use apply() for custom logic.

✅ Use String Methods for text cleaning.

✅ Use Datetime features for time-based analysis.

---

# Revision Checklist

- [x] Pivot Tables
- [x] apply()
- [x] lambda
- [x] String Methods
- [x] Datetime
- [x] Feature Engineering
- [x] Final Project

---

# Next Step

➡️ Machine Learning with **Scikit-learn**

You now have the Pandas skills needed for:

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Preparing datasets for ML models