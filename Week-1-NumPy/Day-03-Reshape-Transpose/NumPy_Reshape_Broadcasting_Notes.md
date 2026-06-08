# NumPy Reshape, Flatten, Ravel and Broadcasting Notes

## What is Reshape?

Reshape changes the structure (shape) of an array without changing its data.

Example:

python import numpy as np  arr = np.arange(1, 13)  arr.reshape(3, 4) 

Output:

python [[ 1  2  3  4]  [ 5  6  7  8]  [ 9 10 11 12]] 

Important:

text Reshape changes layout, not values. 

---

# Reshape Rule

The total number of elements must remain the same.

Formula:

text rows × columns = total elements 

Example:

python arr = np.arange(1, 13) 

Contains:

text 12 elements 

Valid reshapes:

python arr.reshape(2, 6) arr.reshape(3, 4) arr.reshape(4, 3) arr.reshape(6, 2) arr.reshape(12, 1) arr.reshape(1, 12) 

Because:

text 2 × 6 = 12 3 × 4 = 12 4 × 3 = 12 6 × 2 = 12 12 × 1 = 12 1 × 12 = 12 

Invalid:

python arr.reshape(3, 5) 

Because:

text 3 × 5 = 15  15 ≠ 12 

NumPy raises an error.

---

# Automatic Dimension Inference (-1)

NumPy can automatically calculate one dimension.

Example:

python arr.reshape(-1, 3) 

Meaning:

text I want 3 columns. NumPy calculates rows. 

Output:

python [[ 1  2  3]  [ 4  5  6]  [ 7  8  9]  [10 11 12]] 

Shape:

python (4, 3) 

---

Example:

python arr.reshape(2, -1) 

Output:

python [[ 1  2  3  4  5  6]  [ 7  8  9 10 11 12]] 

Shape:

python (2, 6) 

---

# Flatten

Flatten converts a multi-dimensional array into a 1D array.

Example:

python matrix = arr.reshape(3, 4)  flat = matrix.flatten() 

Output:

python [ 1  2  3  4  5  6  7  8  9 10 11 12] 

---

# Important Property of Flatten

python flatten() 

returns a:

text COPY 

Example:

python flat = matrix.flatten()  flat[0] = 999 

Result:

python flat 

python [999   2   3   4   5   6   7   8   9  10  11  12] 

Original matrix:

python [[ 1  2  3  4]  [ 5  6  7  8]  [ 9 10 11 12]] 

Matrix remains unchanged.

---

# Ravel

Ravel also converts arrays into 1D arrays.

Example:

python r = matrix.ravel() 

Output:

python [ 1  2  3  4  5  6  7  8  9 10 11 12] 

---

# Important Property of Ravel

python ravel() 

returns:

text VIEW (whenever possible) 

Example:

python r = matrix.ravel()  r[0] = 999 

Result:

python matrix 

python [[999   2   3   4]  [  5   6   7   8]  [  9  10  11  12]] 

The original matrix changes because ravel usually shares memory.

---

# Flatten vs Ravel

| Feature | flatten() | ravel() |
|----------|----------|----------|
| Returns | Copy | View (if possible) |
| Memory Usage | More | Less |
| Original Array Changes | No | Usually Yes |
| Speed | Slightly Slower | Slightly Faster |

Interview Answer:

text flatten() returns a copy  ravel() returns a view whenever possible 

---

# What is Broadcasting?

Broadcasting allows NumPy to perform operations on arrays of different shapes without writing loops.

Example:

python marks = np.array([45, 55, 65, 75, 85])  marks + 5 

Output:

python [50 60 70 80 90] 

No loop required.

---

# Common Broadcasting Operations

Add:

python marks + 5 

Multiply:

python marks * 2 

Divide:

python marks / 100 

Comparison:

python marks > 60 

Output:

python [False False True True True] 

---

# Broadcasting Mental Model

When NumPy sees:

python marks + 5 

Think:

python marks + [5, 5, 5, 5, 5] 

NumPy behaves this way internally without actually creating the extra array.

---

# 2D Broadcasting

Example:

python scores = np.array([     [70, 80, 90],     [60, 75, 85],     [90, 95, 100] ])  bonus = np.array([5, 10, 2])  scores + bonus 

NumPy treats:

python [5, 10, 2] 

as:

python [  [5,10,2],  [5,10,2],  [5,10,2] ] 

Output:

python [[ 75  90  92]  [ 65  85  87]  [ 95 105 102]] 

---

# Why Broadcasting is Important

Without broadcasting:

python for row in scores:     ... 

With broadcasting:

python scores + bonus 

Cleaner, faster, and more readable.

---

# Common Broadcasting Error

Example:

python scores.shape 

python (3, 4) 

and

python bonus.shape 

python (3,) 

Sometimes dimensions cannot align.

Example:

python scores + np.array([1, 2]) 

Error:

text operands could not be broadcast together 

Reason:

text Shapes are incompatible. 

---

# Stretch Goal: Normalization

Normalization scales values into a fixed range.

Example:

python normalized = (     (matrix - matrix.min())     /     (matrix.max() - matrix.min()) ) 

Output Range:

text 0 → 1 

Widely used in:

- Machine Learning
- Deep Learning
- Computer Vision
- Robotics Perception

---

# Key Takeaways

- Reshape changes structure, not values.
- Total elements must remain constant.
- -1 lets NumPy calculate one dimension automatically.
- flatten() returns a copy.
- ravel() returns a view whenever possible.
- Broadcasting removes the need for many loops.
- Broadcasting works by expanding dimensions automatically.
- Shape compatibility is required for broadcasting.
- Normalization is commonly used before feeding data into ML models.