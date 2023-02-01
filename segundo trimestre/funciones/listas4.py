''' 5. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
aleatorios. Solicite al usuario un número para buscar en la lista. Diga cuantas veces está y en que 
posiciones esta. Si no está agréguelo al final de la lista. '''

def buscar(lista):
    veces = 0
    for indice in range(len(lista)):
        if numero == lista[indice]:
            veces += 1
    return veces

def posiciones(lista):
    posiciones = []
    for indice in range(len(lista)):
        if numero == lista[indice]:
            posiciones.append(indice)
    return posiciones

import random

lista=[int(random.random()*100) for i in range (random.randint(10,25))]
print(lista,"\nEl tamaño de la lista es: ", len(lista))

numero = int(input("Ingrese un número para buscar en la lista: "))

posiciones(lista)
buscar(lista)
if buscar(lista) > 0:
    print("El número ingresado está",buscar(lista),"veces.","\nLa posicion del número es: ",posiciones(lista))
else:
    print("El número no está en la lista, así que fue agregado.")
    lista.append(numero)
    print("Lista: ",lista)
"""este codigo no lo hice yo, lo hizo dionigi """   
