"""deberiamos ser capaces de imprimir una tabla de multiplicar 
anidando dos bucles while"""
numero= int(input("numero a multiplicar"))
tope = 10
contador = 1
while contador <= tope:
    multiplicacion = numero * contador
    print(numero, "*", contador, "=", multiplicacion)
    contador += 1