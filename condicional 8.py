minutos = int(input("cuantos minutos?"))
minutos_1 = minutos * 67 - 1
minutos_3 = (minutos - 3)
if minutos <= 3:
    print (" en total son ",minutos_1)
else:
    print ("en total son ", minutos_3 * 50 + 200)