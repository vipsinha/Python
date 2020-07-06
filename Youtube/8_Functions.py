# Functions 1
print('####Functions_1#####')

def hello_func_1():
    pass

print(hello_func_1())

# Functions 2
print('####Functions_2#####')

def hello_func_2():
   pass
print(hello_func_2)

# Functions 3
print('####Functions_3#####')

def hello_func_3():
    print('Hello Function!')

hello_func_3()

# Functions 4
print('####Functions_4#####')

def hello_func_4():
    return 'Hello Function with return'

print(hello_func_4())

# Functions 5
print('####Functions_5#####')

def hello_func_5():
    return 'Hello Function with return'

print(hello_func_5().upper())

# Functions 6
print('####Functions_6#####')

def hello_func_6(greeting):
    return '{} World'.format(greeting)

print(hello_func_6('Hello'))
print(hello_func_6('Cool'))

# Functions 7
print('####Functions_7#####')

def hello_func_7(greeting, name = 'You'):
    return '{} World by {}'.format(greeting, name)

print(hello_func_7('Hello'))
print(hello_func_7('Hello', 'Vipul'))

# Functions 8
print('####Functions_8#####')

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='Vipul', age=29)

# Functions 9
print('####Functions_9#####')

def func_9(*args, **kwargs):
    print(args)
    print(kwargs)

coureses = ['Math', 'Art'] # List
student_info = {'name': 'Vipul', 'age': '29'} # dictionary
func_9(*coureses, **student_info)