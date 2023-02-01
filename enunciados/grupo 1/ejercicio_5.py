"""Escriba un programa que lea una cadena y 
devuelva un diccionario con la cantidad de
apariciones de cada caracter en la cadena"""
frace = input("Ingrese una frace: ")

apariciones = {}
for i in frace:
    if i not in apariciones:
        apariciones[i] = 1
    else:
        apariciones[i] += 1
print(apariciones)
