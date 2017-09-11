#import time

def reverseNumber(string):

    for i in range(0, int(len(string)/2)):
        temp_val = string[i]
        string[i] = string[len(string)-1-i]
        string[len(string)-1-i] = temp_val

    return "".join(string)


def func():

    f = input()

    b = []

    for i in range(0, int(f)):
        
        d, e = input().split(" ")

        b.append(int(reverseNumber(list(str(int(reverseNumber(list(d))) + int(reverseNumber(list(e))))))))

    for num in b:
        print (num)

#print (int(reverseNumber(list("1234500"))))

#t1 = time.time()
func()
#t2 = time.time()
#print (t2-t1)

