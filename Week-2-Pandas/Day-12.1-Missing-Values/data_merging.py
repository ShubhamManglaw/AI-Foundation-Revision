import pandas as pd

students = pd.read_csv("/Users/shubhammanglaw/Desktop/AI-Foundation-Revision/Week-2-Pandas/Day-12-Missing-Values/students.csv")
marks = pd.read_csv("/Users/shubhammanglaw/Desktop/AI-Foundation-Revision/Week-2-Pandas/Day-12-Missing-Values/marks.csv")
attendance = pd.read_csv("/Users/shubhammanglaw/Desktop/AI-Foundation-Revision/Week-2-Pandas/Day-12-Missing-Values/attendance.csv")

master = pd.merge(students, marks, on="Student_ID")
master = pd.merge(master, attendance, on="Student_ID")
master["Total"] = (
    master["Math"]
    + master["Physics"]
    + master["Computer"]
)
master["Average"] = master["Total"] / 3
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"

master["Grade"] = master["Average"].apply(grade)
master.to_csv(
    "/Users/shubhammanglaw/Desktop/AI-Foundation-Revision/Week-2-Pandas/Day-12-Missing-Values/school_master_dataset.csv",
    index=False
)