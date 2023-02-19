"""Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona y que calcule
 su índice de masa corporal (imc).
Se recuerda que el imc se calcula con la fórmula imc = peso / altura 2"""
def masa():
    respuesta = peso // (altura**2)
    print("su imc es: ",respuesta)
    if respuesta <= 25.0 and respuesta >= 20.0:
        print("te encuentras bien dentro de los indices de masa corporal ")
    else:
        print("te encuentras fuera de los rango de masa corporal (imc). Los valores normales de imc estan entre los 20 y 25")

peso = float(input("numero de peso: "))
altura = float(input("numero de altura: "))
masa()
