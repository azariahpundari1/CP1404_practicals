"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Sales: "))
total = 0
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.10
        total += bonus
        sales = float(input("Sales: "))
    else:
        bonus = sales * 0.15
        total += bonus
        sales = float(input("Sales: "))
print(total)
