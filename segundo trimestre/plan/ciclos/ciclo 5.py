"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
 anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
 año que dura la inversión."""

inversion = int(input("el monto a ingresar: "))
Cinteres = int(input("que interes se va a manejar: "))
años = int(input("cantidad de años: "))
for i in range(años):
    inversion *= 1 + Cinteres /100
    print("su inversion del año ",i,"es",round(inversion))
