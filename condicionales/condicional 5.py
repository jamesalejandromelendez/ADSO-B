x = ("si")
y = ("no")
print ("para poder jugar responde con un SI o un NO")
print ("Colon descubrió América?")
res = (input("la respuesta es "))
if res == x: 
    print(" La independencia de Colombia fue en el año 1810?") 
    res = (input("la respuesta es "))
    if res == x:
        print("The Doors fue un grupo de rock Americano?")
        res = (input("la respuesta es "))
        if res == x:
            print("                            FELICIDADES  GANASTE EL JUEGO")
        else:
            print ("incorrecta\njuego terminado") 
    else:
        print ("incorrecta\njuego terminado") 
else:
     print ("incorrecta\njuego terminado") 