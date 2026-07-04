# Day 11 - Pandas Data Manipulation

## Objective

Learn how to modify the structure of a DataFrame using Pandas.

Topics covered:

- rename()
- drop()
- insert()
- set_index()
- reset_index()
- reindex()

---

# 1. Rename Columns

Rename one or multiple columns.

```python
df = df.rename(columns={
    "Name": "Student_Name",
    "Computer": "Computer_Science"
})
```

---

# 2. Drop Rows and Columns

Drop columns

```python
df = df.drop(columns=["Age"])
```

Drop multiple columns

```python
df = df.drop(columns=["Age", "Class"])
```

Drop rows

```python
df = df.drop(index=0)
```

---

# 3. Insert Columns

Insert a constant column

```python
df.insert(len(df.columns), "Bonus_Marks", 5)
```

Insert at a specific position

```python
df.insert(7, "Grade", "")
```

---

# 4. Create Calculated Columns

```python
df["Total"] = df["Math"] + df["Physics"] + df["Computer"]
```

---

# 5. Reorder Columns

```python
cols = [
    "Student_ID",
    "Name",
    "Math",
    "Physics",
    "Computer",
    "Average"
]

df = df[cols]
```

---

# 6. Set Index

```python
df = df.set_index("Student_ID")
```

Benefits

- Faster lookup
- Cleaner reports
- Better joins

---

# 7. Reset Index

```python
df = df.reset_index()
```

Restores the default integer index.

---

# 8. Custom Index

```python
df.index = [f"S{i}" for i in range(1, len(df)+1)]
```

Output

```
S1
S2
S3
...
```

---

# 9. Reindex

Reverse rows

```python
df = df.reindex(df.index[::-1])
```

Add new labels

```python
df = df.reindex(list(df.index) + ["X1", "X2"])
```

Missing labels produce NaN rows.

---

# 10. Save CSV

```python
df.to_csv("student_report.csv", index=False)
```

---

# Common Methods

| Method | Purpose |
|--------|---------|
| rename() | Rename columns |
| drop() | Remove rows/columns |
| insert() | Add a new column |
| set_index() | Set an index |
| reset_index() | Restore default index |
| reindex() | Reorder/add labels |
| to_csv() | Export DataFrame |

---

# Best Practices

- Keep original column names meaningful.
- Create a backup before modifying data.

```python
backup = df.copy()
```

- Use `set_index()` only when a column uniquely identifies each row.
- Export cleaned datasets instead of overwriting raw data.

---

# Key Takeaways

- `rename()` changes column names.
- `drop()` removes rows or columns.
- `insert()` adds new columns.
- `set_index()` changes row labels.
- `reset_index()` restores default indexing.
- `reindex()` changes row order or adds new labels.
- Always save cleaned datasets separately.

---

# Revision Checklist

- [x] Rename columns
- [x] Drop rows
- [x] Drop columns
- [x] Insert columns
- [x] Reorder columns
- [x] Set index
- [x] Reset index
- [x] Reindex DataFrame
- [x] Export CSV
- [x] Complete practice questions