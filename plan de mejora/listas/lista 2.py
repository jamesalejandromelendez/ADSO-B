"""Dada una lista L de N elementos, diseñar un algoritmo que calcule de forma independiente la suma de
los números pares y la suma de los números impares."""
from random import randint
lista=[]
suma1,suma2,suma3,suma4 = 0,0,0,0
for i in range(2):
    row = [(randint(0,10)) for i in range(2)]
    lista.append(row)
print(lista)
for i in (lista[0]):
    if i % 2 == 0:
        suma1 += i
for i in (lista[1]):
    if i % 2 == 0:
        suma1 += i
print("la suma de numeros pares es: ",suma1)

for i in (lista[0]):
    if i % 2 != 0:
        suma2 += i
for i in (lista[1]):
    if i % 2 != 0:
        suma2 += i
print("la suma de numeros impares es: ",suma2)

