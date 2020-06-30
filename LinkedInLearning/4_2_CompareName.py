#Compare name

name = input("Names ? ")
seasonName = input("Season Names ? ")

if name == "Vipul":
    print("He is the owner")
    print("His name is",name)
elif name == "Summer":
    print("She is the good")
    print("His name is",name)
elif name == "July":
    print("This is season")
    if name == seasonName :
        print("Season name",seasonName)
    else:
        print("Season name not match",name,"!=",seasonName) 
    print("This is end")
else:
    print("The name entered is not valid")


