
#Object programming
class person:
    #constructor
    def __init__(self):
        print("Our class is created")
    def __init__(self,id):
        print("Our class is created")
        self.id = id
        print("id is = {}".format(self.id))
        
    #destructor
    def __del__(self):
        print("Our class is destructed")
        print("id is = ",self.id)
        
    #member function
    #self is like void
    def setPersonName(self,firstName,lastName):
        person.firstName = firstName
        person.lastName = lastName
    def printPersonName(self):
        print(person.firstName,person.lastName)

#Object is creted
#calling instructor automatically        
person1 = person(5)
#calling member function
person1.setPersonName("Vipul","Sinha")
person1.printPersonName()
#calling destructor
#person1.__del__()
