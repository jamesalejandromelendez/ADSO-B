
n = 0
c = 0
suma = 0
while n >= 0:
    n = int(input("Ingresa un numero: "))
    if n > 0:
        c += 1
        suma += n
print("El total de numeros positivos es: ",c)
print("EL promedio de los numeros es: ",suma/c)