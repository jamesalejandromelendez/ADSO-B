"""imprimir todas las horas posibles de un dia en formato horas minutos y segundos """
for horas in range (0, 13,1):
    for minutos in range (0, 60, 1):
        for segundos in range (0, 60, 1):
         print (horas, minutos, segundos, sep=":")