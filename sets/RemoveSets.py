thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #will rasise an error if doesnt exist
print(thisset)

#or

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #will not raise an error if doesnt exist
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.clear()#empties the set
print(thisset)
