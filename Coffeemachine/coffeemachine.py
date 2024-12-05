print("Write how many cups of coffee you will need:")
cups = int(input("> "))

water = cups * 200
milk = cups * 50
coffee_beans = cups * 15

print(f"\nFor {cups} cups of coffee you will need:")
print(f"{water} ml of water")
print(f"{milk} ml of milk")
print(f"{coffee_beans} g of coffee beans")
