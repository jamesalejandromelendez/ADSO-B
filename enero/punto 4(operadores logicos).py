#se saco de la miselania 1 ejercicio 5
x = ("si")
y = ("no")
print ("para poder jugar responde con un SI o un NO")
print ("Colon descubrió América?")
res = (input("la respuesta es "))
if res == x or res != y: 
    print(" La independencia de Colombia fue en el año 1810?") 
    res = (input("la respuesta es "))
    if res == x or res != y:
        print("The Doors fue un grupo de rock Americano?")
        res = (input("la respuesta es "))
        if res == x or res != y:
            print("                            FELICIDADES  GANASTE EL JUEGO")
        else:
            print ("incorrecta\njuego terminado") 
    else:
        print ("incorrecta\njuego terminado") 
else:
     print ("incorrecta\njuego terminado") 

# Usamos el operador lógico "and" para determinar si x es mayor que y y menor que z, pero no igual a 5
x = 5
y = 3
z = 7
if x > y and x < z or x != 5:
    print("x es mayor que y, menor que z pero no igual a 5")
else:
    print("x no es mayor que y, no menor que z o igual a 5")

# Usamos el operador lógico "not or" para determinar si x no es mayor que y y no es menor que z
x = 5
y = 3
z = 7
if not (x > y or x < z):
    print("x no es mayor que y y no es menor que z")
else:
    print("x es mayor que y o x es menor que z")