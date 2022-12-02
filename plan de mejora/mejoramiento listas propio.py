"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
 Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for i in subjects:
    score = float(input("¿Qué nota has sacado en " + i + "?"))
    if score >= 5:
        passed.append(i)
for i in passed:
    subjects.remove(i)
print("Tienes que repetir ", str(subjects))
