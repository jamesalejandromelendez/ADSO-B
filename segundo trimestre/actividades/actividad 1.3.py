import random
x = random.randint(1,10)
n = 0
cont = 0
while n != x:
    n = int(input("escriba un numero"))
    cont += 1
    if n > x:
        print(n, "esmuy grande")
    else:
        print(n, "es muy pequeño")
print ("numero de intentos =",cont)