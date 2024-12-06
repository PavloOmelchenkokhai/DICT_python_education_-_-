class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 400,
            "milk": 540,
            "coffee_beans": 120,
            "disposable_cups": 9,
            "money": 550
        }
        self.coffee_types = {
            "1": {"name": "espresso", "water": 250, "milk": 0, "coffee_beans": 16, "cost": 4},
            "2": {"name": "latte", "water": 350, "milk": 75, "coffee_beans": 20, "cost": 7},
            "3": {"name": "cappuccino", "water": 200, "milk": 100, "coffee_beans": 12, "cost": 6}
        }
        self.state = "action"  # Початковий стан: очікування дії
        self.fill_stage = None  # Етап поповнення запасів

    def handle_input(self, user_input):
        if self.state == "action":
            self.handle_action(user_input)
        elif self.state == "buy":
            self.handle_buy(user_input)
        elif self.state == "fill":
            self.handle_fill(user_input)

    def handle_action(self, action):
        if action == "buy":
            self.state = "buy"
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        elif action == "fill":
            self.state = "fill"
            self.fill_stage = "water"
            print("Write how many ml of water you want to add:")
        elif action == "take":
            print(f"I gave you {self.resources['money']}")
            self.resources["money"] = 0
        elif action == "remaining":
            self.show_remaining()
        elif action == "exit":
            self.state = "exit"
        else:
            print("Invalid action!")

    def handle_buy(self, choice):
        if choice == "back":
            self.state = "action"
        elif choice in self.coffee_types:
            coffee = self.coffee_types[choice]
            if self.check_resources(coffee):
                self.resources["water"] -= coffee["water"]
                self.resources["milk"] -= coffee["milk"]
                self.resources["coffee_beans"] -= coffee["coffee_beans"]
                self.resources["disposable_cups"] -= 1
                self.resources["money"] += coffee["cost"]
                print(f"I have enough resources, making you a {coffee['name']}!")
            self.state = "action"
        else:
            print("Invalid coffee type!")

    def handle_fill(self, amount):
        if self.fill_stage == "water":
            self.resources["water"] += int(amount)
            self.fill_stage = "milk"
            print("Write how many ml of milk you want to add:")
        elif self.fill_stage == "milk":
            self.resources["milk"] += int(amount)
            self.fill_stage = "coffee_beans"
            print("Write how many grams of coffee beans you want to add:")
        elif self.fill_stage == "coffee_beans":
            self.resources["coffee_beans"] += int(amount)
            self.fill_stage = "disposable_cups"
            print("Write how many disposable coffee cups you want to add:")
        elif self.fill_stage == "disposable_cups":
            self.resources["disposable_cups"] += int(amount)
            self.state = "action"
            self.fill_stage = None

    def show_remaining(self):
        print("\nThe coffee machine has:")
        print(f"{self.resources['water']} of water")
        print(f"{self.resources['milk']} of milk")
        print(f"{self.resources['coffee_beans']} of coffee beans")
        print(f"{self.resources['disposable_cups']} of disposable cups")
        print(f"{self.resources['money']} of money\n")

    def check_resources(self, coffee):
        for ingredient, amount in coffee.items():
            if ingredient in self.resources and self.resources[ingredient] < amount:
                print(f"Sorry, not enough {ingredient}!")
                return False
        return True


machine = CoffeeMachine()

while machine.state != "exit":
    if machine.state == "action":
        action = input("Write action (buy, fill, take, remaining, exit): ")
        machine.handle_input(action)
    elif machine.state == "buy":
        choice = input()
        machine.handle_input(choice)
    elif machine.state == "fill":
        amount = input()
        machine.handle_input(amount)
