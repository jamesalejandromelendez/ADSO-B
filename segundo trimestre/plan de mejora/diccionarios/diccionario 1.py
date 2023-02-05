"""Escribir un programa que vaya solicitando al usuario que ingrese nombres.
Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar el teléfono y, 
opcionalmente, permitir modificarlo si no es correcto.
Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. 
El usuario puede utilizar la cadena "*", para salir del programa."""
usuarios = {"alejo":3052829469 }
while True:
    ingreso=input("busca o ingresa un nombre")
    if ingreso == "*":
        break
    if ingreso  not in usuarios:
        telefono= input("numero de telefono: ")
        usuarios[ingreso] = telefono
    if ingreso in usuarios:
        print(usuarios[ingreso])
        x=input("desea cambiar el numero? ")
        if x == "si":
            y=input("ingrese su nuevo numero: ")
            usuarios = { **usuarios, ingreso: y}
    print(usuarios)