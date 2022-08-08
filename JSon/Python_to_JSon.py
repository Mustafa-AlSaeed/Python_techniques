import json

#a python object(dict)

x = {
    "name":"Mustafa",
    "Age":"24",
    "Deg":"CVG and CSI"
    }

#converts python(dic) into JSon, json.dumps()
y = json.dumps(x)

#result is JSon string

print(y)
