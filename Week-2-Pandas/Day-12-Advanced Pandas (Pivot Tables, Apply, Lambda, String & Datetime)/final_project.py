"""
===========================================================
Day 12 - Final Project
Sales & Customer Analytics using Pandas

Concepts Covered
----------------
✔ Read CSV
✔ Data Inspection
✔ Missing Values
✔ Remove Duplicates
✔ Rename Columns
✔ Datatype Conversion
✔ String Cleaning
✔ Datetime Features
✔ Feature Engineering
✔ apply()
✔ lambda
✔ GroupBy
✔ Pivot Tables
✔ Export Reports

Author: Shubham Manglaw
===========================================================
"""

import pandas as pd

# ==========================================================
# LOAD DATA
# ==========================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv("sales.csv")

# ==========================================================
# DATA INSPECTION
# ==========================================================

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns.tolist())

print("\nSummary Statistics")
print(df.describe(include="all"))

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# ==========================================================
# DATA CLEANING
# ==========================================================

print("\nCleaning Dataset...")

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df = df.fillna(0)

# Remove spaces from column names
df.columns = df.columns.str.strip()

# ==========================================================
# STRING CLEANING
# ==========================================================

if "Customer_Name" in df.columns:
    df["Customer_Name"] = (
        df["Customer_Name"]
        .astype(str)
        .str.strip()
        .str.title()
    )

if "Category" in df.columns:
    df["Category"] = (
        df["Category"]
        .astype(str)
        .str.strip()
        .str.title()
    )

if "Product" in df.columns:
    df["Product"] = (
        df["Product"]
        .astype(str)
        .str.strip()
        .str.title()
    )

if "City" in df.columns:
    df["City"] = (
        df["City"]
        .astype(str)
        .str.strip()
        .str.title()
    )

# ==========================================================
# DATETIME
# ==========================================================

if "Date" in df.columns:

    df["Date"] = pd.to_datetime(df["Date"])

    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month_name()
    df["Day"] = df["Date"].dt.day
    df["Weekday"] = df["Date"].dt.day_name()
    df["Quarter"] = df["Date"].dt.quarter

# ==========================================================
# FEATURE ENGINEERING
# ==========================================================

if {"Quantity", "Price"}.issubset(df.columns):

    df["Revenue"] = df["Quantity"] * df["Price"]

if "Revenue" in df.columns:

    df["Sales_Level"] = df["Revenue"].apply(
        lambda x:
        "High" if x >= 10000
        else "Medium" if x >= 5000
        else "Low"
    )

# ==========================================================
# GROUPBY ANALYSIS
# ==========================================================

print("\n" + "=" * 60)
print("GROUPBY ANALYSIS")
print("=" * 60)

if {"Category", "Revenue"}.issubset(df.columns):

    category_summary = (
        df.groupby("Category")["Revenue"]
        .agg(["sum", "mean", "max", "min", "count"])
        .round(2)
    )

    print("\nRevenue by Category")
    print(category_summary)

if {"City", "Revenue"}.issubset(df.columns):

    city_summary = (
        df.groupby("City")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nRevenue by City")
    print(city_summary)

# ==========================================================
# PIVOT TABLES
# ==========================================================

print("\n" + "=" * 60)
print("PIVOT TABLES")
print("=" * 60)

if {"Category", "Revenue"}.issubset(df.columns):

    pivot_category = pd.pivot_table(
        df,
        values="Revenue",
        index="Category",
        aggfunc="sum",
        margins=True,
    )

    print("\nRevenue by Category")
    print(pivot_category)

if {"Month", "Revenue"}.issubset(df.columns):

    pivot_month = pd.pivot_table(
        df,
        values="Revenue",
        index="Month",
        aggfunc="sum",
        fill_value=0,
    )

    print("\nMonthly Revenue")
    print(pivot_month)

if {"Category", "Month", "Revenue"}.issubset(df.columns):

    pivot_report = pd.pivot_table(
        df,
        values="Revenue",
        index="Category",
        columns="Month",
        aggfunc="sum",
        fill_value=0,
        margins=True,
    )

    print("\nCategory vs Month")
    print(pivot_report)

# ==========================================================
# TOP PRODUCTS
# ==========================================================

if {"Product", "Revenue"}.issubset(df.columns):

    print("\nTop Products")

    print(
        df.groupby("Product")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

# ==========================================================
# EXPORT REPORTS
# ==========================================================

print("\nSaving Files...")

df.to_csv("cleaned_sales.csv", index=False)

if "pivot_report" in locals():
    pivot_report.to_csv("summary_report.csv")

print("Files Saved Successfully!")

# ==========================================================
# FINAL DATASET
# ==========================================================

print("\nFinal Dataset Preview")
print(df.head())

print("\nFinal Shape:", df.shape)

# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

if "Revenue" in df.columns:
    print("Total Revenue :", df["Revenue"].sum())

if "Revenue" in df.columns:
    print("Average Revenue :", round(df["Revenue"].mean(), 2))

if "Sales_Level" in df.columns:
    print("\nSales Level Distribution")
    print(df["Sales_Level"].value_counts())

print("\nProject Completed Successfully!")
print("=" * 60)