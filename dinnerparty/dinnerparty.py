num_of_friends = int(input("Enter the number of friends joining (including you): "))

if num_of_friends <= 0:
    print("No one is joining for the party")
else:
    friends = {}

    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_of_friends):
        name = input("> ")
        friends[name] = 0

    print(friends)
