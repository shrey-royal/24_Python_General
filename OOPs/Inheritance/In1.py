# Type 1: Single Inheritance

class Vehicle:  # parent/super/base class
    def __init__(self, speed) -> None:
        self.speed = speed
    
    def drive(self):
        return f"Driving at {self.speed} km/h"
    
class Car(Vehicle): # child/sub/derived class
    def __init__(self, speed, doors) -> None:
        super().__init__(speed)
        self.doors = doors

    def show_details(self):
        return f"This car has {self.doors} doors."
    
if __name__ == "__main__":
    my_car = Car(120, 4)
    print(my_car.drive())
    print(my_car.show_details())