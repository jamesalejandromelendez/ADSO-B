my_list = {}
def añadirartista(my_list):
    x=input("nombre del artista: ")
    my_list.update({x:{}})
def agregarcancion(my_list): 
    while True:
        name = input("Ingresa el nombre del artista: ")
        if name =="":
            break
        if name not in my_list:
            print("no se encuentra el artista ")
        else:
            cancion = input("Ingresa una cancion: ")
            genero = input("ingresa el genero: ")
            duracion = input("duracion de la cancion: ")
            z={"cancion":cancion,"genero":genero,"duracion":duracion}
            if name in my_list:
                my_list[name] = z,
            print(my_list)
        
def n():
    while True:
        m=input("presiona 1 para agregar un artista\npresiona 2 para agregar cancion\npresiona 3 para buscar artista\npresiona 4 para eliminar un artista\npresiona 5 para buscar una cancion\npresione 6 para ver el listado de artistas\n")
        if m=="":
            break
        if m =="1":
            print(añadirartista(my_list))
        elif m=="2":
            print(agregarcancion(my_list))
        elif m=="3":
            x=input("nombre del artista al buscar")
            if x in my_list:
                print("si se encuentra registrado\n y cuenta con estas canciones:",my_list[x])  
            else:
                print("no se encuentra registrado ")
        elif m=="4":
            E=input("que artista desea eliminar? ")
            del my_list[E]
        elif m=="5":
            #print(buscarcancion(my_list))
            print()
        elif m=="6":
            x=input("desea ver el listado con canciones? ")
            if x=="si":
                for y, z in my_list.items():
                    print(y, "->", z)
            else:
                for i in my_list.keys():
                    print(i)
        else:
            print("por favor agrega una opcion que este dentro del menu ")
n()