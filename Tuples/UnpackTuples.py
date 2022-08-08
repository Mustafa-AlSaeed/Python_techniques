#to pack tuples
fruits = ("apple", "banana", "cherry")
#python also allows us to unpack

(red,yellow,green) = fruits

print(red)
print(yellow)
print(green)





#now if use Asterisk*
#If the number of variables is less than the number of values, you can add an *
#to the variable name and the
#values will be assigned to the variable as a list

players = ("messi","zidane","tevez","beckham","giggs")
(barcelona, madrid, *manU) = players
print(barcelona)
print(madrid)
print(manU)
