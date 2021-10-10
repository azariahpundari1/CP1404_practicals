from prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(0, 100)
        if random_number > self.reliability:
            distance_driven = 0
        else:
            distance_driven = super().drive(distance) # dont fully understand 'super' yet so looked in solutions
        return distance_driven
