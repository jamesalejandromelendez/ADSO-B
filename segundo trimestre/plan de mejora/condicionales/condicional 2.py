"""4.9: Un ángulo se considera agudo si es menor de 90
grados, obtuso si es mayor de 90 grados y recto si
es igual a 90 grados. Utilizando esta información,
escribir un algoritmo que acepte un ángulo en grados
y visualice el tipo de ángulo correspondiente a los
grados introducidos."""

grados=int(input("ingrese el numero de grados que contiene el angulo "))  
if grados > 90:
    print("su angulo es de tipo:\n obtuso")
elif grados < 90:
    print("su angulo es de tipo:\n agudo")
else:
    print("su angulo es de tipo:\n recto")