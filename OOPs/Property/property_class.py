"""
property class:
syntax:
    property(fget=None, fset=none, fdel=None, doc=None)
"""

from pprint import pprint

class Person:
    def __init__(self, name: str, age: str):
        self.__name = name
        self.__age = age

    def set_name(self, name: str) -> None:
        if name == None or name == "":
            print("Name value is invalid.")
        else:
            self.__name = name

    def get_name(self) -> str:
        return self.__name
    
    def set_age(self, age: str) -> None:
        if age <= 0:
            print("Age value is invalid.")
        else:
            self.__age = age

    def get_age(self) -> str:
        return self.__age
    
    def __str__(self) -> str:
        return f"Myself {self.__name}, I'm {self.__age} years old."
    
    name = property(fget=get_name, fset=set_name)
    age = property(fget=get_age, fset=set_age)


p = Person('meet', 23)

print(p.name)   # act as a getter method
print(p.age)

p.name = 'dhyey'    # act as a setter method
p.age = 24

# print(p.__dict__)
# print(Person.__dict__)
pprint(Person.__dict__)