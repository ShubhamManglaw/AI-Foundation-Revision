📘 Day 12 – Pandas Merging, Joining & Concatenation

🎯 Objective

Learn how to combine multiple datasets using Pandas. This is one of the most important topics in data analysis, machine learning, and data engineering because real-world data is usually spread across multiple files or tables.

⸻

1. pd.concat()

Definition

concat() combines multiple DataFrames by stacking them either vertically (rows) or horizontally (columns).

Syntax

pd.concat([df1, df2], axis=0)

Parameters

Parameter	Meaning
axis=0	Stack rows (default)
axis=1	Combine columns
ignore_index=True	Reset index after concatenation

Vertical Concatenation

result = pd.concat([df1, df2], ignore_index=True)

Used when both DataFrames have the same columns.

Example:

A
B
+
C
D
=
A
B
C
D

Horizontal Concatenation

result = pd.concat([df1, df2], axis=1)

Used when both DataFrames represent different columns of the same observations.

⸻

2. pd.merge()

Definition

merge() combines DataFrames using one or more common columns called keys.

Syntax

pd.merge(df1, df2, on="Student_ID")

Example:

Students

Student_ID	Name
101	Shubham
102	Amit

Marks

Student_ID	Math
101	95
102	80

Merged Result

Student_ID	Name	Math
101	Shubham	95
102	Amit	80

⸻

3. Primary Key

A Primary Key is a column that uniquely identifies each row.

Examples:

* Student_ID
* Employee_ID
* Order_ID
* Customer_ID

Primary keys are used to merge related datasets.

⸻

4. Join Types

Inner Join

pd.merge(df1, df2, how="inner")

Returns only matching rows.

Example:

Left : 101 102 103
Right: 101 102 104
Result:
101
102

⸻

Left Join

pd.merge(df1, df2, how="left")

Keeps all rows from the left DataFrame.

Missing matches become NaN.

⸻

Right Join

pd.merge(df1, df2, how="right")

Keeps all rows from the right DataFrame.

Missing values from the left become NaN.

⸻

Outer Join

pd.merge(df1, df2, how="outer")

Keeps every row from both DataFrames.

Non-matching values become NaN.

⸻

5. DataFrame.join()

join() combines DataFrames using their indexes.

Syntax

df1.join(df2)

Use join() when the indexes already match.

⸻

6. Difference Between concat() and merge()

Feature	concat()	merge()
Purpose	Stack DataFrames	Match DataFrames
Based On	Axis	Common key
Matching Required	No	Yes
Common Usage	Combine files	Relational data

⸻

7. Difference Between merge() and join()

merge()	join()
Joins on columns	Joins on indexes
More flexible	Simpler syntax
Most commonly used	Useful for index-based joins

⸻

8. Handling Missing Values After Joins

Joins may introduce missing values represented as NaN.

Example:

df.fillna(0)

or

df.dropna()

⸻

9. Mini Project Workflow

1. Load students.csv
2. Load marks.csv
3. Load attendance.csv
4. Merge students and marks
5. Merge attendance
6. Calculate Total
7. Calculate Average
8. Assign Grade
9. Export final dataset

⸻

10. Key Functions

pd.concat()
pd.merge()
df.join()
fillna()
dropna()
to_csv()
read_csv()

⸻

11. Interview Questions

* What is concat()?
* What is merge()?
* What is a primary key?
* Explain Inner Join.
* Explain Left Join.
* Explain Right Join.
* Explain Outer Join.
* Difference between merge() and join().
* Difference between concat() and merge().
* Why do joins produce NaN values?

⸻

12. Quick Revision

Function	Purpose
pd.concat()	Stack DataFrames vertically or horizontally
pd.merge()	Merge DataFrames using common key(s)
df.join()	Join DataFrames using indexes
how="inner"	Matching rows only
how="left"	Keep all rows from left DataFrame
how="right"	Keep all rows from right DataFrame
how="outer"	Keep all rows from both DataFrames
ignore_index=True	Reset index after concatenation
to_csv()	Save DataFrame to CSV
read_csv()	Load CSV into a DataFrame

⸻

✅ Learning Outcomes

After completing this topic, you should be able to:

* Combine datasets using concat().
* Merge tables using common keys.
* Choose the correct join type for a problem.
* Explain primary keys and relational data.
* Build a master dataset from multiple CSV files.
* Prepare datasets for machine learning and data analysis.