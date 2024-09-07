# print(dir(list))    # for getting all the methods of the class

"""
Dunder Methods: Special Methods (starts and ends with '__')
-> A method that is called implicitly by Python to execute a certain operation on a type, such as addition. Such methods have names starting and ending with double underscores.

__init__: used to initialize the data attributes of a class.
__str__: it represents the object in string format
__repr__: The __repr__ does the same as __str__ does but it is used to make data machine-readable.
__eq__: Python automatically calls the __eq__ method of a class when you use the == operator to compare the instances of the class. By default, Python uses the is operator if you don't provide a specific implementation for the __eq__ method.
__hash__: The hash() function accepts an object and returns the hash value as an integer. When you pass an object to the hash() function, Python will execute the __hash__ special method of the object.
__del__: Python calls the __del__ method when all object references are gone. And you cannot control it in most cases. (not recommended)
"""

class Person:
    def __init__(self, firstName, lastName, age) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        print("__init__ was called.")

    # def __str__(self) -> str:
    #     return f'Person("{self.firstName}","{self.lastName}",{self.age})'
    
    # def __repr__(self):
    #     return f'Person("{self.firstName}","{self.lastName}",{self.age})'

    # def __eq__(self, other: object) -> bool:
    #     return self.age == other.age
    #     # return self.age == age

    #     if isinstance(other, Person):
    #         return self.age == other.age
    #     return False

    # def __hash__(self, other: object) -> int:
    #     if isinstance(other, Person):
    #         return self.__eq__(other)
        # return id(self)

    # def __bool__(self) -> bool:
    #     if self.age >= 1 and self.age <= 80:
    #         return True
    #     return False

    def __del__(self) -> None:  # destructor
        print("__del__ was called.")


meet = Person("Meet", "Sarvaiya", 22)
dhyeySir = Person("Dhyey Sir", "Patel", 21)

# print(str(meet))
# print(meet == dhyeySir)
# print(meet == 20)
# print(meet)
# print(repr(meet))

# print(hash(dhyeySir))
# print(hash(meet))
# print(meet.__hash__(dhyeySir))

# print(bool(meet))
# del meet
# meet = None
# print(meet.firstName)
