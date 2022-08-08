#Array is like a list in python

cars = ["ford","volvo","bmw"]

x = cars[0]
print(x)

cars[0] = "Toyota"
y=cars[0]
print(y)


z = len(cars)
print(z)

#to loop array elements
for x in cars:
    print(x)

#to add an element to the array, use append()

cars.append("honda")
print(cars)



#you can use pop() method to remove an element from the array

cars.pop(1)#uses index
print(cars)


#you can use remove
cars.remove("bmw")
print(cars)



