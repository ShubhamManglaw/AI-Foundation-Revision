Day 10 - Pandas Cleaning, Missing Values and GroupBy

Objective

Learn how to clean messy datasets and generate meaningful summaries using Pandas.

⸻

1. Missing Values

Missing values occur when data is unavailable.

Detect Missing Values

df.isnull()

Count Missing Values

df.isnull().sum()

Total Missing Values

df.isnull().sum().sum()

⸻

2. fillna()

Used to replace missing values.

Example

df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)

Common Strategies

* Mean
* Median
* Mode
* Fixed Value

⸻

3. dropna()

Removes missing records.

Example

df = df.dropna(
    subset=["Name"]
)

Use when missing data makes a row unusable.

⸻

4. Duplicates

Detect Duplicates

df.duplicated()

Count Duplicates

df.duplicated().sum()

Remove Duplicates

df = df.drop_duplicates()

⸻

5. value_counts()

Counts occurrences of unique values.

Example

df["Class"].value_counts()

Output

A    4
B    3
C    3

Useful for:

* Categories
* Labels
* Frequencies

⸻

6. GroupBy

Used to split data into groups and perform calculations.

Example

df.groupby("Class")

Groups students according to class.

⸻

7. Group Statistics

Average Total Marks Per Class

df.groupby("Class")["Total"].mean()

Student Count Per Class

df.groupby("Class").size()

⸻

8. agg()

Performs multiple calculations simultaneously.

Example

df.groupby("Class").agg({
    "Math": "mean",
    "Physics": "mean",
    "Computer": "mean",
    "Total": ["mean", "max", "min"]
})

Common Aggregations

mean
max
min
sum
count

⸻

9. Feature Engineering

Creating new columns from existing data.

Total

df["Total"] = (
    df["Math"]
    + df["Physics"]
    + df["Computer"]
)

Average

df["Average"] = df["Total"] / 3

⸻

10. Exporting Data

Export Clean Dataset

df.to_csv(
    "cleaned_students.csv",
    index=False
)

Export Summary Report

class_summary.to_csv(
    "class_summary.csv"
)

⸻

Common Mistakes

Forgetting Assignment

Wrong

df.fillna(0)

Correct

df = df.fillna(0)

or

df["Age"] = df["Age"].fillna(0)

⸻

Using GroupBy Without Aggregation

Wrong

df.groupby("Class")

Correct

df.groupby("Class").mean()

⸻

Key Functions

isnull()
fillna()
dropna()
duplicated()
drop_duplicates()
groupby()
agg()
value_counts()

⸻

Day 10 Summary

✅ Missing Value Detection

✅ Missing Value Handling

✅ Duplicate Detection

✅ Duplicate Removal

✅ value_counts()

✅ groupby()

✅ agg()

✅ Feature Engineering

✅ CSV Export

Day 10 covers the most important data-cleaning and aggregation skills used in real-world machine learning and data analysis workflows.