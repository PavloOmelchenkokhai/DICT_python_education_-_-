def print_board(cells):
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {cells[i]} {cells[i+1]} {cells[i+2]} |")
    print("---------")

def check_winner(cells, symbol):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(cells[a] == cells[b] == cells[c] == symbol for a, b, c in win_positions)

def analyze_game(cells):
    x_count = cells.count('X')
    o_count = cells.count('O')
    empty_count = cells.count('_')

    x_wins = check_winner(cells, 'X')
    o_wins = check_winner(cells, 'O')

    if abs(x_count - o_count) > 1 or (x_wins and o_wins):
        return "Impossible"
    elif x_wins:
        return "X wins"
    elif o_wins:
        return "O wins"
    elif empty_count > 0:
        return "Game not finished"
    else:
        return "Draw"

cells = input("Enter cells: ")
print_board(cells)
result = analyze_game(cells)
print(result)
