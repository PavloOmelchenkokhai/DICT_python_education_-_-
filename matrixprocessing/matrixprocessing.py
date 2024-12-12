def read_matrix_with_validation():
    """Зчитує матрицю з перевіркою правильності вводу."""
    while True:
        try:
            n, m = map(int, input("Введіть кількість рядків і стовпців через пробіл: ").split())
            break
        except ValueError:
            print("Помилка! Введіть два цілі числа.")

    matrix = []
    for i in range(n):
        while True:
            try:
                row = list(map(int, input(f"Введіть рядок {i + 1} з {m} елементів: ").split()))
                if len(row) != m:
                    raise ValueError
                matrix.append(row)
                break
            except ValueError:
                print(f"Помилка! Введіть рівно {m} цілих чисел.")
    return n, m, matrix


def read_constant():
    """Зчитує константу з перевіркою правильності вводу."""
    while True:
        try:
            constant = int(input("Введіть константу (ціле число): "))
            return constant
        except ValueError:
            print("Помилка! Введіть ціле число.")


def multiply_matrix_by_constant(matrix, constant):
    """Множить матрицю на константу."""
    _, _, a = matrix
    result = [[element * constant for element in row] for row in a]
    return result


def print_matrix(matrix):
    """Виводить матрицю у відповідному форматі."""
    for row in matrix:
        print(" ".join(map(str, row)))


# Основна програма
print("Введення матриці:")
matrix = read_matrix_with_validation()

constant = read_constant()

result = multiply_matrix_by_constant(matrix, constant)

print("Результат множення матриці на константу:")
print_matrix(result)
