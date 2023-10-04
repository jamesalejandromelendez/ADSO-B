try:
    g = {1: 'a', 2: 'b', 3: 'c'}
    g[4]
except KeyError:
    print("Ha ocurrido un error al intentar acceder a una clave inexistente en el diccionario")
