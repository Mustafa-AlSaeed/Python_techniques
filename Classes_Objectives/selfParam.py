#The self parameter is a reference to the current instance of the class,
#and is used to access variables that belongs to the clas
#It does not have to be named self , you can call it whatever
#you like, but it has to be the first parameter of any function in the class:
#for example

class Person:
    def __init__(mySillyObject, name, age):
        mySillyObject.name = name
        mySillyObject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John",36)
p1.myfunc()

print(p1.age)
print(p1.name)

p1.age = 40

print(p1.age)
