#arguments

def my_function(name):
    print(name + " Al-Saeed")

my_function("Abdulla")
my_function("Mohammed")
my_function("Ahmed")


#a function can have many argumenst, but same number should be called

#arbitruary arguments, *args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition
#This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(*players):
    print("the following is gonna be successful and dayen ", players[0]) #if i remove index it prints all

my_function("Mustafa Al-Saeed","ronaldo","beckham")
    


#keyword arguments
def my_function(child3, child2, child1):
    print("the youngest child is child 3 "+ child3)

my_function(child1 = "Mo",child2="moose",child3="Hamoody")

#aribtruary keyword arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function,
#add two asterisk: ** before the parameter name in the function definition
#This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_function(**kid):
    print("his last name is " + kid["lname"])

my_function(fname = "Mustafa", lname = "AlSaeed")

