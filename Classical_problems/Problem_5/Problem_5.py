import time

def isPalindrome(string):
        
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

def checkTens(string, index):

    for i in range(0, index + 1):
        if int(string[len(string)-1-i]) >= 10:
            return True
    return False

def fixTens(string, index):
    blabla = 0
    for i in range(1, index + 1):
        if int(string[len(string)-1-i]) >= 10:
            string[len(string)-1-i] = string[len(string)-1-i][1]
            string[len(string)-2-i] = str(int(string[len(string)-2-i])+1)
        else:
            blabla+=1
        if blabla > 2:
            break
    return string;

def nextPalindrome(string):

    for i in range(0, int(len(string)/2)):
        first = string[i]
        last = string[len(string)-1-i]
        if first > last:
            string[len(string)-1-i] = "" + first
        elif first < last:
            string[len(string)-1-i] = first
            string[len(string)-2-i] = str(int(string[len(string)-2-i])+1)
        string = fixTens(string, len(string)-2-i)

    return "".join(string)

def func():

    f = input()

    b = []

    for i in range(0, int(f)):
        
        a = input()
        temp_list = list(a)
        if isPalindrome(temp_list):
            temp2_list = list(str(int(a)+1))
            if isPalindrome(temp2_list):
                b.append("".join(temp2_list))
            else:
                heh = nextPalindrome(temp2_list)
                while not isPalindrome(heh):
                    heh = nextPalindrome(list(heh))
                b.append(heh)
        else:
            heh = nextPalindrome(temp_list)
            while not isPalindrome(heh):
                heh = nextPalindrome(list(heh))
            b.append(heh)
                

    for num in b:
        print (num)


t1=time.time()
func()
t2=time.time()
#print (t2-t1)
