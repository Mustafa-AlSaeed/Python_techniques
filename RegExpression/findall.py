import re

txt = "the rain in Spain"

#prints a list of all a matches

x = re.findall("ai",txt)

print(x)


#the list contains the matches in the order they are found in
#if no matches are foind, an empty list is returned

y = re.findall("portugal",txt)

print(y)


