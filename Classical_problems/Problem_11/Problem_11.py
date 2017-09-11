#import time

def func():

    f = input()

    b = []

    for i in range(0, int(f)):
        
        a = input()

        fives = 0
        i = 1
        while 5**i <= int(a):
             fives += int(int(a) / (5**i))
             i+=1
        b.append(fives)

    for num in b:
        print (num)

#t1 = time.time()
func()
#t2 = time.time()
#print (t2-t1)

