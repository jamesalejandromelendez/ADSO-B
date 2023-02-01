#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono 
#y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años,
#vive en <dirección> y su número de teléfono es <teléfono>.
persona={}
nombre = input("ingresa tu nombre")
edad = int(input("ingresa tu edad"))
direccion = input("ingresa tu direccion")
telefono = int(input("ingresa tu numero telefonico"))
registro ={"nombre":nombre,"edad":edad,"direccion":direccion,"telefono":telefono}
persona = registro

print(nombre," tiene",edad," años, vive en ",direccion,"y su numero telefonico es ",telefono)