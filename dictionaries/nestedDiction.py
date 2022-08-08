#create three dicionaries, then add all into one direction

child1 = {
    "name":"Emil",
    "year":"2004",
    }

child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

#this dictionary has all the three dictionaries 
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily.values())
print(myfamily.items())
