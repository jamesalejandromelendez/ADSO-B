#Escriba un programa que permita crear una lista de palabras. Para ello, 
#el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. 
#Por último, el programa tiene que escribir la lista.
n = int(input("numero de palabras: "))
lista=[]
for i in range (n) :
    p=input("escribe tu palabra: ")
    lista.append(p)
print(lista)
