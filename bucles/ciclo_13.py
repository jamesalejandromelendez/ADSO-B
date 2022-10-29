"""Solicitar al usuario un número de hasta 9 dígitos e
imprimirlo en orden contrario. Ej. digito 6754 imprimo 4576"""

N=int(input('Ingrese un numero '))


c9= N%10 
c8= int((N%100)/10)
c7= int((N%1000)/100)
c6= int((N%10000)/1000)
c5= int((N%100000)/10000)
c4= int((N%1000000)/10000)
c3= int((N%10000000)/10000)
c2= int((N%100000000)/10000)
c1= int((N%1000000000)/10000)

print(str(c4)+str(c3)+str(c2)+str(c1))