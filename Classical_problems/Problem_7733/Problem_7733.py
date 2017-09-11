#import time

def sumSquaredDigits(num):

    sumSquared = 0
    for a in num:
        sumSquared += int(a)**2

    return "".join(str(sumSquared))

def func():

    f = input()
    #f="204"

    f = list(f)

    testSet = set([1])
    i = 1
    cycle = sumSquaredDigits(f)
    
    while int(cycle) not in testSet:
        testSet.add(int(cycle))
        cycle = sumSquaredDigits(list(cycle))
        i+=1

    if cycle == "1":
        print (i)
    else:
        print ("-1")
        

func()
        

    

