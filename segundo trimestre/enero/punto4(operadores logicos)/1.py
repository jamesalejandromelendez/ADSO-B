#se saco de la miselania 1 ejercicio 5
def juego():
    x = ("si")
    y = ("no")
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

print ("para poder jugar responde con un SI o un NO")
print ("Colon descubrió América?")
juego()