mylist =["apple","banana","orange"]
mylist[1] = "cherry"
print(mylist)



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#change the second value by replacing it by two values.
#If you insert more items than you replace, the new items will be inserted...
#where you specified, and the remaining items will move accordingly.
thislist1 = ["apple", "banana", "cherry"]
thislist1[1:2] = ["blackcurrant", "watermelon"]
print(thislist1)


#change the second and third value by replacing it with 1 value
thislist2 = ["apple", "banana", "cherry"]
thislist2[1:3] = ["blackcurrant"]
print(thislist2)



#INSERT!!!!!!!!!!!!!!!!!!!!!!!

mylist1 = ["Mohammed","Mustafa","Zina","ahmed","mama","baba"]
mylist1.insert(2,"watermelon") #insert(index,whatYouWantToInsert) to insert something
print(mylist1)


