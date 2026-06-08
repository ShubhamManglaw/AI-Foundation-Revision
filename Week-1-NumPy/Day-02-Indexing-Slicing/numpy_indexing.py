# Section 1: 1D Indexing
import numpy as np
arr=np.array([10,20,30,40,50,60,70,80])
# print(arr[0],arr[3],arr[-1],arr[-2],arr[-5])
#  Output = 10 40 80 70 40


# Section 2: 1D Slicing
# print(arr[1:5],arr[:4],arr[3:],arr[:],arr[::2],arr[1::2],arr[::-1])
# Output = [20 30 40 50] [10 20 30 40] [40 50 60 70 80] [10 20 30 40 50 60 70 80] [10 30 50 70] [20 40 60 80] [80 70 60 50 40 30 20 10]


# Section 3: 2D Indexing
matrix = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ])
# print(matrix[0,0],matrix[1,1],matrix[2,2],matrix[1,3],matrix[-1,-1])
# Output = [20 30 40 50] [10 20 30 40] [40 50 60 70 80] [10 20 30 40 50 60 70 80] [10 30 50 70] [20 40 60 80] [80 70 60 50 40 30 20 10] 1 6 11 8 12


# Section 4: Row Extraction
# print(matrix[1])
# print(matrix[1,:])
# Output = [5 6 7 8] [5 6 7 8]

# Section 5: Column Extraction
# print(matrix[:,1])
# print(matrix[:,-1])
# Output = [ 2  6 10] [ 4  8 12]

# # Note = matrix[1] is row and matrix[:,1] is colum


# Section 6: Submatrices
# print(matrix[:,1:3])
# """
#     [[ 2  3]
#     [ 6  7]
#     [10 11]]
# """
# print(matrix[:2,1:3])
# """[[2 3]
#      [6 7]]"""

# # Section 7: Reverse Operations
# print(matrix[:,::-1])
# """[[ 4  3  2  1]
#     [ 8  7  6  5]
#     [12 11 10  9]]"""
# print(matrix[::-1,::-1])
# """[[12 11 10  9]
#     [ 8  7  6  5]
#     [ 4  3  2  1]]"""






########## Mini Challenge
marks = np.array([
    [80,75,90],
    [65,70,72],
    [95,92,96]
])
First_student_marks = marks[0]
Second_student_marks = marks[1]
Third_student_science_mark=marks[2,1]
All_maths_marks = marks[:,0]
All_science_marks=marks[:,1]
First_two_students=marks[0:2]
Last_two_students=marks[-2:]
Highest_mark=np.max(marks)
Lowest_mark=np.min(marks)
Average_mark=int(np.average(marks))
print(Average_mark)

image = np.random.randint(
    0,
    256,
    (5,5)
)
Top_row=image[0]
Bottom_row=image[-1]
Left_column=image[:,0]
Right_column=image[:,-1]
Center_pixel=image[2,2]
Center_3x3_crop=image[1:4,1:4]
Reverse_image_vertically=image[::-1,:]
Reverse_image_horizontally=image[:,::-1]
# print(image)
# print(Reverse_image_horizontally)
print(arr[1:5:2])
print(matrix[1:, :-1])
print(matrix[:, ::-1])
