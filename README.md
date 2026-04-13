# MATRIX OPERATIONS TOOL USING PYTHON AND NUMPY

## INTRODUCTION
Matrix operations are fundamental in various fields such as computer science, engineering, data science, and artificial intelligence. Performing these operations manually can be time-consuming and error-prone, especially for large matrices. This project focuses on developing a Matrix Operations Tool using Python and the NumPy library to simplify and automate these calculations.

## OBJECTIVE
The main objective of this project is to create an interactive application that allows users to perform common matrix operations efficiently. The tool aims to provide a user-friendly interface for:
1. Matrix Addition
2. Matrix Subtraction
3. Matrix Multiplication
4. Matrix Transpose
5. Determinant Calculation

## TECHNOLOGIES USED
1. Python
2. NumPy Library

## SYSTEM DESIGN
The system is designed as a menu-driven console application. The user is prompted to select an operation, input matrices, and view results in a structured format.
1. Input Module: Takes matrix input from the user
2. Processing Module: Performs matrix operations using NumPy
3. Output Module: Displays results clearly

## ALGORITHM
1. Start the program
2. Display menu options
3. Take user choice
4. Input matrix/matrices
5. Perform selected operation
6. Display result
7. Repeat until exit option is selected

## IMPLEMENTATION DETAILS
### Matrix Input
The user enters the number of rows and columns, followed by matrix elements row-wise. The program validates input to ensure correct dimensions.

### Matrix Operations
### Addition
Adds two matrices of the same dimensions.
### Subtraction
Subtracts one matrix from another of the same dimensions.
### Multiplication
Multiplies two matrices where the number of columns of the first matrix equals the number of rows of the second.
### Transpose
Converts rows into columns for a given matrix.
### Determinant
Calculates the determinant of a square matrix using NumPy.

## PROGRAM/CODE
```
import numpy as np
def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))

    print(f"Enter elements of {name} row-wise:")
    elements = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Invalid input. Please enter the correct number of elements.")
            return input_matrix(name)
        elements.append(row)

    return np.array(elements)
def display_matrix(matrix, title="Result"):
    print(f"\n--- {title} ---")
    print(matrix)

def matrix_addition(A, B):
    return A + B

def matrix_subtraction(A, B):
    return A - B

def matrix_multiplication(A, B):
    return np.dot(A, B)

def matrix_transpose(A):
    return A.T

def matrix_determinant(A):
    return np.linalg.det(A)

def main():
    print("\n===== MATRIX OPERATIONS TOOL =====")

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            try:
                result = matrix_addition(A, B)
                display_matrix(result, "Addition Result")
            except:
                print("Error: Matrices must have same dimensions.")

        elif choice == '2':
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            try:
                result = matrix_subtraction(A, B)
                display_matrix(result, "Subtraction Result")
            except:
                print("Error: Matrices must have same dimensions.")

        elif choice == '3':
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            try:
                result = matrix_multiplication(A, B)
                display_matrix(result, "Multiplication Result")
            except:
                print("Error: Columns of A must equal rows of B.")

        elif choice == '4':
            A = input_matrix("Matrix")
            result = matrix_transpose(A)
            display_matrix(result, "Transpose Result")

        elif choice == '5':
            A = input_matrix("Matrix")
            try:
                result = matrix_determinant(A)
                print(f"\nDeterminant: {result}")
            except:
                print("Error: Determinant requires a square matrix.")

        elif choice == '6':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

## OUTPUT
### ADDITION OF TWO MATRIX
<img width="464" height="689" alt="image" src="https://github.com/user-attachments/assets/de75b411-7fc9-4697-a7c9-177a8fe3d69b" />

### SUBTRACTION OF TWO MATRIX
<img width="440" height="696" alt="image" src="https://github.com/user-attachments/assets/81498423-972e-4ff5-983d-0fa32d39417c" />

### MULTIPLICATION OF TWO MATRIX
<img width="411" height="621" alt="image" src="https://github.com/user-attachments/assets/36e9b4da-c9a9-463a-ad83-d61c5f22b7d8" />

### TRANSPOSE OF A MATRIX
<img width="370" height="541" alt="image" src="https://github.com/user-attachments/assets/e5b8eaca-6ab3-4005-af4c-0e428d067609" />

### DETERMINANT OF A MATRIX
<img width="372" height="449" alt="image" src="https://github.com/user-attachments/assets/7d239bea-e411-4971-b0d7-1fada7fddd0d" />

### EXIT OF THE PROGRAM
<img width="355" height="373" alt="image" src="https://github.com/user-attachments/assets/dd057bc1-5c75-4615-a852-c0e67acd3497" />

## ADVANTAGES
1. Reduces manual calculation errors
2. Fast and efficient computation
3. User-friendly interface
4. Supports multiple matrix operations

## LIMITATIONS
1. Console-based interface only
2. Requires correct user input format
3. Limited to basic operations

## FUTURE ENHANCEMENTS
1. Develop a graphical user interface (GUI)
2. Add advanced operations (inverse, eigenvalues, rank)
3. Integrate file input/output support
4. Deploy as a web application

## CONCLUSION
The Matrix Operations Tool successfully demonstrates how Python and NumPy can be used to perform mathematical computations efficiently. The application is simple, interactive, and useful for students and professionals dealing with matrix operations.
