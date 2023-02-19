
"""Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
valor del medio es 11. usando operadores lógicos"""
def numero():
	if x>y and x>=z:
		print("el primer numero '",x,"' es el mayor ")
	if y>x and y>z:
		print("el segundo numero '",y,"' es el mayor ")
	if z>x and z>y:
		print("el tercer numero '",z,"' es el mayor ")
    	

x = int (input('digite el primer numero'))
y = int (input('digite el segundo numero'))
z = int (input('digite el tercer numero'))
numero()
#este ultimo ejercicio fue tomado en base de la primera miselania
def edad():
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

edad = int(input('¿Cuál es tu edad?\n'))
edad()