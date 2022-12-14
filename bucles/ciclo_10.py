"""Algoritmo para hallar el m.c.d de dos números m y n por
el algoritmo de Euclides"""

def mcd_euclides(x,y):

	while x%y!=0: 

		x,y=y,x%y 

	return y

print(mcd_euclides(68, 48))