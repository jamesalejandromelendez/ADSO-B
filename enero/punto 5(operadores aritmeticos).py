"""Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona y que calcule
 su índice de masa corporal (imc).
Se recuerda que el imc se calcula con la fórmula imc = peso / altura 2"""

peso = float(input("numero de peso: "))
altura = float(input("numero de altura: "))
respuesta = peso // (altura**2)
print("su imc es: ",respuesta)
if respuesta <= 25.0 and respuesta >= 20.0:
    print("te encuentras bien dentro de los indices de masa corporal ")
else:
    print("te encuentras fuera de los rango de masa corporal (imc). Los valores normales de imc estan entre los 20 y 25")

"""crea una calcuradora basica"""
def suma ():
    if o == "+":
        r = m + x
    print("su resultado es: ",r)
def resta ():
    if o == "-":
        r = m - x
    print("su resultado es: ",r)
def multiplicar ():
    if o == "*":
        r = m * x
    print("su resultado es: ",r)
def dividir ():
    if o == "*":
        r = m * x
    print("su resultado es: ",r)

while True:
    m = int(input("1.) digita tu numero: "))
    if m == 0 or "":
        print("...")
        break
    x = int(input("2.) digita tu numero: "))
    if x == 0 or "":
        print("...")
        break
    o = input("que operacion desea realizar\nsuma= +\nresta= -\nmultiplicar= *\ndividir= /\n: ")
    if o == "":
        print("...")
        break
    if o == "+":
        suma()
    if o == "-":
        resta()
    if o == "*":
        multiplicar()
    if o == "/":
        dividir()

"""Calcular el área de un triángulo dado el valor de sus lados
el área de un triángulo se puede calcular a partir de la fórmula de Herón"""

a = int(input("Ingrese el valor del lado a: "))
b = int(input("Ingrese el valor del lado b: "))
c = int(input("Ingrese el valor del lado c: "))

p = (a + b + c) / 2

area = (p*(p - a)*(p - b)*(p - c)) ** 0.5
print(area)
