#https://www.youtube.com/watch?v=HXkPrXHm0so
"""determinar la solucion logica de esta operacion
((3+5*8)<3 and ((-6/3*4)+2<2)) or (a>b)"""
"""a = float (input("ingresa el vaor de A: "))
b = float (input("ingresa el vaor de B: "))
R = ((3+5*8)<3 and ((-6/3*4)+2<2)) or (a>b)
print("su resultado es ", R)"""

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad > 18 and edad <= 45:
	print('Eres mayor de edad.')
elif edad > 45 and edad <= 100:
	print('Eres mayor de edad, pero ya no tan joven.')
elif edad > 100 and edad <= 120:
	print('Eres muy mayor.')
else:
	print('Edad no válida.')

"""escribe un programa que tome la longitud de una palabra o frace y ademas 
se pueda escoger el minimo y el maximo que deberia tener """
texto = input("escribe un mensaje: ")
minimo = int(input("minimo de letras: "))
maximo = int(input("maximo de letras: "))
logitud = len (texto) >= minimo and len (texto) < maximo
print(logitud)

"""Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
valor del medio es 11. usando operadores lógicos"""
x = int (input('digite el primer numero'))
y = int (input('digite el segundo numero'))
z = int (input('digite el tercer numero'))

if x>y and x>=z:
    print("el primer numero '",x,"' es el mayor ")
elif y>x and y>z:
    print("el segundo numero '",y,"' es el mayor ")
elif z>x and z>y:
    print("el tercer numero '",z,"' es el mayor ")
#este ultimo ejercicio fue tomado en base de la primera miselania
