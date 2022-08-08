mylist = ["Mohammed","Zina"]
print(mylist)
mylist.append("Abdalla") #use append() when i want to add to end of list
print(mylist)


#to insert item with specified index use insert()
mylist1 = ["Oday","Mohammed"]
print(mylist1)
mylist1.insert(1,"Hind")
print(mylist1)


#to append elements from another list to a list, use extend()
names = ["mustafa","ahmed","mohammed"]
age= [24,20,33]
names.extend(age)
print(names)


#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
