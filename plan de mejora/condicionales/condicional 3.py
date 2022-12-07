"""4.7: Se desea realizar una estadística de los pesos de los
alumnos de un colegio de acuerdo a la siguiente tabla:
Alumnos de menos de 40 kg.
Alumnos entre 40 y 50 kg.
Alumnos de más de 50 kg y menos de 60 kg.
Alumnos de más o igual a 60 kg."""
a,b,c,d=0,0,0,0
while True:
    kg=int(input("ingresa el numero de kilogramos "))
    if kg == 0:
        print("estadisticas:")
        break
    elif kg < 40:
        a+=1
    elif kg <= 50:
        b+=1
    elif kg < 60:
        c+=1
    else:
        d+=1
print("alumnos con peso de menos de 40 KG:",a,"\nalumnos con peso entre 40 y 50:",b,"\nalumnos con peso de mas de 50 y menos de 60:",c,"\nalumnos con peso de mas de 60:",d)