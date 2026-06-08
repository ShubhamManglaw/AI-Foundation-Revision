import numpy as np

# ==================================================
# RESHAPE
# ==================================================

arr = np.arange(1, 13)

reshape_2x6 = arr.reshape(2, 6)
reshape_3x4 = arr.reshape(3, 4)
reshape_4x3 = arr.reshape(4, 3)
reshape_6x2 = arr.reshape(6, 2)
reshape_12x1 = arr.reshape(12, 1)
reshape_1x12 = arr.reshape(1, 12)

reshape_neg1_3 = arr.reshape(-1, 3)
reshape_2_neg1 = arr.reshape(2, -1)

# print(reshape_2x6)
# print(reshape_3x4)
# print(reshape_4x3)
# print(reshape_6x2)
# print(reshape_12x1)
# print(reshape_1x12)
# print(reshape_neg1_3)
# print(reshape_2_neg1)


# ==================================================
# FLATTEN
# ==================================================

matrix = arr.reshape(3, 4)

flatten_array = matrix.flatten()

flatten_array[0] = 999

flatten_modified = flatten_array
flatten_original_matrix = matrix

# print(flatten_modified)
# print(flatten_original_matrix)


# ==================================================
# RAVEL
# ==================================================

matrix2 = arr.reshape(3, 4)

ravel_array = matrix2.ravel()

ravel_array[0] = 999

ravel_modified = ravel_array
ravel_original_matrix = matrix2

# print(ravel_modified)
# print(ravel_original_matrix)


# ==================================================
# BASIC BROADCASTING
# ==================================================

marks = np.array([45, 55, 65, 75, 85])

bonus_marks = marks + 5
double_marks = marks * 2
percentage_marks = marks / 100
marks_above_60 = marks > 60

# print(bonus_marks)
# print(double_marks)
# print(percentage_marks)
# print(marks_above_60)


# ==================================================
# 2D BROADCASTING
# ==================================================

scores = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 100]
])

bonus = np.array([5, 10, 2])

updated_scores = scores + bonus

# print(updated_scores)


# ==================================================
# MINI CHALLENGE
# ==================================================

student_marks = np.array([
    [70, 80, 90, 60],
    [65, 75, 85, 95],
    [90, 88, 92, 94],
    [55, 60, 65, 70],
    [85, 90, 80, 75]
])

grace_marks = student_marks + 5

subject_bonus = np.array([5, 2, 3, 4])

updated_marks = grace_marks + subject_bonus

percentage = updated_marks / 100

total_marks = np.sum(updated_marks, axis=1)

subject_average = np.mean(updated_marks, axis=0)

topper_index = np.argmax(total_marks)

topper_total = total_marks[topper_index]

# print(grace_marks)
# print(updated_marks)
# print(percentage)
# print(total_marks)
# print(subject_average)
# print(topper_index)
# print(topper_total)


# ==================================================
# STRETCH GOAL
# ==================================================

random_matrix = np.random.randint(0, 100, (4, 4))

normalized_matrix = (
    (random_matrix - random_matrix.min())
    /
    (random_matrix.max() - random_matrix.min())
)

# print(random_matrix)
# print(normalized_matrix)


