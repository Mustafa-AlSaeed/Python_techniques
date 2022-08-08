thisdict = {
    "brand":"ford",
    "model":"mustang",
    "year":1964
    }
x = thisdict["model"]
print(x)


#There is also a method called get() that will give you the same result:

y = thisdict.get("model")
print(y)
