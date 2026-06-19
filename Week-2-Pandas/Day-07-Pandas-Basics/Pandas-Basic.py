"""
Day 7 - Pandas Basics
Topics:
1. Series
2. DataFrame
3. DataFrame Inspection
4. CSV Export
5. Mini Product Challenge
"""

import pandas as pd

# ==================================================
# 1. SERIES
# ==================================================

print("\n===== SERIES EXAMPLES =====\n")

student_names = pd.Series(
    ["Shubham", "Amit", "Rohit", "Priya", "Neha"]
)

student_marks = pd.Series(
    [85, 92, 78, 88, 95]
)

attendance = pd.Series(
    [95, 92, 88, 90, 97]
)

print("Student Names Series:")
print(student_names)

print("\nStudent Marks Series:")
print(student_marks)

print("\nAttendance Series:")
print(attendance)

# ==================================================
# 2. STUDENT DATAFRAME
# ==================================================

print("\n===== STUDENT DATAFRAME =====\n")

students_df = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105,
                   106, 107, 108, 109, 110],

    "Name": ["Shubham", "Amit", "Rohit", "Priya",
             "Neha", "Vikas", "Sonia", "Karan",
             "Anjali", "Deepak"],

    "Age": [16, 17, 16, 18, 17,
            16, 18, 17, 18, 16],

    "Class": ["11A", "11B", "11A", "12A", "11B",
              "12A", "12B", "11B", "12B", "11A"],

    "Math": [85, 92, 78, 88, 95,
             82, 74, 90, 86, 79],

    "Physics": [80, 88, 82, 91, 89,
                76, 84, 92, 85, 78],

    "Chemistry": [88, 90, 85, 89, 93,
                  80, 79, 94, 88, 84],

    "English": [90, 85, 92, 88, 82,
                91, 87, 95, 89, 84],

    "Computer": [92, 95, 88, 90, 96,
                 84, 88, 92, 90, 86]
})

print(students_df)

# ==================================================
# 3. DATAFRAME INSPECTION
# ==================================================

print("\n===== DATAFRAME INSPECTION =====\n")

print("HEAD:")
print(students_df.head())

print("\nTAIL:")
print(students_df.tail())

print("\nSHAPE:")
print(students_df.shape)

print("\nCOLUMNS:")
print(students_df.columns)

print("\nINDEX:")
print(students_df.index)

print("\nDATA TYPES:")
print(students_df.dtypes)

# ==================================================
# 4. EXPORT CSV
# ==================================================

students_df.to_csv(
    "students.csv",
    index=False
)

print("\nstudents.csv saved successfully!")

# ==================================================
# 5. PRODUCT DATAFRAME CHALLENGE
# ==================================================

print("\n===== PRODUCT DATAFRAME =====\n")

products_df = pd.DataFrame({
    "Product_ID": [1, 2, 3, 4, 5],

    "Product_Name": [
        "Laptop",
        "Mouse",
        "Keyboard",
        "Monitor",
        "Headphone"
    ],

    "Category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics"
    ],

    "Price": [
        50000,
        500,
        1500,
        12000,
        2000
    ],

    "Quantity": [
        10,
        50,
        20,
        15,
        30
    ]
})

products_df["Total_Value"] = (
    products_df["Price"]
    * products_df["Quantity"]
)

print(products_df)

products_df.to_csv(
    "products.csv",
    index=False
)

print("\nproducts.csv saved successfully!")

# ==================================================
# 6. EMPLOYEE DATAFRAME
# ==================================================

print("\n===== EMPLOYEE DATAFRAME =====\n")

employees_df = pd.DataFrame({
    "Emp_ID": [1, 2, 3, 4, 5],

    "Name": [
        "Amit",
        "Riya",
        "Karan",
        "Neha",
        "Vikas"
    ],

    "Salary": [
        50000,
        60000,
        55000,
        65000,
        70000
    ]
})

print(employees_df.head())
print(employees_df.tail())
print(employees_df.shape)
print(employees_df.columns)
print(employees_df.dtypes)

employees_df.to_csv(
    "employees.csv",
    index=False
)

print("\nemployees.csv saved successfully!")

print("\nDay 7 Completed Successfully!")