pencil = input("How many pencils would you like to use: ")

while True:
    player1 = "Alex"
    player2 = "Artem"
    first_player = input(f"Who will be the first ({player1}, {player2}): ").capitalize()
    if first_player not in [player1, player2]:
        print(f"Choose between {player1} and {player2}")
    else:
        pencil = int(pencil)
        break

current_player  = first_player

print("|" * pencil)
print(f"{current_player} is going first!")

while True:
    try:
        taken = int(input("> "))
        if taken not in [1, 2, 3]:
            print("Possible values: '1', '2' or '3'")
        elif taken > pencil:
            print("Too many pencils were taken")
        else:
            pencil -= taken
            break
    except ValueError:
        print("Please input a number between 1 and 3.")

    current_player = player1 if current_player == player2 else player2

    print("Game over!")