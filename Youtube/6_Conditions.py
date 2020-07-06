# Condition 1
print('####Condition_1#####')
if True:
    print('Condition is true')
elif False:
    print('Condition is false')
else:
    print('Condition is Grey')

# Condition 2
print('####Condition_2#####')
language = 'Python'
if language == 'Python':
    print('I am in Python')

# Condition 3
print('####Condition_3#####')
language = 'Python'
if language == 'Java':
    print('I am in Python')
else:
    print('Not in python')

# Condition 4
print('####Condition_4#####')
language = 'Java'
if language == 'Python':
    print('I am in Python')
elif language == 'Java':
    print ('I am in Java')
else:
    print('Not in python')

# Condition 5
print('####Condition_5#####')
user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad credential')

# Condition 6
print('####Condition_6#####')
user = 'Admin'
logged_in = False
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad credential')

# Condition 7
print('####Condition_7#####')
user = 'Admin'
logged_in = False
if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad credential')

# Condition 8
print('####Condition_8#####')
user = 'Admin'
logged_in = True
if not logged_in:
    print('Admin Page')
else:
    print('Bad credential')

# Condition 9
print('####Condition_9#####')
user = 'Admin'
logged_in = True
if not logged_in:
    print('Admin Page')
else:
    print('Bad credential')

# Condition 10
print('####Condition_10#####')
a = [1,2,3]
b = [1,2,3]
print(id(a))
print(id(b))
print (a == b)

# Condition 11
print('####Condition_11#####')
a = [1,2,3]
b = [1,2,3]
print(id(a))
print(id(b))
print (a is b)

# Condition 12
print('####Condition_12#####')
a = [1,2,3]
a = b
print(id(a))
print(id(b))
print (a is b)

# Condition 13
print('####Condition_13#####')
a = [1,2,3]
a = b
print (id(a) == id(b))
