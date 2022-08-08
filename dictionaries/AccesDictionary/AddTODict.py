thisdict = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
    }
#the ones on the left is called keys, the ones on the right are the values
print(thisdict)
print(thisdict["model"])

#There is also a method called get() that will give you the same result
x = thisdict.get("model")
print(x)

#The keys() method will return a list of all the keys in the dictionary.
y = thisdict.keys()
print(y)
#The values() method will return a list of all the values in the dictionary.
r = thisdict.values()
print(r)




#to add a key and its value
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

z = car.keys()
print(z)
car["colour"] = "Offwhite"
w = car.keys()
print(w)



#The items() method will return each item in a dictionary, as tuples in a list.

q = thisdict.items()
print(q)


#to check if key exists
if "brand" in car:
    print (True)


