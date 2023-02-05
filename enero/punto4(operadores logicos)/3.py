# Usamos el operador lógico "not or" para determinar si x no es mayor que y y no es menor que z
def m():
    if not (x > y or x < z):
        print("x no es mayor que y y no es menor que z")
    else:
        print("x es mayor que y o x es menor que z")

x = 5
y = 3
z = 7
m()
