from prac_06.guitar import Guitar

guitars = []
guitar_name = input("Name: ")
while guitar_name != "":
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: "))
    appending_guitars = Guitar(guitar_name, guitar_year, guitar_cost)
    guitars.append(appending_guitars)
    print(appending_guitars, "added")
    guitar_name = input("Name: ")

# testing
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("\n... snip ...\n")
print("These are my guitars:")
for i, guitar in enumerate(guitars):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = " (vintage)"
    print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")