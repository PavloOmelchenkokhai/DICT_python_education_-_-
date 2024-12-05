resources = {
    "water": 400,
    "milk": 540,
    "coffee_beans": 120,
    "disposable_cups": 9,
    "money": 550
}

coffee_types = {
    "1": {"name": "espresso", "water": 250, "milk": 0, "coffee_beans": 16, "cost": 4},
    "2": {"name": "latte", "water": 350, "milk": 75, "coffee_beans": 20, "cost": 7},
    "3": {"name": "cappuccino", "water": 200, "milk": 100, "coffee_beans": 12, "cost": 6}
}

def check_resources(coffee_type):
    for ingredient, amount in coffee_type.items():
        if ingredient in resources and resources[ingredient] < amount:
            print(f"Sorry, not enough {ingredient}!")
            return False
    return True

def buy():
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    if choice in coffee_types:
        coffee = coffee_types[choice]
        if check_resources(coffee):
            resources["water"] -= coffee["water"]
            resources["milk"] -= coffee["milk"]
            resources["coffee_beans"] -= coffee["coffee_beans"]
            resources["disposable_cups"] -= 1
            resources["money"] += coffee["cost"]
            print(f"I have enough resources, making you a {coffee['name']}!")
    elif choice == "back":
        return

def fill():
    resources["water"] += int(input("Write how many ml of water you want to add: "))
    resources["milk"] += int(input("Write how many ml of milk you want to add: "))
    resources["coffee_beans"] += int(input("Write how many grams of coffee beans you want to add: "))
    resources["disposable_cups"] += int(input("Write how many disposable coffee cups you want to add: "))

def take():
    print(f"I gave you {resources['money']}")
    resources["money"] = 0

def remaining():
    print("\nThe coffee machine has:")
    print(f"{resources['water']} of water")
    print(f"{resources['milk']} of milk")
    print(f"{resources['coffee_beans']} of coffee beans")
    print(f"{resources['disposable_cups']} of disposable cups")
    print(f"{resources['money']} of money\n")

while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        remaining()
    elif action == "exit":
        break
    else:
        print("Invalid action!")
