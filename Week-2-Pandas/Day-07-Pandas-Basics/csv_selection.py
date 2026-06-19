import pandas as pd

# =========================
# Load CSV Files
# =========================

students = pd.read_csv("students.csv")
products = pd.read_csv("products.csv")

# =========================
# Dataset Inspection
# =========================

print("\n===== STUDENTS DATASET =====\n")

print("First 5 Rows:")
print(students.head())

print("\nLast 5 Rows:")
print(students.tail())

print("\nShape:")
print(students.shape)

print("\nSize:")
print(students.size)

print("\nDimensions:")
print(students.ndim)

print("\nColumns:")
print(students.columns.tolist())

print("\nDataset Info:")
students.info()

print("\nStatistics:")
print(students.describe())

# =========================
# Column Selection
# =========================

print("\n===== COLUMN SELECTION =====\n")

print("Student Names:")
print(students["Name"])

print("\nNames and Math Marks:")
print(students[["Name", "Math"]])

print("\nName, Math and Computer:")
print(students[["Name", "Math", "Computer"]])

# =========================
# Row Selection using iloc
# =========================

print("\n===== ILOC PRACTICE =====\n")

print("First Row:")
print(students.iloc[0])

print("\nFirst 5 Rows:")
print(students.iloc[:5])

print("\nRows 2 to 5:")
print(students.iloc[2:6])

# =========================
# Value Selection using iloc
# =========================

print("\n===== SINGLE VALUE USING ILOC =====\n")

print("Math Marks of First Student:")
print(students.iloc[0, 4])

print("\nPhysics Marks of Third Student:")
print(students.iloc[2, 5])

# =========================
# loc Practice
# =========================

print("\n===== LOC PRACTICE =====\n")

print("Student Name at Index 0:")
print(students.loc[0, "Name"])

print("\nMath Marks at Index 0:")
print(students.loc[0, "Math"])

print("\nPhysics Marks at Index 2:")
print(students.loc[2, "Physics"])

print("\nRows 0 to 5 (loc includes end index):")
print(students.loc[0:5, ["Name", "Math"]])

print("\nAll Student Names:")
print(students.loc[:, "Name"])

print("\nAll Names and Math Marks:")
print(students.loc[:, ["Name", "Math"]])

# =========================
# Products Mini Challenge
# =========================

print("\n===== PRODUCTS MINI CHALLENGE =====\n")

print("Product Names:")
print(products["Product_Name"])

print("\nProduct Names and Prices:")
print(products[["Product_Name", "Price"]])

print("\nFirst 5 Products:")
print(products.head())

print("\nRows 1 to 3:")
print(products.iloc[1:4])

print("\nCategory and Quantity:")
print(products[["Category", "Quantity"]])

print("\nPrice of Product at Index 2:")
print(products.loc[2, "Price"])

print("\nTotal Value of Product at Index 4:")
print(products.loc[4, "Total_Value"])

print("\n===== DAY 8 COMPLETED =====")