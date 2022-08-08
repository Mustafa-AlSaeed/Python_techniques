#The search() function searches the string for a match, and returns a Match object if there is a match.
#If there is more than one match, only the first occurrence of the match will be returned:


import re

txt = "the rain in Spain"


#ex: search foor white space
x=re.search("\s",txt)
print("first white space is in position",x.start())

z = re.search("Spain",txt)
if z:
    print(True)
else:
    print(False)

#if no matches are foind the valie None is returned
q = re.search("Port",txt)
print(q) 
