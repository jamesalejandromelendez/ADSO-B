"""Escribir un algoritmo que permita sumar el número
de elementos positivos y el de negativos de una tabla
T de n filas y m columnas."""
from random import randint
lista=[]
suma1,suma2,suma3,suma4 = 0,0,0,0
for i in range(2):
    row = [(randint(-10,10)) for i in range(2)]
    lista.append(row)
print(lista)
for i in (lista[0]):
    if i > 0:
        suma3 += i
for i in (lista[1]):
    if i > 0:
        suma4+=i
for i in (lista[0]):
    if i < 0:
        suma1 += i
for i in (lista[1]):
    if i < 0:
        suma2 += i
print("la suma de negativos es: ",suma1 + suma2)
print("la suma de los positivos es: ",suma3 + suma4)
