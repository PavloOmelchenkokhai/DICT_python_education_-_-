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

print("|" * pencil)
print(f"{first_player} is going first!")
