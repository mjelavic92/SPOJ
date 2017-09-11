def func():

    suma = 0
    for i in range(0,10):
        f = input()
        f = int(f)
        if abs(suma-100) >= abs(suma+f-100):
            suma+=f

    return suma

suma = func()
print (suma)
        

