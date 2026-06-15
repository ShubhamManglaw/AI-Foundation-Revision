Day 7 - Pandas Basics Notes

What is Pandas?

Pandas is a Python library used for data analysis and data manipulation.

It provides two important data structures:

1. Series
2. DataFrame

⸻

Series

A Series is a one-dimensional labeled array.

Example:

import pandas as pd
marks = pd.Series([85, 90, 95])

Output:

0    85
1    90
2    95

Characteristics:

* One-dimensional
* Has values
* Has an index
* Similar to a single column in Excel

⸻

DataFrame

A DataFrame is a two-dimensional table consisting of rows and columns.

Example:

df = pd.DataFrame({
    "Name": ["Amit", "Riya"],
    "Marks": [85, 90]
})

Output:

   Name  Marks
0  Amit     85
1  Riya     90

Characteristics:

* Rows and columns
* Similar to an Excel sheet
* Most commonly used Pandas object

⸻

Row vs Column

Row:

A single record

Example:

101  Shubham  85

Column:

A single attribute

Example:

Name
Math
Physics

⸻

Index

Every row in Pandas has an index.

Default index:

0
1
2
3
...

Example:

df.index

Output:

RangeIndex(start=0, stop=10, step=1)

Purpose:

* Identifies rows
* Enables fast access
* Supports filtering and selection

⸻

Data Types (dtype)

Every column has a data type.

Examples:

int64
float64
object
bool

Check dtypes:

df.dtypes

Example:

Age         int64
Name       object
Math        int64

⸻

Useful DataFrame Functions

View First Rows

df.head()

View Last Rows

df.tail()

Shape

df.shape

Returns:

(rows, columns)

Column Names

df.columns

Index

df.index

Data Types

df.dtypes

⸻

Export CSV

Save DataFrame:

df.to_csv("students.csv", index=False)

Why index=False?

Because we usually do not want Pandas to save the automatic row numbers.

⸻

NumPy vs Pandas

NumPy:

* Numerical computing
* Arrays only
* No column names

Pandas:

* Tabular data
* Rows and columns
* Easier data analysis

⸻

Key Takeaways

* Series = One-dimensional data
* DataFrame = Two-dimensional table
* DataFrame contains rows and columns
* Every row has an index
* Every column has a dtype
* head(), tail(), shape, columns, index and dtypes are essential inspection tools
* to_csv() saves DataFrames to CSV files
* Pandas is the foundation of data analysis and machine learning preprocessing