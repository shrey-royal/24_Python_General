class Person:
    def __init__(self, name: str, age: str):
        self.__name = name
        self.__age = age

    # Getter and Setter Methods
    # they are public methods which helps user get or set the data of private attributes
    
    def set_name(self, name: str) -> None:
        if name == None or name == "":
            print("Name not changed, Either None or Empty string provided.")
        else:
            self.__name = name
            

    def get_name(self) -> str:
        return self.__name
    
    def set_age(self, age) -> None:     # setter
        if age >= 0:
            self.__age = age
        else:
            print("Age not changed, value should be positive")
    
    def get_age(self) -> str:     # getter
        return self.__age

    def __str__(self):
        return f"Myself {self.__name}, I'm {self.__age} years old."

if __name__ == '__main__':
    dhairya = Person('Dhairya', 21)

    print(dhairya)

    # dhairya.age = 19
    # age = -1

    dhairya.set_name("Meet")
    dhairya.set_age(-9)

    print(dhairya) 


"""
The Getter Setter method works just fine but it has a backward compatibility issue.

to solve this we will use property class

"""