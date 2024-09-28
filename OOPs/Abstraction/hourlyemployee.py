from employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, firstname, lastname, worked_hours, rate) -> None:
        super().__init__(firstname, lastname)
        self.worked_hours = worked_hours
        self.rate = rate

    def get_salary(self):
        return self.worked_hours * self.rate