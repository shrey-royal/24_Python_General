from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"
    
    @abstractmethod
    def get_salary(self):   # abstract method doesn't have any body
        pass