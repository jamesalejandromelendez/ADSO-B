''' 7. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
aleatorios. Encuentre la suma y el promedio de los números de la lista. '''

def suma(lista):
    suma=0
    for indice in range(len(lista)):
        suma += lista[indice]
    return suma

def prom(lista):
    suma=0
    for indice in range(len(lista)):
        suma += lista[indice]
    promedio = suma//len(lista)
    return promedio

import random

lista=[int(random.random()*100) for i in range (random.randint(10,25))]
print(lista,"\nEl tamaño de la lista es: ", len(lista))

print('La suma es de la lista es:',suma(lista),'Y el promedio es: ',prom(lista))
"""este codigo no lo hice yo, lo hizo dionigi """  