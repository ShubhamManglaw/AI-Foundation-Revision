import pandas as pd
df = pd.read_csv("/Users/shubhammanglaw/Desktop/AI-Foundation-Revision/Week-2-Pandas/Day-11-Data-Manipulation/students.csv")
df1=df.rename(columns={
    "Name": "Student_Name",
    "Computer": "Computer_Science"
})
df2=df.drop(columns=["Age"])
df.drop(columns=["Age", "Class"])
df.insert(7, "Grade", "")


def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(grade)
df = df[
    [
        "Student_ID",
        "Student_Name",
        "Class",
        "Math",
        "Physics",
        "Computer_Science",
        "Average",
        "Grade",
        "Bonus_Marks",
    ]
]
df = df.set_index("Student_ID")
df = df.reset_index()
df = df.reset_index()
new_order = [
    "STU_5",
    "STU_2",
    "STU_8",
    "STU_1",
    "STU_3",
]

print(df.reindex(new_order))
df.to_csv("student_report.csv", index=True)