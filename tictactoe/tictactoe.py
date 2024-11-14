def print_board(cells):
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {cells[i]} {cells[i + 1]} {cells[i + 2]} |")
    print("---------")


def get_index(row, col):
    return (row - 1) * 3 + (col - 1)


def check_game_state(cells):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combination in win_combinations:
        if cells[combination[0]] == cells[combination[1]] == cells[combination[2]] != '_':
            return f"{cells[combination[0]]} wins"

    if '_' not in cells:
        return "Draw"

    return "Game not finished"


cells = "_________"
print_board(cells)
current_player = "X"

while True:
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

        break

    cells = cells[:index] + current_player + cells[index + 1:]
    print_board(cells)

    game_state = check_game_state(cells)
    if game_state != "Game not finished":
        print(game_state)
        break

    current_player = "O" if current_player == "X" else "X"
