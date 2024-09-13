"""
getter always gets the @property tag
setter always gets the prop.setter tag
"""

class StreetFood:
    def __init__(self, name, price) -> None:
        self.__name = name
        self.__price = price

    @property   # @name.getter
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def price(self) -> int:
        return self.__price

    @price.setter
    def price(self, price: int) -> None:
        self.__price = price

vadapav = StreetFood("Vadapav", 20)
print(f'Name: {vadapav.name}\tPrice: {vadapav.price}')

vadapav.name = "Bombay Special vadapav"
vadapav.price = 35

print(f'Name: {vadapav.name}\tPrice: {vadapav.price}')