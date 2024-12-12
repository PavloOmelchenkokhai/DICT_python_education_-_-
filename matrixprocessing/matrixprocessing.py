def transpose_matrix(matrix, method):
    """Транспонує матрицю відповідно до вибраного методу."""
    rows, cols, mat = matrix
    if method == "1":  # Main diagonal
        result = [[mat[j][i] for j in range(rows)] for i in range(cols)]
    elif method == "2":  # Side diagonal
        result = [[mat[rows - j - 1][cols - i - 1] for j in range(rows)] for i in range(cols)]
    elif method == "3":  # Vertical line
        result = [[mat[i][cols - j - 1] for j in range(cols)] for i in range(rows)]
    elif method == "4":  # Horizontal line
        result = [[mat[rows - i - 1][j] for j in range(cols)] for i in range(rows)]
    else:
        result = "Invalid transpose option."
    return result


def main():
    while True:
        print("\n1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("0. Exit")
        choice = input("Your choice: > ")

        if choice == "0":
            break
        elif choice == "1":
            print("Enter size of first matrix:")
            matrix1 = read_matrix("Enter size of first matrix")
            print("Enter size of second matrix:")
            matrix2 = read_matrix("Enter size of second matrix")
            result = add_matrices(matrix1, matrix2)
            print_matrix(result)
        elif choice == "2":
            print("Enter size of matrix:")
            matrix = read_matrix("Enter size of matrix")
            while True:
                try:
                    constant = float(input("Enter constant: > "))
                    break
                except ValueError:
                    print("Помилка! Введіть число.")
            result = multiply_matrix_by_constant(matrix, constant)
            print_matrix(result)
        elif choice == "3":
            print("Enter size of first matrix:")
            matrix1 = read_matrix("Enter size of first matrix")
            print("Enter size of second matrix:")
            matrix2 = read_matrix("Enter size of second matrix")
            result = multiply_matrices(matrix1, matrix2)
            print_matrix(result)
        elif choice == "4":
            print("\n1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            method = input("Your choice: > ")
            print("Enter matrix size:")
            matrix = read_matrix("Enter matrix size")
            result = transpose_matrix(matrix, method)
            print_matrix(result)
        else:
            print("Помилка! Виберіть опцію з меню.")


# Запуск програми
if __name__ == "__main__":
    main()
