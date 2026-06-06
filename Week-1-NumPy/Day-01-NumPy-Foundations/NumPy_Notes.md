# NumPy Foundations Notes

## What is NumPy?

NumPy (Numerical Python) is a Python library used for numerical computing.

Benefits:

- Faster than Python lists
- Uses less memory
- Supports vectorized operations
- Widely used in AI, ML, Data Science, Computer Vision, and Robotics

---

# ndarray

The core data structure in NumPy is called an ndarray.

Example:

python import numpy as np  arr = np.array([1, 2, 3, 4]) 

Characteristics:

- Stores elements of the same datatype
- Supports fast mathematical operations
- Can be multi-dimensional

---

# Shape

Shape describes the dimensions of an array.

Example:

python arr = np.array([     [1, 2, 3],     [4, 5, 6] ])  print(arr.shape) 

Output:

python (2, 3) 

Meaning:

- 2 rows
- 3 columns

---

# Size

Size represents the total number of elements.

Example:

python arr = np.zeros((3, 4)) 

Shape:

python (3, 4) 

Size:

python 12 

Formula:

text size = rows × columns × ... 

---

# Shape vs Size

Shape:

python (3, 4) 

Tells dimensions.

Size:

python 12 

Tells total number of elements.

---

# ndim

ndim means Number of Dimensions.

Examples:

python [1,2,3] 

1D Array

python [[1,2],[3,4]] 

2D Array

python [[[1,2],[3,4]]] 

3D Array

Example:

python arr.ndim 

---

# dtype

dtype means Data Type.

Examples:

python int32 int64 float32 float64 

Check datatype:

python arr.dtype 

---

# Common Array Creation Functions

## np.array()

Creates arrays manually.

python np.array([1,2,3]) 

---

## np.zeros()

Creates arrays filled with zeros.

python np.zeros((3,3)) 

---

## np.ones()

Creates arrays filled with ones.

python np.ones((3,3)) 

---

## np.full()

Creates arrays filled with a chosen value.

python np.full((3,3), 7) 

---

## np.arange()

Creates values using a step size.

python np.arange(0, 10, 2) 

Output:

python [0 2 4 6 8] 

---

## np.linspace()

Creates evenly spaced values.

python np.linspace(0, 10, 5) 

Output:

python [0. 2.5 5. 7.5 10.] 

---

# arange vs linspace

arange:

python np.arange(start, stop, step) 

Uses step size.

Example:

python np.arange(0, 10, 2) 

Output:

python [0 2 4 6 8] 

linspace:

python np.linspace(start, stop, number_of_values) 

Uses number of values.

Example:

python np.linspace(0, 10, 5) 

Output:

python [0. 2.5 5. 7.5 10.] 

---

# Important Attributes

python arr.shape arr.size arr.ndim arr.dtype 

These four attributes are used constantly in Machine Learning and Computer Vision.

---

# Key Takeaways

- NumPy uses ndarray objects.
- shape gives dimensions.
- size gives total elements.
- ndim gives number of dimensions.
- dtype gives datatype.
- arange uses step size.
- linspace uses number of values.
- NumPy is faster and more memory efficient than Python lists.
```
:::

These are more than sufficient for a Day 1 GitHub commit and revision reference.