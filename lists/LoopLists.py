mylist = ["Messi","Zidane","Ronaldinho"]
for x in mylist:
    print(x)
#the two ways are possible ways of looping through a list,
#first one is using elements
#second one  is using the index

for i in range(len(mylist)):
    print(mylist[i])



#now using while loop

thislist = ["Mustafa","Oday","Al-Saeed"]
i = 0
while i < len(thislist):
    print (thislist[i])
    i = i+1
