# Print variable messages
courses = ['Eng', 'Hindi', 'Math', 'Physics', 'CompSci']

print(courses)
print(len(courses))
print(courses[0])
print(courses[4])
print('Last item = ' + courses[-1])
# print('courses[0:2] = ' + courses[0:2])
print(courses[0:2])
# print(courses[-1:2])

# add item item to our list
courses.append('Art')
print(courses)

# add item item to our list at sepcific location
courses.insert(2,'Bio')
print(courses)

# add item item to our list at sepcific location
courses_add = ['Music', 'PhysicalEdu']
courses.insert(0,courses_add)
print(courses)
print(courses[0])


# add item item to our list at sepcific location
courses_extend = ['Games', 'Cooking']
courses.extend(courses_extend)
print(courses)

# remove item item from list
courses.remove('Math')
print(courses)

# remove last item item from list
popped = courses.pop()
print(courses)
# print the item popped
print(popped)


# reverse the list
courses.reverse()
print(courses)



# sort the list
# remove last item item from list else
# parenthesis materials cause issue
popped = courses.pop()
print(popped)
print(courses)

# Now sorting can be done
courses_sorted = sorted(courses)
print('coureses =')
print(courses)
print('courses_sorted =')
print(courses_sorted)

# Now sorting can be done
courses.sort()
print(courses)


num = [1,5,2,4,3]
print(num)
#ascending order
num.sort()
print(num)
#descending order
num.sort(reverse=True)
print(num)

print(min(num))
print(max(num))
print(sum(num))

print(courses.index('Games'))
# print(courses.index('Cooking'))

print('Games' in courses)
print('Cooking' in courses)

print('#####Subjects#####')
for sub in courses:
    print(sub)

print('#####Subjects with index#####')
for index, sub in enumerate(courses):
    print(index, sub)    

print('#####Subjects with index starting at 2#####')
for index, sub in enumerate(courses, start=2):
    print(index, sub)      

courses_str = ' - ' .join(courses)  
print(courses_str)

courses_str_reverse = courses_str.split(' - ')  
print(courses_str_reverse)

# tupple is Immutable
courses_1 = courses
print(courses)
print(courses_1)

courses_1[0] = 'GermanLanguage' 
print(courses)
print(courses_1)

tuple_1 = ('English', 'Hindi', 'maths')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple can't be modified, checked based on the parenthesis
#tuple_1[0] = 'Art'


# Sets
courses_set = {'History', 'Maths', 'Physics'}
print(courses_set)

courses_set = {'History', 'Maths', 'Physics', 'Maths'}
print(courses_set)

#Sets intersection
courses_set_1 = {'History', 'Art', 'Physics', 'Language'}
print(courses_set.intersection(courses_set_1))
print(courses_set.difference(courses_set_1))
print(courses_set.union(courses_set_1))

#empty list
empty_list = []
empty_list = list() # this is same
print(empty_list)

#empty tuple
empty_tuple = ()
empty_tuple = tuple() # this is same
print(empty_tuple)

#empty sets
empty_sets = {} # this is not right, it will create a dictionary
empty_sets = set()
print(empty_sets)

# to see the attributes can be used
# print(dir(name))

# to get the help
# print(help(str))
# print(help(str.lower))