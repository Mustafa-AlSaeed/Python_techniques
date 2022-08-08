def printWords(x):
    #splitting the string
    x = x.split(' ')

    #iterate words of x
    for word in x:
        if len(word) > 0:
            print (word)


#driver code

x = "I am Mustafa Al-Saeed"
printWords(x)

    
