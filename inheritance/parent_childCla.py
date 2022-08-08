class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printName(self):
        print(self.fname,self.lname)

        #create a child class

class Student(Person):
    pass #use this when you do npt want to add any other prop or methods to class (it will have the same ones
        


p1 = Person("Mustafa","Al-Saeed")
p1.printName()
x = Student("Ahmed","Oday")
x.printName()
