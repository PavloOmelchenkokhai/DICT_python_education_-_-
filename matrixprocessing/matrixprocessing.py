def read_matrix():
    """Функція для зчитування матриці від користувача."""
    try:
        rows, cols = map(int, input("Enter matrix size: > ").split())
        print("Enter matrix:")
        matrix = []
        for _ in range(rows):
            row = list(map(float, input("> ").split()))
            if len(row) != cols:
                raise ValueError("Invalid row size")
            matrix.append(row)
        return matrix, rows, cols
    except ValueError as e:
        print(f"Error: {e}")
        return None, 0, 0

def print_matrix(matrix):
    """Функція для друку матриці."""
    for row in matrix:
        print(" ".join(map(str, row)))

def determinant(matrix):
    """Рекурсивна функція для обчислення визначника квадратної матриці."""
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(size):
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)
    return det

def add_matrices():
    """Функція для додавання двох матриць."""
    matrix1, rows1, cols1 = read_matrix()
    if not matrix1:
        return
    matrix2, rows2, cols2 = read_matrix()
    if not matrix2 or rows1 != rows2 or cols1 != cols2:
        print("The operation cannot be performed.")
        return
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols1)] for i in range(rows1)]
    print("The result is:")
    print_matrix(result)

def multiply_matrix_by_constant():
    """Функція для множення матриці на константу."""
    matrix, rows, cols = read_matrix()
    if not matrix:
        return
    try:
        constant = float(input("Enter constant: > "))
        result = [[element * constant for element in row] for row in matrix]
        print("The result is:")
        print_matrix(result)
    except ValueError:
        print("Invalid constant value.")

def multiply_matrices():
    """Функція для множення двох матриць."""
    matrix1, rows1, cols1 = read_matrix()
    if not matrix1:
        return
    matrix2, rows2, cols2 = read_matrix()
    if not matrix2 or cols1 != rows2:
        print("The operation cannot be performed.")
        return
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    print("The result is:")
    print_matrix(result)

def transpose_matrix():
    """Функція для транспонування матриці."""
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    choice = input("Your choice: > ").strip()
    matrix, rows, cols = read_matrix()
    if not matrix:
        return
    if choice == "1":
        result = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    elif choice == "2":
        result = [[matrix[rows - 1 - j][cols - 1 - i] for j in range(rows)] for i in range(cols)]
    elif choice == "3":
        result = [list(reversed(row)) for row in matrix]
    elif choice == "4":
        result = list(reversed(matrix))
    else:
        print("Invalid choice.")
        return
    print("The result is:")
    print_matrix(result)

def calculate_determinant():
    """Функція для обчислення визначника."""
    matrix, rows, cols = read_matrix()
    if not matrix or rows != cols:
        print("The operation cannot be performed.")
        return
    result = determinant(matrix)
    print("The result is:")
    print(result)

def main_menu():
    """Головне меню програми."""
    while True:
        print("\n1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("0. Exit")
        choice = input("Your choice: > ").strip()
        if choice == "1":
            add_matrices()
        elif choice == "2":
            multiply_matrix_by_constant()
        elif choice == "3":
            multiply_matrices()
        elif choice == "4":
            transpose_matrix()
        elif choice == "5":
            calculate_determinant()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Запуск програми
main_menu()
