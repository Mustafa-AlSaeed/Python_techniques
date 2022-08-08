car = {
    "brand":"Dodge",
    "model":"viper",
    "engine":"v12",
    "year":2009
    }

#print all key names in dictionary
for x in car:
    print(x)

#print all values in dictionary
for x in car:
    print(car[x])

#you can use the values() methord to return values of a dectionary
for x in car.values():
    print(x)


#You can use the keys() method to return the keys of a dictionary:

for x in car.keys():
    print(x)

#Loop through both keys and values, by using the items() method:

for x, y in car.items():
    print(x,y)
    


