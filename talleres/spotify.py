genero, spotify, canciones={},{},{}
def anadirgenero(genero):
    while True:
        g= input("que genero es ")
        if g == "":
            break
        d=input("duracion de la cancion? ")
        genero["genero"]= g
        genero["duracion"]=d
        return genero
def anadircancion(canciones):
    while True:
        cancion=input("ingrese el nombre de la cancion ")
        if cancion == "":
            break
        g=anadirgenero(genero)
        canciones["NOMBRE DE LA CANCION: ",cancion]=genero
        print(canciones)
def anadirlista (spotify):
    while True:
        nombre = input("ingresa el nombre del artista ")
        if nombre == "":
            break
        cancion= anadircancion(canciones)
        spotify[nombre]=canciones
        print(spotify)

def n():
    while True:
        m=input("presiona 1 para agregar un artista\npresiona 2 para agregar cancion\npresiona 3 para buscar artista\npresiona 4 para eliminar un artista\npresiona 5 para buscar una cancion\npresione 6 para ver el listado de artistas\n")
        if m=="":
            break
        if m =="1":
            print(anadirlista(spotify))
        elif m=="2":
            print(anadirlista(spotify))
        elif m=="3":
            x=input("nombre del artista al buscar")
            if x in spotify:
                print("si se encuentra registrado\n y cuenta con estas canciones")
                print(spotify[x])
            else:
                print("no se encuentra registrado ")
        elif m=="4":
            E=input("que artista desea eliminar? ")
            del spotify[E]
        elif m=="5":
            print()
        elif m=="6":
            for i in spotify.keys():
                print(i)
        else:
            print("lo sentimos")
n()