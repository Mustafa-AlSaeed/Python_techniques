class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self,fname,lname, year):
      Person.__init__(self,fname,lname)
      #or super().__init__(fname, lname)
      self.graduationyear = year #add a graduation year to the student class
      
  def welcome(self):
      print("Welcome ",self.firstname,self.lastname,"to the class of ",self.graduationyear)


x = Student("Hamoody","Al-Saeed",2024)
print(x.graduationyear)
x.welcome()
