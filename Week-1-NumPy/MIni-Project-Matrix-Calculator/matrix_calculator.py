import numpy as np


# Sample Matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])


def add_matrices(a, b):
    if a.shape == b.shape:
        return np.add(a, b)
    return "Error: Matrix dimensions must match."


def subtract_matrices(a, b):
    if a.shape == b.shape:
        return np.subtract(a, b)
    return "Error: Matrix dimensions must match."


def multiply_matrices(a, b):
    if a.shape[1] == b.shape[0]:
        return np.dot(a, b)
    return "Error: Invalid matrix dimensions for multiplication."


def transpose_matrix(a):
    return np.transpose(a)


def determinant_matrix(a):
    if a.shape[0] == a.shape[1]:
        return np.linalg.det(a)
    return "Error: Determinant only exists for square matrices."


def inverse_matrix(a):
    if a.shape[0] != a.shape[1]:
        return "Error: Inverse only exists for square matrices."

    if np.isclose(np.linalg.det(a), 0):
        return "Error: Matrix is singular and cannot be inverted."

    return np.linalg.inv(a)


def display_matrices():
    print("\nMatrix A:")
    print(A)

    print("\nMatrix B:")
    print(B)


def show_menu():
    print("\n===== MATRIX CALCULATOR =====")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose Matrix A")
    print("5. Determinant of Matrix A")
    print("6. Inverse of Matrix A")
    print("7. Display Matrices")
    print("8. Exit")


def main():
    print("Welcome to the NumPy Matrix Calculator!")

    while True:
        show_menu()

        try:
            choice = input("\nEnter your choice (1-8): ")

            if choice == "1":
                print("\nResult:")
                print(add_matrices(A, B))

            elif choice == "2":
                print("\nResult:")
                print(subtract_matrices(A, B))

            elif choice == "3":
                print("\nResult:")
                print(multiply_matrices(A, B))

            elif choice == "4":
                print("\nTranspose of Matrix A:")
                print(transpose_matrix(A))

            elif choice == "5":
                print("\nDeterminant of Matrix A:")
                print(determinant_matrix(A))

            elif choice == "6":
                print("\nInverse of Matrix A:")
                print(inverse_matrix(A))

            elif choice == "7":
                display_matrices()

            elif choice == "8":
                print("\nThank you for using Matrix Calculator!")
                break

            else:
                print("\nError: Invalid choice. Please enter a number from 1 to 8.")

        except Exception as e:
            print(f"\nUnexpected Error: {e}")


if __name__ == "__main__":
    main()