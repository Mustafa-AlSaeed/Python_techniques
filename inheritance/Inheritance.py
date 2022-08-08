#create a parent class, w fname and lname prop, and printname method

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printName(self):#you have to pit self as param
        print(self.fname,self.lname)

#use the person class to crete an object, adn then execute the printame method

p1 = Person("Mustafa ","Al-Saeed")
p1.printName()


