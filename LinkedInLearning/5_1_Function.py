
#Simple function
def funcName(a,b):
    if a>b:
        print("a is greater than b")
    else:
        print("a is smaller than b")

#Hello Function
def funcHello(name):
    print("Hello",name)

#Return function
def funcSum(a,b):
    return(a+b)

#Good coding
def funcStudentScore(name = "Vipul", marks = 100):
    print(name,"scored",marks,"marks")

#Pass an array
def funcStudentMarks(name = "Vipul", *marks):
    print(name)
    print(marks)
