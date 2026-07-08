import pandas as pd

# df1 = pd.DataFrame({
#     "Name": ["A", "B"]
# })

# df2 = pd.DataFrame({
#     "Name": ["C", "D"]
# })

# result = pd.concat([df1, df2])

# print(result)
# electronics = pd.DataFrame({
#     "Product": ["Laptop", "Mouse"],
#     "Price": [60000, 700]
# })

# accessories = pd.DataFrame({
#     "Product": ["Keyboard", "Headphone"],
#     "Price": [1200, 2500]
# })
# result = pd.concat([electronics,accessories])
# result = result.reset_index(drop=True)
# print(result)
# students = pd.DataFrame({
#     "Name": ["Shubham", "Amit", "Priya"]
# })

# ages = pd.DataFrame({
#     "Age": [21, 20, 22]
# })
# df=pd.concat([students,ages],axis=1)
# print(df)


# Merge
import pandas as pd

students = pd.DataFrame({
    "Student_ID":[101,102,103],
    "Name":["Shubham","Amit","Priya"]
})

marks = pd.DataFrame({
    "Student_ID":[101,102,103],
    "Math":[95,80,91]
})

merged = pd.merge(students, marks, on="Student_ID")
# print(merged)
# print(pd.merge(students, marks, on="Student_ID", how="inner"))
# print(pd.merge(students, marks, on="Student_ID", how="left"))
# print(pd.merge(students, marks, on="Student_ID", how="right"))
students = pd.DataFrame({
    "Name":["Shubham","Amit","Priya"]
})

marks = pd.DataFrame({
    "Math":[95,80,91]
})

new=students.join(marks)
print(new)
