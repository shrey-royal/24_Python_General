from employee import Employee

class FullTimeEmployee(Employee):
    def __init__(self, firstname, lastname, salary) -> None:
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_salary(self):
        return self.salary