"""hacer un programa que pemita que el usuario ingrese una frace y una letra
basado en esto devuelva cuantas veces se repite la letra en la frase"""

f = input("ingresa una frace: ")
l = input("ingresa una letra: ")

c=0
for i in f:
    if i  == l:
        c+= 1
print ("la letra ",l, "se repite ",c, "veces")


