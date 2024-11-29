import random

while True:
    pencil = input("How many pencils would you like to use: ")
    if not pencil.isdigit():
        print("The number of pencils should be numeric")
    elif int(pencil) <= 0:
        print("The number of pencils should be positive")
    else:
        pencil = int(pencil)
        break

player1 = "John"
player2 = "Jack"

while True:
    first_player = input(f"Who will be the first ({player1}, {player2}): ").capitalize()
    if first_player not in [player1, player2]:
        print(f"Choose between {player1} and {player2}")
    else:
        break

current_player = first_player

while pencil > 0:
    print("|" * pencil)
    print(f"{current_player}'s turn!")

    if current_player == player2:  # Якщо хід бота
        if pencil % 4 == 0:
            taken = 3
        elif pencil % 4 == 3:
            taken = 2
        elif pencil % 4 == 2:
            taken = 1
        else:
            taken = random.randint(1, min(3, pencil))  # Випадковий хід у програшній позиції
        print(taken)
    else:
        while True:
            try:
                taken = int(input("> "))
                if taken not in [1, 2, 3]:
                    print("Possible values: '1', '2' or '3'")
                elif taken > pencil:
                    print("Too many pencils were taken")
                else:
                    break
            except ValueError:
                print("Please input a number between 1 and 3.")

    pencil -= taken

    if pencil > 0:
        current_player = player1 if current_player == player2 else player2

winner = player1 if current_player == player2 else player2
print(f"{winner} won!")
