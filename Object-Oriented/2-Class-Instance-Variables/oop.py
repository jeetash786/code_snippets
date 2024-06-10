#OLD AND SAME CODE OF PREVIOUS LECTURE
# class Employee:

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'Employee', 60000)

#SIMPLE AND CODE OF 2nd LECTURE

class Employee:
    raise_amount = 1.04
    no_emp = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.no_emp += 1
    
    def pay_raise(self):
        self.pay = int(self.pay *  self.raise_amount)
emp_1 = Employee('PEWDIE','PIE',5000)
emp_2 = Employee('Mr','Beast',5000)
emp_1.pay_raise()
print(emp_1.pay)
print(Employee.no_emp)
