thisdict = {
    "brand":"ford",
    "model":"mustang",
    "year" : 1955
    }
print(thisdict)
thisdict.pop("model")#removes item with specified key name
print(thisdict)

#popitem() removes the last inserted item


thisdict1 = {
    "brand":"ford",
    "model":"mustang",
    "year" : 1955
    }
thisdict1.popitem()

print(thisdict1)


#clear() method empties the dictionary
thisdict = {
    "brand": "Ford",
  "model": "Mustang",
  "year": 1964
    }

thisdict.clear()
print(thisdict)
