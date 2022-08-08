#changing tuple values
x = ("apple", "banana", "cherry")
#we know that tuple are unchangable, so we need to convert it to a list first
x = list(x)
x[1] = "Mustafa"
print(x)



#adding to a tuple
y=list(x)
y=y.append("orange")
print(y)


#adding tuple to tuple
x = ("apple", "banana", "cherry")
z = ("Mustafa",)
x += z #(x = x+z)
print(x)


#removing from a tuple (first conv to str)
x = ("apple", "banana", "cherry")
x = list(x)
x.remove("apple")
print(x)
