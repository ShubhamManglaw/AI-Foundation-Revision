Day 8 — Pandas CSV Reading and Data Selection

1. Reading CSV Files

Load a CSV file into a Pandas DataFrame.

import pandas as pd
df = pd.read_csv("students.csv")

A DataFrame is a table-like structure consisting of rows and columns.

⸻

2. Dataset Inspection

head()

Displays the first 5 rows.

df.head()

Display first 3 rows:

df.head(3)

⸻

tail()

Displays the last 5 rows.

df.tail()

Display last 2 rows:

df.tail(2)

⸻

shape

Returns:

(rows, columns)

Example:

df.shape

Output:

(10, 9)

⸻

size

Returns total number of values.

df.size

Example:

10 × 9 = 90

⸻

ndim

Returns number of dimensions.

df.ndim

Output:

2

DataFrames are two-dimensional.

⸻

columns

Displays all column names.

df.columns

Convert to list:

df.columns.tolist()

⸻

info()

Provides:

* Column names
* Data types
* Non-null values
* Memory usage

df.info()

⸻

describe()

Provides statistics for numeric columns.

df.describe()

Includes:

* count
* mean
* std
* min
* max
* quartiles

⸻

3. Column Selection

Single Column

df["Name"]

Returns:

Series

⸻

Multiple Columns

df[["Name", "Math"]]

Returns:

DataFrame

⸻

4. Series vs DataFrame

Series

One-dimensional structure.

df["Name"]

Output:

pandas.Series

⸻

DataFrame

Two-dimensional structure.

df[["Name"]]

Output:

pandas.DataFrame

⸻

5. iloc (Position-Based Selection)

Uses row and column positions.

Syntax:

df.iloc[row_position, column_position]

Example:

df.iloc[0, 1]

Returns:

Shubham

⸻

Row Selection

df.iloc[0]

First row

df.iloc[:5]

First 5 rows

df.iloc[2:6]

Rows:

2 3 4 5

End index excluded.

⸻

Multiple Rows and Columns

df.iloc[0:3, 1:3]

Rows:

0 1 2

Columns:

Name
Age

⸻

6. loc (Label-Based Selection)

Uses row labels and column names.

Syntax:

df.loc[row_label, column_name]

Example:

df.loc[0, "Name"]

Returns:

Shubham

⸻

Row Selection

df.loc[0:5]

Returns:

0 1 2 3 4 5

Important:

loc includes the ending label.

⸻

Column Selection

df.loc[:, "Math"]

All rows from Math column.

df.loc[:, ["Name", "Math"]]

All rows from Name and Math columns.

⸻

7. loc vs iloc

Feature	loc	iloc
Selection Type	Labels	Positions
Row Access	Label	Position
Column Access	Name	Index
End Included	Yes	No

Examples:

df.loc[0, "Math"]
df.iloc[0, 4]

Both may return the same value.

⸻

Key Takeaways

* Use read_csv() to load CSV files.
* Use head() and tail() to preview data.
* Use info() to inspect structure.
* Use describe() for statistics.
* Single column returns a Series.
* Multiple columns return a DataFrame.
* iloc uses positions.
* loc uses labels.
* loc includes ending index.
* iloc excludes ending index.
* Understanding selection is essential before filtering and data analysis.