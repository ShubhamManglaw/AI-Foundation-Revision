# NumPy Matrix Calculator

## Project Overview

This project is a menu-driven Matrix Calculator built using NumPy. It performs common matrix operations such as addition, subtraction, multiplication, transpose, determinant calculation, and matrix inversion.

The project was created as part of NumPy revision and practice.

---

## Features

- Add two matrices
- Subtract two matrices
- Multiply two matrices
- Transpose a matrix
- Calculate determinant
- Find inverse of a matrix
- Error handling for invalid operations
- Menu-driven interface

---

## NumPy Functions Used

The following NumPy functions were used:

python np.add() np.subtract() np.dot() np.transpose() np.linalg.det() np.linalg.inv() 

---

## Project Structure

text numpy-matrix-calculator/ │ ├── matrix_calculator.py └── README.md 

---

## How to Run

### Clone Repository

bash git clone <repository-url> 

### Navigate to Project Folder

bash cd numpy-matrix-calculator 

### Run Program

bash python3 matrix_calculator.py 

---

## Sample Matrices

python A = [[1, 2],      [3, 4]]  B = [[5, 6],      [7, 8]] 

---

## Example Outputs

### Matrix Addition

text [[ 6  8]  [10 12]] 

### Matrix Subtraction

text [[-4 -4]  [-4 -4]] 

### Matrix Multiplication

text [[19 22]  [43 50]] 

### Matrix Transpose

text [[1 3]  [2 4]] 

### Determinant

text -2.0 

### Inverse

text [[-2.   1. ]  [ 1.5 -0.5]] 

---

## Errors Handled

The program handles:

- Matrix dimension mismatch during addition
- Matrix dimension mismatch during subtraction
- Invalid dimensions for multiplication
- Determinant calculation on non-square matrices
- Inverse calculation on non-square matrices
- Singular matrices (determinant = 0)
- Invalid menu choices
- Unexpected runtime errors

---

## What I Learned

- Creating and manipulating NumPy arrays
- Matrix arithmetic operations
- Matrix multiplication using dot product
- Matrix transpose operations
- Determinant calculation
- Matrix inversion
- Shape validation and error handling
- Building menu-driven Python applications
- Writing modular code using functions

---

## Future Improvements

- User-defined matrix input
- Support for larger matrices
- Matrix rank calculation
- Eigenvalues and eigenvectors
- Better user interface

---

## Author

Shubham Manglaw

NumPy Revision Project – Day 6