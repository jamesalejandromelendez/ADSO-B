my_list = {}

def añadirartista(my_list):
    x=input("nombre del artista: ")
    my_list [x] = ()

def añadircancion(my_list):
    try:
        while True:
            name = input("Ingresa el nombre del artista: ")
            if name == '':
                break
            cancion = input("Ingresa una cancion: ")
            genero = input("ingresa el genero: ")
            duracion = input("duracion de la cancion: ")
            canciones = {"cancion":cancion,"genero":genero,"duracion":duracion}
            if name in my_list:
                my_list[name] += (canciones,)
            else:
                my_list[name] = (canciones,)
        print(my_list)
    except:
        print("lamentamos el error")

def buscarcancion ():
    try:
        x=input("nombre del artista: ")
        #buscar=input('¿Que cancion desea buscar?: ') 
        #for a in (my_list.values()): 
        if x in my_list: 
            print(my_list[x]["cancion"])  
        else:  
            print('no se encuentra la cancion')
    except TypeError:
        print("error en el sistema ")
    except:
        print("lo sentimos ")
        
def buscarartista():
    x=input("nombre del artista al buscar ")
    if x in my_list:
        print("si se encuentra registrado\n y cuenta con estas canciones:\n")        
        for i in my_list.keys():
            print(i, "\n", my_list[i])
            print()
    else:
            print("no se encuentra registrado ")

def listadoartistas(my_list):
    x=input("desea ver el listado con canciones? ")
    if x=="si":
        for y, z in my_list.items():
            print(y, "->", z)
    else:
        for i in my_list.keys():
            print(i)

def eliminar(my_list):
    E=input("que artista desea eliminar? ")
    del my_list[E]

def maslarga():
    
    print()

def ordenarLista(my_list):
    sorted(my_list.keys())
    print(my_list)

while True:
    print("bienvenido a spotify")
    m=input("presiona 1 para agregar un artista\npresiona 2 para agregar cancion\npresiona 3 para buscar artista\npresiona 4 para eliminar un artista\npresiona 5 para buscar una cancion\npresione 6 para ver el listado de artistas\npresione 7 para ordenar los artistas\n")
    if m=="":
        print("hasta pronto")
        break
    if m =="1":
        añadirartista(my_list)
    elif m=="2":
        añadircancion(my_list)
    elif m=="3":
        buscarartista()
    elif m=="4":
        eliminar()
    elif m=="5":
        buscarcancion()
    elif m=="6":
        listadoartistas()
    elif m=="7":
        ordenarLista()
    else:
        print("por favor agrega una opcion que este dentro del menu ")