# Classes 1
print('####Classes_1#####')

class Employee_1:
    pass

emp_1 = Employee_1()
emp_2 = Employee_1()

print(emp_1)
print(emp_2)

emp_1.first = 'Vipul'
emp_1.last = 'Sinha'
emp_1.email = 'Vipul.Sinha@company.com'
emp_1.pay = 80000

emp_2.first = 'Check'
emp_2.last = 'Mate'
emp_2.email = 'Check.Mate@company.com'
emp_2.pay = 70000

print(emp_1.email)
print(emp_2.email)

# Classes 2
print('####Classes_2#####')

class Employee_2:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

emp_1 = Employee_2('Vipul', 'Sinha', 90000)
emp_2 = Employee_2('Test', 'User', 95000)

print(emp_1.email)
print(emp_2.email)
print('{} {}'.format(emp_1.first, emp_1.last))

# Classes 3
print('####Classes_3#####')

## Clasess
class Employee_3:
    # Constructor/ initialised
    # self is an instance and others are arguments
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    # methods
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

# data and functions associated with a class are called attributes
#instances of a class
emp_1 = Employee_3('Check', 'Mate', 90000)
emp_2 = Employee_3('Test', 'User', 95000)
print(emp_1.full_name())
print(Employee_3.full_name(emp_2)) # instance passed as an argument