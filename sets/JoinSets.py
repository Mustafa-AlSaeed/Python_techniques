set1 = {"a","b","c"}
set2 = {1,2,3}

set3 = set1.union(set2) #union() is how to add sets
print(set3)


#update() inserts set2 to  into set1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


#keep only the diplicates of two sets
x = {"apple","body","boy"}
y = {"body","arm","legs"}

x.intersection_update(y)

print(x)


#the intersection method will return a new set, that only contains the items that
#present in both sets


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


#keep all, but not the duplicates

