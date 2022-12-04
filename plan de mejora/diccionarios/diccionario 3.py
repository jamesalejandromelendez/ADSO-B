"""Diseñar un algoritmo que permita crear un archivo
AGENDA de direcciones cuyos registros constan de los
siguientes campos:
NOMBRE
DIRECCION
CIUDAD
CODIGO POSTAL
TELEFO
edad"""
archivo = {}
while True:
    nombre = input("nombre del vecino: ")
    if nombre == "":
        break
    edad = input("edad del vecino: ")
    telefono = input("telefono del vecino: ")
    ciudad = input("ciudad del vecino: ")
    direccion = input("direccion del vecino: ")
    codigoP = input("codigo postal del vecino: ")
    datos = {"edad":edad,"telefono":telefono,"ciudad":ciudad,"direccion":direccion,"codigo postal":codigoP}
    if nombre in archivo:
        archivo[nombre]+=(datos)
    else:
        archivo[nombre]=(datos)
print(archivo)