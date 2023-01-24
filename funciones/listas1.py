'''1. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. De cada elemento de la lista diga si el elemento está por encima del promedio, debajo
del promedio o es igual al promedio de todos los números de la lista.'''


def promedio(lista):
    suma=0
    for indice in range(len(lista)):
        suma += lista[indice]
    promedio = suma//len(lista)
    return promedio

import random

tam=random.randint(10,25)
lista=[]

for indice in range(tam):
    lista.append(round(random.random()*100))
print(lista,"\nEl tamaño de la lista es: ", len(lista))

print('El promedio es: ',promedio(lista))

for indice in range(len(lista)):
    if lista[indice] == promedio(lista):
        print("El valor ",lista[indice],"es igual al promedio ",promedio(lista))
    elif lista[indice] > promedio(lista):
        print("El valor ",lista[indice],"es mayor al promedio ",promedio(lista))
    elif lista[indice] < promedio(lista):
        print("El valor ",lista[indice],"es menor al promedio ",promedio(lista))
"""este codigo no lo hice yo, lo hizo dionigi """        