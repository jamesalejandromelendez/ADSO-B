"""Calcular el área de un triángulo dado el valor de sus lados
el área de un triángulo se puede calcular a partir de la fórmula de Herón"""
def area():
    p = (a + b + c) / 2
    area = (p*(p - a)*(p - b)*(p - c)) ** 0.5
    print(area)

a = int(input("Ingrese el valor del lado a: "))
b = int(input("Ingrese el valor del lado b: "))
c = int(input("Ingrese el valor del lado c: "))

