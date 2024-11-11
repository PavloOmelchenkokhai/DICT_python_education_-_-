cells = input("Enter cells: ").strip()

print("---------")

for i in range(0, 9, 3):
    print(f"| {cells[i]} {cells[i+1]} {cells[i+2]} |")

print("---------")
