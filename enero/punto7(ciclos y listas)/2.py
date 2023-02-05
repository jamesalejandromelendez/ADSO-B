""" 7.28: Se dispone de una lista de N nombres de alumnos.
Escribir un algoritmo que solicite el nombre de un
alumno y busque en la lista (array) si el nombre está
en la lista."""
def alumnos():
    while True:
        buscar = input("alumno a buscar: ")
        if buscar == "":
            break
        if buscar in array:
            print("el alumno si se encuentra ")
        else:
            print("el alumno no se encuentra ")
            agregar = input("lo desea agragar? ")
            if agregar == "si":
                array.append(buscar)
            else:
                print()

array = ["james","alejandro"]
alumnos()
