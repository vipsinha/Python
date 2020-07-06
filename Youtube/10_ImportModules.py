import my_module




# to take all, but tracking problem
#from my_module import * 

import sys
# if other directory is used for the import library
# sys.path (/path to import module)



# Import 1
print('####Import_1#####')

# courses = ['English', 'Hindi', 'Maths', 'Science', 'SST']
courses = [1,2,3,4,5]
#index = my_module.find_index(courses,'Maths')
index = my_module.find_index(courses,4)
print(index)

# Import 2
print('####Import_2#####')

courses = ['English', 'Hindi', 'Maths', 'Science', 'SST']
index = my_module.find_index(courses,'Maths')
print(index)

# Import 3
print('####Import_3#####')

import my_module as mm
courses = ['English', 'Hindi', 'Maths', 'Science', 'SST']
index = mm.find_index(courses,'SST')
print(index)

# Import 4
print('####Import_4#####')

from my_module import find_index
courses = ['English', 'Hindi', 'Maths', 'Science', 'SST']
index = find_index(courses,'Science')
print(index)

# Import 5
print('####Import_5#####')

from my_module import find_index, test
courses = ['English', 'Hindi', 'Maths', 'Science', 'SST']
index = find_index(courses,'Science')
print(index)
print(test)

# Import 6
print('####Import_6#####')

from my_module import find_index as fi, test as t
courses = ['English', 'Hindi', 'Maths', 'Science', 'SST']
index = fi(courses,'English')
print(index)
print(t)

# Import 7
print('####Import_7#####')

courses = ['English', 'Hindi', 'Maths', 'Science', 'SST']
index = fi(courses,'English')
# print(index)
# print(t)
# paths added in the python
print(sys.path)

# Import 9
print('####Import_9#####')

import random
courses = ['English', 'Hindi', 'Maths', 'Science', 'SST']
courses_random = random.choice(courses)
print(courses_random)

# Import 10
print('####Import_10#####')

import math
rad = math.radians(90)
print(rad)

sin_value = math.sin(rad)
print(sin_value)

# Import 11
print('####Import_11#####')

import datetime
today = datetime.date.today()
print(today)

import calendar
leap_year = calendar.isleap(2020)
print(leap_year)

# Import 12
print('####Import_12#####')

import os
print(os.getcwdb())
# shows all the libraries
print(os.__file__)

# Import 13
print('####Import_13#####')

import antigravity


