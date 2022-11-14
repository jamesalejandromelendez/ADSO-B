def natural(num):
    cont=0
    while cont*(cont+1)<=2*num:
        cont+=1
    print ("El número natural mas pequeño es:",cont)
num = int(input("Ingrese el número máximo  "))
natural(num)