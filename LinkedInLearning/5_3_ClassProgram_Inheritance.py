
#Object programming
class parent:
    
    #constructor
    def __init__(self):
        print("Our class is created")
        
    #destructor
    def __del__(self):
        print("Our class is destructed")       

    #member function
    #self is like void
    def printParent(self):
        print(self.value1)
 
    #member variables
    value1 = "Father"
    value2 = "Mother"

class elderParent:
    value3 = "GrandFather"
    value4 = "GrandMother"

class child (parent,elderParent):
    pass

#Object is creted
#calling instructor automatically        
parent1 = parent()
child1 = child()
#calling member function
#parent1.setPersonName("Vipul","Sinha")
parent1.printParent()
print(child1.value2)
print(child1.value3)
print(child1.value4)
#calling destructor
parent1.__del__()
