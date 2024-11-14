# Функція для виведення ігрового поля
def print_board(cells):
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {cells[i]} {cells[i+1]} {cells[i+2]} |")
    print("---------")

def get_index(row, col):
    return (row - 1) * 3 + (col - 1)

cells = input("Enter cells: ")
print_board(cells)

while True:
    coordinates = input("Enter the coordinates: ").split()

    if not all(coord.isdigit() for coord in coordinates):
        print("You should enter numbers!")
        continue

    row, col = map(int, coordinates)

    if not (1 <= row <= 3) or not (1 <= col <= 3):
        print("Coordinates should be from 1 to 3!")
        continue

    index = get_index(row, col)

    if cells[index] != '_':
        print("This cell is occupied! Choose another one!")
        continue

    cells = cells[:index] + 'X' + cells[index + 1:]
    print_board(cells)
    break
