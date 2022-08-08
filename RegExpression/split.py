#The split() function returns a list where the string has been split at each match:

import re

txt = "the rain in Spain"

#split at each whote space characters
x = re.split("\s",txt)

print(x)

#split the string only at the first occurence
z = re.split("\s",txt,1)
print(x)
