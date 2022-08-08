#iterators uses, iter() and next()

mytuple = ("mustafa","oday","alsaeed")
myiterator = iter(mytuple)

print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
#if i do one more its AN ERROR

mystr = "banana"

myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
