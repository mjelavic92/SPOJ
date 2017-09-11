#import time


def func():

    f = input()

    b = []

    for i in range(0, int(f)):
        
        d, e = input().split(" ")

        d = int(d)
        e = int(e)

        if d == e:
            if d == 0:
                b.append("0")
            elif d % 2 == 0:
                b.append(str(int(d**2 / (d/2))))
            else:
                b.append(str(d+e-1))
        elif d == (e + 2):
            if d % 2 == 0:
                b.append(str(d+e))
            else:
                b.append(str(d+e-1))
        else:
            b.append("No Number")

    for num in b:
        print (num)

#print (int(reverseNumber(list("1234500"))))

#t1 = time.time()
func()
#t2 = time.time()
#print (t2-t1)

