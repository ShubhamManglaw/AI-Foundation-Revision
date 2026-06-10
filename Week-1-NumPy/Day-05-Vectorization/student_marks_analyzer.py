import numpy as np

# -----------------------------
# Dataset
# -----------------------------

marks = np.array([
    [78, 85, 90, 66, 74],
    [45, 55, 60, 39, 50],
    [88, 92, 81, 76, 95],
    [33, 40, 38, 45, 42],
    [70, 68, 75, 80, 72]
])

students = np.array([
    "Aman",
    "Riya",
    "Karan",
    "Neha",
    "Shubham"
])

subjects = np.array([
    "Math",
    "Physics",
    "Chemistry",
    "English",
    "CS"
])


# -----------------------------
# Functions
# -----------------------------

def show_all_marks():
    print("\nSTUDENT MARKS")
    print("-" * 50)

    for i in range(len(students)):
        print(f"{students[i]:10} : {marks[i]}")


def student_averages():
    averages = np.mean(marks, axis=1)

    print("\nAVERAGE MARKS PER STUDENT")
    print("-" * 50)

    for student, avg in zip(students, averages):
        print(f"{student:10} : {avg:.2f}")


def subject_averages():
    averages = np.mean(marks, axis=0)

    print("\nAVERAGE MARKS PER SUBJECT")
    print("-" * 50)

    for subject, avg in zip(subjects, averages):
        print(f"{subject:10} : {avg:.2f}")


def highest_student():
    totals = np.sum(marks, axis=1)

    topper_index = np.argmax(totals)

    print("\nHIGHEST SCORING STUDENT")
    print("-" * 50)

    print(f"Student : {students[topper_index]}")
    print(f"Total   : {totals[topper_index]}")


def lowest_student():
    totals = np.sum(marks, axis=1)

    lowest_index = np.argmin(totals)

    print("\nLOWEST SCORING STUDENT")
    print("-" * 50)

    print(f"Student : {students[lowest_index]}")
    print(f"Total   : {totals[lowest_index]}")


def pass_fail_list():
    results = np.all(marks >= 40, axis=1)

    print("\nPASS / FAIL LIST")
    print("-" * 50)

    for student, result in zip(students, results):
        status = "PASS" if result else "FAIL"
        print(f"{student:10} : {status}")


def subject_toppers():
    print("\nSUBJECT TOPPERS")
    print("-" * 50)

    topper_indices = np.argmax(marks, axis=0)

    for subject, idx in zip(subjects, topper_indices):
        print(
            f"{subject:10} : "
            f"{students[idx]} ({marks[idx, np.where(subjects == subject)[0][0]]})"
        )


def grade_calculator():
    averages = np.mean(marks, axis=1)

    print("\nGRADE REPORT")
    print("-" * 50)

    for student, avg in zip(students, averages):

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        elif avg >= 40:
            grade = "D"
        else:
            grade = "F"

        print(f"{student:10} : {grade}")


# -----------------------------
# Menu
# -----------------------------

def menu():

    while True:

        print("\n" + "=" * 50)
        print("STUDENT MARKS ANALYZER")
        print("=" * 50)

        print("1. Show all marks")
        print("2. Average marks of each student")
        print("3. Average marks of each subject")
        print("4. Highest scoring student")
        print("5. Lowest scoring student")
        print("6. Pass/Fail list")
        print("7. Subject toppers")
        print("8. Grade report")
        print("9. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            show_all_marks()

        elif choice == "2":
            student_averages()

        elif choice == "3":
            subject_averages()

        elif choice == "4":
            highest_student()

        elif choice == "5":
            lowest_student()

        elif choice == "6":
            pass_fail_list()

        elif choice == "7":
            subject_toppers()

        elif choice == "8":
            grade_calculator()

        elif choice == "9":
            print("\nExiting Program...")
            break

        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    menu()