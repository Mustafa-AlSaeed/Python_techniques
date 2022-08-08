class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def my_function(self):
        print("hellp my name is "+ self.name)

p1 = Person("John",36)
p1.my_function()


print(p1.name)
print(p1.age)




