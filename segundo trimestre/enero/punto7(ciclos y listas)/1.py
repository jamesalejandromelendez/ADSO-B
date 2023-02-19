"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química,
 Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de 
 la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
 usuario tiene que repetir."""
def puntuacion():
    for i in materias:
        p = float(input("¿Qué nota has sacado en "+i+"?"))
        if p >= 5:
            aprovadas.append(i)
    for i in aprovadas:
        materias.remove(i)
    print("Tienes que repetir ", str(materias))
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprovadas = []
puntuacion()