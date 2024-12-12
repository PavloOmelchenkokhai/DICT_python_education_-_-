def read_matrix():
    """Зчитує матрицю з вводу з перевіркою правильності вводу."""
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


def add_matrices(matrix_a, matrix_b):
    """Додає дві матриці."""
    n_a, m_a, a = matrix_a
    n_b, m_b, b = matrix_b

    if n_a != n_b or m_a != m_b:
        return "ERROR"

    result = []
    for i in range(n_a):
        row = [a[i][j] + b[i][j] for j in range(m_a)]
        result.append(row)
    return result


def print_matrix(matrix):
    """Виводить матрицю у відповідному форматі."""
    for row in matrix:
        print(" ".join(map(str, row)))


# Основна програма
print("Введення першої матриці:")
matrix_a = read_matrix()

print("Введення другої матриці:")
matrix_b = read_matrix()

result = add_matrices(matrix_a, matrix_b)

if result == "ERROR":
    print("ERROR")
else:
    print("Результат додавання матриць:")
    print_matrix(result)
