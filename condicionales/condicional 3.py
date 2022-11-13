num = int(input("digite su numero de 0 a 9999"))
if (num<10):
   print ("su numero es de una cifra")
elif num < 100 :
    print ("el numero es de dos cifras")
elif num < 1000:
    print ("el numero es de tres cifras")
elif num < 10000: 
    print ("el numeo es de cuatro cifras")
elif num < 100000:
    print ("superaste el limite")
