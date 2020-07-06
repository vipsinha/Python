# Classes 1
print('####Classes_1#####')

## Clasess
class Employee_1:
    # Constructor/ initialised
    # self is an instance and others are arguments
    def __init__(self, first, last, pay):
        self.first = first # class variable
        self.last = last # class variable
        self.email = first + '.' + last + '@company.com'
        self.pay = pay # class variable

    # methods
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.10)

# data and functions associated with a class are called attributes
#instances of a class
emp_1 = Employee_1('Check', 'Mate', 65000)
emp_2 = Employee_1('Test', 'User', 95000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# Classes 2
print('####Classes_2#####')

## Clasess
class Employee_2:
    #class variable
    raise_amount = 1.10
    # Constructor/ initialised
    # self is an instance and others are arguments
    def __init__(self, first, last, pay):
        self.first = first # class variable
        self.last = last # class variable
        self.email = first + '.' + last + '@company.com'
        self.pay = pay # class variable

    # methods
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee_2.raise_amount)

# data and functions associated with a class are called attributes
#instances of a class
emp_1 = Employee_2('Check', 'Mate', 65000)
emp_2 = Employee_2('Test', 'User', 95000)

print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

# Classes 3
print('####Classes_3#####')

## Clasess
class Employee_3:
    #class variable
    raise_amount = 1.10
    # Constructor/ initialised
    # self is an instance and others are arguments
    def __init__(self, first, last, pay):
        self.first = first # class variable
        self.last = last # class variable
        self.email = first + '.' + last + '@company.com'
        self.pay = pay # class variable

    # methods
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    # methods
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# data and functions associated with a class are called attributes
#instances of a class
emp_1 = Employee_3('Check', 'Mate', 65000)
emp_2 = Employee_3('Test', 'User', 95000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)
print(Employee_3.__dict__)


# Classes 4
print('####Classes_4#####')

## Clasess
class Employee_4:
    #class variable
    raise_amount = 1.10
    # Constructor/ initialised
    # self is an instance and others are arguments
    def __init__(self, first, last, pay):
        self.first = first # class variable
        self.last = last # class variable
        self.email = first + '.' + last + '@company.com'
        self.pay = pay # class variable

    # methods
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    # methods
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# data and functions associated with a class are called attributes
#instances of a class
emp_1 = Employee_4('Check', 'Mate', 65000)
emp_2 = Employee_4('Test', 'User', 95000)

emp_1.raise_amount = 1.20
print(Employee_4.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# Classes 5
print('####Classes_5#####')

## Clasess
class Employee_5:
    #class variable
    raise_amount = 1.10
    num_of_employee = 0
    # Constructor/ initialised
    # self is an instance and others are arguments
    def __init__(self, first, last, pay):
        self.first = first # class variable
        self.last = last # class variable
        self.email = first + '.' + last + '@company.com'
        self.pay = pay # class variable
        
        # This way it will be same for all the instances
        Employee_5.num_of_employee += 1

    # methods
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    # methods
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# data and functions associated with a class are called attributes
#instances of a class
print(Employee_5.num_of_employee)
emp_1 = Employee_5('Check', 'Mate', 65000)
emp_2 = Employee_5('Test', 'User', 95000)
print(Employee_5.num_of_employee)