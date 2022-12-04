"""Leer una matriz de 3 por 3 elementos y calcular la
suma de cada una de sus filas y columnas, dejando
dichos resultados en dos vectores, uno de la suma de
las filas y otro de las columnas."""
import random
lista=[]
for i in range(3):
    row = [int(random.random()*10) for i in range(3)]
    lista.append(row)
print(lista)
def sumacolumnas():
    suma = (lista[0][0])
    suma1 = (lista[1][0])
    suma2 = (lista[2][0])
    columna1 = suma + suma1 + suma2 
    sumas = (lista[0][1])
    sumas1 = (lista[1][1])
    sumas2 = (lista[2][1])
    columna2 = sumas + sumas1 + sumas2
    sumass = (lista[0][2])
    sumass1 = (lista[1][2])
    sumass2 = (lista[2][2])
    columna3 = sumass + sumass1 + sumass2
    print("columna 1:",columna1, "\ncolumna 2:",columna2, "\ncolumna 3:",columna3)
def sumafilas():
    suma = sum(lista[0])
    suma1 = sum(lista[1])
    suma2 = sum(lista[2])
    print("fila 1:",suma, "\nfila 2:",suma1, "\nfila 3 :",suma2)
print(sumacolumnas())
print(sumafilas())