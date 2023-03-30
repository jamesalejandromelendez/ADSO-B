from datos import *
import csv
listaAprendices=[]
with open('C:\\Users\\Administrador\\Desktop\\JAMES') as z:
    csvReader=csv.reader(z)
    #print(csvReader)
    for row in csvReader:
        apr=Aprendiz(row[0],row[1],row[2],row[3])
        listaAprendices.append(apr)

print(listaAprendices)
for apr in listaAprendices:
    print(apr.nombreCompleto())

    