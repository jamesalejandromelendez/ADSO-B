#http://patriciaemiguel.com/ejercicios/python/2019/03/10/ejercicios-decision-python.html
print("ejercicio 1")
"""6. Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación, 
imprimir “coincidencia” si los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. 
Si no es así, imprimir “no hay coincidencia”."""

def comparacion (nombre1,nombre2):
    final=len(nombre1)-1
    final2=len(nombre2)-1
    if nombre1[0] == nombre2[0]:
        print("hay coincidencia coincidencia en la primera letra")
    elif nombre1[final] == nombre2[final2]:
        print("hay conicidencia en la ultima letra")
    else:
        print("no hay coincidencia")    
nombre1=input("Un nombre: ")
nombre2=input("Otro nombre: ")
comparacion(nombre1,nombre2)

print("\n ejercicio 2")
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


print("ejercicio 3")

"""4.7: Se desea realizar una estadística de los pesos de los
alumnos de un colegio de acuerdo a la siguiente tabla:
Alumnos de menos de 40 kg.
Alumnos entre 40 y 50 kg.
Alumnos de más de 50 kg y menos de 60 kg.
Alumnos de más o igual a 60 kg."""

def alumnos (kg):
    a,b,c,d=0,0,0,0
    if kg < 40:
        a+=1
    elif kg <= 50:
        b+=1
    elif kg < 60:
        c+=1
    else:
        d+=1
    print("alumnos con peso de menos de 40 KG:",a,"\nalumnos con peso entre 40 y 50:",b,"\nalumnos con peso de mas de 50 y menos de 60:",c,"\nalumnos con peso de mas de 60:",d)

print("para parar ingrese el numero '0' ")
while True:
        kg=int(input("ingresa el numero de kilogramos:  "))
        if kg == 0:
            print("estadisticas:")
            break
alumnos(kg)
    

