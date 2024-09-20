# Imagine you have a company that manages employees. You want to create a basic structure for Employee details, and then create more specialized roles like Manager, who inherits basic employee details but also has additional attributes like a list of team members.

class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Manager (Employee):
    def __init__(self, name, salary, teamName) -> None:
        super().__init__(name, salary)
        self.teamName = teamName

    def getDetails(self):
        print(f"Team Name: {self.teamName}")
        super().showDetails();

if __name__ == "__main__":
    shreya = Manager("Shreya", 1000000, "team1")
    shreya.getDetails()