from fulltimeemployee import FullTimeEmployee
from hourlyemployee import HourlyEmployee
from payroll import Payroll
from employee import Employee


payroll = Payroll()

payroll.add(FullTimeEmployee('Himesh', 'Patel', 60000))
payroll.add(FullTimeEmployee('Meet', 'Sarvaiya', 45000))
payroll.add(FullTimeEmployee('Dhyey', 'Patel', 120000))
payroll.add(HourlyEmployee('Dhairya', 'Patel', 200, 12000))
payroll.add(HourlyEmployee('Riya', 'Patel', 150, 5000))

payroll.print()