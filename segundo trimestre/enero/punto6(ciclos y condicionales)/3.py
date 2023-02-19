# Escriba un programa que imprima todos los números entre 1 y 200 que sean divisibles por 3 y por 5 al mismo tiempo.

for num in range(1, 201):
    if num % 3 == 0 and num % 5 == 0:
        print(num)