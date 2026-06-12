# Day 5 — NumPy Project: Student Marks Analyzer

## Objective

Build a menu-driven NumPy project that performs student performance analysis using arrays, statistics, boolean filtering, and axis operations.

---

# Concepts Used

## Arrays

python np.array() 

Store student marks, names, and subject names.

---

## Statistics

### Mean

python np.mean() 

Used for:

- Student averages
- Subject averages

### Sum

python np.sum() 

Used for:

- Total marks calculation

### Argmax

python np.argmax() 

Used to find:

- Highest scoring student
- Subject toppers

### Argmin

python np.argmin() 

Used to find:

- Lowest scoring student

---

# Axis Concept

## Student Analysis

python np.mean(marks, axis=1) 

Rows represent students.

Axis = 1 performs row-wise operations.

---

## Subject Analysis

python np.mean(marks, axis=0) 

Columns represent subjects.

Axis = 0 performs column-wise operations.

---

# Boolean Filtering

## Pass / Fail Detection

Passing rule:

python marks >= 40 

Check every subject:

python np.all(marks >= 40, axis=1) 

Returns:

python [True, False, True, False, True] 

---

# Features Implemented

- Show all marks
- Student averages
- Subject averages
- Highest scoring student
- Lowest scoring student
- Pass/Fail list
- Subject toppers
- Grade report
- Menu-driven interface

---

# Grade Rules

| Average | Grade |
|----------|--------|
| 90+ | A |
| 75–89 | B |
| 60–74 | C |
| 40–59 | D |
| Below 40 | F |

---

# Learning Outcomes

After completing this project I can:

- Work with 2D NumPy arrays
- Use axis correctly
- Perform statistical analysis
- Apply boolean masking
- Use argmax and argmin
- Build menu-driven Python programs
- Organize code using functions

---

# Future Improvements

- Read marks from CSV files
- Add Pandas integration
- Export reports
- Create graphical dashboard
- Visualize performance using Matplotlib
```
:::

This is strong enough to close Day 5 and demonstrates all the concepts listed in your Notion requirements.ff