def read_matrix(prompt):
    """Зчитує матрицю з введенням розмірів і перевіркою правильності."""
    while True:
        try:
            rows, cols = map(int, input(f"{prompt} > ").split())
            break
        except ValueError:
            print("Помилка! Введіть два цілих числа.")
    matrix = []
    print("Enter matrix:")
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"> ").split()))
                if len(row) != cols:
                    raise ValueError
                matrix.append(row)
                break
            except ValueError:
                print(f"Помилка! Введіть рівно {cols} чисел.")
    return rows, cols, matrix


def add_matrices(matrix1, matrix2):
    """Додає дві матриці, якщо їх розміри збігаються."""
    (rows1, cols1, mat1), (rows2, cols2, mat2) = matrix1, matrix2
    if rows1 != rows2 or cols1 != cols2:
        return "The operation cannot be performed."
    result = [[mat1[i][j] + mat2[i][j] for j in range(cols1)] for i in range(rows1)]
    return result


def multiply_matrix_by_constant(matrix, constant):
    """Множить матрицю на задану константу."""
    _, _, mat = matrix
    result = [[element * constant for element in row] for row in mat]
    return result


def multiply_matrices(matrix1, matrix2):
    """Множить дві матриці, якщо кількість стовпців першої дорівнює кількості рядків другої."""
    (rows1, cols1, mat1), (rows2, cols2, mat2) = matrix1, matrix2
    if cols1 != rows2:
        return "The operation cannot be performed."
    result = [[sum(mat1[i][k] * mat2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    return result


def print_matrix(matrix):
    """Виводить матрицю у відповідному форматі."""
    if isinstance(matrix, str):
        print(matrix)
    else:
        print("The result is:")
        for row in matrix:
            print(" ".join(map(lambda x: f"{x:.2f}" if isinstance(x, float) else str(x), row)))


def main():
    while True:
        print("\n1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
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
        else:
            print("Помилка! Виберіть опцію з меню.")


# Запуск програми
if __name__ == "__main__":
    main()