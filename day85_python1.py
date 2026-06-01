inventory = {}

while True:
    item = input("Enter item (or exit): ")

    if item.lower() == "exit":
        break

    qty = int(input("Quantity: "))
    inventory[item] = qty

print("Inventory:")
for item, qty in inventory.items():
    print(item, ":", qty)
