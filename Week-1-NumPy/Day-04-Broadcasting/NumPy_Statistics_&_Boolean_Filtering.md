# Day 4 — NumPy Statistics & Boolean Filtering

## 1. Basic Statistics

### Mean
python np.mean(arr) 

Average value of all elements.

---

### Median
python np.median(arr) 

Middle value after sorting.

---

### Standard Deviation
python np.std(arr) 

Measures spread of data.

---

### Maximum / Minimum
python np.max(arr) np.min(arr) 

Returns largest and smallest values.

---

### Argmax / Argmin
python np.argmax(arr) np.argmin(arr) 

Returns index of largest/smallest value.

Example:

python arr = np.array([80, 45, 65, 92])  np.max(arr)      # 92 np.argmax(arr)   # 3 

---

### Sum
python np.sum(arr) 

Returns total of all elements.

---

# 2. Boolean Masks

A boolean mask is an array of True/False values.

Example:

python arr = np.array([80, 45, 65, 92])  arr > 70 

Output:

python [ True False False True ] 

---

# 3. Filtering

### Values Greater Than 70

python arr[arr > 70] 

---

### Values Less Than 50

python arr[arr < 50] 

---

### Even Numbers

python arr[arr % 2 == 0] 

---

### Odd Numbers

python arr[arr % 2 == 1] 

---

### Multiple Conditions

python arr[(arr >= 50) & (arr <= 80)] 

Use:

python & | ~ 

instead of:

python and or not 

for NumPy arrays.

---

# 4. Counting Using Masks

Count students scoring above 70:

python np.sum(arr > 70) 

Because:

python True  = 1 False = 0 

Example:

python arr > 70  [ True False False True ] 

Count:

python np.sum(arr > 70)  # 2 

---

# 5. Axis Concept (Most Important)

Assume:

python matrix = np.array([     [1,2,3],     [4,5,6] ]) 

Rows = Students

Columns = Subjects

---

## axis=0

Work vertically (column-wise)

python np.sum(matrix, axis=0) 

Output:

python [5 7 9] 

Calculation:

text 1+4 2+5 3+6 

---

## axis=1

Work horizontally (row-wise)

python np.sum(matrix, axis=1) 

Output:

python [6 15] 

Calculation:

text 1+2+3 4+5+6 

---

### Shortcut

text axis=0 → Columns axis=1 → Rows 

For Student Marks Matrix:

text axis=0 → Subject Analysis axis=1 → Student Analysis 

---

# 6. Student Analysis

### Total Marks Per Student

python np.sum(student_marks, axis=1) 

---

### Average Marks Per Student

python np.mean(student_marks, axis=1) 

---

### Subject Averages

python np.mean(student_marks, axis=0) 

---

### Subject Highest Marks

python np.max(student_marks, axis=0) 

---

### Subject Lowest Marks

python np.min(student_marks, axis=0) 

---

# 7. Ranking

### Topper

python totals = np.sum(student_marks, axis=1)  np.argmax(totals) 

---

### Lowest Scoring Student

python np.argmin(totals) 

---

# 8. np.all()

Checks if ALL values satisfy a condition.

Example:

python np.all(student_marks >= 40, axis=1) 

Output:

python [ True True True False True ] 

Meaning:

text Student 0 → Pass Student 1 → Pass Student 2 → Pass Student 3 → Fail Student 4 → Pass 

---

# 9. np.any()

Checks if ANY value satisfies a condition.

Example:

python np.any(student_marks < 40, axis=1) 

Output:

python [False False False True False] 

Meaning Student 3 failed at least one subject.

---

# 10. np.where()

Returns indices matching a condition.

Pass Students:

python np.where(     np.all(student_marks >= 40, axis=1) )[0] 

Output:

python [0 1 2 4] 

---

Fail Students:

python np.where(     np.any(student_marks < 40, axis=1) )[0] 

Output:

python [3] 

---

# 11. Failed Subject Count

Count failed subjects per student:

python np.sum(student_marks < 40, axis=1) 

Output:

python [0 0 0 1 0] 

---

# Revision Checklist

## Statistics
- [ ] mean
- [ ] median
- [ ] std
- [ ] max
- [ ] min
- [ ] argmax
- [ ] argmin
- [ ] sum

## Boolean Filtering
- [ ] >
- [ ] <
- [ ] >=
- [ ] &
- [ ] |

## Counting
- [ ] np.sum(mask)

## Axis
- [ ] axis=0
- [ ] axis=1

## Analysis
- [ ] np.all()
- [ ] np.any()
- [ ] np.where()

## Mini Project
- [ ] Student Result Analyzer