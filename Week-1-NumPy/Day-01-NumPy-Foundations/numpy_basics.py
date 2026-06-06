import numpy as np

print("=" * 50)
print("NUMPY FOUNDATIONS")
print("=" * 50)

# --------------------------------------------------
# 1D ARRAY
# --------------------------------------------------
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("\n1D ARRAY")
print(arr1)
print("Shape:", arr1.shape)
print("Dimensions:", arr1.ndim)
print("Data Type:", arr1.dtype)
print("Size:", arr1.size)

# --------------------------------------------------
# 2D ARRAY
# --------------------------------------------------
arr2 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("\n2D ARRAY")
print(arr2)
print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Data Type:", arr2.dtype)
print("Size:", arr2.size)

# --------------------------------------------------
# 3D ARRAY
# --------------------------------------------------
arr3 = np.arange(24).reshape(2, 3, 4)

print("\n3D ARRAY")
print(arr3)
print("Shape:", arr3.shape)
print("Dimensions:", arr3.ndim)
print("Data Type:", arr3.dtype)
print("Size:", arr3.size)

# --------------------------------------------------
# ZEROS MATRIX
# --------------------------------------------------
zeros_matrix = np.zeros((5, 5))

print("\n5x5 ZEROS MATRIX")
print(zeros_matrix)

# --------------------------------------------------
# ONES MATRIX
# --------------------------------------------------
ones_matrix = np.ones((4, 4))

print("\n4x4 ONES MATRIX")
print(ones_matrix)

# --------------------------------------------------
# FULL MATRIX
# --------------------------------------------------
full_matrix = np.full((3, 3), 7)

print("\n3x3 FULL MATRIX")
print(full_matrix)

# --------------------------------------------------
# ARANGE
# --------------------------------------------------
arange_array = np.arange(1, 51)

print("\nARANGE ARRAY")
print(arange_array)

# --------------------------------------------------
# LINSPACE
# --------------------------------------------------
linspace_array = np.linspace(0, 1, 20)

print("\nLINSPACE ARRAY")
print(linspace_array)

# --------------------------------------------------
# MINI CHALLENGE
# --------------------------------------------------
student_marks = np.array([78, 85, 92, 67, 55])

print("\nSTUDENT MARKS")
print(student_marks)

print("Highest Mark:", student_marks.max())
print("Lowest Mark:", student_marks.min())
print("Total Marks:", student_marks.sum())
print("Average Marks:", student_marks.mean())

# --------------------------------------------------
# STRETCH GOAL
# --------------------------------------------------
zeros_10 = np.zeros((10, 10))
ones_10 = np.ones((10, 10))
random_matrix = np.random.randint(1, 101, (10, 10))

print("\n10x10 RANDOM INTEGER MATRIX")
print(random_matrix)

print("\nPROGRAM COMPLETED SUCCESSFULLY")