age = 24
name = "Mustafa Al-Saeed"

print(str(age)+' '+name)


ages = 33
txt = "my name is mohammed and my age is {}"

print(txt.format(ages))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
#to make sure that the right word falls in its place you should indexing, like so

quantity = 4
orderNum = 333202
price = 4455
myOrder = "I want {0} playstations and my order number is {1}, i am willing to pay {2}"
print(myOrder.format(quantity,orderNum,price))

//#format() did all the work for us
