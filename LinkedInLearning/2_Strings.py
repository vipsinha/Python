a = 'Hello, I am Vipul Sinha\n'
b = "I am from delhi\n"
c = """Hello Mr. Vipul Sinha"""
d = 'We want to use don\'t'
e = "\"Hello to Python\""
f = 'lets divide \\'
g = 5

print('***print the string***')
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

print('***length of string***')
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
print(len(str(g)))

print('***lets concenate***')
print(a+b)
print(e+str(g))


print('***lets multiply***')
print((e+str(g)) * 2)

print('***string check***')
string = "abcde"

x1 = [1,2,3]
x2 = [1,2,3]
x3 = x4 = [1,2,3]

x = 'a' in f
y = 'a' in string
z = 'ac' in string
check1 = x1 is x2
check2 = x3 is x4
print("",x,"\n",y,"\n",z,"\n",check1,"\n",check2)
