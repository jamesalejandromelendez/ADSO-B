# Usamos el operador lógico "and" para determinar si x es mayor que y y menor que z, pero no igual a 5
def m():
    if x > y and x < z or x != 5:
        print("x es mayor que y, menor que z pero no igual a 5")
    else:
        print("x no es mayor que y, no menor que z o igual a 5")

x = 5
y = 3
z = 7
m()