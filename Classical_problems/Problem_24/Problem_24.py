#import time

def func():

    f = input()

    b = []

    for i in range(0, int(f)):
        
        a = input()

        fact = 1
        for i in range(1, int(a)+1):
            fact *= i
        b.append(fact)
            

    for num in b:
        print (num)

#t1 = time.time()
func()
#t2 = time.time()
#print (t2-t1)

