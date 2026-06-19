"""
Day 10 - Pandas Cleaning, Missing Values and GroupBy

Concepts Covered:
- isnull()
- fillna()
- dropna()
- duplicated()
- drop_duplicates()
- groupby()
- agg()
- value_counts()
"""

import pandas as pd

# =====================================
# Load Dataset
# =====================================

df = pd.read_csv("messy_students.csv")

print("\n===== Original Dataset =====")
print(df)

# =====================================
# Dataset Information
# =====================================

print("\n===== Dataset Shape =====")
print(df.shape)

print("\n===== Dataset Info =====")
print(df.info())

print("\n===== Missing Values =====")
print(df.isnull().sum())

print("\n===== Total Missing Values =====")
print(df.isnull().sum().sum())

# =====================================
# Handle Missing Values
# =====================================

df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)

df["Math"] = df["Math"].fillna(
    df["Math"].mean()
)

df["Physics"] = df["Physics"].fillna(
    df["Physics"].mean()
)

df["Computer"] = df["Computer"].fillna(
    df["Computer"].mean()
)

# Remove rows with missing names
df = df.dropna(subset=["Name"])

# =====================================
# Duplicate Handling
# =====================================

print("\n===== Duplicate Rows =====")
print(df.duplicated().sum())

df = df.drop_duplicates()

# =====================================
# Feature Engineering
# =====================================

df["Total"] = (
    df["Math"]
    + df["Physics"]
    + df["Computer"]
)

df["Average"] = round(
    df["Total"] / 3,
    2
)

# =====================================
# Value Counts
# =====================================

print("\n===== Students Per Class =====")
print(df["Class"].value_counts())

# =====================================
# GroupBy Operations
# =====================================

print("\n===== Number of Students Per Class =====")
print(df.groupby("Class").size())

print("\n===== Average Total Per Class =====")
print(
    df.groupby("Class")["Total"].mean()
)

# =====================================
# Aggregation
# =====================================

summary = df.groupby("Class").agg({
    "Math": "mean",
    "Physics": "mean",
    "Computer": "mean",
    "Total": ["mean", "max", "min"]
})

print("\n===== Aggregated Summary =====")
print(summary)

# =====================================
# Class Summary Report
# =====================================

class_summary = (
    df.groupby("Class")
    .agg(
        Student_Count=("Name", "count"),
        Average_Total=("Total", "mean"),
        Highest_Total=("Total", "max"),
        Lowest_Total=("Total", "min")
    )
)

print("\n===== Class Summary =====")
print(class_summary)

# =====================================
# Gender Analysis (Stretch Goal)
# =====================================

gender_summary = (
    df.groupby("Gender")["Total"]
    .mean()
)

print("\n===== Gender Wise Average =====")
print(gender_summary)

# =====================================
# Export Files
# =====================================

df.to_csv(
    "cleaned_students.csv",
    index=False
)

class_summary.to_csv(
    "class_summary.csv"
)

print("\nFiles exported successfully.")