"""
Display title
get cents_per_kWh
get daily_use_kWh
get no_of_days
estimate_bill = daily_use_kWh * no_of_days / cents_per_kWh
"""

print("Electricity bill estimator")
cents_per_kwh = int(input("Cents per kWh: "))
daily_use_kwh = float(input("Daily use per: "))
no_of_days = int(input("Number of days: "))
estimate_bill = (daily_use_kwh * no_of_days) / cents_per_kwh
print(f"Your estimate bill is ${estimate_bill}")
