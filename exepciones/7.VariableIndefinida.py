a=0
try:
    b=a
    #variable = x
except NameError:
    print("Ha ocurrido un error al intentar acceder a una variable no definida")
except:
    print('Todo salio mal')