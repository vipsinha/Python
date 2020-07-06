my_student = {'name': 'Vipul', 'age': '29', 'courses' : ['Math', 'CompSci']}


print(my_student)
print(my_student['name'])

my_student_new = {1: 'Vipul', 2: '29', 'courses' : ['Math', 'CompSci']}
print(my_student_new[2])

print(my_student.get('name'))
print(my_student.get('phone'))
print(my_student.get('phone', 'Not Found'))

my_student['phone'] = '123-5555'
print(my_student.get('phone', 'Not Found'))

my_student['name'] = 'Sinha'
print(my_student)

my_student.update({'name': 'Mr Sinha','age':'29.5', 'phone' : '5555-1234'})
print(my_student)

del my_student['age']
print(my_student)

courses = my_student.pop('courses')
print(my_student)
print(courses)

print(len(my_student))
print(my_student.keys())
print(my_student.values())
print(my_student.items())

for keys in my_student:
    print(keys)

for keys,values in my_student.items():
    print(keys, values)    