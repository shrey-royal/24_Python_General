'''
Public AM (default): accessible from outside
Protected AM (_): Intended for internal use or subclasses
Private AM (__): Not meant to be accessed from outside the class
'''


class Car:
    def __init__(self, brand, model):
        # public attributes
        self.brand = brand
        self.model = model

        # protected attribute
        self._engine = 'V6'

        # private attibute
        self.__fuelCapacity = 50

    # public method
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

    # protected method
    def _engine_info(self):
        print(f"Engine Type: {self._engine}")

    # private method
    def __fuel_info(self):
        print(f"Fuel Capacity: {self.__fuelCapacity} liters")

    # Method to access private method within the class
    def show_fuel_info(self):
        print(self.__fuelCapacity)
        self.__fuel_info()


if __name__ == "__main__":
    my_car = Car("Toyota", "Hyryder")

    # public
    # print(my_car.brand)
    # print(my_car.model)
    # my_car.display_info()

    # protected (this way of accessing directly is not recommended)
    # print(my_car._engine)
    # my_car._engine_info()

    # private (will raise an AttributeError)
    # print(my_car.__fuelCapacity)
    # my_car.__fuel_info()

    # we are accessing the private attributes and methods through public method 
    # my_car.show_fuel_info()