import platform

x = platform.system()
print(x)


#There is a built-in function to list all the function names
#(or variable names) in a module. The dir() function:

y = dir(platform)
print(y)
