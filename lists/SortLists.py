thislist =["orange","Mango","kiwi","pineapple"]
thislist.sort() #ordered aphabetically
print(thislist)

thislist1 = [11,100,20,12,33,4,5,19090,12,0]
thislist1.sort() #ordered numerically
print(thislist1)


#to sort descinding
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True) 
print(thislist)

#to sort descedning
thislist1 = [100,20,3,4,55,85,34,44]
thislist1.sort(reverse=True)
print(thislist1)


#custumize sort()

def myfunc(n):
    return abs(n-50)

thislist=[100,50,65,82,23]
thislist.sort(key = myfunc)
print(thislist)

    
#sort() is case sensitive (it will always put capital letters first)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#if you want to make it non case sensetive
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key =str.lower)
print(thislist)


#to reverse oder of list, regardless of the alphabet
thislist = ["Mustafa","Oday","Al-SAeed"]
thislist.reverse()
print(thislist)
