import json

#some json:

x = '{ "name":"John", "age":30, "city":"New York"}'

#json.loads() parses x:
y = json.loads(x)

print(x)#will print pyth dictionart
print(y["age"])
