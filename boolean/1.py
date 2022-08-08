#bool() allows you to evaluate any value
a = 200
b = 3300

if a > b:
    print("A is bigger than B")
else :
    print("B is bigger than A")


print(bool("Hello"))
print(bool(15))




def myFunc():
    return False

if myFunc():
    print("yes")
else:
    print("no")


    

#isinstance() function can be used to check whether an object is of a certain data types

x = 200
print(isinstance(x,int))
    
