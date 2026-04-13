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