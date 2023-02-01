"""Escribir un programa que visualice la siguiente figura,
utilizando ciclos. El usuario decide cuantas líneas quiere
imprimir """
x = "*"
l = int(input("lineas a imprimir: "))
for i in range (l):
    print(x)
    x += "*"
    
    