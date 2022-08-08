#before i import it
#download package:
#open cmd and tell PIP to install paclage you want
#to get this one
#pip install camelcase
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

#This method capitalizes the first letter of each word.
