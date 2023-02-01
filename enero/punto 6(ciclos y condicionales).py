"""Ejercicio de practica"""

def pago():
    if horas <= 40:
        salario = horas * presio
        print("el salario de ",nombre, "es", salario)
    else:
        salario = 40 * presio + 1.5 * (horas-40)*presio
        print("el salario de ",nombre, "es", salario)

while True:
    horas=int(input("numero de horas: "))
    if horas == 0 or horas == "":
        print("gracias por usar nuestros servicios")
        break
    presio=int(input("que presio tiene la hora?  "))
    nombre=input("nombre: ")
    pago()

"""escribe un codigo para hacer un temporizador"""
def tem():
    for horas in range (0, 13,1):
        if horas == h:
            break
        for minutos in range (0, 60, 1):
            if minutos == m:
                break
            for segundos in range (0, 60, 1):
                if segundos == s:
                    break
                print (horas, minutos, segundos, sep=":")

h = int(input("hora: "))
m = int(input("minuto: "))
s = int(input("segundo: "))
tem()
# Escriba un programa que imprima todos los números entre 1 y 200 que sean divisibles por 3 y por 5 al mismo tiempo.

for num in range(1, 201):
    if num % 3 == 0 and num % 5 == 0:
        print(num)