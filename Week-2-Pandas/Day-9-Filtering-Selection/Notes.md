Day 9 - Pandas Filtering, Sorting and Ranking

Objective

Learn how to query, organize, and analyze data using filtering, sorting, ranking, and calculated columns.

⸻

1. Calculated Columns

Create new columns from existing data.

Example

df["Total"] = (
    df["Math"]
    + df["Physics"]
    + df["Chemistry"]
    + df["English"]
    + df["Computer"]
)
df["Average"] = df["Total"] / 5
df["Percentage"] = (df["Total"] / 500) * 100

Use Cases

* Total Marks
* Average Marks
* Profit
* Revenue
* Performance Metrics

⸻

2. Boolean Filtering

Select rows that satisfy a condition.

Syntax

df[df["Math"] > 80]

Example

math_topper = df[df["Math"] > 80]

⸻

3. Multiple Conditions

AND Condition

Use &

df[
    (df["Math"] > 80)
    &
    (df["Computer"] > 90)
]

OR Condition

Use |

df[
    (df["Class"] == "A")
    |
    (df["Class"] == "B")
]

Important

Always use parentheses.

Correct:

(df["Math"] > 80) & (df["Computer"] > 90)

Wrong:

df["Math"] > 80 & df["Computer"] > 90

⸻

4. Filtering by Category

Example

class_a = df[df["Class"] == "A"]
class_b = df[df["Class"] == "B"]

Useful for:

* Departments
* Classes
* Cities
* Product Categories

⸻

5. Sorting Data

Descending Order

df.sort_values(
    by="Average",
    ascending=False
)

Ascending Order

df.sort_values(
    by="Name",
    ascending=True
)

Common Sorting Columns

Math
Computer
Average
Total
Name

⸻

6. Ranking

Assign positions based on values.

Example

df["Total_Rank"] = (
    df["Total"]
    .rank(ascending=False)
)

Other Rankings

df["Math_Rank"]
df["Computer_Rank"]

Use Cases

* Student Rankings
* Product Rankings
* Sales Rankings
* Competition Leaderboards

⸻

7. Pass / Fail Analysis

Fail Condition

failed_students = df[
    (df["Math"] < 40)
    |
    (df["Physics"] < 40)
    |
    (df["Chemistry"] < 40)
    |
    (df["English"] < 40)
    |
    (df["Computer"] < 40)
]

Pass Condition

passed_students = df[
    (df["Math"] >= 40)
    &
    (df["Physics"] >= 40)
    &
    (df["Chemistry"] >= 40)
    &
    (df["English"] >= 40)
    &
    (df["Computer"] >= 40)
]

⸻

8. Exporting Data

Save filtered data to CSV.

Example

top_students.to_csv(
    "top_students.csv",
    index=False
)

Files Generated

top_students.csv
failed_students.csv
class_A_students.csv
students_with_ranks.csv

⸻

Common Mistakes

Using and instead of &

Wrong:

(df["Math"] > 80) and (df["Computer"] > 90)

Correct:

(df["Math"] > 80) & (df["Computer"] > 90)

Using or instead of |

Wrong:

(df["Class"] == "A") or (df["Class"] == "B")

Correct:

(df["Class"] == "A") | (df["Class"] == "B")

Forgetting Parentheses

Wrong:

df["Math"] > 80 & df["Computer"] > 90

Correct:

(df["Math"] > 80) & (df["Computer"] > 90)

⸻

Key Functions

sort_values()
rank()
to_csv()
head()
tail()

⸻

Day 9 Summary

✅ Calculated Columns

✅ Boolean Filtering

✅ Multiple Conditions

✅ Sorting

✅ Ranking

✅ Pass/Fail Analysis

✅ CSV Export

Day 9 teaches how to ask questions from data and generate useful reports using Pandas.