total = 0
items = int(input("Number of items: "))
while items <= 0:
    print("Invalid number of items")
    items = int(input("Number of items: "))
for i in range(0, items):
    price = float(input("Price of item: "))
    total += price
if total >= 100:
    discount = total * 0.10
    total = total - discount
print(f"Total price for", items, "items is: ", total)
