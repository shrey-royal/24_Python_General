class Payroll:
    def __init__(self) -> None:
        self.employee_list = []

    def add(self, employee) -> None:
        self.employee_list.append(employee)

    def print(self) -> None:
        for emp in self.employee_list:
            print(f"{emp.full_name} \t Rs.{emp.get_salary()}")