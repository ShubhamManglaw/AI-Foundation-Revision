# day4_numpy_statistics_filtering.py

import numpy as np

# ==================================================
# DATASET 1: 1D ARRAY
# ==================================================

marks = np.array([80, 45, 65, 92, 55, 70, 30, 99])

print("\n===== BASIC STATISTICS =====")
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Std Dev:", np.std(marks))
print("Max:", np.max(marks))
print("Min:", np.min(marks))
print("Argmax:", np.argmax(marks))
print("Argmin:", np.argmin(marks))
print("Total:", np.sum(marks))

# ==================================================
# BOOLEAN FILTERING
# ==================================================

print("\n===== BOOLEAN FILTERING =====")
print("Marks > 70:", marks[marks > 70])
print("Marks < 50:", marks[marks < 50])
print("Marks >= 60:", marks[marks >= 60])
print("Even Marks:", marks[marks % 2 == 0])
print("Odd Marks:", marks[marks % 2 == 1])

# ==================================================
# COUNTING WITH MASKS
# ==================================================

print("\n===== COUNTING =====")
print("Students > 70:", np.sum(marks > 70))
print("Students Failed (<40):", np.sum(marks < 40))
print("Marks Between 50 and 80:",
      np.sum((marks >= 50) & (marks <= 80)))

# ==================================================
# DATASET 2: 2D ARRAY
# Rows -> Students
# Columns -> Subjects
# ==================================================

student_marks = np.array([
    [80, 75, 90, 85],
    [60, 55, 70, 65],
    [95, 90, 92, 88],
    [40, 45, 50, 35],
    [78, 82, 80, 76]
])

print("\n===== STUDENT MARKS MATRIX =====")
print(student_marks)

# ==================================================
# AXIS REVISION
# axis=0 -> Columns (Subjects)
# axis=1 -> Rows (Students)
# ==================================================

student_totals = np.sum(student_marks, axis=1)
student_avg = np.mean(student_marks, axis=1)

subject_avg = np.mean(student_marks, axis=0)
subject_max = np.max(student_marks, axis=0)
subject_min = np.min(student_marks, axis=0)

print("\n===== STUDENT ANALYSIS =====")
print("Student Totals:", student_totals)
print("Student Average:", student_avg)

print("\n===== SUBJECT ANALYSIS =====")
print("Subject Average:", subject_avg)
print("Subject Highest:", subject_max)
print("Subject Lowest:", subject_min)

# ==================================================
# TOPPER ANALYSIS
# ==================================================

topper_index = np.argmax(student_totals)
lowest_student_index = np.argmin(student_totals)

print("\n===== RANKING =====")
print("Topper Index:", topper_index)
print("Lowest Student Index:", lowest_student_index)

# ==================================================
# PASS / FAIL ANALYSIS
# Pass Mark = 40
# ==================================================

pass_students = np.where(
    np.all(student_marks >= 40, axis=1)
)[0]

fail_students = np.where(
    np.any(student_marks < 40, axis=1)
)[0]

failed_subject_count = np.sum(
    student_marks < 40,
    axis=1
)

print("\n===== PASS / FAIL =====")
print("Pass Students:", pass_students)
print("Fail Students:", fail_students)
print("Failed Subject Count:", failed_subject_count)

# ==================================================
# MINI RESULT ANALYZER
# ==================================================

class_average = np.mean(student_marks)

print("\n===== RESULT ANALYZER =====")
print("Class Average:", class_average)
print("Subject Averages:", subject_avg)
print("Topper Index:", topper_index)
print("Pass Students:", pass_students)
print("Fail Students:", fail_students)