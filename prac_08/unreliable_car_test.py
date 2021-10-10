from prac_08.unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("Good car", 100, 40)
    unreliable_car = UnreliableCar("Unreliable car", 90, 50)
    good_car.drive(40)
    unreliable_car.drive(40)
    print(good_car)
    print(unreliable_car)

# the results change after repeated attempts


main()