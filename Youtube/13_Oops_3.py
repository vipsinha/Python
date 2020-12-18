# Classes 1
print('####Classes_1#####')

## Clasess
class Employee_1:
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
        Employee_1.num_of_employee += 1

    # regular methods
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    # regular methods
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# data and functions associated with a class are called attributes
#instances of a class

emp_1 = Employee_1('Check', 'Mate', 65000)
emp_2 = Employee_1('Test', 'User', 95000)

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee_1.raise_amount)

# Classes 2
print('####Classes_2#####')

## Clasess
class Employee_2:
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
        Employee_1.num_of_employee += 1

    # regular methods
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    # regular methods
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # alternative constructors
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# data and functions associated with a class are called attributes
#instances of a class

emp_1 = Employee_2('Check', 'Mate', 65000)
emp_2 = Employee_2('Test', 'User', 95000)


print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee_2.raise_amount)

Employee_2.set_raise_amount(1.3)
#emp_1.set_raise_amount(1.3) # But doesn't make sense

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee_2.raise_amount)

# Classes 3
print('####Classes_3#####')

## Clasess
class Employee_3:
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
        Employee_3.num_of_employee += 1

    # regular methods
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    # regular methods
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # class method
    # alternative constructors
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string):
        first, last, pay = string.split('-')
        return cls(first, last, pay)



# data and functions associated with a class are called attributes
#instances of a class

emp_1 = Employee_3('Check', 'Mate', 65000)
emp_2 = Employee_3('Test', 'User', 95000)
emp_str_1 = 'Vipul-Sinha-75000'
emp_3 = Employee_3.from_string(emp_str_1)
print(emp_3.email)
print(emp_3.pay)

# Classes 4
print('####Classes_4#####')

import datetime
## Clasess
class Employee_4:
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
        Employee_4.num_of_employee += 1

    # regular methods
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    # regular methods
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # class method
    # alternative constructors
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string):
        first, last, pay = string.split('-')
        return cls(first, last, pay)

    # static method
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

# data and functions associated with a class are called attributes
#instances of a class

emp_1 = Employee_4('Check', 'Mate', 65000)
emp_2 = Employee_4('Test', 'User', 95000)
emp_str_1 = 'Vipul-Sinha-75000'
emp_3 = Employee_4.from_string(emp_str_1)
print(emp_3.email)
print(emp_3.pay)
my_day = datetime.date(2017, 1, 31)
print(my_day)
print(emp_3.is_workday(my_day))