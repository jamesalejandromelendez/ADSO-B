"""Escribir un programa que seleccione la operación
aritmética a ejecutar entre dos números dependiendo
del valor de una variable denominada seleccionOp."""
print("tipos de operaciones\n '+'para sumar\n '-'para restar\n '*'para multiplicar\n '/'para dividir")
num1=int(input("introduce tu primer numero "))
num2=int(input("introduce tu segundo numero "))
seleccionOp=input("escoja el tipo de operacion ")
if seleccionOp == "+":
    print(num1 + num2)
elif seleccionOp == "-":
    print(num1 - num2)
elif seleccionOp == "*":
    print(num1 * num2)
elif seleccionOp == "/":
    print(num1 // num2)
else:
    print()