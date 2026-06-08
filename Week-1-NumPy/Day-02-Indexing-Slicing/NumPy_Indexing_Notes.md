# NumPy Indexing and Slicing Notes

## What is Indexing?

Indexing is the process of accessing individual elements from a NumPy array.

Example:

python import numpy as np  arr = np.array([10, 20, 30, 40, 50])  print(arr[0]) 

Output:

python 10 

Indexing starts from 0.

text Index : 0  1  2  3  4 Value :10 20 30 40 50 

---

# Positive Indexing

Positive indexing starts from the beginning of the array.

Example:

python arr[0] 

Output:

python 10 

Example:

python arr[3] 

Output:

python 40 

---

# Negative Indexing

Negative indexing starts from the end of the array.

text Value :10 20 30 40 50 Index : 0  1  2  3  4  Index :-5 -4 -3 -2 -1 

Example:

python arr[-1] 

Output:

python 50 

Example:

python arr[-2] 

Output:

python 40 

Negative indexing is useful when accessing elements relative to the end of an array.

---

# What is Slicing?

Slicing extracts multiple elements from an array.

Syntax:

python arr[start:end] 

Rule:

text start -> included end   -> excluded 

Example:

python arr = np.array([10,20,30,40,50])  arr[1:4] 

Output:

python [20 30 40] 

Explanation:

text Index 1 included Index 4 excluded 

---

# Omitting Start or End

Beginning to a position:

python arr[:3] 

Output:

python [10 20 30] 

Position to end:

python arr[2:] 

Output:

python [30 40 50] 

Entire array:

python arr[:] 

Output:

python [10 20 30 40 50] 

---

# Step Parameter

Syntax:

python arr[start:end:step] 

The step controls how many positions NumPy jumps.

Example:

python arr = np.array([1,2,3,4,5,6,7,8])  arr[::2] 

Output:

python [1 3 5 7] 

Example:

python arr[1::2] 

Output:

python [2 4 6 8] 

---

# Reverse Slicing

A negative step reverses the array.

Example:

python arr[::-1] 

Output:

python [8 7 6 5 4 3 2 1] 

---

# 2D Indexing

For matrices, indexing follows:

python matrix[row, column] 

Example:

python matrix = np.array([     [1,2,3,4],     [5,6,7,8],     [9,10,11,12] ]) 

Visualization:

text       c0 c1 c2 c3  r0 -> 1  2  3  4 r1 -> 5  6  7  8 r2 -> 9 10 11 12 

Example:

python matrix[1,1] 

Output:

python 6 

Example:

python matrix[2,2] 

Output:

python 11 

---

# Row Extraction

To extract a row:

python matrix[row] 

or

python matrix[row, :] 

Example:

python matrix[1] 

Output:

python [5 6 7 8] 

Example:

python matrix[-1] 

Output:

python [ 9 10 11 12] 

---

# Column Extraction

To extract a column:

python matrix[:, column] 

Example:

python matrix[:,1] 

Output:

python [ 2  6 10] 

Example:

python matrix[:,-1] 

Output:

python [ 4  8 12] 

---

# Difference Between Row and Column Extraction

Row:

python matrix[1] 

Output:

python [5 6 7 8] 

Column:

python matrix[:,1] 

Output:

python [ 2  6 10] 

Remember:

text matrix[row] returns a row  matrix[:, column] returns a column 

---

# Submatrix Extraction

Extract part of a matrix using row and column slicing together.

Example:

python matrix[:,1:3] 

Output:

python [[ 2  3]  [ 6  7]  [10 11]] 

Example:

python matrix[:2,1:3] 

Output:

python [[2 3]  [6 7]] 

---

# Matrix Reversal

Reverse rows:

python matrix[::-1] 

Output:

python [[ 9 10 11 12]  [ 5  6  7  8]  [ 1  2  3  4]] 

Reverse columns:

python matrix[:,::-1] 

Output:

python [[ 4  3  2  1]  [ 8  7  6  5]  [12 11 10  9]] 

Reverse both:

python matrix[::-1,::-1] 

Output:

python [[12 11 10  9]  [ 8  7  6  5]  [ 4  3  2  1]] 

---

# Common Mistakes

## Mistake 1: Forgetting End is Excluded

python arr[1:4] 

Returns:

python [20 30 40] 

Not:

python [20 30 40 50] 

---

## Mistake 2: Confusing Rows and Columns

python matrix[1] 

Returns a row.

python matrix[:,1] 

Returns a column.

---

## Mistake 3: Incorrect Last Elements Slice

python marks[1:-1] 

Does NOT return the last two rows.

Correct:

python marks[-2:] 

---

# Key Takeaways

- Indexing starts at 0.
- Negative indexing starts from the end.
- Slicing follows start:end where end is excluded.
- Step controls jumps between elements.
- [::-1] reverses arrays.
- 2D indexing uses [row, column].
- matrix[row] extracts a row.
- matrix[:, column] extracts a column.
- Submatrices are extracted using row and column slicing together.
- Understanding indexing and slicing is essential for OpenCV, Computer Vision, and Robotics because images are stored as NumPy arrays.