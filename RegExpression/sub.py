import re

txt = "The rain in Spain"


#repalces the matches woth the text of your choice
x = re.sub("\s","9",txt)
print(x)



#you can cpontrol the number of replacements by specifying the count parameter
z = re.sub("\s","9",txt,2)
print(x)
