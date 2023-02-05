""" 7. Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo,
 candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje
 “Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”"""

def votaciones(candidato):
    if candidato == "A":
        print("usted ha votado por el partido de color 'rojo'")
    if candidato == "B":
        print("usted ha votado por el partido de color 'verde'")
    if candidato == "C":
        print("usted ha votado por el partido de color 'azul'")
print("lista de candidatos:\n\tpartido rojo: A\n\tpartido verde: B\n\tpartido azul: C")
print("por favor responda en mayusculas")
candidato = input("su votacion es: ")
votaciones(candidato)