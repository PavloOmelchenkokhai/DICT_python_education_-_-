import random

num_of_friends = int(input("Enter the number of friends joining (including you): "))

if num_of_friends <= 0:
    print("No one is joining for the party")
else:
    friends = {}

    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_of_friends):
        name = input("> ")
        friends[name] = 0

    total_amount = float(input("Enter the total amount: "))

    split_amount = round(total_amount / num_of_friends, 2)

    for name in friends:
        friends[name] = split_amount

    choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ').strip().lower()

    if choice == "yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")

        new_split = round(total_amount / (num_of_friends - 1), 2)

        for name in friends:
            friends[name] = new_split if name != lucky_one else 0

    else:
        print("No one is going to be lucky")

    print(friends)
