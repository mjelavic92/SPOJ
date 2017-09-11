#import time

def func():

    f = input()

    b = []

    for i in range(0, int(f)):
        
        d, e = input().split(" ")

        print (d, e)

    for num in b:
        print (num)

#t1 = time.time()
func()
#t2 = time.time()
#print (t2-t1)

