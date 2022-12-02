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