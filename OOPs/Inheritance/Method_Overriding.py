# class Person:
    # def __init__(self, name: str, age: int) -> None:
    #     self._name = name
    #     self._age = age

    # def displayPerson(self) -> None:
    #     print(f"Name: {self._name!r}")
    #     print(f"Age: {self._age}")

# class Employee(Person):
#     def __init__(self, id: int, name: str, age: int, designation: str, salary: float) -> None:
#         self._name = name
#         self._age = age
#         self.__id = id
#         self.__designation = designation
#         self.__salary = salary

#     def displayEmployee(self) -> None:
#         print(f"Id: {self.__id}")
#         print(f"Designation: {self.__designation}")
#         print(f"Salary: {self.__salary}")
        
# isinstance -> returns true when the object is an instance of the class
# issubclass
# if __name__ == "__main__":
#     p = Person()
#     e = Employee(10012, "Arin", 21, "Product Manager", 23000.51)

    # e.displayPerson()
    # e.displayEmployee()

    # print(isinstance(e, Employee))
    # print(isinstance(p, Person))
    # print(isinstance(e, Person))
    # print(isinstance(p, Employee))

    # print(issubclass(Person, Employee))
    # print(issubclass(Employee, Person))
    # print(issubclass(Employee, Employee))
    # print(issubclass(Person, Person))

###################################################################################################

class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def get_pay(self) -> float:
        return self.salary
    
class SalesEmployee(Employee):
    def __init__(self, name: str, salary: float, incentive: float) -> None:
        self.name = name
        self.salary = salary
        self.sales_incentive = incentive

    def get_pay(self) -> float: # Method Overriden
        return self.salary + (self.salary * self.sales_incentive)
    
if __name__ == "__main__":
    meet = Employee("meet", 40000)
    arin = SalesEmployee("Arin", 30000, 5)

    print(f"Meet: {meet.get_pay()}")
    print(f"Arin: {arin.get_pay()}")