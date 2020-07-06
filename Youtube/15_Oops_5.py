# Classes 1
print('####Classes_1#####')

import datetime
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
        if day.weekday()==5 or day.weekday==6:
            return False
        return True

    # magic / operator overloading / dunder
    # repr is used for debugging, logging
    def __repr__ (self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
        
    # used for display
    def __str__ (self):
        return "Employee('{}' - '{}')".format(self.full_name(), self.email) # Don't miss the parenthesis for full name

# An inheritance of the base class employee 1
class Developer_1(Employee_1):
    raise_amount = 1.2

    # add new attribute
    def __init__(self, first, last, pay, prog_lang):
        # this is better approach then below, as it will be useful in 
        # multiple inhertence
        super().__init__(first, last, pay)
        # Employee_3.__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager_1(Employee_1):
    def __init__(self, first, last, pay, employees=None):
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emply in self.employees:
            print('-->' + emply.full_name())




# data and functions associated with a class are called attributes
#instances of a class

# Use of instance
emp_1 = Employee_1('Check', 'Mate', 65000)
# emp_2 = Developer_1('Test', 'User', 65000, 'C++')

# mgr_1 = Manager_1('Björn', 'Besser', 90000, [emp_1])


# Can't pass the programming lang to Employee class,
# it has not attribute
# emp_2 = Employee_3('Test', 'User', 65000, 'C++')

# emp_str_1 = 'Vipul-Sinha-75000'
# emp_3 = Employee_1.from_string(emp_str_1)
# print(emp_3.email)
# print(emp_3.pay)
# my_day = datetime.date(2017, 1, 31)
# print(my_day)
# print(emp_3.is_workday(my_day))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# # print(help(Developer_2))
# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)

# print(emp_1.prog_lang)
# print(emp_2.prog_lang)
# print(mgr_1.print_emp())

# mgr_1.add_emp(emp_2)

# print(mgr_1.print_emp())

# mgr_1.remove_emp(emp_1)

# print(mgr_1.print_emp())

# to check whether is class of inhereted
# print(isinstance(mgr_1, Manager_1))
# print(isinstance(emp_2, Manager_1))
# print(isinstance(mgr_1, Employee_1))

# print(issubclass(Manager_4, Employee_1))

print(emp_1)
print(emp_1.__repr__()) # or print(repr(emp_1))
print(emp_1.__str__()) # or print(str(emp_1))

print(int.__add__(1,2)) # print(1+2)
print(str.__add__('A','B')) # print('A'+'B')

# Classes 2
print('####Classes_2#####')

import datetime
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
        Employee_2.num_of_employee += 1

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
        if day.weekday()==5 or day.weekday==6:
            return False
        return True

    # magic / operator overloading / dunder
    # repr is used for debugging, logging
    def __repr__ (self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
        
    # used for display
    def __str__ (self):
        return "Employee('{}' - '{}')".format(self.full_name(), self.email) # Don't miss the parenthesis for full name

    def __add__(self, other):
        return self.pay + other.pay


# An inheritance of the base class employee 1
class Developer_2(Employee_2):
    raise_amount = 1.2

    # add new attribute
    def __init__(self, first, last, pay, prog_lang):
        # this is better approach then below, as it will be useful in 
        # multiple inhertence
        super().__init__(first, last, pay)
        # Employee_3.__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager_2(Employee_2):
    def __init__(self, first, last, pay, employees=None):
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emply in self.employees:
            print('-->' + emply.full_name())




# data and functions associated with a class are called attributes
#instances of a class

# Use of instance
emp_1 = Employee_2('Check', 'Mate', 65000)
emp_2 = Employee_2('User', 'Check', 70000)
# emp_2 = Developer_2('Test', 'User', 65000, 'C++')

# mgr_1 = Manager_2('Björn', 'Besser', 90000, [emp_1])


# Can't pass the programming lang to Employee class,
# it has not attribute
# emp_2 = Employee_2('Test', 'User', 65000, 'C++')

# emp_str_1 = 'Vipul-Sinha-75000'
# emp_3 = Employee_2.from_string(emp_str_1)
# print(emp_3.email)
# print(emp_3.pay)
# my_day = datetime.date(2017, 1, 31)
# print(my_day)
# print(emp_3.is_workday(my_day))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# # print(help(Developer_2))
# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)

# print(emp_1.prog_lang)
# print(emp_2.prog_lang)
# print(mgr_1.print_emp())

# mgr_1.add_emp(emp_2)

# print(mgr_1.print_emp())

# mgr_1.remove_emp(emp_1)

# print(mgr_1.print_emp())

# to check whether is class of inhereted
# print(isinstance(mgr_1, Manager_2))
# print(isinstance(emp_2, Manager_2))
# print(isinstance(mgr_1, Employee_2))

# print(issubclass(Manager_2, Employee_2))

print(emp_1)
print(emp_1.__repr__()) # or print(repr(emp_1))
print(emp_1.__str__()) # or print(str(emp_1))

# print(int.__add__(1,2)) # print(1+2)
# print(str.__add__('A','B')) # print('A'+'B')

# print(emp_1.__add__(emp_2)) or
print(emp_1 + emp_2)

# Classes 3
print('####Classes_3#####')

import datetime
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

    # static method
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday==6:
            return False
        return True

    # magic / operator overloading / dunder
    # repr is used for debugging, logging
    def __repr__ (self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
        
    # used for display
    def __str__ (self):
        return "Employee('{}' - '{}')".format(self.full_name(), self.email) # Don't miss the parenthesis for full name

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


# An inheritance of the base class employee 1
class Developer_3(Employee_3):
    raise_amount = 1.2

    # add new attribute
    def __init__(self, first, last, pay, prog_lang):
        # this is better approach then below, as it will be useful in 
        # multiple inhertence
        super().__init__(first, last, pay)
        # Employee_3.__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager_3(Employee_3):
    def __init__(self, first, last, pay, employees=None):
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emply in self.employees:
            print('-->' + emply.full_name())




# data and functions associated with a class are called attributes
#instances of a class

# Use of instance
emp_1 = Employee_3('Check', 'Mate', 65000)
emp_2 = Employee_3('User', 'Check', 70000)
# emp_2 = Developer_3('Test', 'User', 65000, 'C++')

# mgr_1 = Manager_3('Björn', 'Besser', 90000, [emp_1])


# Can't pass the programming lang to Employee class,
# it has not attribute
# emp_2 = Employee_3('Test', 'User', 65000, 'C++')

# emp_str_1 = 'Vipul-Sinha-75000'
# emp_3 = Employee_3.from_string(emp_str_1)
# print(emp_3.email)
# print(emp_3.pay)
# my_day = datetime.date(2017, 1, 31)
# print(my_day)
# print(emp_3.is_workday(my_day))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# # print(help(Developer_3))
# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)

# print(emp_1.prog_lang)
# print(emp_2.prog_lang)
# print(mgr_1.print_emp())

# mgr_1.add_emp(emp_2)

# print(mgr_1.print_emp())

# mgr_1.remove_emp(emp_1)

# print(mgr_1.print_emp())

# to check whether is class of inhereted
# print(isinstance(mgr_1, Manager_3))
# print(isinstance(emp_2, Manager_3))
# print(isinstance(mgr_1, Employee_3))

# print(issubclass(Manager_3, Employee_3))

print(emp_1)
print(emp_1.__repr__()) # or print(repr(emp_1))
print(emp_1.__str__()) # or print(str(emp_1))

# print(int.__add__(1,2)) # print(1+2)
# print(str.__add__('A','B')) # print('A'+'B')

# print(emp_1.__add__(emp_2)) or
# print(emp_1 + emp_2)

print(len(emp_1))