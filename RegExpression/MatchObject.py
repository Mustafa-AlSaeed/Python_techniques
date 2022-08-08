import re

txt = "the rain in Spain"
x = re.search("ai",txt)
print(x)#this will print an object



#.span() return a tuple containing the start-, and end positions of the match
#.string returns the string passed into the function
#.group() returns the part of the string where the was a match



#Print the position (start- and end-position) of the first match occurrence.
#The e regular expression looks for any words that starts with an upper case "S"


x = re.search(r"\bS\w+", txt)
print(x.span())


#print the string intp the function
x = re.search(r"\bS\w+", txt)
print(x.string)





#print the part of the strinf where there was a match
#the regular expression looks for any words that starts with an upper case "S":
x = re.search(r"\bS\w+", txt)
print(x.group())
