print("Write how many ml of water the coffee machine has:")
water_available = int(input("> "))

print("Write how many ml of milk the coffee machine has:")
milk_available = int(input("> "))

print("Write how many grams of coffee beans the coffee machine has:")
coffee_beans_available = int(input("> "))

print("Write how many cups of coffee you will need:")
cups_needed = int(input("> "))

water_per_cup = 200
milk_per_cup = 50
coffee_beans_per_cup = 15

max_cups = min(
    water_available // water_per_cup,
    milk_available // milk_per_cup,
    coffee_beans_available // coffee_beans_per_cup
)

if max_cups == cups_needed:
    print("Yes, I can make that amount of coffee")
elif max_cups > cups_needed:
    extra_cups = max_cups - cups_needed
    print(f"Yes, I can make that amount of coffee (and even {extra_cups} more than that)")
else:
    print(f"No, I can make only {max_cups} cups of coffee")
