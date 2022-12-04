""". Diseñar un algoritmo que permita modificar el contenido de alguno de los 
registros del archivo secuencial BIBLIOTECA mediante datos introducidos por
teclado."""
biblioteca = {}
while True:
    nombre=input("nombre del libro: ")
    if nombre == "":
        break
    autor=input("auto del libro: ")
    año=input("de que año es: ")
    datos= ({"autor":autor,"año":año})
    biblioteca[nombre]=(datos)
print(biblioteca)
