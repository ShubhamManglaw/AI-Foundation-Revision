
"""
Advanced Pandas Revision Script (AI/ML Focus)

Topics
1. Data Inspection
2. Selection & Filtering
3. Missing Values
4. Cleaning
5. Sorting
6. GroupBy
7. Pivot Tables
8. apply()
9. lambda
10. String Methods
11. Datetime
12. Feature Engineering
13. Export
"""

import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)

# ==========================================================
# SAMPLE DATA
# ==========================================================
students = pd.DataFrame({
    "Student":[" Alice ","Bob","Charlie","David","Eva"],
    "Class":["A","A","B","B","A"],
    "Gender":["F","M","M","M","F"],
    "Subject":["Math","Science","Math","Science","Math"],
    "Marks":[95,72,81,np.nan,90],
    "Email":[
        " ALICE@gmail.com ",
        "bob@yahoo.com",
        "CHARLIE@gmail.com",
        " david@outlook.com ",
        "eva@gmail.com"
    ],
    "Date":[
        "2025-01-15",
        "2025-02-20",
        "2025-03-05",
        "2025-04-10",
        "2025-05-01"
    ]
})

print("="*60)
print("ORIGINAL DATA")
print(students)

# ==========================================================
# DATA INSPECTION
# ==========================================================
print("\nINFO")
print(students.info())

print("\nDESCRIBE")
print(students.describe(include="all"))

print("\nSHAPE:", students.shape)
print("COLUMNS:", students.columns.tolist())

# ==========================================================
# SELECTION
# ==========================================================
print("\nFirst 3 rows")
print(students.head(3))

print("\nMarks Column")
print(students["Marks"])

print("\nloc Example")
print(students.loc[:,["Student","Marks"]])

# ==========================================================
# FILTERING
# ==========================================================
print("\nMarks >=80")
print(students[students["Marks"]>=80])

# ==========================================================
# MISSING VALUES
# ==========================================================
print("\nMissing Values")
print(students.isnull().sum())

students["Marks"]=students["Marks"].fillna(students["Marks"].mean())

# ==========================================================
# CLEANING
# ==========================================================
students["Student"]=students["Student"].str.strip().str.title()
students["Email"]=students["Email"].str.strip().str.lower()

students.rename(columns={"Marks":"Score"},inplace=True)

# ==========================================================
# SORTING
# ==========================================================
students.sort_values("Score",ascending=False,inplace=True)

# ==========================================================
# GROUPBY
# ==========================================================
print("\nAverage Score by Class")
print(students.groupby("Class")["Score"].mean())

# ==========================================================
# PIVOT TABLE
# ==========================================================
print("\nPivot Table")
pivot=students.pivot_table(
    values="Score",
    index="Class",
    columns="Subject",
    aggfunc="mean",
    fill_value=0,
    margins=True
)
print(pivot)

# ==========================================================
# APPLY
# ==========================================================
students["Result"]=students["Score"].apply(
    lambda x:"Pass" if x>=40 else "Fail"
)

def grade(score):
    if score>=90:
        return "A"
    elif score>=75:
        return "B"
    elif score>=60:
        return "C"
    return "D"

students["Grade"]=students["Score"].apply(grade)

# ==========================================================
# LAMBDA
# ==========================================================
students["Double"]=students["Score"].apply(lambda x:x*2)
students["Half"]=students["Score"].apply(lambda x:x/2)

students["Summary"]=students.apply(
    lambda row:f"{row['Student']} scored {row['Score']} ({row['Grade']})",
    axis=1
)

# ==========================================================
# STRING METHODS
# ==========================================================
students["Name_Length"]=students["Student"].str.len()
students["Is_Gmail"]=students["Email"].str.contains("gmail")
students["Username"]=students["Email"].str.split("@").str[0]

# ==========================================================
# DATETIME
# ==========================================================
students["Date"]=pd.to_datetime(students["Date"])

students["Year"]=students["Date"].dt.year
students["Month"]=students["Date"].dt.month_name()
students["Day"]=students["Date"].dt.day
students["Weekday"]=students["Date"].dt.day_name()
students["Quarter"]=students["Date"].dt.quarter

# ==========================================================
# FEATURE ENGINEERING
# ==========================================================
students["Eligible"]=students["Score"].apply(
    lambda x:1 if x>=75 else 0
)

students["Performance"]=students["Score"].apply(
    lambda x:
    "Excellent" if x>=90
    else "Good" if x>=75
    else "Average"
)

# ==========================================================
# EXPORT
# ==========================================================
students.to_csv("students_clean.csv",index=False)

print("\nFINAL DATA")
print(students)

print("\nExported: students_clean.csv")

print("""
================ AI/ML CHEAT SHEET ================

Inspection:
head() tail() info() describe()

Cleaning:
fillna()
dropna()
drop_duplicates()
rename()

Grouping:
groupby()
pivot_table()

Transformation:
apply()
lambda

Strings:
str.lower()
str.strip()
str.contains()

Datetime:
pd.to_datetime()
dt.year
dt.month
dt.day_name()

Export:
to_csv()
===================================================
""")
