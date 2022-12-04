"""Se dispone de las notas de cuarenta alumnos. Cada
uno de ellos puede tener una o varias notas. Escribir
un algoritmo que permita obtener la media de cada
alumno y la media de la clase a partir de la entrada
de las notas desde el terminal."""
alumnos = {}
while True:
    nombre = input("Ingresa el nombre del estudiante: ")
    if nombre == "":
        break
    nota = int(input("Ingresa la calificación del estudiante (0-10): "))
    if nombre in alumnos:
        alumnos[nombre] += (nota,)
    else:
        alumnos[nombre] = (nota,)
for nombre in sorted(alumnos.keys()):
    puntuacion = 0
    contador = 0
    for score in alumnos[nombre]:
        puntuacion += score
        contador += 1
        total = puntuacion / contador
    print(nombre, "->", total)
total = alumnos.values
print(total)