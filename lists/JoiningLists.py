list1 = [1,2,3]
list2 = ["a","aA","nn"]
print(list1+list2)

#or
for x in list2:
    list1.append(x)
print(list1)

#or
list1.extend(list2)
print(list1)
