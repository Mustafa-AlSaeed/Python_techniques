#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern

import re #used to wa=ork with regEx

txt = "the rain in Spain"

#search the string

x = re.search("^The.*Spain$", txt)

if x :
    print("Yes , match")

else:
    print("no match")

y = re.search("Mustafa",txt)
if y:
    print(True)
else:
    print(False)
    
