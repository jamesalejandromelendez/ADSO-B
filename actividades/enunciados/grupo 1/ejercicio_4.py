"""escriba un programa que indique cuando se escriban valores negativos y agregar excepciones si el 
usuario ingresa división por cero y si ingresa una letra"""

try:
    a = int(input("ingresa el numero divisor: "))
    b = int(input("ingresa el numero dividendo: "))
    if a or b < 0:
        print("has ingresado un valor negativo")
    print("su resultado es ", a//b)
except ZeroDivisionError:
    print("no se puede dividir por cero\nintentalo de nuevo")
except ValueError:
    print("ingresaste un valor no numero\nintentalo de nuevo")
