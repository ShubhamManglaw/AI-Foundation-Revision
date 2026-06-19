"""
Day 9 - Pandas Filtering, Sorting and Ranking
Dataset Columns:
Student_ID
Name
Class
Math
Physics
Computer
"""
import pandas as pd
# =====================================
# Load Dataset
# =====================================
df = pd.read_csv("students.csv")
print("\n===== Original Dataset =====")
print(df)
# =====================================
# Calculated Columns
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
df["Percentage"] = round(
    (df["Total"] / 300) * 100,
    2
)
# =====================================
# Single Condition Filtering
# =====================================
math_topper = df[df["Math"] > 80]
physics_topper = df[df["Physics"] > 75]
computer_topper = df[df["Computer"] > 90]
average_topper = df[df["Average"] > 75]
# =====================================
# Multiple Condition Filtering
# =====================================
high_performers = df[
    (df["Math"] > 80)
    & (df["Computer"] > 90)
]
# =====================================
# Class Filtering
# =====================================
class_a = df[df["Class"] == "A"]
class_b = df[df["Class"] == "B"]
class_a_b = df[
    (df["Class"] == "A")
    | (df["Class"] == "B")
]
# =====================================
# Pass / Fail Analysis
# =====================================
failed_students = df[
    (df["Math"] < 40)
    | (df["Physics"] < 40)
    | (df["Computer"] < 40)
]
passed_students = df[
    (df["Math"] >= 40)
    & (df["Physics"] >= 40)
    & (df["Computer"] >= 40)
]
# =====================================
# Sorting
# =====================================
sorted_by_average = df.sort_values(
    by="Average",
    ascending=False
)
sorted_by_total = df.sort_values(
    by="Total",
    ascending=False
)
sorted_by_math = df.sort_values(
    by="Math",
    ascending=False
)
sorted_by_computer = df.sort_values(
    by="Computer",
    ascending=False
)
sorted_by_name = df.sort_values(
    by="Name"
)
# =====================================
# Ranking
# =====================================
df["Total_Rank"] = (
    df["Total"]
    .rank(
        ascending=False,
        method="dense"
    )
    .astype(int)
)
df["Math_Rank"] = (
    df["Math"]
    .rank(
        ascending=False,
        method="dense"
    )
    .astype(int)
)
df["Computer_Rank"] = (
    df["Computer"]
    .rank(
        ascending=False,
        method="dense"
    )
    .astype(int)
)
# =====================================
# Top 3 Students
# =====================================
top_3_students = (
    df.sort_values(
        by="Total",
        ascending=False
    )
    .head(3)
)
# =====================================
# Display Results
# =====================================
print("\n===== Student Performance =====")
print(
    df[
        [
            "Name",
            "Total",
            "Average",
            "Percentage",
            "Total_Rank"
        ]
    ]
)
print("\n===== Top 3 Students =====")
print(
    top_3_students[
        [
            "Name",
            "Total",
            "Total_Rank"
        ]
    ]
)
print("\n===== Failed Students =====")
print(
    failed_students[
        [
            "Name",
            "Math",
            "Physics",
            "Computer"
        ]
    ]
)
# =====================================
# CSV Exports
# =====================================
top_students = df[
    df["Average"] > 80
]
top_students.to_csv(
    "top_students.csv",
    index=False
)
failed_students.to_csv(
    "failed_students.csv",
    index=False
)
class_a.to_csv(
    "class_A_students.csv",
    index=False
)
df.to_csv(
    "students_with_ranks.csv",
    index=False
)
print("\nCSV files exported successfully.")