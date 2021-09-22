from prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)
other_guitar = Guitar("Other Guitar", 2005, 1809.50)

# expected guitar age
print(f"{name}, {guitar.get_age()} - Expected 99. Got {guitar.get_age()}")
print(f"{other_guitar.name}, {other_guitar.get_age()} - Expected 16. Got {other_guitar.get_age()}")

# vintage or not vintage
print(f"{name} {guitar.is_vintage()} - Expected True. Got {guitar.is_vintage()}")
print(f"{other_guitar.name} {other_guitar.is_vintage()} - Expected False. Got {other_guitar.is_vintage()}")